import cv2
import numpy as np

num = 766
while num in (766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798):
    x = str(num)+"img.png"
    y = str(num)+"-GT.png"
    z = str(num)+"img_15GdB_GT.png"
    img = cv2.imread(x)
    b,g,r = cv2.split(img)
    img1 = cv2.imread(y)
    imGT = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    [rows,cols] = np.shape(b)
    matrix_GdivB = np.zeros((rows,cols))
    for i in range(rows):
        for j in range(cols):
            matrix_GdivB[i,j]= float(g[i,j])/float(b[i,j])
    min_value = np.min(matrix_GdivB)
    max_value = np.max(matrix_GdivB)
    range_value = max_value - min_value
    new_matrix = matrix_GdivB.astype(float)
    arr1 = ((new_matrix - min_value)/range_value)*255
    final_matrix = arr1.astype(np.uint8)
    thresh, bw_im = cv2.threshold(final_matrix,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imwrite(z,bw_im)
    
    err = bw_im.astype("float") - imGT.astype("float")
    percentage_err = np.count_nonzero(err)/(float(bw_im.shape[0]*bw_im.shape[1]))*100
    print percentage_err
    num += 1
