import time
import requests
from bs4 import BeautifulSoup
import json
import requests_cache
import os
requests_cache.install_cache('dajare')


class Crawler:
    def __init__(self, output_directory='./data', sleep_time=1.):
        if not os.path.exists(output_directory):
            os.mkdir(output_directory)
        self.output_directory = output_directory
        self.sleep_time = sleep_time

    def get_bs(self, url, encoding=None):
        while 1:
            try:
                response = requests.get(url)
                break
            except:
                time.sleep(self.sleep_time)
        if encoding:
            response.encoding = encoding
        return BeautifulSoup(response.text, features='html.parser')

    def post_bs(self, url, data, encoding=None):
        time.sleep(self.sleep_time)
        response = requests.post(url, data)
        if encoding:
            response.encoding = encoding
        return BeautifulSoup(response.text, features='html.parser')

    def output(self, output_list, file_name):
        with open(os.path.join(self.output_directory, file_name), 'w') as f:
            json.dump(output_list, f, ensure_ascii=False)
