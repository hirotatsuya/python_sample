# ============================================
#
# bitflyer_api.py
# Created by hirotatsu on 2017/12/07
#
# ============================================

# 必要なライブラリのimport
import requests
import time
import hmac
import hashlib
import json

from config import bitflyer_config

# publicなapiを実行する関数
def public_api(target_path):
  endpoint = 'https://api.bitflyer.jp'
  path = target_path
  response = requests.get(endpoint + path)
  return response.text

# privateなapiを実行する関数
def private_api(target_method, target_path, target_payload={}):
  api_key = str(bitflyer_config.API_KEY)
  api_secret = bytes(str(bitflyer_config.API_SECRET), 'latin-1')
  endpoint = 'https://api.bitflyer.jp'
  timestamp = str(time.time())
  method = target_method
  path = target_path
  payload = str(json.dumps(target_payload))
  text = timestamp + method + path + payload
  sign = hmac.new(api_secret, text.encode('utf-8'), hashlib.sha256).hexdigest()
  headers = {
    'ACCESS-KEY': api_key,
    'ACCESS-TIMESTAMP': timestamp,
    'ACCESS-SIGN': sign,
    'Content-Type': 'application/json'
  }
  if method == 'GET':
    response = requests.get(endpoint + path, data=payload, headers=headers)
  elif method == 'POST':
    response = requests.post(endpoint + path, data=payload, headers=headers)
  return response.text

# public_api関数の実行
path = '/v1/getticker'
print(public_api(path))

# private_api関数の実行
method = 'GET'
path = '/v1/me/getbalance'
print(private_api(method, path))
