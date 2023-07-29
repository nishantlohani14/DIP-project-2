import cv2

img_path = "./Images/4.jpg"

img = cv2.imread(img_path)

# print(img)

# print(img.shape)

# cv2.imshow("Image" , img)

# cv2.waitKey()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #BGR 2 HSV , RGB , GRAY

cv2.imshow("Image" , img)

# cv2.imshow("Gray Image" , img_gray)

cv2.imwrite("./Images/4_gray.jpg" , img_gray)

print("image shape" , img.shape)

print("gray image shape"  , img_gray.shape)

img_resize = cv2.resize(img , (500,500))

cv2.imshow("resized Image "   , img_resize)

rows, cols, colors = img.shape
img_crop = img[ : , cols//2:]

cv2.imshow("cropped image " , img_crop)

cv2.waitKey()
