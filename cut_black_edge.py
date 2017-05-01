import cv2
import numpy as np

count = 0
obs=np.array((0,0))
def cut(size):
    global count,obs
    for i in range(1, size+1):
        name = "./input/C"+str(i)+"/perss2.jpg"
        im_src = cv2.imread(name)
        im_dst=cv2.bitwise_not(im_src)
        gray = cv2.cvtColor(im_dst, cv2.COLOR_BGR2GRAY)
        ret,gray = cv2.threshold(gray,127,255,0)
        kernel = np.ones((5,5),np.uint8)
        gray=cv2.erode(gray,kernel,iterations = 3);
        gray=cv2.dilate(gray,kernel,iterations = 3);
        #cv2.namedWindow('Iimage',cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('Iimage', 600,600)
        cv2.imshow('Iimage',gray)
        cv2.waitKey(0)
        (_,cnts, hie) = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros(gray.shape[:2], dtype="uint8") * 255
        for c in cnts:
            #print c
            area = cv2.contourArea(c)
            x,y,w,h = cv2.boundingRect(c)
            #cv2.rectangle(mask,(x,y),(x+w,y+h),(128,255,0),18)
            #print(area)
            if area < 10000:
                count = count + 1
                x,y,w,h = cv2.boundingRect(c)
                #print (x,y,w,h)
                M = cv2.moments(c)
                X = int(M["m10"] / M["m00"])
                Y = int(M["m01"] / M["m00"])
                temp=np.array([X,Y])
                t1=np.vstack((obs,temp))
                obs=t1
                text_file = open("./Matrices/obstacle.txt", "a")
                text_file.write("%d %d\n" % ((360-(X*360/500)),Y*200/255))
                print ((360-(X*360/500)),Y*200/255)
                text_file.close()
                cv2.drawContours(mask, [c], -1, (128,255,0), -1)
        #cv2.namedWindow('Image',cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('Image', 600,600)
        cv2.imshow('Image',mask)
        cv2.waitKey(0)
        if i is 1:
        	#print ('okk')
        	im_done=mask
        #h,w=im_done.shape[:2]
        #mask= cv2.resize(mask, (w, h))
        im_done=cv2.bitwise_or(im_done,mask)
        #im_dst=cv2.bitwise_not(im_done)
        ret,im_done = cv2.threshold(im_done,127,255,0)
        #im_done=cv2.bitwise_not(im_done)
        #im_dst=cv2.dilate(im_dst,kernel,iterations = 10);
        #im_dst=cv2.erode(im_dst,kernel,iterations = 10);
        #cv2.namedWindow('done',cv2.WINDOW_NORMAL)
        #cv2.resizeWindow('done', 600,600)

        #im_dst=cv2.dilate(im_dst,kernel,iterations = 10);
        #im_dst=cv2.erode(im_dst,kernel,iterations = 10);

        cv2.imshow('done',im_done)
        cv2.imwrite('./input/Output.jpg', im_done)
        cv2.waitKey(0)

cut(2)
a=cv2.imread('./input/Output.jpg')
a=cv2.bitwise_not(a)
print(count)
#text_file = open("./Matrices/obstacle.txt", "a")
#text_file.write("%d %d\n" %  () )
#np.savetxt('text_file', obs, fmt="%d")
#text_file.close()
cv2.imwrite('./input/Output.jpg', a)
cv2.imshow('aaa',a)
cv2.waitKey(0)
