import cv2

img =cv2.imread('Flower-profile-photo-13.jpg')

cv2.line(img, (0, 0), (100, 100), (255, 0, 0), 5)
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 10)
cv2.circle(img, (100, 100),80, (0, 0, 255), 3)
cv2.putText(img, "OPENCV", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2,(255, 255, 255), 3)

cv2.imshow('image', img)


cv2.waitKey(0)
cv2.destroyAllWindows()