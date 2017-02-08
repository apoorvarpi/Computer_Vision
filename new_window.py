import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

def new_win(var):
    for i in range(1,var+1):
        x = str(i)
        im_name = "input/C"+x+"/calib.jpg"
        print (im_name)
        image = cv2.imread(im_name)
        im_title = "Camera "+x
        tt = cv2.imread("input/C1/calib.jpg")
        cv2.imshow(im_title,image)
        cv2.waitKey(0)
