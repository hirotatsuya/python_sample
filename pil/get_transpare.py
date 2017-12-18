# ============================================
#
# get_transpare.py
# Created by hirotatsu on 2017/12/08
#
# ============================================

from PIL import Image # pip install pillow

# 透過したい画像を読み込み
path = 'original.png'
org = Image.open(path)

# 読み込んだ画像と同じサイズの画像を作成
trans = Image.new('RGBA', org.size, (0,0,0,0))

width = org.size[0]
height = org.size[1]

for x in range(width):
  for y in range(height):
    pixel = org.getpixel((x, y))

    # 白なら処理しない
    if pixel[0] == 255 and pixel[1] == 255 and pixel[2] == 255:
      continue
    
    # 白以外なら用意した画像にピクセルを書き込み
    trans.putpixel((x, y), pixel)

# 透過後の画像を保存
trans.save('trans.png')