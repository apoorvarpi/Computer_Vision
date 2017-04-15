import numpy as np
import cv2
from collections import deque
import argparse
import imutils

cap = cv2.VideoCapture(-1)
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
output="./input/C4"+"/output.jpg"
im_src = cv2.imread(output)

while(cap.isOpened()):

    ret, frame = cap.read()
    # Our operations on the frame come here
    if ret==True:
        #print 'a ma'
        frame = imutils.resize(frame, width=600)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        #hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        hsv=frame
        mask=hsv
        h,w=mask.shape[:2]
        #mask= cv2.resize(mask, (w, h)) 
        nnn="./Matrices/pres"+str(1)+".npy"
        M2 = np.load(nnn,)
        #print M2
        #M2=np.array([[5.0,0.0,1.0],[5.0,0.0,1.0],[5.0,0.0,1.0]])
        mask = cv2.warpPerspective(mask, M2, (w, h))
        
        mask=  cv2.medianBlur(mask,5)
        mask = cv2.inRange(mask, (0, 0, 0, 0), (180, 255, 30, 0));
        
        #mask = cv2.inRange(hsv, greenLower, greenUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        mask=cv2.bitwise_not(mask)
        cv2.imshow('image',mask)
        cv2.waitKey(30)
        img = np.zeros((512,512,3), np.uint8)
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
        #center = None 
        #if len(cnts) > 0:
        for c in cnts:
            area = cv2.contourArea(c)
            print area
            if area > 0:
                cv2.drawContours(img,[c], -1, (0,255,0), 3)
                cv2.imshow('frame',img)
            #print(cnts)
        # Display the resulting frame
        #cv2.imshow('frame',mask)
    #print 'pp
    if cv2.waitKey(1) == 27:
        print 'okk\n'
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
for i in range (1,5):
    cv2.waitKey(1)
