#!/usr/bin/env python

import cv2
import numpy as np
from utils import get_four_points


if __name__ == '__main__' :

    # Read in the image.
    im_src = cv2.imread("./input/C3/pers1.jpg")

    # Destination image
    size = (cv2.imread("./input/C1/pers1.jpg")).shape

    im_dst = np.zeros(size, np.uint8)


    pts_dst = np.array(
                       [
                        [0,0],
                        [size[0] - 1, 0],
                        [size[0] - 1, size[1] -1],
                        [0, size[1] - 1 ]
                        ], dtype=float
                       )

    # Show image and wait for 4 clicks.
    cv2.imshow("Image", im_src)
    pts_src = get_four_points(im_src,"Image");

    # Calculate the homography
    h, status = cv2.findHomography(pts_src, pts_dst)

    # Warp source image to destination
    im_dst = cv2.warpPerspective(im_src, h, size[0:2])

    # Show output
    cv2.imshow("Image", im_dst)
    cv2.imwrite("./input/C3/pers2.jpg", im_dst)
    cv2.waitKey(0)
