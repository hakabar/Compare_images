"""
Script developed by Diego Alonso San Alberto

Code to compare almost identical images in the same directory against one of them to detect changes in the image by subtracting the mean px values from the images.
This code has been build to detect in which image/frame insect appears (from a group of images). In all the images/frames the background stay the same.

User settings must be filled in file configuration_file.py that you will find in this folder

"""

import numpy as np
import cv2
import os
import time
import sys
import argparse as ap

from configuration_file import imgFolderPath, threshold

#Subtract the average pixel value of the previous image to the current one
def subtract_avg(firstImg,img, threshold, name, count):
	value= np.around(abs(np.mean(img) - np.mean(firstImg)), decimals= 3)
	#If value is bigger than threshold, more chances a moth is passing by
	if (threshold <= value):
		print(" * Possible element found in image: %s --subtraction value: %s"%(name, value))
		count+=1
	return count


# -------------- MAIN CODE --------------------------
#The values for imgFolderPath and threshold has been set in a file called configuration_file.py

#Load first image from the directory targeted and convert it in numpy array
imgList= os.listdir(imgFolderPath)
img0= cv2.imread(imgFolderPath+str(imgList[0]),0)
npImg0= np.array(img0)

frameCounter= 0	#To know the amount of frames with a possible change detected

t1=time.time()

#For loop using only CPU and Numpy
for imgName in imgList[0:]:
	#Read 1 image and comapre mean px values to detect changes between frames
	img= cv2.imread(imgFolderPath+str(imgName),0).astype(np.float32)
	npImg= np.array(img)
	frameCounter= subtract_avg(npImg0, npImg, threshold, imgName, frameCounter)

t3=time.time()
print("\n CPU Total duration: %s -- Frames found with pixel variation: %s"%((t3-t1), frameCounter))
print("\n ------------------------------ \n")
sys.exit()