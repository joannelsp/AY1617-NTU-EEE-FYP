import cv2
import numpy as np
from matplotlib import pyplot as plt

num = 320
while num in (319,320,321):
    x = str(num)+"img.png"
    y = str(num)+"-GT.png"
    z = str(num)+"img_13RdB_GT.png"
    img = cv2.imread(x)
    b,g,r = cv2.split(img)
    img1 = cv2.imread(y)
    imGT = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    [rows,cols] = np.shape(b)
    matrix_RdivB = np.zeros((rows,cols))
    for i in range(rows):
        for j in range(cols):
            matrix_RdivB[i,j]= float(r[i,j])/float(b[i,j])
    min_value = np.min(matrix_RdivB)
    max_value = np.max(matrix_RdivB)
    range_value = max_value - min_value
    new_matrix = matrix_RdivB.astype(float)
    arr = ((new_matrix - min_value)/range_value)*255
    final_matrix = arr.astype(np.uint8)
    thresh, bw_im = cv2.threshold(final_matrix,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imwrite(z,bw_im)
    
    err = bw_im.astype("float") - imGT.astype("float")
    percentage_err = np.count_nonzero(err)/(float(bw_im.shape[0]*bw_im.shape[1]))*100
    print percentage_err
    num += 1
