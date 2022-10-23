import os
import requests
from bs4 import BeautifulSoup

from constants import app_constants
from settings import app_settings

LINK_SEPARATOR = "BID="


def get_bid_from_link(link: str):
    before_sep, sep, after_sep = link.partition(LINK_SEPARATOR)
    return after_sep


def process_html(content: bytes):
    soup = BeautifulSoup(content, 'html5lib')
    table = soup.find('div', attrs={'id': app_constants.ATTENDANCE_EVENTS_TABLE_ID})  # attendance records list table

    first_row = table.findAll('div', attrs={'class': 'row margin_h0 margin-Top-15'})[0]
    link = first_row.findAll('div', attrs={'class': 'col-xs-12 col-lg-3 ar-no-padding'})[0]
    link_text = link.find('a').get('href')

    return get_bid_from_link(link_text)


class AbsenceEventListScraper:

    def __init__(self):
        self.url = app_constants.ATTENDANCE_EVENTS_URL

    def get_content(self):
        try:
            r = requests.get(self.url)
            print("Page exists.")
            return r.content
        except requests.exceptions.Timeout as e:
            print("Timeout error: {0}".format(e))
        except requests.exceptions.TooManyRedirects as e:
            print("Try a different URL: {0}".format(e))
        except requests.exceptions.RequestException as e:
            print("Unexpected error: {0}".format(e))

    def scrape_events_list(self):
        page_content = self.get_content()
        process_html(page_content)

        last_bid = process_html(page_content)

        if app_settings.is_to_save_files:
            if not os.path.exists('data/' + last_bid + '.json'):
                print(f'Attendance page (BID: {last_bid}) needs to be scraped.')
                return last_bid
            else:
                print('File already exists, no need to re-scrape it.')
                return ''
        else:
            print(f'Not working with files. Sending BID: {last_bid}.')
            return last_bid


absence_event_list_scraper = AbsenceEventListScraper()
