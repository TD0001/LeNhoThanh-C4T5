import cv2
import numpy as np

I = cv2.imread("C:\\Users\\ADMIN\\Desktop\\barrons-how-to-prepare-for-the-sat.jpeg")


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

#detect siFt
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray, None)
newImg = I.copy()
cv2.drawKeypoints(I, kp1, newImg)

#load 2th
cap = cv2.VideoCapture(0)
while True:

    red, I2 = cap.read()
    # convert to rgb
    gray2 = cv2.cvtColor(I2,cv2.COLOR_BGR2GRAY)
    cv2.waitKey(1)
    #detect siFt
    sift2 = cv2.xfeatures2d.SIFT_create()
    kp2, des2 = sift2.detectAndCompute(gray2, None)
    #matching Image
    bf = cv2.BFMatcher_create()
    if des2 is None:
        continue
    if len(des2)>4:
        matches = bf.knnMatch(des1, des2, k = 2)
        #choose good points
        good = []
        for m, n in matches:
            if m.distance < 0.7* n.distance:
                good.append(m)
        goodMatch_Img = cv2.drawMatches(I,kp1,I2,kp2,good,None)
        cv2.imshow("goodMatches",goodMatch_Img)
        cv2.waitKey(1)