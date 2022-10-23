import os
import json
from typing import Union, Any

import requests
from bs4 import BeautifulSoup

from constants import app_constants
from settings import app_settings


def process_html(content: bytes):
    attendance_data = []

    soup = BeautifulSoup(content, 'html5lib')
    title = soup.find('span', attrs={'id': app_constants.ATTENDANCE_PAGE_TITLE}).text
    table = soup.find('div', attrs={'id': app_constants.ATTENDANCE_TABLE_ID})  # attendance table

    for row in table.findAll('div', attrs={'class': 'row margin_h0 margin-Top-15'}):
        person_name = row.find('a').text
        person_info = row.find_all('span', attrs={'class': 'TextoRegular'})
        party = person_info[0].text
        is_present = True if person_info[1].text == 'Presença (P)' else False

        attendance_row = {
            'deputado': person_name,
            'partido': party,
            'is_present': is_present
        }
        attendance_data.append(attendance_row)
    return {'title': title, 'data': attendance_data}


class AbsenceScraper:

    def __init__(self, bid):
        self.bid = bid
        self.url = app_constants.ATTENDANCE_TABLE_URL + bid
        self.is_save_files = app_settings.is_to_save_files

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

    def save_json(self, content: dict[str, Union[str, list[dict[str, Union[bool, Any]]]]]):
        with open('data/' + self.bid + '.json', 'w') as fp:
            json_data = json.dumps(content, indent=4)
            json.dump(json_data, fp)

    def scrape_data(self):
        if self.is_save_files:
            if not os.path.exists('data/' + self.bid + '.json'):
                page_content = self.get_content()
                processed_content = process_html(page_content)
                self.save_json(processed_content)
            else:
                print('File already exists, no need to re-scrape it.')
        else:
            return process_html(self.get_content())
