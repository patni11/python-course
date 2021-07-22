import cv2
import os
import time
video = cv2.VideoCapture(0)

face = cv2.CascadeClassifier(
    f'{os.getcwd()}/tasks/haarcascade_frontalface_alt2.xml')

while True:
    _, frames = video.read()
    frames = cv2.flip(frames, 1)

    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

    if len(faces) != 0:
        for x, y, w, h in faces:
            roi = gray[y:y+h, x:x+h]
            cv2.rectangle(frames, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.imshow('frame', frames)
            time.sleep(0.5)

    key = cv2.waitKey(100)
    if key == 27:
        break

cv2.destroyAllWindows()
