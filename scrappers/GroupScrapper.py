import json
import urllib.request
import urllib.parse
import sys


class GroupScrapper:
    def scrape(self, meth, user_id):
        token = sys.argv[3]
        url = u'https://api.vk.com/method/%s?' % meth
        method = ({'groups.get': 'user_id=%s&access_token=%s&v=5.100'}[meth] % (user_id, token)).encode("utf-8")
        resp = urllib.request.urlopen(url, method).read()
        my_json = resp.decode('utf8').replace("'", '"')
        data = json.loads(my_json)
        if 'response' in data:
            return data["response"]["items"]
        else:
            return []
