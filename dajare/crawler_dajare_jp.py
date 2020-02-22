import re
from dajare.crawler import Crawler
from tqdm import tqdm

category_rex = re.compile(r'/category/*')
works_rex = re.compile(r'/works/*')
mean_rex = re.compile(r'平均スコア：([0-9\.]+)')
dev_rex = re.compile(r'だじゃれ偏差値：([0-9\.]+)')


class CrawlerDajareJp(Crawler):
    def run(self):
        # from category
        category_link_set = self._get_category_link_set()
        category_works_link_set = self._get_category_works_link_set(category_link_set)
        output_list = self._get_output_list(category_works_link_set)
        # from author
        author_works_link_set = self._get_author_works_link_set(output_list, category_works_link_set)
        output_list += self._get_output_list(author_works_link_set)
        # from tag
        tag_works_link_set = self._get_tag_works_link_set(output_list, category_works_link_set | author_works_link_set)
        output_list += self._get_output_list(tag_works_link_set)

        self.output(output_list, 'dajare_jp.json')

    def _get_category_link_set(self):
        bs = self.get_bs('https://dajare.jp/')
        category_link_set = set()
        for x in bs.find_all('a', href=category_rex):
            if len(x.get('href').split('/')) == 6:
                category_link_set.add(x.get('href'))
        return category_link_set

    def _get_category_works_link_set(self, link_set):
        dajare_link_set = set()
        for x in tqdm(link_set):
            x = x.split('/')
            data = {'ViewQuantity': 10000, 'CategoryLarge': x[2], 'CategoryMiddle': x[3], 'CategorySmall': x[4], 'ViewOffset': 0}
            bs = self.post_bs('https://dajare.jp/search/', data)
            for u in bs.find_all('a', href=works_rex):
                dajare_link_set.add(u.get('href'))
        return dajare_link_set

    def _get_author_works_link_set(self, output_list, link_set):
        author_link = {x['author'] for x in output_list}
        dajare_link_set = set()
        for x in tqdm(author_link):
            data = {'ViewQuantity': 10000, 'AuthorName': x, 'ViewOffset': 0}
            bs = self.post_bs('https://dajare.jp/search/', data)
            for u in bs.find_all('a', href=works_rex):
                dajare_link_set.add(u.get('href'))
        return dajare_link_set - link_set

    def _get_tag_works_link_set(self, output_list, link_set):
        tag_link = set()
        for x in output_list:
            for y in x['tag']:
                tag_link.add(y['text'])
        dajare_link_set = set()
        for x in tqdm(tag_link):
            data = {'Keyword': x, 'ViewQuantity': 10000, 'ViewOffset': 0}
            bs = self.post_bs('https://dajare.jp/search/', data)
            for u in bs.find_all('a', href=works_rex):
                dajare_link_set.add(u.get('href'))
        return dajare_link_set - link_set

    def _get_output_list(self, link_set):
        output_list = []
        for i in tqdm(link_set):
            url = f'https://dajare.jp{i}'
            bs = self.get_bs(url)

            # panel
            bs = bs.find(id='PanelContentMain')

            # dajare text, author
            panel = bs.find(class_='PanelBox')
            text = panel.find('span').text
            a = panel.find('a')
            author = a.text if a else panel.find('div', align="right").text
            author_link = panel.find('a').get('href') if a else ''

            # dajare meta data
            fieldset = bs.find_all('fieldset')
            eval_list = []
            for field in fieldset:
                legend = field.find('legend')
                if not legend:
                    if '平均スコア' in field.text:
                        # dajare score
                        x = field.text.replace('\n', '')
                        mean_score = float(mean_rex.findall(x)[0])
                        dev_score = float(dev_rex.findall(x)[0])
                    else:
                        # dajare evaluation scores
                        eval_row = {}
                        for row in field.find_all(class_='PanelWorkEvaluationList'):
                            col = row.find('dt').text.strip()
                            if col == '投稿者':
                                a = row.find('a')
                                href = a.get('href') if a else ''
                                eval_row.update({'author': {'link': href, 'text': row.text.strip()}})
                            if col == 'スコア':
                                eval_row.update({'score': float(row.text.replace('スコア\n', ''))})
                            if col == '評価投稿時刻':
                                eval_row.update({'datetime': row.text.replace('評価投稿時刻', '').strip()})
                        eval_list.append(eval_row)
                elif 'カテゴリー' in legend.text:
                    # dajare category
                    category = [{'link': x.get("href"), 'text': x.text} for x in set(field.find_all('a'))]
                elif 'タグ' in legend.text:
                    # dajare tags
                    tag = [{'link': x.get("href"), 'text': x.text} for x in field.find_all('a')]

            output_list.append({
                'url': url,
                'text': text,
                'author': author,
                'author_link': author_link,
                'mean_score': mean_score,
                'deviation_score': dev_score,
                'category': category,
                'tag': tag,
                'eval_list': eval_list
            })
        return output_list
