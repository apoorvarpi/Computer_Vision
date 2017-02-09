from save_matrices import *
import matplotlib.pyplot as plt

def new_win(var):
    a = 1;
    b = 1;
    for i in range(1,var+1):
        b = var/a;
        if a*b>=var and b<=a:
            break
        a = a+1
    b = var/a
    plt.figure(1)
    y = a*100+b*10+1
    for i in range(1,var+1):
        x = str(i)
        im_nm = "calib.jpg"
        im_cam = "C"+str(i)
        im_name = "./input/"+im_cam+"/calib.jpg"
        im_src = cv2.imread(im_name)
        plt.subplot(y)
        y = y+1
        cv2.imshow(im_cam,im_src)
