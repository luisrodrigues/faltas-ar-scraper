import os
from dotenv import load_dotenv

load_dotenv()


class ScraperSettings:
    def __init__(self):
        # if True it will skip the list scraping part, the BID in the constants file should be filled in
        self.is_to_skip_event_list = False
        # if True it will save and retrieve scraped data from files in the "data" directory
        self.is_to_save_files = False
        # if True, it will post text on Twitter (not working yet)
        self.is_to_post_on_twitter = False
        # Twitter stuff
        self.consumer_key = os.getenv("CONSUMER_KEY")
        self.consumer_secret = os.getenv("CONSUMER_SECRET")
        self.access_token = os.getenv("ACCESS_TOKEN")
        self.access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


app_settings = ScraperSettings()
