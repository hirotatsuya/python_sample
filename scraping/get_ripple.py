# ============================================
#
# get_ripple.py
# Created by hirotatsu on 2017/12/14
#
# ============================================

# 必要なライブラリのimport
import re
import slackweb
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver

# coincheckのサイトにアクセスしてRippleの現在の値段をスクレイピングしてslackに通知する関数
def get_ripple():
  # slackのwebhookのURL
  slack = slackweb.Slack(url='https://hooks.slack.com/services/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')

  # coincheckのURL
  target_url = 'https://coincheck.com/ja/exchange'

  # phantomjsのpath
  # windowsの場合
  phantomjs_path = '../node_modules/phantomjs/lib/phantom/bin/phantomjs'
  # macの場合
  # phantomjs_path = '../node_modules/phantomjs/bin/phantomjs'

  try:
    # seleniumによりphantomjsを起動
    browser = webdriver.PhantomJS(executable_path=phantomjs_path)

    # phantomjsでcoincheckにアクセス
    browser.get(target_url)

    # JavaScriptのレンダリング後のcoincheckのサイトのソースを取得
    source = browser.page_source

    # 取得したhtmlをファイル出力
    with open('coincheck.html', mode='w', encoding='utf-8') as f:
      f.write(source)

    # htmlを解析
    soup = BeautifulSoup(source, 'lxml')

    # Rippleの値段をスクレイプ
    ripple = soup.find_all(class_=re.compile('currency_desc ng-binding'))[7].text

    # print(ripple)
  finally:
    # ブラウザを終了
    browser.quit()
  message = '*Ripple Price*\n`' + ripple + '`'
  # markdownを使ってslackに通知
  slack.notify(text=message, mrkdwn=True)

# 関数を実行
if __name__ == '__main__':
  get_ripple()
