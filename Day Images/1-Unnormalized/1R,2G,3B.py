import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('B1.jpg')
b,g,r = cv2.split(img)
plt.subplot(221), plt.imshow(r,'gray')
plt.subplot(222), plt.hist(r.flatten(),255,[0,255])
plt.xlim([0,255])
plt.show()
print min(r.flatten()),max(r.flatten())
