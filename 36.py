import cv2

img =cv2.imread('Flower-profile-photo-13.jpg')

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        b, g, r = img[y,x]
        a = (int(b) + int(g) + int(r)) // 3
        img[y, x] = [a, a, a]

cv2.imshow('image', img)


cv2.waitKey(0)
cv2.destroyAllWindows()