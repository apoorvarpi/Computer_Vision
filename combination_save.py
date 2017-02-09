import cv2
import numpy as np
from utils import get_four_points

def obtain(im_nm,im_cam):
    im_name = "input/"+im_cam+"/"+im_nm
    im_src = cv2.imread(im_name)
    pts_src = get_four_points(im_src,im_cam);
    return pts_src

def transform(im_cam1,im_nm1,im_cam2,im_nm2):
    pts_src1 = obtain(im_nm1,im_cam1)
    pts_src2 = obtain(im_nm2,im_cam2)

    pts_src1 = np.float32(pts_src1)
    pts_src2 = np.float32(pts_src2)

    M = cv2.getPerspectiveTransform(pts_src2,pts_src1)
    #saving the matrix
    file_name = "./Matrices/"+im_cam1+"_"+im_cam2+".txt"
    np.savetxt(file_name,M)
    print("Saved file ",im_cam1,"_",im_cam2)
