import numpy as np
import cv2
from Translate import *

def find_mins(number):
    img1 = cv2.imread("./input/C1/calib.jpg")

    rows, cols, ch = img1.shape
    minx = 9999999
    miny = 9999999

    arr = np.array([[0,0], [0,rows-1], [cols-1, rows-1], [cols-1,0]])

    for i in range(2,number+1):
        name = "./Matrices/C"+str(i)+"_C1.npy"
        M = np.load(name)

        for j in range(0,4):
            x = (M[0][0]*arr[j][0] + M[0][1]*arr[j][1] + M[0][2])/(M[2][0]*arr[j][0] + M[2][1]*arr[j][1] + M[2][2])
            y = (M[1][0]*arr[j][0] + M[1][1]*arr[j][1] + M[1][2])/(M[2][0]*arr[j][0] + M[2][1]*arr[j][1] + M[2][2])

            if x < minx:
                minx = x
            if y < miny:
                miny = y

    print(miny," ",miny)

find_mins(4)
