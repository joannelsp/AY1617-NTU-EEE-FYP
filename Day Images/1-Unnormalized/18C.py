import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('B1.jpg')
b,g,r = cv2.split(img)
[rows,cols] = np.shape(b)
matrix_C = np.zeros((rows,cols))
for i in range(rows):
    for j in range(cols):
        U = np.array(b[i,j])
        V = np.array(g[i,j])
        W = np.array(r[i,j])
        matrix_C[i,j] = np.maximum.reduce([U,V,W]) - np.minimum.reduce([U,V,W])
plt.subplot(221), plt.imshow(matrix_C,'gray')
plt.subplot(222), plt.hist(matrix_C.flatten(),255,[0,255])
plt.xlim([0,255])
plt.show()
