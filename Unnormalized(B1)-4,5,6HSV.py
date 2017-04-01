import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('B1.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
plt.subplot(221), plt.imshow(h,'gray')
plt.subplot(222), plt.hist(h.flatten(),255,[0,255])
plt.xlim([0,255])
plt.show()
