from tqdm import tqdm
from dajare.crawler import Crawler
import re

rex = re.compile(r'^[0-9]+.htm')


class CrawlerDajareNet(Crawler):
    def run(self):
        output_list = self._run()
        self.output(output_list, 'dajare_net.json')

    def _run(self):
        bs = self.get_bs('http://www.dajare.net/', 'shift-jis')
        dump_list = self._get_dump_link_path_list(bs)
        return self._get_output_list(dump_list)

    def _get_dump_link_path_list(self, bs):
        return ['{:03}.htm'.format(x) for x in range(1, 50 + 1)] + [x.get('href') for x in bs.find_all('a', href=rex)]

    def _get_output_list(self, dump_list):
        for x in tqdm(dump_list):
            url = f'http://www.dajare.net/{x}'
            bs = self.get_bs(url, 'shift-jis')
            bs = bs.find('table')
            output_list = []
            for row in bs.find('td').text.strip().split('\n'):
                row = row.strip().split(' ')
                if row[0].startswith('['):
                    author = row[1]
                else:
                    text = ' '.join(row).replace('\u3000', '')
                    output_list.append({
                        'text': text,
                        'url': url,
                        'author': author,
                        'author_link': 'dajare.net',
                        'mean_score': 0.,
                        'deviation_score': 0.,
                        'category': [],
                        'tag': [],
                        'eval_list': []
                    })
        return output_list
