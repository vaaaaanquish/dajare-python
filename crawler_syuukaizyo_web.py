from tqdm import tqdm
from dajare.crawler import Crawler


class CrawlerSyuukaizyoWeb(Crawler):
    def run(self):
        output_list = self._run()
        self.output(output_list, 'dajare_syuukaizyo_web.json')

    def _run(self):
        url = 'http://syuukaizyo.fc2web.com/02.html'
        bs = self.get_bs(url, 'shift-jis')
        output_list = []
        for x in tqdm(bs.find('pre').text.split('\n')):
            if x.startswith('・'):
                output_list.append({
                    'text': x.replace('・', '').strip(),
                    'url': url,
                    'author': 'syuukaizyo',
                    'author_link': 'syuukaizyo.fc2web.com',
                    'mean_score': 0.,
                    'deviation_score': 0.,
                    'category': [],
                    'tag': [],
                    'eval_list': []
                })
        return output_list
