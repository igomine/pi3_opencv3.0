import cv2

filename = '../images/face_dect3.JPG'


def detect(filename):
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
    img = cv2.imread(filename)
    img2 = cv2.resize(img, (800, 800), interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img2 = cv2.rectangle(img2, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.namedWindow('Vikings Detected!!')
    cv2.imshow('Vikings Detected!!', img2)
    # cv2.imwrite('./vikings.jpg', img)
    cv2.waitKey(0)

detect(filename)
