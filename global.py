import numpy as np
import cv2

def find_mins():
    img1 = cv2.imread("./input/C1/calib.jpg")

    M1 = np.load("./Matrices/C2_C1.npy")
    M2 = np.load("./Matrices/C3_C1.npy")
    M3 = np.load("./Matrices/C4_C1.npy")

    rows, cols,ch = img1.shape
    xc1 = [0, 0, rows-1, rows-1]
    xc2 = [0, cols-1, cols-1, 0]

    xxmin = 0
    yymin = 0

    xmin = 999999
    ymin = 999999
    for i in range(0,rows):
        for j in range(0,cols):
            x = (M1[0][0]*i + M1[0][1]*j + M1[0][2])/(M1[2][0]*i + M1[2][1]*j + M1[2][2])
            y = (M1[1][0]*i + M1[1][1]*j + M1[1][2])/(M1[2][0]*i + M1[2][1]*j + M1[2][2])
            if x<xmin:
                xmin = x
            if y<ymin:
                ymin = y

    if xmin<xxmin:
        xxmin = xmin
    if ymin<yymin:
        yymin = ymin

    xmin = 999999
    ymin = 999999
    for i in range(0,rows):
        for j in range(0,cols):
            x = (M2[0][0]*i + M2[0][1]*j + M2[0][2])/(M2[2][0]*i + M2[2][1]*j + M2[2][2])
            y = (M2[1][0]*i + M2[1][1]*j + M2[1][2])/(M2[2][0]*i + M2[2][1]*j + M2[2][2])
            if x<xmin:
                xmin = x
            if y<ymin:
                ymin = y

    if xmin<xxmin:
        xxmin = xmin
    if ymin<yymin:
        yymin = ymin

    xmin = 999999
    ymin = 999999
    for i in range(0,rows):
        for j in range(0,cols):
            x = (M3[0][0]*i + M3[0][1]*j + M3[0][2])/(M3[2][0]*i + M3[2][1]*j + M3[2][2])
            y = (M3[1][0]*i + M3[1][1]*j + M3[1][2])/(M3[2][0]*i + M3[2][1]*j + M3[2][2])
            if x<xmin:
                xmin = x
            if y<ymin:
                ymin = y

    if xmin<xxmin:
        xxmin = xmin
    if ymin<yymin:
        yymin = ymin

    print(xxmin," ",yymin)

find_mins()
