import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('B1.jpg')
b,g,r = cv2.split(img)
[rows,cols] = np.shape(b)
matrix_RdivG = np.zeros((rows,cols))
for i in range(rows):
    for j in range(cols):
        matrix_RdivG[i,j]= float(r[i,j])/float(g[i,j])
plt.subplot(221), plt.imshow(matrix_RdivG,'gray')
plt.subplot(222), plt.hist(matrix_RdivG.flatten(),255,[0,255])
plt.xlim([0,255])
plt.show()
