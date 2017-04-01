import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('B1.jpg')
b,g,r = cv2.split(img)
y = 0.299*r + 0.587*g + 0.114*b
i = 0.596*r - 0.274*g - 0.322*b
q = 0.211*r - 0.523*g + 0.312*b
plt.subplot(221), plt.imshow(y,'gray')
plt.subplot(222), plt.hist(y.flatten(),255,[0,255])
plt.subplot(223), plt.imshow(i,'gray')
plt.subplot(224), plt.hist(i.flatten(),255,[0,255])
plt.xlim([0,255])
plt.show()
