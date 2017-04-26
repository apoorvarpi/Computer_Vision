import cv2
import numpy
from tkinter import *
from PIL import Image, ImageTk
import argparse

#count=1
def on_mouse(event,x,y,flags,params):
	#print("getting")
	if event == cv2.EVENT_LBUTTONDOWN:
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		print("ok\n")
		name = "frame.jpg"   # save frame as JPEG file
		#count=count+1
		cv2.imwrite(name,frame)


top=Toplevel()
top.title("camera "+X)
top.geometry("1000x800")
top.resizable(0, 0)
#cv2.VideoCapture cap;
#cap.open("http://rit2014023:got%40S4L2@172.16.15.215:8081/?action=stream?dummy=param.mjpg");
cap = cv2.VideoCapture("http://rit2014023:got%40S4L2@172.16.15.245:8081/?action=stream?dummy=param.mjpg")
#cap = cv2.VideoCapture(0)
#cap.open("http://rit2014023:got%40S4L2@172.16.15.215:8081.mjpeg/")
if ~cap.isOpened():
    print ('error')
#cv2.setMouseCallback('frame', on_mouse)
while cap.isOpened():
		_,frame = cap.read()
		#cv2.namedWindow('frame')
		cv2.imshow("stream",frame)
		cv2.setMouseCallback('stream', on_mouse)
		c = cv2.waitKey(1)
		if c == 27:
			break
