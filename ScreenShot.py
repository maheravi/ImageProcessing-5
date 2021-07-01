import cv2
import random

import keyboard  # using module keyboard
from instapy import InstaPy
from instapy_cli import client
from instabot import Bot

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

my_video = cv2.VideoCapture('Obama.mp4')

while True:

    validation, frame = my_video.read()
    # screen = False

    if validation is not True:
        break

    if keyboard.is_pressed('q'):
        cv2.imwrite('screen.jpg', frame)
        bot = Bot()
        bot.login(username="****",
                  password="****")
        bot.upload_photo("screen.jpg",
                         caption="Barak Obama 2020")
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(frame_gray, 1.3)

    for i, face in enumerate(faces):
        x, y, w, h = face

        frame_face = frame[y:y + h, x:x + w]
        cv2.imwrite(f'kalle ha/kalle{i}.png', frame_face)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 8)

    cv2.imshow('output', frame)
    cv2.waitKey(1)
