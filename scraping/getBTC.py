# coding: UTF-8
import requests
import slackweb
from bs4 import BeautifulSoup
from datetime import datetime

def get_bfPriceAsk_1():
  target_url = 'https://bitflyer.jp/ja-jp'
  res = requests.get(target_url)
  soup = BeautifulSoup(res.text, 'lxml')
  return soup.find(id="bfPriceAsk_1").text

def get_bfPriceBid_1():
  target_url = 'https://bitflyer.jp/ja-jp'
  res = requests.get(target_url)
  soup = BeautifulSoup(res.text, 'lxml')
  return soup.find(id="bfPriceBid_1").text

slack = slackweb.Slack(url="https://hooks.slack.com/services/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")

# slack.notify(text=get_ticker())
nowdate = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
slack.notify(text=nowdate)
slack.notify(text="Ask: " + str(get_bfPriceAsk_1()))
slack.notify(text="Bid: " + str(get_bfPriceBid_1()))

