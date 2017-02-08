import cv2
import numpy as np
from utils import get_four_points


def modifyValue(vec,img,factor,flag):
    rows,cols,ch = img.shape
    if flag == 1:
        for x in range(0, 4):
            vec[x][0] *= factor
            vec[x][1] *= factor
        return vec
    else:
        for x in range(0,4):
            vec[x][0] += (factor-1)*cols*0.5
            vec[x][1] += (factor-1)*rows*0.5
        return vec

def resizeOnCenter(img, factor):        # resizing image keeping it in center
    rows,cols,ch = img.shape
    tx = (factor-1)*rows*0.5
    ty = (factor-1)*cols*0.5
    trans = np.float32([[1,0,ty],[0,1,tx]])
    foreground = cv2.warpAffine(img,trans,(factor*cols,factor*rows))
    return foreground

if __name__ == '__main__':
    # Read in the image.
    im_nm1 = input("First image name: ")
    im_cam1 = input("First camera name: ")
    im_nm2 = input("Second image name: ")
    im_cam2 = input("First camera name: ")
    im_name1 = "input/"+im_cam1+"/"+im_nm1
    im_name2 = "input/"+im_cam2+"/"+im_nm2
    im_src1 = cv2.imread(im_name1)
    im_src2 = cv2.imread(im_name2)

    # Destination image
    size = (300,400,3)

    im_dst = np.zeros(size, np.uint8)

    pts_dst = np.array(
                       [
                        [0,0],
                        [size[0] - 1, 0],
                        [size[0] - 1, size[1] -1],
                        [0, size[1] - 1 ]
                        ], dtype=float
                       )


    print ('''
        Click on the four corners of the book -- top left first and
        bottom left last -- and then hit ENTER
        ''')

    # Show image and wait for 4 clicks.
    pts_src1 = get_four_points(im_src1);

    print('''
        Repeat the above step for the next image
        ''')

    #Show second image and wait for four clicks
    pts_src2 = get_four_points(im_src2);

    rows,cols,ch = im_src1.shape

    pts_src1 = np.float32(pts_src1)
    pts_src2 = np.float32(pts_src2)

    M = cv2.getPerspectiveTransform(pts_src2,pts_src1)
    #saving the matrix
    file_name = "./Matrices/"+im_cam1+"_"+im_cam2+".txt"
    np.savetxt(file_name,M)
    im_src = cv2.warpPerspective(im_src2, M, (cols,rows))
    #Display new image and wait for four clicks

    print('''
            Click on the four corners
        ''')
    pts_src = get_four_points(im_src);

    # Calculate the homography
    h, status = cv2.findHomography(pts_src, pts_dst)

    # Warp source image to destination
    im_dst = cv2.warpPerspective(im_src, h, size[0:2])

    # Show output
    cv2.imshow("Final Image", im_dst)
    cv2.waitKey(0)
