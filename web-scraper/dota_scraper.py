from bs4 import BeautifulSoup
import urllib.request

class hero_obj():

    def __init__(
        self,
        name: str,
        attr: str,
        range: int,
        ms: int
    ):
        self.name = name
        self.attr = attr
        self.range = range
        self.ms = ms

    def hero_info(self):
        return {'Name': self.name, 'Attribute': self.attr, 'Attack Range' : self.range, 'Movement Speed' : self.ms}

class dota_scraper():

    def __init__(self): # Consider making no arguments here and instead adding one to get_hero_info
        self.hero_objs = []

    """
    def preprocess(self):
        self.get_hero_soup()
        page_name = self.hero_soup.h1.text
        hero_name = page_name.strip()
    """

    def get_hero_soup(self, hero: str):
        hero_url = "https://dota2.fandom.com/wiki/"+hero
        fid = urllib.request.urlopen(hero_url)
        webpage = fid.read().decode('utf-8')
        hero_soup = BeautifulSoup(webpage, 'html.parser')
        return hero_soup

    def get_hero_info(self, hero_soup: BeautifulSoup):
        table = hero_soup.find('table', attrs={'class':'infobox'})
        table_body = table.find('tbody')
        table_header = table.find('th')
        rows = table_body.find_all('tr')

        name = table_header.text.split('\n')[0]

        attr = table_header.find(id='primaryAttribute').a.attrs['title']

        range_row = rows[24].find_all('td')
        range = range_row[0].find(href='/wiki/Attack_range#Melee_and_ranged').img.attrs['alt']

        ms_row = rows[28].find_all('td')
        ms = int(ms_row[1].text.split()[0])

        return hero_obj(name, attr, range, ms)