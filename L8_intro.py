import cv2
import numpy as np
from random import randint
#read image
I = cv2.imread("Img/8.jpg")
cv2.imshow("image",I)
cv2.waitKey(1)
#convert IMG to gray
gray = cv2.cvtColor(I,cv2.COLOR_RGB2GRAY)
gray4filter = gray.copy()
# truy xuat du lieu anh
for row in range(10):
    for col in range(10):
        print(gray[row,col], end = " ")
    print()
#cach gan du lieu cho anh
for row in range(50,100):
    for col in range(20,50):
        gray[row,col]= 0
cv2.imshow("grayNew", gray)
cv2.waitKey(1)
# implement filter
def mean_3x3(row, col,gray4filter):
    sum_v = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            sum_v = sum_v + gray4filter[i,j]
    sum_v = sum_v/9
    return sum_v
def median_filter(row,col,gray4filter):
    array_value = []
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            array_value.append(gray4filter[i,j])
    array_value.sort()
    return array_value[4]
rows = gray4filter.shape[0]
cols = gray4filter.shape[1]
gray_New = gray4filter.copy()
for row in range (1, rows - 1):
    for col in range (1, cols -1):
        gray_New[row,col] = mean_3x3(row,col,gray4filter)
cv2.imshow("grayNewssssss", gray_New)
cv2.waitKey(1)
gray_s = gray_New.copy()
#lọc median
for row in range (1, rows - 1):
    for col in range (1, cols -1):
        gray_s[row,col] = median_filter(row,col,gray4filter)
cv2.imshow("graycailon", gray_s)
cv2.waitKey()



