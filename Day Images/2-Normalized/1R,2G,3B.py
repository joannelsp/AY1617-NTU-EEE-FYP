import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('B1.jpg')
b,g,r = cv2.split(img)
min_value = np.min(r)
max_value = np.max(r)
range_value = max_value - min_value
new_r = r.astype(float)
arr = ((new_r - min_value)/range_value)*255
final_r = arr.astype(int)
plt.subplot(221), plt.imshow(final_r,'gray')
plt.subplot(222), plt.hist(final_r.flatten(),255,[0,255])
plt.xlim([0,255])
plt.show()
