import cv2
import os

import numpy as np
from omnimatte.datasets import confidence

def flow_cal():
    pass


def vid2frame(src,vidDir):
	if not os.path.exists(vidDir):
		os.makedirs(vidDir)
	cap = cv2.VideoCapture(src)
	count = 0
	while(cap.isOpened()==True):
		flag, frame= cap.read()
		if not flag:
			print("Finished!")
			break
		else:
			img_name = +str(count).rjust(5,'0') + ".png"
			new_path = vidDir + img_name
			cv2.imwrite(new_path,frame)
			count += 1
	cap.release()

def homographi(img1,img2):
	h, status = cv2.findHomography(img1,img2)
	h = h.resize(1,9)
	return h

def write_homo_text(img1,img2):
	H = []
	for i in range(100): #change
		h = homographi(img1,img2)
		H.append(h)
	np.savetxt("homographies.txt",H,fmt='%f')



def confidence_map(dataroot):
	conf_map = confidence.main(dataroot=dataroot)
