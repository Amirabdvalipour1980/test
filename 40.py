import cv2

img =cv2.imread('Flower-profile-photo-13.jpg')
resized = cv2.resize(img, (500,400))
cv2.rectangle(resized, (0, 0), (500, 400), (255, 235, 0), 10)
cv2.imshow('image', img)
cv2.imshow('resized', resized)

cv2.waitKey(0)
cv2.destroyAllWindows()