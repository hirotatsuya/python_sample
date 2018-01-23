# ============================================
#
# set_cron.py
# Created by hirotatsu on 2017/12/14
#
# ============================================

import re
import slackweb
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from os import path

APP_ROOT = path.dirname(path.dirname(path.abspath(__file__)))

def get_ripple():
  slack = slackweb.Slack(url='https://hooks.slack.com/services/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')

  target_url = 'https://coincheck.com/ja/exchange'

  # phantomjs_path = APP_ROOT + '/node_modules/phantomjs/lib/phantom/bin/phantomjs' # win
  phantomjs_path = APP_ROOT + '/node_modules/phantomjs/bin/phantomjs' # mac

  try:
    browser = webdriver.PhantomJS(executable_path=phantomjs_path)
    browser.get(target_url)
    source = browser.page_source
    # with open('coincheck.html', mode='w', encoding='utf-8') as f:
    #   f.write(html)
    soup = BeautifulSoup(source, 'lxml')
    ripple = soup.find_all(class_=re.compile('currency_desc ng-binding'))[7].text
    nem = soup.find_all(class_=re.compile('currency_desc ng-binding'))[9].text
  finally:
    browser.quit()
  message = '*Ripple Price by coincheck*\n`' + ripple + '`' + '\n*NEM Price by coincheck*\n`' + nem + '`'
  slack.notify(text=message, mrkdwn=True)

if __name__ == '__main__':
  get_ripple()
