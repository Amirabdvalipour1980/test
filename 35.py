import cv2

img =cv2.imread('Flower-profile-photo-13.jpg')
resized = cv2.resize(img, (500,300))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', img)
cv2.imshow('gray', gray)
cv2.imshow('resized', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
