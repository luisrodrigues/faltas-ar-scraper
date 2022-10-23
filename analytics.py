import pyperclip
import collections.abc
import os
import json
from typing import Union, Any

from constants import app_constants
from settings import app_settings


def load_data(filename: str):
    with open(filename, 'r') as file:
        raw = json.load(file)
        return json.loads(raw)


def process_data(data: collections.abc.Iterable):
    absence_report = {}

    for item in data:
        is_present = item['is_present']
        party = item['partido']
        if party not in absence_report.keys() and is_present:
            absence_report[party] = {'faltas': 0, 'total': 1}
        elif party not in absence_report.keys() and not is_present:
            absence_report[party] = {'faltas': 1, 'total': 1}
        elif party in absence_report.keys() and is_present:
            absence_report[party]['faltas'] = absence_report[party]['faltas']
            absence_report[party]['total'] = absence_report[party]['total'] + 1
        else:
            absence_report[party]['faltas'] = absence_report[party]['faltas'] + 1
            absence_report[party]['total'] = absence_report[party]['total'] + 1
    # sort report
    absence_report = dict(sorted(absence_report.items(), key=lambda x: x[1]['faltas'], reverse=True))
    return absence_report


def prettify(data_report: dict[Any, Union[dict[str, int], Any]]):
    data = ""
    for party_alias in data_report.keys():
        absences = data_report[party_alias]['faltas']
        total = data_report[party_alias]['total']
        ticker = " ✅ " if absences == 0 else " ❌ "
        line_to_print = party_alias + ticker + ": " + str(absences) + "/" + str(total) + " (" + str(round(absences/total * 100)) + "%)"
        data = data + line_to_print + "\n"
    return data


def process_title(title: str):
    return title.replace(" de ", ":").replace(".", "").split(":")


def process_date(date: str):
    return "/".join(date.split("-")[::-1])


class AbsenceAnalytics:

    def __init__(self, scraped_data, bid):
        self.scraped_data = scraped_data
        self.bid = bid
        self.url = app_constants.ATTENDANCE_TABLE_URL + bid
        self.is_save_files = app_settings.is_to_save_files

    def analyze_data(self):
        absences_filename = 'data/' + self.bid + '.json'
        if self.is_save_files:
            if os.path.exists(absences_filename):
                absences_data = load_data(absences_filename)
            else:
                print('File does not exist, scrape it!')
                return ""
        else:
            if self.scraped_data:
                absences_data = self.scraped_data
            else:
                print('Data not sent!')
                return ""
        post_date = process_title(absences_data['title'])[1]
        post_string = "🗓️" + process_date(post_date) + "\n"
        post_title = process_title(absences_data['title'])[0]
        post_string = post_string + "📝" + post_title + "\n"
        post_string = post_string + "➡️Nº de faltas por grupo parlamentar:" + "\n"
        report = process_data(absences_data['data'])
        post_string = post_string + prettify(report)
        post_string = post_string + "🔗" + self.url
        # when script runs, the new post will be saved on your clipboard
        pyperclip.copy(post_string)
        print(post_string)
        return post_string
