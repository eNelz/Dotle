from dota_scraper import *
import sys
"""
This script will kick off the process to scrape a user specified
number of games from j_archive.
How to run:
python __main__.py <start_game_id> [<end_game_id>]
"""
if __name__ == "__main__":
    hero_obj = dota_scraper("Phantom_Assassin") # doesn't correctly parse names of characters with more than one word in their name
    hero_obj.preprocess()
    soup = hero_obj.get_hero_soup()
    print(hero_obj.get_hero_info())