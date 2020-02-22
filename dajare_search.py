import argparse
import requests
from bs4 import BeautifulSoup
import urllib

parser = argparse.ArgumentParser(description='駄洒落検索')
parser.add_argument('arg1', help='検索用query')
args = parser.parse_args()
query = args.arg1

q_quote = urllib.parse.quote(query)
r = requests.get(f'https://dajare.jp/keyword/{q_quote}/')
bs = BeautifulSoup(r.text, features="html.parser")
l = []
for x in bs.find_all('tr'):
    dajare = x.find("td", class_='ListWorkBody')
    if not dajare:
        continue
    score = x.find("td", class_="ListWorkScore")
    l.append({'text': dajare.text, 'score': float(score.text.split(' (')[0])})

print('\n'.join([x['text'] for x in sorted(l, key=lambda x: x['score'], reverse=True)]))
