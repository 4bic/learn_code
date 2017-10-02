import cv2,time

# capture frames
first_frame = None
# capture video
video=cv2.VideoCapture(0)# 0-built in cam, 1-external cam

while True:
    # create frame to read images captures by cam
    check, frame= video.read()
    # convert image to grayscale
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # check confirms video is running

    if first_frame is None:
        first_frame = gray_img
        continue
            
    # display window
    cv2.imshow("Video Capturing", gray_img)
    # period window to stay active
    key = cv2.waitKey(1)

    if key==ord('q'):
        break

# release video.camera
video.release()
# destroy all open windows
cv2.destroyAllWindows()
