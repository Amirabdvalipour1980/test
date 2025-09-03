import cv2

img =cv2.imread('Flower-profile-photo-13.jpg')
resized = cv2.resize(img, (500,500))
cv2.imshow('image', img)
cv2.imshow('resized', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()