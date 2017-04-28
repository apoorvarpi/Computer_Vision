import cv2
import numpy as np
from change_color import *
from utils import *

video1 = cv2.VideoCapture('http://rit2014044:iiita665@172.16.15.245:8081/?action=stream?dummy=param.mjpg')

loop = True
while(loop == True):
    val1, img1 = video1.read()
    M = np.load('./Matrices/C2.npy')

    Mx = np.float32([[1,0,100],[0,1,100],[0,0,1]])
    M = np.dot(M, Mx)

#print(M);
    img1 = cv2.warpPerspective(img1, M, (1000, 1000));
    cv2.imshow("Camera 1", img1)
#print(get_four_points(img1, "Image"))


    if cv2.waitKey(1) == 27:
        break  # esc to quit
