import cv2
import numpy as np

num=766

while num in (766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798):
    x = str(num)+"img.png"
    y = str(num)+"-GT.png"
    z = str(num)+"img_4H_GT.png"
    img = cv2.imread(x)
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    img1 = cv2.imread(y)
    imGT = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    min_value = np.min(h)
    max_value = np.max(h)
    range_value = max_value - min_value
    new_matrix = h.astype(float)
    arr1 = ((new_matrix - min_value)/range_value)*255
    final_matrix = arr1.astype(np.uint8)
    thresh, bw_im = cv2.threshold(final_matrix,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    cv2.imwrite(z,bw_im)
    
    err = bw_im.astype("float") - imGT.astype("float")
    percentage_err = np.count_nonzero(err)/(float(bw_im.shape[0]*bw_im.shape[1]))*100
    print percentage_err
    num += 1
