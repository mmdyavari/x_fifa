import bs4
import requests

import os;os.system('clear')

class Scraping:
    def __init__ (self, url, tag, class_name = ''):
        self.url = url
        self.tag = tag
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        self.__page = requests.get(url, headers=self.__headers).content
        self.__soup = bs4.BeautifulSoup(self.__page, 'html.parser')
        self.__result = self.__soup.find_all(self.tag, class_ = class_name)

    @property
    def result (self):
        return self.__result

#! testing
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/List_of_authors_by_name:_A"
    tets = Scraping(url=url, tag='a')

    singers = []
    for i in tets.result:
        singers.append(i.string)

    print(tets.result)