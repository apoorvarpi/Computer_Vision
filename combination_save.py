import cv2
import numpy as np
from utils import get_four_points

def transform(im_cam1,im_cam2):
    add_src1 = "./Matrices/"+im_cam1+".npy"
    add_src2 = "./Matrices/"+im_cam2+".npy"

    pts_src1 = np.load(add_src1)
    pts_src2 = np.load(add_src2)

    pts_src1 = np.float32(pts_src1)
    pts_src2 = np.float32(pts_src2)

    M = cv2.getPerspectiveTransform(pts_src2,pts_src1)
    #saving the matrix
    file_name = "./Matrices/"+im_cam1+"_"+im_cam2+".txt"
    np.savetxt(file_name,M)
    print("Saved file ",im_cam1,"_",im_cam2)
