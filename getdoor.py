
# import the necessary packages
from __future__ import print_function
from imutils.object_detection import non_max_suppression
from imutils import paths
from collections import deque
import numpy as np
import argparse
import imutils
import time
import cv2
import math
# initialize the list of reference points and boolean indicating

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=32,
	help="max buffer size")
args = vars(ap.parse_args())

# whether cropping is being performed or not
refPt = []
check = False
def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]

	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		# draw a rectangle around the region of interest
		#Calculate parallel coordinate of 2 line
		x1=refPt[0][0]
		y1=refPt[0][1]
		x2=refPt[1][0]
		y2=refPt[1][1]
		a=1
		b=2*(x1*y2-x2*y1)
		c=(x1*y2-x2*y1)**2-100*((y2-y1)**2+(x2-x1)**2)
		d = b**2-4*a*c # discriminant
		if d == 0:
			x = (-b+math.sqrt(d))/(2*a)
		else:
			c1 = (-b+math.sqrt(d))/(2*a)
			c2 = (-b-math.sqrt(d))/(2*a)
		#sx1,sx2,sx3,sx4,sy1,sy2,sy3,sy4 is the coordinate of 4 point that make a rectangular with the main line is in the middle 
		sx1=(-c1-(x1/(y2-y1)+y1)*(x1-x2))/(y2-y1+(x2-x1)/(y2-y1))
		sy1=x1/(y2-y1)+y1-sx1/(y2-y1)
		
		sx2=(-c1-(x2/(y2-y1)+y2)*(x1-x2))/(y2-y1+(x2-x1)/(y2-y1))
		sy2=x2/(y2-y1)+y2-sx2/(y2-y1)
		
		sx3=(-c2-(x1/(y2-y1)+y1)*(x1-x2))/(y2-y1+(x2-x1)/(y2-y1))
		sy3=x1/(y2-y1)+y1-sx3/(y2-y1)
		
		sx4=(-c2-(x2/(y2-y1)+y2)*(x1-x2))/(y2-y1+(x2-x1)/(y2-y1))
		sy4=x2/(y2-y1)+y2-sx4/(y2-y1)
		
		cv2.line(image, refPt[0], refPt[1],(255,0,0),3,8,0)
		cv2.line(image, (int(sx1),int(sy1)), (int(sx2),int(sy2)),(0,255,0),3,8,0)
		cv2.line(image, (int(sx3),int(sy3)), (int(sx4),int(sy4)),(0,255,0),3,8,0)
		cv2.imshow("image", image)

	
# load the image, clone it, and setup the mouse callback function
if not args.get("video", False):
	camera.start_preview()
	sleep(5)
	camera.capture('image.jpg')
	image=imread('image.jpg', CV_LOAD_IMAGE_COLOR)

# otherwise, grab a reference to the video file
else:
	image = cv2.VideoCapture(args["video"])

ret, image=image.read()
image=imutils.resize(image,width=min(400,image.shape[1]))
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress

	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("d"):
		image = cv2.VideoCapture("test1.mp4")
		ret, image=image.read()
		image=imutils.resize(image, width=min(400, image.shape[1]))
		cv2.setMouseCallback("image", click_and_crop)
		print ("Deleted")
	if key == ord("s"):
		file=open("setting.txt","w")
		#Calculate parallel coordinate of 2 line
		x1=refPt[0][0]
		y1=refPt[0][1]
		x2=refPt[1][0]
		y2=refPt[1][1]
		a=1
		b=2*(x1*y2-x2*y1)
		c=(x1*y2-x2*y1)**2-100*((y2-y1)**2+(x2-x1)**2)
		d = b**2-4*a*c # discriminant
		if d == 0:
			x = (-b+math.sqrt(d))/(2*a)
		else:
			c1 = (-b+math.sqrt(d))/(2*a)
			c2 = (-b-math.sqrt(d))/(2*a)
		#sx1,sx2,sx3,sx4,sy1,sy2,sy3,sy4 is the coordinate of 4 point that make a rectangular with the main line is in the middle 
		sx1=int((-c1-(x1/(y2-y1)+y1)*(x1-x2))/(y2-y1+(x2-x1)/(y2-y1)))
		sy1=int(x1/(y2-y1)+y1-sx1/(y2-y1))
		
		sx2=int((-c1-(x2/(y2-y1)+y2)*(x1-x2))/(y2-y1+(x2-x1)/(y2-y1)))
		sy2=int(x2/(y2-y1)+y2-sx2/(y2-y1))
		
		sx3=int((-c2-(x1/(y2-y1)+y1)*(x1-x2))/(y2-y1+(x2-x1)/(y2-y1)))
		sy3=int(x1/(y2-y1)+y1-sx3/(y2-y1))
		
		sx4=int((-c2-(x2/(y2-y1)+y2)*(x1-x2))/(y2-y1+(x2-x1)/(y2-y1)))
		sy4=int(x2/(y2-y1)+y2-sx4/(y2-y1))
		
		st=str(refPt[0][0])+"\n"+str(refPt[0][1])+"\n"+str(refPt[1][0])+"\n"+str(refPt[1][1])+"\n"+str(sx1)+"\n"+str(sy1)+"\n"+str(sx2)+"\n"+str(sy2)+"\n"+str(sx3)+"\n"+str(sy3)+"\n"+str(sx4)+"\n"+str(sy4)
		print("Line mid: " + str(refPt[0][0])+"-"+str(refPt[0][1])+"\t"+str(refPt[1][0])+"-"+str(refPt[1][1]))
		print("Line top: " + str(sx1)+"-"+str(sy1)+"\t"+str(sx2)+"-"+str(sy2))
		print("Line bot: " + str(sx3)+"-"+str(sy3)+"\t"+str(sx4)+"-"+str(sy4))
		file.write(st)
		file.close()
		print ("Saved")
	# if the 'c' key is pressed, break from the loop
	if key == ord("c"):
		break


# close all open windows
cv2.destroyAllWindows()

