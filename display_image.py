import cv2
import numpy as np

def display():
    img1 = cv2.imread("./input/C1/calib.jpg")
    img2 = cv2.imread("./input/C2/calib.jpg")

    M = np.load("./Matrices/C2_C1.npy")
    print(M)

    dst = cv2.warpPerspective(img2, M, (10000,10000))

    cv2.imshow("Final Image",dst)
    cv2.imshow("From",img2)
    cv2.imshow("To",img1)
    cv2.waitKey(0)

display()
