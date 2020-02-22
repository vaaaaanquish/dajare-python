# dajare

皆さんに *幸* が訪れる駄洒落の *検索(Search)* を行うスクリプトと、駄洒落の *玄人* になりたい人向けにWebサイトからデータをの *クロール* するスクリプトです。

<br/>

# 環境構築

「pipenv」もしくは「自前で設定したpython環境」を利用する事ができます。  
pipenvを用いる場合は`pipenv install`の実行のみでOKです。  
pipenvを利用しない場合は、requirements.txtを利用して各moduleをinstallして下さい。  
```
$ pipenv install
or
$ pip install -r requirements.txt
```


<br/>

# 利用方法

検索用の「dajare_search.py」と各ダジャレサイトのクローラとなる「dajare_crawler.py」を用意しています。

## 検索

ダジャレステーションの検索窓を利用して、ダジャレを検索します。


pipenvを利用する場合は以下のように実行します。

```
$ pipenv run python dajare_search.py みかん

みかん星は、まだ未完成‼️
南関東では皆、みかん党
みかんが三日も見っかんねぇ
...
```


## スクレイピング

Webサイト *で得た* *データ* をjsonにdumpします。


<br/>

pipenvを利用する場合は以下のように実行します。
```
$ pipenv run python dajare_crawler.py --all
```

<br/>

dajare_crawler.pyの引数は以下のようになっています。

| args | description | クロール先 |
| --- | --- | ---|
| -h, --help | help表示 | - |
| -a, --all | 全てのサイトのクロール | - |
| -b, --b | ダジャレナビ | https://dajarenavi.net |
| -c, --c | ダジャレステーション | https://dajare.jp |
| -d, --d | ダジャレネット | http://www.dajare.net |
| -e, --e | バカダス | http://www.biwa.ne.jp/~aki-ina/gyagu.html |
| -f, --f | ダジャレ辞典 | https://dajareshuu.web.fc2.com |
| -g, --g | 究極のダジャレ集 | http://syuukaizyo.fc2web.com/02.html |
| --output OUTPUT | 出力ディレクトリを指定 | - |
| --sleep SLEEP | requests毎のsleep (float) | - |

<br/>

ダジャレネットのデータをsampleディレクトリにsleep 3.0秒/requests で取得する時は以下のようになります。
```
$ python dajare_crawler.py -d --output ./sample --sleep 3.0
```

<br/>

