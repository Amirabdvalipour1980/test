import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, h, w) in faces:
        cv2.rectangle(frame, (x, y),(100, 100),80, (0, 255, 0), 2)
        # cv2.circle(frame,80,(x, y),(x+w, y+h), (0, 0, 255), 3)
    cv2.imshow('webcam main frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()