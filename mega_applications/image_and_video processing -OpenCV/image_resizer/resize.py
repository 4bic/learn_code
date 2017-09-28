import cv2
import glob

# open all image files from folder
images = glob.glob("*.jpg")

def resize():
    for image in images:
        img = cv2.imread(image, 0)
        re_img = cv2.resize(img,(100,100))
        cv2.imshow("hey", re_img)
        cv2.waitKey(500)
        cv2.destroyAllWindows()
        cv2.imwrite("resized_"+image, re_img)


resize()
