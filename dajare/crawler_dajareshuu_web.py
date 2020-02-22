from tqdm import tqdm
from dajare.crawler import Crawler


class CrawlerDajareshuuWeb(Crawler):
    def run(self):
        output_list = self._run()
        self.output(output_list, 'dajare_shuu_web.json')

    def _run(self):
        url = 'https://dajareshuu.web.fc2.com/'
        bs = self.get_bs(url, 'utf-8')

        output_list = []
        for tr in tqdm(bs.find_all('tr')):
            flag = True
            for td in tr.find_all('td'):
                if not td.find('a'):
                    if flag:
                        keyword = td.text.strip()
                        flag = False
                    else:
                        output_list.append({
                            'text': td.text.strip(),
                            'url': url,
                            'author': 'dajareshuu',
                            'author_link': 'dajareshuu.web.fc2.com',
                            'mean_score': 0.,
                            'deviation_score': 0.,
                            'category': [],
                            'tag': [{
                                'link': 'dajareshuu.web.fc2.com',
                                'text': keyword
                            }],
                            'eval_list': []
                        })
                        flag = True
        return output_list
