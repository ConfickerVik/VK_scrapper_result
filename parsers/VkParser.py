from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import ClauseElement
from parsers.UserListParser import UserListParser
from db import database


class VkParse:
    user_list_parser_class = UserListParser

    def parse(self):
        user_list_parser = self.user_list_parser_class()
        for user_list in user_list_parser.parse():
            self.parse_user(user)

    def parse_user(self, user):
        Session = sessionmaker(bind=database.db_engine)
        session = Session()

        id_user = user['user_id']
        list_music = user['list_music']
        list_group = user['list_group']

        user_db = self.get_or_create(session, database.Users, id_user=id_user)[0]

        if list_music is not []:
            for tracks in list_music:
                track_db = self.get_or_create(session, database.Tracks, defaults={"url": tracks["url"]},
                                   artist=tracks["artist"], title=tracks["title"],
                                   duration=tracks["duration"])[0]
                user_db.children_track.append(track_db)
                session.commit()
        else:
            pass

        if list_group is not []:
            for i in range(len(list_group)):
                group_db = self.get_or_create(session, database.Groups, id_group=list_group[i])[0]
                user_db.children_group.append(group_db)
                session.commit()
        else:
            pass

    def get_or_create(self, session, model, defaults=None, **kwargs):
        instance = session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance, False
        else:
            params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
            params.update(defaults or {})
            instance = model(**params)
            session.add(instance)
            session.commit()
            return instance, True
