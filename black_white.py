from change_color import *
import cv2

def color_correct(size):
    for i in range(1, size+1):
        name = "input/C"+str(i)+"/calib.jpg"
        img = cv2.imread(name)
        img1 = threshold(img)
        name1 = "input/C"+str(i)+"/bw.jpg"
        cv2.imwrite(name1,img1)

color_correct(4)
