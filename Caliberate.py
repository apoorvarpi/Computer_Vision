import cv2
import sys
import numpy as np
from PIL import Image

def store_point_coordinate(event,x,y,flags,param):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event ==cv2.EVENT_FLAG_LBUTTON and len(pts1) < 4:
        cv2.circle(fig1,(x,y),2,(255,255,255),-1)
        cv2.putText(fig1,str(x)+' '+str(y),(x-20,y-20),font,0.3,(255,255,255),1,cv2.LINE_AA)
        pts1.append([x,y])
        print(x,y)

def inputImage():
  first_image = 'input/Camera1/img1.jpg'
  second_image = 'input/Camera/img2.jpg'
  return first_image, second_image

def main(fig1,pts1):
  first_image, second_image = inputImage() #get input

  fig1 = cv2.imread(first_image) #reading Image
  fig1 = cv2.resize(fig1, (0,0), fx = 0.5, fy = 0.5)
  rows, cols, ch = fig1.shape

  cv2.namedWindow('Image 1')
  cv2.setMouseCallback('Image 2', store_point_coordinate)

  while(True):
      cv2.imshow('Image 1',fig1)
      if(cv2.waitKey(30) == 27 or len(pts1) >= 4):
          break

  pts1 = np.float32(pts1)

  x = 0
  while(True):
      cv2.imshow('Image 1',fig1)
      x = x+1
      if(cv2.waitKey(30) == 27):
          break

pts1 = []
pts2 = []
fig1 = np.zeros((2000,2000,3),np.uint8)
fig2 = np.zeros((2000,2000,3),np.uint8)

main(fig1,pts1)
