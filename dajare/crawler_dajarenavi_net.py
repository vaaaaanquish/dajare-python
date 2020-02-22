from tqdm import tqdm
from dajare.crawler import Crawler


class CrawlerDajarenaviNet(Crawler):
    def run(self):
        output_list = self._run()
        self.output(output_list, 'dajarenavi_net.json')

    def _run(self):
        bs = self.get_bs('https://dajarenavi.net/index.htm')
        link_list = self._get_aiueo_link_list(bs)
        link_list = self._get_fukugo_link_list(link_list)
        link_list = self._get_keyrowd_link_list(link_list)
        return self._get_output_list(link_list)

    def _get_aiueo_link_list(self, bs):
        link_list = []
        for x in bs.find_all('tr', bgcolor="#000000"):
            for y in x.find_all('a'):
                link_list.append(y.get('href'))
        return link_list

    def _get_fukugo_link_list(self, link_list):
        fukugo_link_list = []
        for keyword_link in tqdm(link_list):
            bs = self.get_bs(f'https://dajarenavi.net/{keyword_link}')
            for x in bs.find_all('tr', bgcolor="#000000"):
                for y in x.find_all('a'):
                    fukugo_link_list.append(y.get('href'))
        return fukugo_link_list

    def _get_keyrowd_link_list(self, link_list):
        keyword_link_list = []
        for link in tqdm(link_list):
            bs = self.get_bs(f'https://dajarenavi.net/menu/0/{link}')
            for x in bs.find_all('tr', bgcolor="#000000"):
                for a in x.find_all('a'):
                    if not a.get('target'):
                        keyword_link_list.append(a.get('href'))
        for link in [w for w in keyword_link_list if w.startswith('../t/')]:
            bs = self.get_bs(f'https://dajarenavi.net/menu/0/{link.replace("../","")}')
            for x in bs.find_all('tr', bgcolor="#000000"):
                for a in x.find_all('a'):
                    if not a.get('target'):
                        keyword_link_list.append(a.get('href'))
        return [l for l in keyword_link_list if l.startswith('../../')]

    def _get_output_list(self, link_list):
        output_list = []
        for link in tqdm(link_list):
            url = f'https://dajarenavi.net/{link.replace("../../","")}'
            bs = self.get_bs(url, 'shift-jis')
            try:
                keyword = bs.find(class_="kw_title").find('span').text.strip()
            except Exception:
                # href設定にいくつかミスがある
                continue
            for x in bs.find_all(class_="dajare"):
                d = {
                    'url': url,
                    'text': x.text.strip(),
                    'author': 'dajarenavi',
                    'author_link': 'dajarenavi.net',
                    'mean_score': 0.,
                    'deviation_score': 0.,
                    'category': [],
                    'tag': [{
                        'link': link.replace("../..", ""),
                        'text': keyword
                    }],
                    'eval_list': []
                }
                output_list.append(d)
        return output_list
