import cv2 as cv
import numpy as np


def nothing(x):
    pass


def createTrackbar():
    cv.namedWindow("Thresholding")
    cv.createTrackbar("LH", "Thresholding", 0, 255, nothing)
    cv.namedWindow("Thresholding")
    cv.createTrackbar("LS", "Thresholding", 0, 255, nothing)
    cv.namedWindow("Thresholding")
    cv.createTrackbar("LV", "Thresholding", 0, 255, nothing)
    cv.namedWindow("Thresholding")
    cv.createTrackbar("UH", "Thresholding", 0, 255, nothing)
    cv.namedWindow("Thresholding")
    cv.createTrackbar("US", "Thresholding", 0, 255, nothing)
    cv.namedWindow("Thresholding")
    cv.createTrackbar("UV", "Thresholding", 0, 255, nothing)


img = cv.imread('./Images/1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# cv.imshow("gray" ,gray)

_, threshimg = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

# cv.imshow("thresh" , threshimg)

createTrackbar()

while True:
    LH = cv.getTrackbarPos("LH", "Thresholding")
    LS = cv.getTrackbarPos("LS", "Thresholding")
    LV = cv.getTrackbarPos("LV", "Thresholding")
    UH = cv.getTrackbarPos("UH", "Thresholding")
    US = cv.getTrackbarPos("US", "Thresholding")
    UV = cv.getTrackbarPos("UV", "Thresholding")
    # print(LH)
    # print(UH)
    # print(LS)
    # print(US)
    # print(LV)
    # print(UV)
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lower = np.array([LH, LS, LV])
    upper = np.array([UH, US, UV])
    thresh_img = cv.inRange(img, lower, upper)

    img_hsv = cv.inRange(img, lower, upper)
    # _ , threshimg = cv.threshold(gray , T , 255  , cv.THRESH_BINARY)
    cv.imshow("hsv_image", thresh_img)
    imageCopy = img.copy()
    contour, _ = cv.findContours(thresh_img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) #CHAIN_APPROX_SIMPLE
    # print(contour)
    cv.drawContours(imageCopy, contour, 1, (255, 0, 0), 2)
    cv.imshow("image", imageCopy)

    key = cv.waitKey(1)
    if key == ord(' ') or key == ord('q'):
        break
cv.destroyAllWindows()
cv.waitKey()
