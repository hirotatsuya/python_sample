# ============================================
#
# send_btc_to_slack_by_bitflyer.py
# Created by hirotatsu on 2017/12/07
#
# ============================================

# 必要なライブラリのimport
import requests
import slackweb
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# 現在時刻の取得
def get_datetime():

  # 現在時刻を取得して、9時間プラスする
  value = datetime.now() + timedelta(hours=9)

  # datetime型かた文字列型に変換
  return value.strftime("%Y/%m/%d %H:%M:%S")

# bitflyerからビットコインの値段をスクレイピングしてslackに通知する関数
def send_btc_to_slack_by_bitflyer():

  # slackのwebhook用のURL
  slack = slackweb.Slack(url="https://hooks.slack.com/services/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")

  # bitflyerのURL(スクレイピング対象)
  target_url = "https://bitflyer.jp/ja-jp"

  # target_urlのhtml情報を取得
  response = requests.get(target_url)

  # responseのtext部分のみスクレイピング
  soup = BeautifulSoup(response.text, "html.parser")

  # idを指定して検索し、一致した部分のtext部分をスクレイピング
  ask = soup.find(id="bfPriceAsk_1").text
  bid = soup.find(id="bfPriceBid_1").text

  # 文字列を整形
  ask_value = "ASK: `" + ask + "`BTC"
  bid_value = "BID: `" + bid + "`BTC"
  title = "*bitcoin ASK and BID by bitflyer*"

  # 現在時刻の取得
  now = "_" + get_datetime() + "_"

  # valueの生成
  value = title + "\n" + now + "\n" + ask_value + "\n" + bid_value

  # slackに通知(markdown記法の使用を指定)
  slack.notify(text=value, username="bitcoin-bot", mrkdwn=True)

# メイン
if __name__ == "__main__":

  # send_btc_to_slack_by_bitflyer関数の実行
  send_btc_to_slack_by_bitflyer()