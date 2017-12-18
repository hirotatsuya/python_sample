import numpy as np
import mahotas as mh
from glob import glob
from mahotas.features import surf
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfTransformer

picture_category_num = 10
feature_category_num = 512

# image surf
images = glob('./*.jpg')
alldescriptors = []
for im in images:
  im = mh.imread(im, as_grey=True)
  im = im.astype(np.uint8)
  alldescriptors.append(surf.surf(im, descriptor_only=True))

# image surf -> basic feature
concatenated = np.concatenate(alldescriptors)
km = KMeans(feature_category_num)
km.fit(concatenated)

# image surf and basic feature -> features
features = []
for d in alldescriptors:
  c = km.predict(d)
  features.append(np.array([np.sum(c == ci) for ci in range(feature_category_num)]))
features = np.array(features)

# features -> tfidf
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(features)
tfidf.toarray() 
# not use tfidf
# tfidf = features

# categorization
km = KMeans(n_clusters=picture_category_num, init='random', n_init=1, verbose=1)
km.fit(tfidf)

# print result
images = np.array(images)
print('images')
print(images)
for i in range(picture_category_num):
  print('image category{0}'.format(i))
  print(images[km.labels_ == i])
