from display_image import *

def save_new(x):
    name = "./input/C1/bw.jpg"
    name2 = "./input/C1/pers1.jpg"
    img = cv2.imread(name)
    cv2.imwrite(name2, img)
    for i in range(2, x+1):
        name1 = "./input/C"+str(i)+"/bw.jpg"
        mat = "./Matrices/C"+str(i)+"_C1.npy"
        img = display(name,name1,mat)
        name2 = "./input/C"+str(i)+"/pers1.jpg"
        cv2.imwrite(name2, img)

save_new(4)
