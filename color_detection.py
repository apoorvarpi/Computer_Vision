import numpy as np
import cv2
from collections import deque
import argparse
import imutils

'''def col(i):
	output="./input/colors/"+str(i)+".jpg"
	src = cv2.imread(output)

	b,g,r = cv2.split(src)#split source  

	#//Note: OpenCV uses BGR color order
	cv2.imshow("blue.png",b)#; //blue channel
	cv2.imshow("green.png",g)#; //green channel
	cv2.imshow("red.png",r)#; //red channel
	cv2.waitKey(0)

for i in range(1,6):
	col(i)'''
green = np.uint8([[[0,255,0 ]]])
hsv_green = cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)
print hsv_green
