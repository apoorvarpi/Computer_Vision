import numpy as np
import cv2
from collections import deque
import argparse
import imutils

def local(xx):
    cap = cv2.VideoCapture(1)
    greenLower = (25, 100, 100)
    greenUpper = (80, 255, 255)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    output="./input/C4"+"/output.jpg"
    im_src = cv2.imread(output)

    while(cap.isOpened()):

        ret, frame = cap.read()
        # Our operations on the frame come here
        if ret==True:
            frame = imutils.resize(frame, width=600)
            frame = cv2.GaussianBlur(frame, (11, 11), 0)
            nnn="./Matrices/C"+str(xx)+".npy"
            M2 = np.load(nnn)
            h,w=frame.shape[:2]
            mask = cv2.warpPerspective(frame, M2,(w, h))
            cv2.imshow('first image',mask)
            cv2.waitKey(30)
            mask = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
            mask=  cv2.medianBlur(mask,5)
            #mask = cv2.inRange(mask, (0, 0, 0, 0), (180, 255, 30, 0))    # for segmenting into black and white
            mask = cv2.inRange(mask, greenLower, greenUpper)
            mask = cv2.erode(mask, None, iterations=2)
            mask = cv2.dilate(mask, None, iterations=2)
            #mask=cv2.bitwise_not(mask)  # for detecting white color on black blackground
            cv2.imshow('image',mask)
            cv2.waitKey(30)
            img = np.zeros((512,512,3), np.uint8)
            cnts = cv2.findContours(mask.copy(), cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]
            for c in cnts:
                area = cv2.contourArea(c)
                #print area
                if area > 5000:
                    M = cv2.moments(c)
                    X = int(M["m10"] / M["m00"])
                    Y = int(M["m01"] / M["m00"])
                    #print X, Y
                    cv2.drawContours(img,[c], -1, (0,255,0), 3)
                    cv2.imshow('frame',img)
            # Display the resulting frame
            #cv2.imshow('frame',img)
        if cv2.waitKey(1) == 27:
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

local(1)
