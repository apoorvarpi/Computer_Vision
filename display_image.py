# size = 450 rows, 800 cols
import cv2
import numpy as np

#def display(n1,n2,mat):
def display():
    img1 = cv2.imread("./input/C1/bw.jpg")
    img2 = cv2.imread("./input/C2/bw.jpg")

    #img1 = cv2.imread(n1)
    #img2 = cv2.imread(n2)
    #M = np.load(mat)
    M = np.load("./Matrices/C2_C1.npy")
    N = np.array([[0.5,0,1000],[0,0.5,100],[0,0,1]], dtype = float)
    #N = np.array([[1,0,1000],[0,1,100],[0,0,1]], dtype = float)
    M = np.matmul(N,M)
    dst = cv2.warpPerspective(img2, M, (10000,10000))

    cv2.imshow("Final Image",dst)
    #return dst
    cv2.waitKey(0)

display()
