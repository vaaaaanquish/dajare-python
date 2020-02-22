from tqdm import tqdm
from dajare.crawler import Crawler


class CrawlerKaishaseikatsuJp(Crawler):
    def run(self):
        output_list = self._run()
        self.output(output_list, 'dajare_kaishaseikatsu_jp.json')

    def _run(self):
        output_list = []
        for i in tqdm(range(0, 2200, 100)):
            url = f'http://archives.kaishaseikatsu.jp/cgi-bin/kaisha2/board_r.cgi?type=kaisha_dajare&next={i}&range=100'
            bs = self.get_bs(url, encoding='shift-jis')
            for x in bs.find_all('tr', bgcolor="#FBFFB2"):
                output_list.append({
                    'text': x.find('td').text,
                    'url': url,
                    'author': 'kaishaseikatsu',
                    'author_link': 'http://archives.kaishaseikatsu.jp',
                    'mean_score': 0.,
                    'deviation_score': 0.,
                    'category': [],
                    'tag': [],
                    'eval_list': []
                })
        return output_list
