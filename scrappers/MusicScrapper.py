import vk_api
from vk_api import audio
import sys


class MusicScrapper:

    def __init__(self):
        self.vk_session = vk_api.VkApi(login=sys.argv[1], password=sys.argv[2])
        self.vk_session.auth()
        self.vk = self.vk_session.get_api()

    def scrape(self, user_id):
        try:
            vk_audio = audio.VkAudio(self.vk_session)
            music = vk_audio.get(owner_id=user_id)
        except Exception:
            return []
        return music
        
