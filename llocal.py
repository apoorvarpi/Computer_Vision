import numpy as np
import cv2
import math
from collections import deque
import argparse
import imutils

#cap1 = cv2.VideoCapture(1)
#cap1 = cv2.VideoCapture('http://172.16.15.215:8081/')
cap1 = cv2.VideoCapture('http://rit2014044:iiita665@172.16.15.215:8081/?action=stream?dummy=param.mjpg')
cap2 = cv2.VideoCapture('http://rit2014044:iiita665@172.16.15.245:8081/?action=stream?dummy=param.mjpg')
cap3=cap1
cap4=cap1
#cap3 = cv2.VideoCapture(2)
#cap4 = cv2.VideoCapture(3)
greenLower = (25, 100, 100)
greenUpper = (80, 255, 255)
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
output="./input/C4"+"/output.jpg"
im_src = cv2.imread(output)
goal=np.array([100,100])
Pa=np.array([0,0])
Pb=np.array([0,0])
Pc=np.array([0,0])
Pd=np.array([0,0])

def local(xx):
	global Pa,Pb,Pc,Pd,goal,greenUpper,greenLower
	if xx==1:
		ret, frame = cap1.read()
		#greenLower = (23, 29, 20)
		#greenUpper = (78, 100, 100)
	if xx==2:
		ret, frame = cap2.read()
	if xx==3:
		ret, frame = cap3.read()
	if xx==4:
		ret, frame = cap4.read()
	# Our operations on the frame come here
	if ret==True:
		#frame = imutils.resize(frame, width=600)
		frame = cv2.GaussianBlur(frame, (11, 11), 0)
		nnn="./Matrices/C"+str(1)+".npy"
		M2 = np.load(nnn)
		h,w=frame.shape[:2]
		mask = cv2.warpPerspective(frame, M2,(w, h))
		cv2.imshow('first image'+str(xx),mask)
		cv2.waitKey(30)
		mask = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
		mask=  cv2.medianBlur(mask,5)
		#mask = cv2.inRange(mask, (0, 0, 0, 0), (180, 255, 30, 0))# for segmenting into black and white
		mask = cv2.inRange(mask, greenLower, greenUpper)
		mask = cv2.erode(mask, None, iterations=2)
		mask = cv2.dilate(mask, None, iterations=2)
		#mask=cv2.bitwise_not(mask)  # for detecting white color on black blackground
		#cv2.imshow('image',mask)
		#cv2.waitKey(30)
		img = np.zeros((512,512,3), np.uint8)
		cnts = cv2.findContours(mask.copy(), cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]
		for c in cnts:
			area = cv2.contourArea(c)
			print (area)
			if area > 50:
				M = cv2.moments(c)
				X = int(M["m10"] / M["m00"])
				Y = int(M["m01"] / M["m00"])
				#print X, Y
                #cv2.drawContours(img,[c], -1, (0,255,0), 3)
				if xx == 1:
					temp=np.array([X,Y])
					t1=np.vstack((Pa,temp))
					Pa=t1

				if xx == 2:
					temp=np.array([X,Y])
					Pb=np.vstack((Pb,temp))
				if xx == 3:
					temp=np.array([X,Y])
					Pc=np.vstack((Pc,temp))
				if xx == 4:
					temp=np.array([X,Y])
					Pd=np.vstack((Pd,temp))
				cv2.drawContours(img,[c], -1, (0,255,0), 3)
                if xx==1:
				 cv2.imshow('frame',img)
		# Display the resulting frame
		#cv2.imshow('frame',img)




def ori(PP):
	global goal
	tem=PP.shape
	temp1=tem[0]
	x1=PP.item((temp1-2,0))
	y1=PP.item((temp1-2,1))
	x2=PP.item((temp1-1,0))
	y2=PP.item((temp1-1,1))
	x3=goal.item(0)
	y3=goal.item(1)
	print (x3,y3)
	print (x1,y1,x2,y2)
	slope1=(x2-x1)/(y2-y1)
	slope2=(x3-x1)/(y3-y1)
	print (slope1,slope2)
	tan=(slope1-slope2)/(1+slope1*slope2)
	if tan < 0:
		tan=tan*-1
	angle = math.degrees(math.atan(tan))
	print (angle)





while(cap1.isOpened()):
	local(1)
	#local(2)
	#local(3)
	#local(4)
	if cv2.waitKey(1) == 27:
		#print Pa
		ori(Pa)
		'''print Pb
		ori(Pb)
		print Pc
		ori(Pc)
		print Pd
		ori(Pd)'''
		break
# When everything done, release the capture
cap1.release()
#cap2.release()
cap3.release()
cap4.release()
cv2.destroyAllWindows()
