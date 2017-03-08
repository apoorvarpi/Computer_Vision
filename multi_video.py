import cv2
import numpy as np

video1 = cv2.VideoCapture('http://rit2014044:iiita665@172.16.15.215:8081/?action=stream?dummy=param.mjpg')

video2 = cv2.VideoCapture(3)

video3 = cv2.VideoCapture(4)

video4 = cv2.VideoCapture(2)

loop = True
while(loop == True):
    val1, img1 = video1.read()
    cv2.imshow("Camera 1", img1)

    val2, img2 = video2.read()
    M = np.load("./Matrices/C2_C1.npy")
    img21 = cv2.warpPerspective(img2, M, (10000,10000))
    cv2.imshow("Camera 2", img21)

    val3, img3 = video3.read()
    M = np.load("./Matrices/C3_C1.npy")
    img31 = cv2.warpPerspective(img3, M, (10000,10000))
    cv2.imshow("Camera 3", img31)

    val4, img4 = video4.read()
    M = np.load("./Matrices/C4_C1.npy")
    #trans = np.matrix('1 0 1000; 0 1 1000; 0 0 1')
    #M = np.matmul(M, trans)
    img41 = cv2.warpPerspective(img4, M, (10000,10000))
    cv2.imshow("Camera 4", img41)

    if cv2.waitKey(1) == 27:
        break  # esc to quit
