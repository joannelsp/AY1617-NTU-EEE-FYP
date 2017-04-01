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
min_value = np.min(matrix_C) #0
max_value = np.max(matrix_C) #105
range_value = max_value - min_value
new_matrix = matrix_C.astype(float)
arr1 = ((new_matrix - min_value)/range_value)*255
final_matrix = arr1.astype(int)
print min_value, max_value, final_matrix
plt.subplot(221), plt.imshow(final_matrix,'gray')
plt.subplot(222), plt.hist(final_matrix.flatten(),255,[0,255])
plt.xlim([0,255])
plt.show()
