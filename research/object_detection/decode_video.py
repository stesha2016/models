import cv2

cap = cv2.VideoCapture('./project_images/boxes/VID_20190129_161859.mp4')
rval = cap.isOpened()
count_frame = 191
n = 0
while rval:
	rval, frame = cap.read()
	n += 1
	if rval and n % 10 == 0:
		count_frame += 1
		cv2.imwrite('./project_images/boxes/box' + str(count_frame) + '.jpeg', frame)