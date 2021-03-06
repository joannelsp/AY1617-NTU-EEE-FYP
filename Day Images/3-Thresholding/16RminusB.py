import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('U9.jpg')
b,g,r = cv2.split(img)
img1 = cv2.imread('U9_GT.jpg')
imGT = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
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
final_matrix = arr1.astype(np.uint8)
thresh, bw_im = cv2.threshold(final_matrix,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
plt.subplot(221), plt.imshow(bw_im,'gray')
plt.subplot(222), plt.imshow(imGT,'gray')
plt.show()

err = bw_im.astype("float") - imGT.astype("float")
percentage_err = np.count_nonzero(err)/(float(bw_im.shape[0]*bw_im.shape[1]))*100
print percentage_err
