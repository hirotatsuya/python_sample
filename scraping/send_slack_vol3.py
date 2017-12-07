import requests
import slackweb
from bs4 import BeautifulSoup
import lxml

def lambda_handler(event, context):
  target_url = "https://bitflyer.jp/ja-jp"
  response = requests.get(target_url)
  soup = BeautifulSoup(response.text, "lxml")
  ask = soup.find(id="bfPriceAsk_1").text
  bid = soup.find(id="bfPriceBid_1").text
  value = "ASK: " + ask + "BTC\nBID: " + bid + "BTC"
  slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
  slack.notify(text=value)
