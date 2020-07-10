from bs4 import BeautifulSoup
import requests
from scrappers.UserScrapper import UserScrapper


class UserListParser:

    base_uri = "https://vk.com"

    def parse(self, uri="catalog.php?selection=0-0-0"):
        page = uri.split("?")[0]
        response = requests.get("%s/%s" % (self.base_uri, uri))
        soup = BeautifulSoup(response.text, 'html.parser')

        catalog_selection = soup.find(class_='catalog_wrap clear_fix')
        catalog_selection_list_items = catalog_selection.find_all('a')

        users = []
        userscrape = UserScrapper()
        for catalog in catalog_selection_list_items:
            href_uri = catalog.get('href')
            if page in href_uri:
                self.parse(href_uri)
            else:
                users.append(userscrape.scrape(href_uri[2:]))
        return users
