import cv2
import numpy as np

def position():
    img = cv2.imread('./input/Output.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h,w=img.shape[:2]
    M = np.zeros((h*w,2), dtype=np.float32)
    count = 0
    for i in range(0, h):
        for j in range(0, w):
            if img[i][j]==0:
                M[count+1][0] = i
                M[count+1][1] = j
                count = count+1

    M[0][0] = count
    M[0][1] = count

    np.save("./Matrices/Obstacles.npy", M)
    #for i in range(1, count+1):
    #    print(M[i][0], " ", M[i][1])



position()
    #M[0][0]=M[0][1] = number of values
