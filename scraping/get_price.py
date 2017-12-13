# ============================================
#
# get_price.py
# Created by hirotatsu on 2017/12/13
#
# ============================================

import time
import re
import slackweb
from bs4 import BeautifulSoup
from selenium import webdriver

def get_price():
  slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
  target_url = "https://coincheck.com/ja/exchange"
  try:
    browser = webdriver.Chrome(executable_path='../selenium/chromedriver')
    browser.get(target_url)
    # time.sleep(3)
    html = browser.page_source
    # 取得したhtmlをファイル出力
    # with open('coincheck.html', mode='w', encoding='utf-8') as f:
    #   f.write(html)
    soup = BeautifulSoup(html, 'lxml')
    ripple = soup.find_all(class_=re.compile('currency_desc ng-binding'))[7].text
    print(ripple)
  finally:
    browser.quit()
  # slack.notify(text=ripple, username="bitcoin-bot", mrkdwn=True)

if __name__ == "__main__":
  get_price()