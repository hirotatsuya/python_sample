# --- coding: utf-8 ---
import requests

# マーケット一覧の取得
def get_market_api():
  # エンドポイントURL
  endpoint = 'https://api.bitflyer.jp'

  # 欲しい情報
  path = '/v1/getmarkets'

  # 完成するURL
  print (endpoint + path)

  # リクエストを送って、レスポンスを受け取っている
  response = requests.get(endpoint + path)
  print (response)

  # 読める形にする
  response = response.text
  return response

# response = get_market_api()
# print (response)


def get_public_api(value):
  response = requests.get('https://api.bitflyer.jp/v1/' + value)
  return response.text

'''
マーケット一覧: getmarkets
板情報: getboard
Ticker: getticker
約定履歴: getexecutions
板の状態: getboardstate
取引所の状態: gethealth
チャット: getchats
'''
response = get_public_api('getticker')
print (response)
