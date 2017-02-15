import cv2
import numpy as np
from matplotlib import pyplot as plt

def threshold():
    img1 = cv2.imread('book1.jpg')
    img = cv2.cvtColor(img1, cv2.COLOR_BGR2YCR_CB)
    cv2.imshow("Images", img1)
    cv2.imshow("YCBCR", img)
    cv2.waitKey(0)

threshold()
