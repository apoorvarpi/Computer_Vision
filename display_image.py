import cv2
import numpy as np
from change_color import *
from utils import *

img1 = cv2.imread('./input/Output.jpg')
#cv2.imshow("Camera 1", img1)
print(get_four_points(img1, "Image"))
