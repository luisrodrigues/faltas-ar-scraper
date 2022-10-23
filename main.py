from absence_data_scraper import AbsenceScraper
from analytics import AbsenceAnalytics
from event_list_scraper import absence_event_list_scraper

from constants import app_constants
from settings import app_settings


def scrape_new_data(bid: str):
    # input: BID string or nothing
    # output: file with new data or nothing if already scraped
    print("Scraping new data...")
    absence_scraper = AbsenceScraper(bid)
    scrape_data = absence_scraper.scrape_data()
    if not app_settings.is_to_save_files:
        return scrape_data


def produce_analytics_post(scraped_data: str, bid: str):
    # input: BID string of the file to analyse
    # output: string that is supposed to be posted on Twitter
    print("Producing social media post...")
    analytics = AbsenceAnalytics(scraped_data, bid)
    return analytics.analyze_data()


def post_to_twitter(text: str):
    # input: post string
    # output: nothing
    if app_settings.is_to_post_on_twitter:
        print(text)
        # twitter_poster.post_content(text)
    else:
        print("Not posting on Twitter...")


if __name__ == '__main__':
    if app_settings.is_to_skip_event_list:
        print("Skipping absence list scraping...")
        bid_to_scrape = app_constants.BID
    else:
        # output: new BID to scrape or do nothing if no new info
        print("Checking the absence list...")
        bid_to_scrape = absence_event_list_scraper.scrape_events_list()

        if not bid_to_scrape:
            print("BID scraping failed, using constant BID.")
            bid_to_scrape = app_constants.BID

    data = scrape_new_data(bid_to_scrape)
    post_text = produce_analytics_post(data, bid_to_scrape)
    post_to_twitter(post_text)