sleep値の設定等、スクレイピング時のルールについては、以下を参考にして下さい。  
[Webスクレイピングする際のルールとPythonによる規約の読み込み - Stimulator](https://vaaaaaanquish.hatenablog.com/entry/2017/12/01/064227)


<br/>

# 既存のデータ

2020/02/21時点でのダジャレ統計は以下の通りです。

| Webサイト | ダジャレ数 |
| --- | --- |
| ダジャレナビ | 48102 |
| ダジャレステーション | 64533 |
| ダジャレネット | 14 |
| バカダス | 1070 |
| ダジャレ辞典 | 275 |
| 究極のダジャレ集 | 1097 |

<br/>

# Json format

出力されるjsonは以下のようなフォーマットです。

```
{
    "url": "https://dajare.jp/works/000/",
    "text": "布団が吹っ飛んだ",
    "author": "サンプル",
    "author_link": "/author/サンプル/",
    "mean_score": 5.0,
    "deviation_score": 30.0,
    "category": [
        {
            "link": "/category/1/",
            "text": "動物"
        },
        {
            "link": "/category/1/1/",
            "text": "全般"
        },
        {
            "link": "/category/1/1/1/",
            "text": "全般"
        }
    ],
    "tag": [
        {
            "link": "/keyword/布団/",
            "text": "布団"
        }
    ],
    "eval_list": [
        {
            "author": {
                "link": "/author/テスト/",
                "text": "テスト"
            },
            "score": 3.0,
            "datetime": "2015/3/14 10:59"
        },
    ]
}
```

取得できない場合は空テキストや0が入ります。このフォーマットは全てのクロール先サイトで共通です。

<br/>

# 参考文献

### ダジャレ検出
- 谷津元樹, 荒木健治. "子音の音韻類似性及び SVM を用いた駄洒落検出手法." 知能と情報 28.5 (2016): 875-886. https://www.jstage.jst.go.jp/article/jsoft/28/5/28_875/_article/-char/ja/
- 谷津元樹, 荒木健治. "動画コメントデータ及びブログ記事における駄洒落の抽出." 情報処理学会第 81 回全国大会 6 (2019): 07. http://arakilab.media.eng.hokudai.ac.jp/~araki/2018/2018-D-11.pdf
- 文章からダジャレのみを抜き出すコマンドを作ってみた - Qiita https://qiita.com/kurehajime/items/a922d42dff5e0f03d32c
- おもしろいダジャレを入力すると布団が吹っ飛ぶ装置を作った - Qiita https://qiita.com/fujit33/items/dbfbd7a2aa3858067b6c
- ダジャレ TechTalk - エムスリーテックブログ https://www.m3tech.blog/entry/2018/08/03/182447
- ニコニココメントデータからの駄洒落検出 - 谷津元樹 青山学院大学 https://www.nii.ac.jp/dsc/idr/userforum/startup/IDR-UF2019_S03.pdf

### ダジャレデータベース
- 荒木健治. "駄洒落データベースの構築及び分析" ことば工学研究会: 人工知能学会第 2 種研究会ことば工学研究会 57 (2018): 39-48. http://arakilab.media.eng.hokudai.ac.jp/~araki/2017/2017-C-3.pdf
- 荒木健治. "駄洒落データベースを用いた駄洒落生成システムの性能評価" ことば工学研究会: 人工知能学会第 2 種研究会ことば工学研究会 56 (2017): 13-24. https://ci.nii.ac.jp/naid/40021582065/
- 荒木健治. "駄洒落データベースの拡張及び分析" ことば工学研究会: 人工知能学会第 2 種研究会ことば工学研究会資料 58 (2018): 1-15. https://ci.nii.ac.jp/naid/40021829772/


### ダジャレ生成
- 内田ゆず, 荒木健治. "オノマトペに着目した駄洒落の面白さの分析―駄洒落の自動生成に向けて―." 日本知能情報ファジィ学 第35回ファジィシステムシンポジウム. 2019. https://www.jstage.jst.go.jp/article/fss/35/0/35_332/_article/-char/ja/
- 金久保正明. "形態素解析手法と通俗的単語群に基づく類音文変換システム." 情報処理学会論文誌 54.7 (2013): 1937-1950. https://ipsj.ixsq.nii.ac.jp/ej/?action=pages_view_main&active_action=repository_view_main_item_detail&item_id=94391&item_no=1&page_id=13&block_id=8
田辺　公一朗. "駄洒落のコンピュータによる処理-- 駄洒落生成システムの基本設計 --" Sanno University Bulletin Vol.26 No. 1 September 2005 https://www.sanno.ac.jp/undergraduate/library/cpir4n0000006hnm-att/260104.pdf
阿部香央莉, et al. "Zunkobot: 複数の知識モジュールを統合した雑談対話システム." SIG-SLUD 5.02 (2018): 112-117. https://jsai.ixsq.nii.ac.jp/ej/?action=repository_action_common_download&item_id=9639&item_no=1&attribute_id=1&file_no=1

### ダジャレ分析
- 内田ゆず, 荒木健治. "駄洒落に使用されるオノマトペの特徴分析." 知能と情報 32.1 (2020): 507-511. https://www.jstage.jst.go.jp/article/jsoft/32/1/32_507/_article/-char/ja/
- 谷津元樹, 荒木健治. "駄洒落の面白さにおける要因の分析." 日本知能情報ファジィ学会 講演論文集 第32回ファジィシステムシンポジウム. 2016. https://www.jstage.jst.go.jp/article/fss/32/0/32_237/_article/-char/ja/
- 川原繁人, 篠原和子. "ダジャレから見る母音の近似性." 音声研究 13.3 (2009): 101-110. https://ci.nii.ac.jp/naid/110008722613/
- 篠原和子, 川原繁人. "日本語のダジャレにおける音節挿入." 日本認知言語学会論文集 10 (2010): 313-323. https://ci.nii.ac.jp/naid/40018766044/
- KOBAYASHI Yoshitomo. "駄洒落の基本構造と笑い" 東京外国語大学 http://www.tufs.ac.jp/st/personal/03/conanweb/dajare.htm

### ダジャレ対話
- 徐云帆, 荒木健治. "雑談対話システムにおける LSTM を用いた駄洒落による対話破綻回避の有効性." SIG-SLUD 5.02 (2018): 143-148. https://jsai.ixsq.nii.ac.jp/ej/?action=repository_action_common_download&item_id=9645&item_no=1&attribute_id=1&file_no=1
- 谷津元樹. "統合型対話システムにおける話題適応及び駄洒落ユーモア処理に関する研究." (2017). https://eprints.lib.hokudai.ac.jp/dspace/bitstream/2115/65779/1/Motoki_Yatsu.pdf

<br/>

# 開発
Pull Requestをお待ちしております
