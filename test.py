import cv2 
img = cv2.imread('/home/python-test/14.jpg')
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
GRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(GRAY)
