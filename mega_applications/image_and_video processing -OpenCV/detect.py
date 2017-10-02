import cv2

# read image
#   0-grayscale, 1-BGR , -1 >color with transparency
img = cv2.imread("resource/galaxy.jpg", 0)

# print (type(img))
# <type 'numpy.ndarray'>
# print img
# [[14 18 14 ..., 20 15 16]
#  [12 16 12 ..., 20 15 17]
#  [12 13 16 ..., 14 24 21]
#  ...,
#  [ 0  0  0 ...,  5  8 14]
#  [ 0  0  0 ...,  2  3  9]
#  [ 1  1  1 ...,  1  1  3]]

# resize img to fit window
# divide by half size from original shape
resized_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))

# show image on a window
cv2.imshow('GaLAXy', resized_img)
# save image to file
cv2.imwrite('resource/new_galaxy.png', resized_img)
# time to close window
cv2.waitKey(2000)
# action to be taken once the window is clicked
cv2.destroyAllWindows()
