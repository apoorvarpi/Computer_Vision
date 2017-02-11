import cv2
#Subplot needs to be resolved..

def new_win(var):
    for i in range(1,var+1):
        x = str(i)
        im_nm = "calib.jpg"
        im_cam = "C"+str(i)
        im_name = "./input/"+im_cam+"/calib.jpg"
        im_src = cv2.imread(im_name)
        cv2.imshow(im_cam,im_src)
        cv2.waitKey(0)
