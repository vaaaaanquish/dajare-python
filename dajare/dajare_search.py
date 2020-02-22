import argparse
import requests
from bs4 import BeautifulSoup
import urllib


def dajare_search(query):
    q_quote = urllib.parse.quote(query)
    r = requests.get(f'https://dajare.jp/keyword/{q_quote}/')
    bs = BeautifulSoup(r.text, features="html.parser")
    dajare = []
    for x in bs.find_all('tr'):
        da = x.find("td", class_='ListWorkBody')
        if not da:
            continue
        score = x.find("td", class_="ListWorkScore")
        dajare.append({'text': da.text, 'score': float(score.text.split(' (')[0])})

    print('\n'.join([x['text'] for x in sorted(dajare, key=lambda x: x['score'], reverse=True)]))


def main():
    parser = argparse.ArgumentParser(description='駄洒落検索')
    parser.add_argument('arg1', help='検索用query')
    args = parser.parse_args()
    query = args.arg1
    dajare_search(query)


if __name__ == '__main__':
    main()
