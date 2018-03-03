# ============================================
#
# get_news_by_yahoo.py
# Created by hirotatsu on 2017/12/07
#
# ============================================

import requests
from bs4 import BeautifulSoup
import re
import slackweb
import lxml

def get_news_by_yahoo():
  # slack webhook
  slack = slackweb.Slack(url="https://hooks.slack.com/services/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")

  # 初回のみ
  target_url = "https://www.yahoo.co.jp/"
  # Requestsを使って、webから取得
  r = requests.get(target_url)
  # 要素を解析
  soup = BeautifulSoup(r.text, 'lxml')

  # HTMLファイルとして保存したい場合はファイルオープンして保存
  # with open('originDataOld.html', mode='w', encoding = 'utf-8') as fw:
  #     fw.write(soup.prettify())

  # soup.find_allを用いてリンク先が「news.yahoo.co.jp/pickup」の項目を全て取得
  elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
  for e in elems:
      # print(e.getText())
      slack.notify(text="*" + e.getText() + "*", username="yahoonews-bot", icon_emoji=":new:", mrkdwn=True)

# メイン
if __name__ == "__main__":

  # get_news_by_yahoo関数の実行
  get_news_by_yahoo()
