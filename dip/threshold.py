import cv2 as cv

img_path = './Images/3.jpg'
img = cv.imread(img_path)
gray_scale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Img", img)

_, thresh_img = cv.threshold(gray_scale_img, 50, 255, cv.THRESH_OTSU)
cv.imshow("img", thresh_img)
cv.waitKey()
