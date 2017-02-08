import cv2
import numpy as np
from utils import get_four_points

def save(im_nm,im_cam):
    im_name = "input/"+im_cam+"/"+im_nm
    im_src = cv2.imread(im_name)
    pts_src = get_four_points(im_src,im_cam);
    pts_src = np.float32(pts_src)
    name = "./Matrices/"+im_cam
    np.save(name,pts_src)
