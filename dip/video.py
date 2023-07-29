import cv2 as cv
video_reader = cv.VideoCapture(0) # 0 is for reading for webcam

while True:
    success , frame = video_reader.read()
    if not success:
        break
    
    cv.imshow("My video" , frame)
    key = cv.waitKey(10)
    
    if key == ord('q') or key == ord('Q'):
    
        break
    
video_reader.release()
cv.distroyAllWindow()
    