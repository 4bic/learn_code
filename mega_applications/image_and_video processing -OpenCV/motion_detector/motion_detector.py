import cv2,time

# capture frames
first_frame = None
# capture video
video=cv2.VideoCapture(0)# 0-built in cam, 1-external cam

while True:
    # create frame to read images captures by cam
    check, frame = video.read()
    # convert image to grayscale
    gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # blur frame to remove noise and increase accuracy
    gray_img= cv2.GaussianBlur(gray_img,(21,21),0)

    if first_frame is None:
        first_frame = gray_img
        continue
    # compare first_frame and current frame
    delta_frame = cv2.absdiff(first_frame,gray_img)

    # threshold - classify the difference values of the pixels 
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    # display window
    cv2.imshow("Video Capturing", gray_img)
    # period window to stay active
    cv2.imshow("Delta Frame",delta_frame)

    cv2.imshow("thresh frame", thresh_frame)

    key = cv2.waitKey(1)
    if key==ord('q'):
        break

# release video.camera
video.release()
# destroy all open windows
cv2.destroyAllWindows()
