from save_matrices import *
#Subplot needs to be added

def new_win(var):
    for i in range(1,var+1):
        x = str(i)
        im_name = "calib.jpg"
        im_cam = "C"+str(i)
        save(im_name,im_cam)
