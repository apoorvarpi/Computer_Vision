import cv2
import numpy as np

def show_webcam(number, mirror=False):
    x = int(number)
    for i in range(0, x):
        name = "Camera "+str(i+1)
        cv2.namedWindow(name)
        

def main():
    number = input("Enter the number of cameras: ")
    show_webcam(number, mirror=True)

if __name__ == '__main__':
    main()
