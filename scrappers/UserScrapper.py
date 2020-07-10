from scrappers.GroupScrapper import GroupScrapper
from scrappers.MusicScrapper import MusicScrapper


class UserScrapper:
    def scrape(self, user_id):
        music = MusicScrapper()
        group = GroupScrapper()

        list_music = music.scrape(user_id)
        list_group = group.scrape('groups.get', user_id)
        batch_resulst = dict(user_id=user_id, list_music=list_music, list_group=list_group)

        return batch_resulst
