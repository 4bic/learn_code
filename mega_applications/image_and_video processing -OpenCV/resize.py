import cv2
import glob
# glob finds file names / patterns

# open all image files from folder
images = glob.glob("*.jpg")

def resize():
    # iterate over folder for every image filw
    for image in images:
        # read image file in grayscale(0)
        img = cv2.imread(image, 0)
        # resize image
        re_img = cv2.resize(img,(100,100))
        # briefly display resized image on window
        cv2.imshow("hey", re_img)
        cv2.waitKey(500)
        # kill the window
        cv2.destroyAllWindows()
        # save resized image to file
        cv2.imwrite("resized_"+image, re_img)

resize()
