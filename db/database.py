from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String, Table, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

user_and_track = Table('user_track', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('track_id', Integer, ForeignKey('tracks.id')))

user_and_group = Table('user_group', Base.metadata,
    Column('id_user', Integer, ForeignKey('users.id')),
    Column('group_id', Integer, ForeignKey('groups.id')))


class Users(Base):

    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    id_user = Column(String)
    children_track = relationship("Tracks", secondary=user_and_audio, back_populates='children_track')
    children_group = relationship("Groups", secondary=user_and_group, back_populates='children_group')

    def __init__(self, id_user):
        self.id_user = id_user

    def __repr__(self):
        return "<Users('%s','%s')>" % (self.id, self.id_user)


class Tracks(Base):

    __tablename__ = 'tracks'
    id = Column(Integer, primary_key=True)
    artist = Column(String)
    title = Column(String)
    duration = Column(Integer)
    url = Column(Text)

    def __init__(self, artist, title, duration, url):
        self.artist = artist
        self.title = title
        self.duration = duration
        self.url = url

    def __repr__(self):
        return "<Tracks('%s','%s', '%s', '%s', '%s')>" % (self.id, self.artist, self.title, self.duration, self.url)


class Groups(Base):

    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    id_group = Column(Integer)

    def __init__(self, id_group):
        self.id_group = id_group

    def __repr__(self):
        return "<Groups('%s','%s')>" % (self.id, self.id_group)

 
db_engine = create_engine("sqlite:///db/VK_scrapper.db", echo=True, pool_pre_ping=True)
Base.metadata.create_all(db_engine)
