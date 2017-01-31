import cv2
import sys
import numpy as np
from PIL import Image

def inputImage():
  first_image = 'input/Camera1/img1.jpg'
  second_image = 'input/Camera/img2.jpg'
  return first_image, second_image

def main(fig1):
  first_image, second_image = inputImage() #get input

  fig1 = cv2.imread(first_image) #reading Image
  fig1 = cv2.resize(fig1, (0,0), fx = 0.5, fy = 0.5)
  rows, cols, ch = fig1.shape
  #print(fig1.shape)

  cv2.namedWindow('First image');
  #cv2.setMouseCallback('First image', store_point_coordinate)

pts1 = []
pts2 = []
fig1 = np.zeros((2000,2000,3),np.uint8)
fig2 = np.zeros((2000,2000,3),np.uint8)

main(fig1)
