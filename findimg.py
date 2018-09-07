import cv2
import numpy as np
from os import listdir
from os.path import isfile, join

mypath = "C:\\Users\\ADMIN\\Desktop\\folder\\Lesson8"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = np.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
    images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
    # cv2.imshow(str(n+1), images[n])
    # cv2.waitKey(1)
I = cv2.imread("C:\\Users\\ADMIN\\Desktop\\Untitled.png")
cv2.imshow("original",I)
cv2.waitKey(1)
# convert to gray
gray = cv2.cvtColor(I,cv2.COLOR_BGR2GRAY)
cv2.imshow("grayImg",gray)
cv2.waitKey(1)
#detect siFt
sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray, None)
newImg = I.copy()
cv2.drawKeypoints(I, kp1, newImg)
cv2.imshow("keypoint",newImg)
cv2.waitKey(0)
s = 0
k = False
for i in range(len(onlyfiles)):
    # convert to rgb
    gray2 = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
    cv2.waitKey(1)
    # detect siFt
    sift2 = cv2.xfeatures2d.SIFT_create()
    kp2, des2 = sift2.detectAndCompute(gray2, None)
    newImg2 = images[i].copy()
    cv2.drawKeypoints(images[i], kp2, newImg2)
            # cv2.imshow("keypoint2", newImg2)
            # cv2.waitKey(1)
    # matching Image
    bf = cv2.BFMatcher_create()
    matches = bf.knnMatch(des1, des2, k=2)
    matchesImg = cv2.drawMatchesKnn(I, kp1, images[i], kp2, matches, None)
        # cv2.imshow("Matches", matchesImg)
        # cv2.waitKey(1)
    # choose good points
    good = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good.append(m)
    goodMatch_Img = cv2.drawMatches(I, kp1, images[i], kp2, good, None)
        # cv2.imshow("goodMatches", goodMatch_Img)
        # cv2.waitKey()
    s = len(good)
    if s > 200:
        cv2.imshow("goodMatches", goodMatch_Img)
        cv2.imshow("anh trong folder", images[i])
        cv2.waitKey(0)
        print("co anh trong folder")
        k = True
if k == False:
    # I2 = cv2.imread("C:\\Users\\ADMIN\\Desktop\\lol.png")
    # cv2.imshow("haha", I2)
    # cv2.waitKey()
    print("deo co anh")


