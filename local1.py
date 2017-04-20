import numpy as np
import cv2
from collections import deque
import argparse
import imutils

greenLower = (25, 100, 100)
greenUpper = (80, 255, 255)
yellowLower = (20, 86, 6)
yellowUpper = (64, 255, 255)
output="./input/C4"+"/output.jpg"
im_src = cv2.imread(output)

i = 1
for i in range(1, 33):
    name = "./input/DataSet/"+str(i)+".jpg"
    frame = cv2.imread(name)
    #frame = imutils.resize(frame, width=600)
    h,w=frame.shape[:2]
    nnn="./Matrices/C"+str(1)+"s.npy"
    M2 = np.load(nnn)
    mask=frame
    mask = cv2.warpPerspective(frame, M2, (w, h))
    mask = cv2.GaussianBlur(mask, (11, 11), 0)
    mask=  cv2.medianBlur(mask,5)
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    #cv2.imshow('image',mask)
    img = mask
    #img = np.zeros((h,w,3), np.uint8)
    mask = cv2.inRange(mask, greenLower,greenUpper)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 0:
            cv2.drawContours(img,[c], -1, (0,255,0), 3)
            cv2.imshow('frame',img)
    if cv2.waitKey(1) == 27:
        break

    cv2.waitKey(0)

cv2.destroyAllWindows()
for i in range (1,5):
    cv2.waitKey(1)
