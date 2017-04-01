import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('U9.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
img1 = cv2.imread('U9_GT.jpg')
imGT = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
min_value = np.min(h) #0
max_value = np.max(h) #170
#min_value = np.min(s) #0
#max_value = np.max(s) #195
#min_value = np.min(v) #92
#max_value = np.max(v) #255
range_value = max_value - min_value
new_matrix = h.astype(float)
#new_matrix = s.astype(float)
#new_matrix = v.astype(float)
arr1 = ((new_matrix - min_value)/range_value)*255
final_matrix = arr1.astype(np.uint8)
thresh, bw_im = cv2.threshold(final_matrix,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
plt.subplot(221), plt.imshow(bw_im,'gray')
plt.subplot(222), plt.imshow(imGT,'gray')
plt.show()

err = bw_im.astype("float") - imGT.astype("float")
percentage_err = np.count_nonzero(err)/(float(bw_im.shape[0]*bw_im.shape[1]))*100
print percentage_err
