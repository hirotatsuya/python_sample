import requests
import config
from PIL import Image

def image_influence_api(img):
  url = 'https://api.a3rt.recruit-tech.co.jp/image_influence/v1/meat_score'
  params = {
    'apikey': config.IMAGE_INFLUENCE_API_KEY,
    'predict': 5,
  }
  imagefile = {
    'imagefile': open(img, 'rb'),
  }
  res = requests.post(url, params, files=imagefile)
  print(res.text)

img = '../scraping/images/_hirotatsu_24124983_944592815694338_3262158318512111616_n.jpg'
image_influence_api(img)
