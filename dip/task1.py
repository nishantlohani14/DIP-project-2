import numpy as np
import cv2 as cv

img_path = "./Images/1.jpg"

img = cv.imread(img_path)

# w = cv.imread("./Images/white.jpg")

w = np.full((img.shape), 255 , dtype = 'uint8')

cv.imshow("White.." , w)

cv.imshow("true image " , img)

final  = cv.subtract(w,img)

cv.imshow("final image: " , final)

cv.waitKey()

# print(w)

# print(img)