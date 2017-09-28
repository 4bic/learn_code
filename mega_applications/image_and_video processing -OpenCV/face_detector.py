import cv2

face_cascade = cv2.CascadeClassifier("resource/haarcascade_frontalface_default.xml")
# open colored image
img = cv2.imread("resource/photo.jpg")
# convert BGR image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# store width and height values of face
faces = face_cascade.detectMultiScale(gray_img,
# once checked, reduce image by 5%
scaleFactor=1.05,
# how many cells to be checked aroung the window
minNeighbors=5)

# print faces
# [[159 124 308 308]]
# draw a rectangle around the face
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y),(x+w, y+h),(0,255,0), 3)

cv2.imshow("Gray", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
