import numpy as np
import pandas as pd
import cv2

# creating numpy arrays out of images
im_g = cv2.imread("smallgray.png", 1) #0-grayscale ; 1-BGR array

print im_g
# results for (0) :[[187 158 104 121 143]
#              [198 125 255 255 147]
#              [209 134 255  97 182]]
