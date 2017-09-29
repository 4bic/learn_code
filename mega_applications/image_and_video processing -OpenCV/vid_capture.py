import cv2,time

# capture video
video=cv2.VideoCapture(0)# 0-built in cam, 1-external cam

# create frame to read images captures by cam
check, frame= video.read()
# check confirms video is running
# print check
# TRUE

time.sleep(3)
# display window
cv2.imshow("Video Capture", frame)

# period window to stay active
cv2.waitKey(0)
# release video.camera
video.release()
# destroy all open windows
cv2.destroyAllWindows()
