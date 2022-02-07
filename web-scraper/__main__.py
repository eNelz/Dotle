from dota_scraper import *
import sys

if __name__ == "__main__":
    scrape = dota_scraper() # doesn't correctly parse names of characters with more than one word in their name
    # hero_obj.preprocess()
    soup = scrape.get_hero_soup("Phantom_Assassin")
    hero = scrape.get_hero_info(soup)
    print(hero.hero_info())