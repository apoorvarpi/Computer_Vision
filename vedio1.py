import cv2
import numpy
from tkinter import *
from PIL import Image, ImageTk
import argparse

xx = 1
flag = 0

def on_mouse(event,x,y,flags,params):
	if event == cv2.EVENT_LBUTTONDOWN:
		global flag
		flag = 1
		print(flag)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		print("ok\n")
		name = "./input/C"+str(xx)+"/calib1.jpg"
		cv2.imwrite(name,frame)

def main(size):
	for i in range(0, size):
		#top=Toplevel()
		#top.title("camera "+str(i+1))
		#top.geometry("1000x800")
		#top.resizable(0, 0)
		print(i)
		cap = cv2.VideoCapture(0)
		#global xx
		#xx = i+1
		loop = True
		while loop == True:
			val, frame = cap.read()
			cv2.imshow('stream', frame)
			cv2.setMouseCallback('stream', on_mouse)
			global flag
			flag = flag+1;
			if flag==250:
				break;

main(1)
