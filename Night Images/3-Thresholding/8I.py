import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('757img.png')
b,g,r = cv2.split(img)
img1 = cv2.imread('757-GT.png')
imGT = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

[rows,cols] = np.shape(b)
matrix_I = np.zeros((rows,cols))

for i in range(rows):
    for j in range(cols):
        matrix_I[i,j]= float(0.596*(r[i,j]))-float(0.274*(g[i,j]))-float(0.322*(b[i,j]))
min_value = np.min(matrix_I) #-48.332
max_value = np.max(matrix_I) #5.734
range_value = max_value - min_value
new_matrix = matrix_I.astype(float)
arr = ((new_matrix - min_value)/range_value)*255
final_matrix = arr.astype(np.uint8)
thresh, bw_im = cv2.threshold(final_matrix,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite('757img_8I_GT.png',bw_im)

err = bw_im.astype("float") - imGT.astype("float")
percentage_err = np.count_nonzero(err)/(float(bw_im.shape[0]*bw_im.shape[1]))*100
print percentage_err
