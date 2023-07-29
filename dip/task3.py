import cv2 as cv
import numpy as np

img = cv.imread('./Images/3.jpg')
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


(h, w) = grayimg.shape

final = np.full(grayimg.shape, 0, dtype='uint8')
# final = grayimg

pixel_val = int(input())

for i in range(0, h):

    for j in range(0, w):

        if (grayimg[i][j] > pixel_val):

            final[i][j] = 255

        else:

            final[i][j] = 0 
            

cv.imshow("final", final)
cv.waitKey()
