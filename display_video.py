import cv2
import numpy as np
from change_color import *

video1 = cv2.VideoCapture('http://rit2014044:iiita665@172.16.15.215:8081/?action=stream?dummy=param.mjpg')

loop = True
while(loop == True):
    val1, img1 = video1.read()
    #img = threshold(img1)
    cv2.imshow("Camera 1", img1)

    if cv2.waitKey(1) == 27:
        break  # esc to quit
