import cv2
import numpy as np

I = cv2.imread("C:\\Users\\ADMIN\\Desktop\\Lesson8-20180824T123334Z-001\\Lesson8\\image1.jpg")
cv2.imshow("original", I)
cv2.waitKey(1)
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("video",frame)
    key = cv2.waitKey(30)
    if key&0xFF == ord('a'):
        cv2.imwrite("image.jpg", frame)
    if key&0xFF == ord('q'):
        break

