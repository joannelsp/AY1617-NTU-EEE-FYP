import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('B1.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
min_value = np.min(h) #0
max_value = np.max(h) #170
range_value = max_value - min_value
new_matrix = h.astype(float)
arr1 = ((new_matrix - min_value)/range_value)*255
final_matrix = arr1.astype(int)

plt.subplot(221), plt.imshow(final_matrix,'gray')
plt.subplot(222), plt.hist(final_matrix.flatten(),255,[0,255])
plt.xlim([0,255])
plt.show()
