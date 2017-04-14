import cv2
import numpy as np

for i in range(1,5):
    name = "./input/C"+str(i)+"/perss2.jpg"
    im_src = cv2.imread(name)
    #cv2.imshow('Image',im_src)
    #cv2.waitKey(0)
    #print(im_src)
    gray=im_src
    im_dst=cv2.bitwise_not(im_src)
    gray = cv2.cvtColor(im_dst, cv2.COLOR_BGR2GRAY)
    ret,gray = cv2.threshold(gray,127,255,0)
    kernel = np.ones((5,5),np.uint8)
    gray=cv2.erode(gray,kernel,iterations = 10);
    gray=cv2.dilate(gray,kernel,iterations = 10);
    #gray=cv2.Canny(gray,100,200)
    cv2.namedWindow('Iimage',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Iimage', 600,600)
    cv2.imshow('Iimage',gray)
    cv2.waitKey(0)
    (_,cnts, hie) = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros(gray.shape[:2], dtype="uint8") * 255
    for c in cnts:
        #print c
        area = cv2.contourArea(c)
        x,y,w,h = cv2.boundingRect(c)
        #cv2.rectangle(mask,(x,y),(x+w,y+h),(128,255,0),18)
        #print area
        if area < 400000:
            cv2.drawContours(mask, [c], -1, (128,255,0), -1)
            #print 'ok\n'
    #gray=cv2.dilate(mask,kernel,iterations = 1);
    cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('Image', 600,600)
    cv2.imshow('Image',mask)
    cv2.waitKey(0)
    if i is 1:
    	print 'okk'
    	im_done=mask

    h,w=im_done.shape[:2]
    mask= cv2.resize(mask, (w, h)) 
    im_done=cv2.bitwise_or(im_done,mask)
    im_dst=cv2.bitwise_not(im_done)
    ret,im_dst = cv2.threshold(im_dst,127,255,1)
    cv2.namedWindow('done',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('done', 600,600)
    cv2.imshow('done',im_dst)
    cv2.waitKey(0)
