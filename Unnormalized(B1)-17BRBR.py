import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('B1.jpg')
b,g,r = cv2.split(img)
[rows,cols] = np.shape(b)
matrix_BRBR = np.zeros((rows,cols))
for i in range(rows):
    for j in range(cols):
        matrix_BRBR[i,j]= (float(b[i,j])-float(r[i,j]))/(float(b[i,j])+float(r[i,j]))
plt.subplot(221), plt.imshow(matrix_BRBR,'gray')
plt.subplot(222), plt.hist(matrix_BRBR.flatten(),255,[0,255])
plt.xlim([0,255])
plt.show()
