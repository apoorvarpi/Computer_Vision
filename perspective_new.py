#!/usr/bin/env python

import cv2
import numpy as np
from utils import get_four_points


def final_pers(name, name1) :

    # Reading the image.
    im_src = cv2.imread(name)
    im_base = cv2.imread("./input/Base.jpg")

    # Show image and wait for 4 clicks.
    pts_src = get_four_points(im_src,"Image")
    pts_src = np.float32(pts_src)

    pts_base = get_four_points(im_base, "Image")
    pts_base = np.float32(pts_base)

    #calculate dimensions
    minx = 9999999
    miny = 9999999
    maxx = 0
    maxy = 0
    for i in range(0,4):
        x = pts_base[i][0]
        y = pts_base[i][1]
        if x>maxx:
            maxx = x
        if x<minx:
            minx = x
        if y>maxy:
            maxy = y
        if y<miny:
            miny = y

    a = 4*int(maxx - minx)
    b = 4*int(maxy - miny)

    #normalise co-ordinates
    for i in range(0,4):
        pts_base[i][0] = 4*(pts_base[i][0] - minx)
        pts_base[i][1] = 4*(pts_base[i][1] - miny)

    # Calculate the homography
    M = cv2.getPerspectiveTransform(pts_src, pts_base)

    # Warp source image to destination
    im_dst = cv2.warpPerspective(im_src, M, (a, b))

    # Show output
    cv2.imshow("Image", im_dst)
    cv2.imwrite(name1, im_dst)
    cv2.waitKey(0)
