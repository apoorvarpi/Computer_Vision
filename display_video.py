import cv2
import numpy as np
from change_color import *

video1 = cv2.VideoCapture(0)

loop = True
while(loop == True):
    val1, img1 = video1.read()
    M = np.load('./Matrices/C1.npy')
    print(M);
    img1 = cv2.warpPerspective(img1, M, (1000, 1000));
    cv2.imshow("Camera 1", img1)

    if cv2.waitKey(1) == 27:
        break  # esc to quit
