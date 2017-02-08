import cv2
import numpy as np

nm = "Image"

def mouse_handler(event, x, y, flags, data) :
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(data['im'], (x,y),3, (0,0,255), 5, 16);
        cv2.imshow(nm, data['im']);
        if len(data['points']) < 4 :
            data['points'].append([x,y])

def get_four_points(im, name):
    # Set up data to send to mouse handler
    data = {}
    data['im'] = im.copy()
    data['points'] = []
    #Set the callback function for any mouse event
    cv2.imshow(nm,im)
    cv2.setMouseCallback(nm, mouse_handler, data)
    cv2.waitKey(0)
    # Convert array to np.array
    points = np.vstack(data['points']).astype(float)

    return points
