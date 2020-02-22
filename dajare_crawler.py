import argparse
from dajare.crawler_dajare_jp import CrawlerDajareJp
from dajare.crawler_dajare_net import CrawlerDajareNet
from dajare.crawler_dajarenavi_net import CrawlerDajarenaviNet
from dajare.crawler_dajareshuu_web import CrawlerDajareshuuWeb
from dajare.crawler_syuukaizyo_web import CrawlerSyuukaizyoWeb
from dajare.crawler_biwa_ne_jp import CrawlerBiwaNeJp
from dajare.crawler_kaishaseikatsu_jp import CrawlerKaishaseikatsuJp

parser = argparse.ArgumentParser(description='クロールするサイトのリスト')
parser.add_argument('-a', '--all', action='store_true', help='全てのサイトのクロール')
parser.add_argument('-b', '--b', action='store_true', help='ダジャレナビ')
parser.add_argument('-c', '--c', action='store_true', help='ダジャレステーション')
parser.add_argument('-d', '--d', action='store_true', help='ダジャレネット')
parser.add_argument('-e', '--e', action='store_true', help='バカダス')
parser.add_argument('-f', '--f', action='store_true', help='ダジャレ辞典')
parser.add_argument('-g', '--g', action='store_true', help='究極のダジャレ集')
parser.add_argument('-i', '--i', action='store_true', help='ダジャレの殿堂')
parser.add_argument('--output', type=str, default='./output', help='出力ディレクトリ')
parser.add_argument('--sleep', type=float, default=1.0, help='requests毎のsleep')
args = parser.parse_args()
o = args.output
s = args.sleep

if args.all:
    CrawlerDajarenaviNet(o, s).run()
    CrawlerDajareJp(o, s).run()
    CrawlerDajareNet(o, s).run()
    CrawlerBiwaNeJp(o, s).run()
    CrawlerDajareshuuWeb(o, s).run()
    CrawlerSyuukaizyoWeb(o, s).run()
    CrawlerKaishaseikatsuJp(o, s).run()
else:
    if args.b:
        CrawlerDajarenaviNet(o, s).run()
    if args.c:
        CrawlerDajareJp(o, s).run()
    if args.d:
        CrawlerDajareNet(o, s).run()
    if args.e:
        CrawlerBiwaNeJp(o, s).run()
    if args.f:
        CrawlerDajareshuuWeb(o, s).run()
    if args.g:
        CrawlerSyuukaizyoWeb(o, s).run()
    if args.i:
        CrawlerKaishaseikatsuJp(o, s).run()
