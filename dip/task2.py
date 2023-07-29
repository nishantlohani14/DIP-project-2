import cv2 as cv
import numpy as np

img_path = "./Images/4.jpg"

img = cv.imread(img_path)

red  =  np.full((img.shape), 50 , dtype = 'uint8')

red[ : , : ,  : 2] = 0

final = red + img

cv.imshow("final " , final)
cv.imshow("img" , img)
cv.imshow("red" , red)
cv.waitKey(0)

print(red)

