import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math as math
import scipy.ndimage.filters as filters
from pims import ND2_Reader

file = 'D:\\ykwang\\Data\\Growth Rate\\phase_3\\20161213\\20161213.nd2'

frames = ND2_Reader(file)

frames.default_coords['c'] = 0  # 0 is the default setting
img = frames[0]

img_max = filters.maximum_filter(img,size=(10,10),mode='reflect')
img_min = filters.minimum_filter(img,size=(10,10),mode='reflect')
img_range = img_max - img_min

plt.imshow(img,cmap='Greys')
plt.show()

frames.close()






