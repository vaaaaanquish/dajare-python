from tqdm import tqdm
from dajare.crawler import Crawler
import re

rex = re.compile(r'^[0-9]+.htm')


class CrawlerBiwaNeJp(Crawler):
    def run(self):
        output_list = self._run()
        self.output(output_list, 'dajare_biwa_ne_jp.json')

    def _run(self):
        url = 'http://www.biwa.ne.jp/~aki-ina/gyagu.html'
        bs = self.get_bs(url, 'utf-8')

        output_list = []
        for ul in tqdm(bs.find_all('ul')):
            for li in ul.find_all('li'):
                if not li.find('a'):
                    output_list.append({
                        'text': li.text.strip(),
                        'url': url,
                        'author': 'BAKADAS',
                        'author_link': 'www.biwa.ne.jp/~aki-ina',
                        'mean_score': 0.,
                        'deviation_score': 0.,
                        'category': [],
                        'tag': [],
                        'eval_list': []
                    })
        return output_list
