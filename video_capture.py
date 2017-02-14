import cv2
import numpy as np

def show_webcam( mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        set_val, img = cam.read()
        if mirror:
            img = cv2.flip(img, 1)
        rows, cols, ch = img.shape
        M = np.load("./Matrices/C3_C1.npy")
        img1 = cv2.warpPerspective(img, M, (cols,rows))
        cv2.imshow('my webcam', img1)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()

def main():
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()
