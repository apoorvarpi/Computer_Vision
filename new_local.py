import numpy as np
import cv2
import math
from collections import deque
import argparse
import imutils
import time
import multiprocessing

#cap1 = cv2.VideoCapture(0)
#cap2 = cqp1
cap1 = cv2.VideoCapture('http://rit2014044:iiita665@172.16.15.215:8081/?action=stream?dummy=param.mjpg')
#cap1.set(CV_CAP_PROP_BUFFERSIZE, 3)
cap2 = cv2.VideoCapture('http://rit2014044:iiita665@172.16.15.245:8081/?action=stream?dummy=param.mjpg')
#cap2.set(CV_CAP_PROP_BUFFERSIZE, 3)
#cap3=cap1
#cap4=cap1
#cap3 = cv2.VideoCapture(2)
#cap4 = cv2.VideoCapture(3)
yellowLower = (25, 100, 100)
yellowUpper = (80, 255, 255)
greenLower = (42, 100, 100)
greenUpper = (58, 255, 255)
pinkl = (155,100,100)
pinku = (170,255,255)
ol=(0,100,100)
ou=(13,255,255)
output="./input/C4"+"/output.jpg"
im_src = cv2.imread(output)
goal=np.array([100,100])
Pa=np.array([0,0])
Pb=np.array([0,0])
Pc=np.array([0,0])
Pd=np.array([0,0])



def local(xx):
	global Pa,Pb,Pc,Pd,goal
	if xx == 1:
		ret, frame = cap1.read()
	if xx==2:
		ret, frame = cap2.read()
	if xx==3:
		ret, frame = cap3.read()
	if xx==4:
		ret, frame = cap4.read()
	if ret==True:
		#frame = cv2.GaussianBlur(frame, (11, 11), 0)
		nnn="./Matrices/C"+str(1)+"s.npy"
		M2 = np.load(nnn)

		Mx = np.float32([[1,0,100],[0,1,100],[0,0,1]])
		M2 = np.dot(M2, Mx)

		h,w=frame.shape[:2]
		#mask=frame
		mask = cv2.warpPerspective(frame, M2,(500, 500))
		cv2.imshow('first image'+str(xx),mask)
		cv2.waitKey(30)
		mask = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
		mask=  cv2.medianBlur(mask,5)

		#mask1 = cv2.inRange(mask, yellowLower, yellowUpper)
		#mask1 = cv2.inRange(mask, greenLower, greenUpper)
		#mask2 = cv2.inRange(mask, pinkl, pinku)
		mask2 = cv2.inRange(mask, ol, ou)
		for i in range(2,3):
			if i == 1:
				maskk=mask1
			if i== 2:
				maskk=mask2
			if i== 3:
				maskk=mask3
			if i==4:
				mask=mask4
			img = np.zeros((512,512,3), np.uint8)
			cnts = cv2.findContours(maskk.copy(), cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)[-2]
			vv =0
			for c in cnts:
				vv=vv+1
				if vv > 2:
					break
				area = cv2.contourArea(c)
				#print (area)
				if area > 0:
					M = cv2.moments(c)
					X = int(M["m10"] / M["m00"])
					Y = int(M["m01"] / M["m00"])
					#print (X, Y)
					cv2.drawContours(img,[c], -1, (0,255,0), 3)
					if i ==  1:
						temp=np.array([X,Y])
						t1=np.vstack((Pa,temp))
						Pa=t1
						cv2.imshow('frame1',img)
						cv2.waitKey(1)
						text_file = open("./Matrices/Pa.txt", "w")
						if xx==1:
							aa = (200-(X-122)*200/110)
							bb = ((Y-70)*200/152)
						elif xx==2:
							aa = 200+(X-105)*160/108
							bb = 200 - (Y-42)*200/185
						text_file.write("%d %d\n" % (aa, bb))
						print(aa," ",bb)
						text_file.close()

					if i == 2 :
						temp=np.array([X,Y])
						Pb=np.vstack((Pb,temp))
						cv2.imshow('frame2',img)
						cv2.waitKey(1)
						text_file = open("./Matrices/Pb.txt", "w")
						if xx==1:
							aa = (200-(X-122)*200/110)
							bb = ((Y-70)*200/152)
						elif xx==2:
							aa = 200+(X-105)*160/108
							bb = 200 - (Y-42)*200/185
						text_file.write("%d %d\n" % (aa, bb))
						print(aa," ",bb)
						text_file.close()
					if i == 3:
						temp=np.array([X,Y])
						Pc=np.vstack((Pc,temp))
						text_file = open("./Matrices/Pc.txt", "w")
						text_file.write("%d %d\n" % (X, Y))
						text_file.close()
						cv2.imshow('frame3',img)
						cv2.waitKey(1)
					if i == 4:
						temp=np.array([X,Y])
						Pd=np.vstack((Pd,temp))
						text_file = open("./Matrices/Pd.txt", "w")
						text_file.write("%d %d\n" % (X, Y))
						text_file.close()
						cv2.imshow('frame4',img)
						cv2.waitKey(1)





while(cap1.isOpened()):
	start_time = time.time()
	local(1)
	#print("--- %s seconds ---" % (time.time() - start_time))
	local(2)
	#local(3)
	#local(4)
	if cv2.waitKey(1) == 27:
		#print (Pa)
		#ori(Pa)
		#print (Pb)
		#ori(Pb)
		#print Pc
		#ori(Pc)
		#print Pd
		#ori(Pd)
		break
# When everything done, release the capture
cap1.release()
cap2.release()
#cap3.release()
#cap4.release()
cv2.destroyAllWindows()
