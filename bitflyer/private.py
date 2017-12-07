# --- coding: utf-8 ---
import requests
import time
import hmac
import hashlib

# API_KEYとAPI_SECRETの取得
from config import bitflyer_config

# API keyとAPI secret
api_key = str(bitflyer_config.API_KEY)
api_secret = bytes(str(bitflyer_config.API_SECRET), 'latin-1')

# 資産残高を取得
def get_balance_api():
  # エンドポイントURL
  endpoint = "https://api.bitflyer.jp"

  # 認証情報の作成
  method = "GET"
  path = "/v1/me/getbalance"
  timestamp = str(time.time())

  text = timestamp + method + path

  sign = hmac.new(api_secret, text.encode('utf-8'), hashlib.sha256).hexdigest()

  # ヘッダの情報
  headers_info = {
    'ACCESS-KEY': api_key,
    'ACCESS-TIMESTAMP': timestamp,
    'ACCESS-SIGN': sign,
    'Content-Type': 'application/json'
  }

  #リクエストを送って、レスポンスを受け取る
  response = requests.get(endpoint + path, headers=headers_info)
  print('HTTP Status code', response)
  response_text = response.text

  return response_text

# response = get_balance_api()
# print(response)

def get_private_api(value):
  endpoint = "https://api.bitflyer.jp"
  method = "GET"
  path = "/v1/me/getbalance"
  timestamp = str(time.time())
  text = timestamp + method + path
  sign = hmac.new(api_secret, text.encode('utf-8'), hashlib.sha256).hexdigest()
  headers_info = {
    'ACCESS-KEY': api_key,
    'ACCESS-TIMESTAMP': timestamp,
    'ACCESS-SIGN': sign,
    'Content-Type': 'application/json'
  }
  response = requests.get(endpoint + path, headers=headers_info)
  response_text = response.text
  return response_text
