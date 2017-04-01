import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('B1.jpg')
Lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
L,a,b = cv2.split(Lab)
plt.subplot(221), plt.imshow(L,'gray')
plt.subplot(222),plt.hist(L.flatten(),255,[0,255])
plt.subplot(223), plt.imshow(a,'gray')
plt.subplot(224),plt.hist(a.flatten(),255,[0,255])
plt.xlim([0,255])
plt.show()
