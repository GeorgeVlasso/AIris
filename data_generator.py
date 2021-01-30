import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
from matplotlib.collections import PatchCollection
import matplotlib.gridspec as gridspec
from numpy.random import choice 
from PIL import Image
import cv2
import gc
import os 
import matplotlib as mtl
import progressbar
from time import sleep

for i in xrange(20):
    bar.update(i+1)
    sleep(0.1)
bar.finish()

def colorFader(c1,c2,mix=0): 
    c1=np.array(mtl.colors.to_rgb(c1))
    c2=np.array(mtl.colors.to_rgb(c2))
    return mtl.colors.to_hex((1-mix)*c1 + mix*c2)


def plot_flower(length, width, s_l, s_w, petal_color, img_name):
  fig = plt.figure()
  fig.dpi = 100
  fig.set_size_inches(5, 5)
  ax = fig.add_subplot(111, aspect='equal')
  #fig, ax = plt.subplots()
  def petal(sepal_length, sepal_width, col):
    Path = mpath.Path
    pp1 = mpatches.PathPatch(
    Path([(0, 0), (sepal_width, 0), (sepal_length, sepal_length),(0,sepal_width), (0, 0)],
         [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CURVE3, Path.CURVE3]),
     transform=ax.transData, color = col, fill = True)
    return(pp1)
  def flower():
    collection = []
    for i in range(10):
      pet = petal()
      t2 = mtl.transforms.Affine2D().rotate_deg(-i*36) + ax.transData
      pet.set_transform(t2)
      collection.append(pet)
      return(collection)
      
  for i in range(10):
    if i % 2 != 0:
      pet = petal(s_l,s_w,"green")
      t2 = mtl.transforms.Affine2D().rotate_deg(-i*36) + ax.transData
      pet.set_transform(t2)
      ax.add_patch(pet)
  for i in range(10):
    if i % 2 == 0:
      pet = petal(length,width, petal_color)
      t2 = mtl.transforms.Affine2D().rotate_deg(-i*36) + ax.transData
      pet.set_transform(t2)
      ax.add_patch(pet)
  ax.add_patch(mpatches.Circle((0,0),
                              radius=0.1,
                              color="yellow", fill=True))  
  
  ax.set_xlim((-1,1))
  ax.set_ylim((-1,1))
  ax.axis('off')
  ax.tick_params(axis = 'both', left = 'off', top = 'off', right = 'off', bottom = 'off',
                 labelleft = 'off', labeltop = 'off', labelright = 'off', labelbottom = 'off')
  fig.savefig(path + "/" + str(img_name) + '.png', dpi = 100, bbox_inches = 'tight', pad_inches = 0.0)

  plt.clf()
  plt.close()
  gc.collect()

path = "Flowers"

wd = os.getcwd()

try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)
    
data_codings = np.load("data/train_codings.npy")

from PIL import Image
import cv2
images     = np.zeros((4000,128,128,3))
bar = progressbar.ProgressBar(maxval=data_codings.shape[0], \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(0,data_codings.shape[0]):
  
  k1 = data_codings[i,0]
  k2 = data_codings[i,1]
  k3 = data_codings[i,2]
  k4 = data_codings[i,3]
  k5 = data_codings[i,4]


  plot_flower(k1,k2, k3, k4, colorFader("red", "magenta",k5), str(i))
  
  im  =  np.array(Image.open(path + "/" + str(i)+ ".png").resize((128,128)))

  img = cv2.cvtColor(im, cv2.COLOR_BGRA2BGR).reshape((1,128,128,3))/255.
  images[i,:,:,:] = img
  bar.update(i+1)
  sleep(0.1)
bar.finish()  
np.savez_compressed("train_images.npy", images)      
