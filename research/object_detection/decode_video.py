import cv2
import os

count_frame = 266
VIDEO_PATH = './project_images/boxes/video_source'
for file in os.listdir(VIDEO_PATH):
	cap = cv2.VideoCapture(os.path.join(VIDEO_PATH, file))
	rval = cap.isOpened()
	n = 0
	while rval:
		rval, frame = cap.read()
		n += 1
		if rval and n % 10 == 0:
			count_frame += 1
			cv2.imwrite('./project_images/boxes/box' + str(count_frame) + '.jpeg', frame)