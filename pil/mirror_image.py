from PIL import Image, ImageOps

im = Image.open('./20160824_863.jpg')
im_mirror = ImageOps.mirror(im)
im_mirror.save('./mirror.jpg', quality=95)
