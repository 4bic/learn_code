import numpy as np
import pandas as pd
import cv2

# creating numpy arrays out of images
im_g = cv2.imread("smallgray.png", 1) #0-grayscale ; 1-BGR array

# creating images from numpy arrays
cv2.imwrite("newsmallgray.png",im_g)

# print im_g
# results for (0) :[[187 158 104 121 143]
#              [198 125 255 255 147]
#              [209 134 255  97 182]]

# slicing an array
# 3rd & 4th elements on first & 2nd rows
im_g[0:2, 2:4]

# check shape of array
img.shape

# iterating thro
#1
for i in im_g:
    print (i)
#2
# value for value
for i in im_g.flat:
    print (i)

# stacking numpy arrays
#Horizontally
ims = numpy.hstack((im_g,im_g)) #tuple of arrays
