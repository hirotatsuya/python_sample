import requests
import slackweb
from bs4 import BeautifulSoup

def get_soup_by_id(response, target_id):
  soup = BeautifulSoup(response.text, "html.parser")
  value = soup.find(id=target_id).text
  return value

def get_btc():
  target_url = "https://bitflyer.jp/ja-jp"
  response = requests.get(target_url)
  ask = get_soup_by_id(response, "bfPriceAsk_1")
  bid = get_soup_by_id(response, "bfPriceBid_1")
  value = "ASK: " + ask + "BTC\nBID: " + bid + "BTC"
  return value

def send_slack(event, context):
  value = get_btc()
  slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
  slack.notify(text=value)

