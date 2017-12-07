import requests
import slackweb
from bs4 import BeautifulSoup

def get_response_by_bitflyer():
  target_url = "https://bitflyer.jp/ja-jp"
  response = requests.get(target_url)
  return response

def get_soup(response):
  soup = BeautifulSoup(response.text, "html.parser")
  return soup

def get_ask():
  response = get_response_by_bitflyer()
  soup = get_soup(response)
  ask = soup.find(id="bfPriceAsk_1").text
  return ask

def get_bid():
  response = get_response_by_bitflyer()
  soup = get_soup(response)
  bid = soup.find(id="bfPriceBid_1").text
  return bid

def get_btc():
  ask = get_ask()
  bid = get_bid()
  value = "ASK: " + ask + "BTC\nBID: " + bid + "BTC"
  return value

def send_slack(event, context):
  value = get_btc()
  slack = slackweb.Slack(url="https://hooks.slack.com/services/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")
  slack.notify(text=value)
