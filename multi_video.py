import cv2
import numpy as np

cv2.namedWindow("Camera 1")
video1 = cv2.VideoCapture(0)

#cv2.namedWindow("Camera 2")
#video2 = cv2.VideoCapture(1)

cv2.namedWindow("Camera 3")
video3 = cv2.VideoCapture(2)
video3.set(cv2.CAP_PROP_FPS, 1)
video3.set(3,20)
video3.set(4,20)

loop = True
while(loop == True):
    val1, img1 = video1.read()
    rows, cols, ch = img1.shape
    #M = np.load("./Matrices/C3_C1.npy")
    #img11 = cv2.warpPerspective(img1, M, (cols,rows))
    cv2.imshow("Camera 1", img1)

    #val2, img2 = video2.read()
    #rows, cols, ch = img2.shape
    #M = np.load("./Matrices/C3_C1.npy")
    #img21 = cv2.warpPerspective(img2, M, (cols,rows))
    #cv2.imshow("Camera 2", img21)

    val1, img3 = video3.read()
    rows, cols, ch = img3.shape
    M = np.load("./Matrices/C2_C1.npy")
    img31 = cv2.warpPerspective(img3, M, (cols,rows))
    cv2.imshow("Camera 3", img31)

    if cv2.waitKey(1) == 27:
        break  # esc to quit
