import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('B1.jpg')
Lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
L,a,b = cv2.split(Lab)
min_value = np.min(L) #57
max_value = np.max(L) #255
range_value = max_value - min_value
new_matrix = a.astype(float)
arr = ((new_matrix - min_value)/range_value)*255
final_matrix = arr.astype(int)

plt.subplot(221), plt.imshow(final_matrix,'gray')
plt.subplot(222), plt.hist(final_matrix.flatten(),255,[0,255],)
plt.xlim([0,255])
plt.show()
