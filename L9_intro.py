#xu li anh
#Silf( for com)
#Surf(for mob)
#Fast(for mob)

import cv2
import numpy as np

I = cv2.imread("C:\\Users\\ADMIN\\Desktop\\Lesson8-20180824T123334Z-001\\Lesson8\\DP7_EN_3.png")
cv2.imshow("original", I)
cv2.waitKey(1)
            # cap = cv2.VideoCapture(0)
            # while True:
            #     ret, frame = cap.read()
            #     cv2.imshow("video",frame)
            #     key = cv2.waitKey(30)
            #     if key&0xFF == ord('a'):
            #         cv2.imwrite("image.jpg", frame)
            #     if key&0xFF == ord('q'):
            #         break

# convert to rgb
gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayImg",gray)
cv2.waitKey(1)
#detect siFt
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray, None)
newImg = I.copy()
cv2.drawKeypoints(I, kp1, newImg)
cv2.imshow("keypoint",newImg)
cv2.waitKey(1)
#load 2th
I2 = cv2.imread("C:\\Users\\ADMIN\\Desktop\\Lesson8-20180824T123334Z-001\\Lesson8\\3image.png")
cv2.waitKey(1)
# convert to rgb
gray2 = cv2.cvtColor(I2,cv2.COLOR_BGR2GRAY)
cv2.waitKey(1)
#detect siFt
sift2 = cv2.xfeatures2d.SIFT_create()
kp2, des2 = sift2.detectAndCompute(gray2, None)
newImg2 = I2.copy()
cv2.drawKeypoints(I2, kp2, newImg2)
cv2.imshow("keypoint2",newImg2)
cv2.waitKey(1)
#matching Image
bf = cv2.BFMatcher_create()
matches = bf.knnMatch(des1, des2, k = 2)
matchesImg = cv2.drawMatchesKnn(I,kp1,I2,kp2,matches, None)
cv2.imshow("Matches",matchesImg)
cv2.waitKey(1)
#choose good points
good = []
for m, n in matches:
    if m.distance < 0.7* n.distance:
        good.append(m)
goodMatch_Img = cv2.drawMatches(I,kp1,I2,kp2,good,None)
cv2.imshow("goodMatches",goodMatch_Img)
cv2.waitKey()