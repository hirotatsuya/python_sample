# ============================================
#
# get_images_py_instagram.py
# Created by hirotatsu on 2017/12/07
#
# ============================================

# 必要なライブラリのimport
import os # ディレクトリ作成
import sys # 実行時引数
import re # 正規表現
import json # JSON形式に変換
import requests # urlアクセス
from bs4 import BeautifulSoup # スクレイピング

# instagramのIDを指定して画像を取得する関数
def get_images_by_instagram():
  # 実行時引数からtarget_instagram_idを取得
  target_instagram_id = sys.argv[1]

  # target_urlの生成
  target_url = "https://www.instagram.com/" + target_instagram_id

  # target_urlのhtml情報を取得(timeoutは10秒)
  res = requests.get(target_url, timeout = 10)

  # target_urlに正常にアクセスできたら200番のstatus_codeが返ってくる
  if res.status_code == 200:

    # resのtext部分のみスクレイピング
    soup = BeautifulSoup(res.text, "html.parser")

    # scriptタグの中から、window._sharedDataという文字列に合致するtextを検索してスクレイピング
    js = soup.find("script", text = re.compile("window._sharedData")).text

    # {}の中身のみを切り出す
    data = js[js.find("{") : js.rfind("}") + 1]

    # 必要な部分のみをjson形式で切り出す
    results = json.loads(data)['entry_data']['ProfilePage'][0]['user']['media']['nodes']

    # imageのurlをすべて格納する箱の生成
    image_urls = []

    # results配列をループ
    for i in range(len(results)):

      # thumbnail_resourcesの部分の配列をループ
      for j in range(len(results[i]['thumbnail_resources'])):

        # src属性の中身を切り出してimage_urlsに格納
        image_urls.append(results[i]['thumbnail_resources'][j]['src'])

    # カレントディレクトリにimagesディレクトリが存在するか調べる
    if not os.path.exists("./images"):

      # カレントディレクトリにimagesディレクトリを作成
      os.mkdir("./images")

    # image_urls配列をループ
    for i in range(len(image_urls)):

      # ひとつのURLを作成
      url = image_urls[i]

      # URLから画像を取得
      image = requests.get(url)

      # imagesディレクトリに格納するファイルをopen
      with open('images/' + target_instagram_id + url.split('/')[-1], 'wb') as f:

        # 画像ファイルを格納
        f.write(image.content)

    # 正常終了を確認
    print('ok')

  # target_urlに正常にアクセスできなかった時
  else:

    # 異常終了を確認
    print('NG')

# メイン
if __name__ == "__main__":

  # get_images_by_instagram関数の実行
  get_images_by_instagram()