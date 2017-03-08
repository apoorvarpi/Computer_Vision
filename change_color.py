import cv2
import numpy as np
import math

def threshold(img2):

    kernel = np.ones((5,5), np.float32)/25
    img1 = cv2.filter2D(img2, -1, kernel)
    img = cv2.cvtColor(img1, cv2.COLOR_BGR2YCR_CB)
    Y, Cb, Cr = cv2.split(img)
    rows, cols = Y.shape
    for i in range(0, rows):
        for j in range(0, cols):
            a = int(Cb[i][j])
            b = int(Cr[i][j])
            c = int(Y[i][j])
            x = math.sqrt(a*a + b*b + c*c)
            if x>210:
                Y[i][j] = 255
            else:
                Y[i][j] = 0
    return Y
    #cv2.imshow("Image", Y)
    #cv2.waitKey(0)
