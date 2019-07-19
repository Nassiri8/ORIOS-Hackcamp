from bs4 import BeautifulSoup as bs4
from urllib.request import urlopen
import re

class Get_Link:
    links = []
    url = "http://orios.louisviallon.fr"
    def get_all_links(self):
        html_page = urlopen(self.url)
        soup = bs4(html_page,  "html.parser")
        for link in soup.findAll('a'):
            fulllink = self.url + "/" + link.get('href')
            if not fulllink in self.links:
                self.regex(link.get('href'))

    def regex(self, link):
        regex = r".*.net"
        regexp = re.compile(regex)
        # for link in links:
        if not regexp.search(link):
            self.links.append(self.url + "/" +  link)

    def launch(self):
        self.get_all_links()
        return (self.links)