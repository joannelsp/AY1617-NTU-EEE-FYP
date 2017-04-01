import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('B1.jpg')
b,g,r = cv2.split(img)
[rows,cols] = np.shape(b)
matrix_RminusB = np.zeros((rows,cols))
for i in range(rows):
    for j in range(cols):
        matrix_RminusB[i,j]= float(r[i,j])-float(b[i,j])
min_value = np.min(matrix_RminusB) #-105.0
max_value = np.max(matrix_RminusB) #11.0
range_value = max_value - min_value
new_matrix = matrix_RminusB.astype(float)
arr1 = ((new_matrix - min_value)/range_value)*255
final_matrix = arr1.astype(int)
print min_value, max_value, arr1
plt.subplot(221), plt.imshow(final_matrix,'gray')
plt.subplot(222), plt.hist(final_matrix.flatten(),255,[0,255])
plt.xlim([0,255])
plt.show()
