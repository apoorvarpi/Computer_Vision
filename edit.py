import cv2
import numpy as np

name1 = "";

def mouse_handler(event, x, y, flags, data) :
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(data['im'], (x,y),3, (0, 0, 0), 5, 16);
        cv2.imshow("Image", data['im']);
        if len(data['points']) < 4 :
            data['points'].append([x,y])
        cv2.imwrite(name1, data['im'])


def dots(size):
    for i in range(1, size+1):
        name = "./input/C"+str(i)+"/calib1.jpg"
        im = cv2.imread(name)
        data = {}
        data['im'] = im.copy()
        data['points'] = []
        cv2.imshow("Image",im)
        global name1;
        name1 = "./input/C"+str(i)+"/calib.jpg";
        cv2.setMouseCallback("Image", mouse_handler, data)
        cv2.waitKey(0)

def resizex(size):
    for i in range(1, size+1):
        name = "./input/C"+str(i)+"/calib1.jpg"
        im_src = cv2.imread(name)
        im_dst = cv2.resize(im_src, (800, 450))
        cv2.imwrite(name, im_dst)

def main(size):
    resizex(size)
    dots(size)

main(2)
