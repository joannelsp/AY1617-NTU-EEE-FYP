import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('B1.jpg')
b,g,r = cv2.split(img)
[rows,cols] = np.shape(b)
matrix_Y = np.zeros((rows,cols))
matrix_I = np.zeros((rows,cols))
matrix_Q = np.zeros((rows,cols))
for i in range(rows):
    for j in range(cols):
        matrix_Y[i,j]= float(0.299*(r[i,j]))+float(0.587*(g[i,j]))+float(0.114*(b[i,j]))
        matrix_I[i,j]= float(0.596*(r[i,j]))-float(0.274*(g[i,j]))-float(0.322*(b[i,j]))
        matrix_Q[i,j]= float(0.211*(r[i,j]))-float(0.523*(g[i,j]))+float(0.312*(b[i,j]))
min_value = np.min(matrix_Y) #48.878
max_value = np.max(matrix_Y) #254.701
range_value = max_value - min_value
new_matrix = matrix_Y.astype(float)
arr = ((new_matrix - min_value)/range_value)*255
final_matrix = arr.astype(int)

plt.subplot(221), plt.imshow(final_matrix,'gray')
plt.subplot(222), plt.hist(final_matrix.flatten(),255,[0,255])
plt.xlim([0,255])
plt.show()
