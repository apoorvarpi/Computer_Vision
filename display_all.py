import cv2

def show_finals():
    print("Original Images")
    for i in range(1, 5):
        name = "./input/C"+str(i)+"/calib.jpg"
        cv2.imshow("Image",cv2.imread(name))
        cv2.waitKey(0)

    print("Black and White Images")
    for i in range(1, 5):
        name = "./input/C"+str(i)+"/bw.jpg"
        cv2.imshow("Image",cv2.imread(name))
        cv2.waitKey(0)

    print("Top View Images")
    for i in range(1, 5):
        name = "./input/C"+str(i)+"/pers2.jpg"
        cv2.imshow("Image",cv2.imread(name))
        cv2.waitKey(0)

show_finals()
