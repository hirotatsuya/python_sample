import requests
from bs4 import BeautifulSoup
import sys
import lxml
import re
import json

def get_image(target_url):
  res = requests.get(target_url, timeout = 10)
  if res.status_code == 200:
    soup = BeautifulSoup(res.text, "html.parser")
    js = soup.find("script", text=re.compile("window._sharedData")).text
    data = js[js.find("{"):js.rfind("}") + 1] 
    results = json.loads(data)['entry_data']['ProfilePage'][0]['user']['media']['nodes']
    image_urls = []
    for i in range(len(results)):
      for j in range(len(results[i]['thumbnail_resources'])):
        image_urls.append(results[i]['thumbnail_resources'][j]['src'])
    for i in range(len(image_urls)):
      url = image_urls[i]
      img = requests.get(url)
      with open('img/' + url.split('/')[-1], 'wb') as f:
        f.write(img.content)
  print('ok')

if __name__ == "__main__":
  target_instagram_id = sys.argv[1]
  target_url = "https://www.instagram.com/" + target_instagram_id
  get_image(target_url)