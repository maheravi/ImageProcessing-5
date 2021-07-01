import cv2
import numpy as np

my_video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
validation, frame = my_video.read()

size = (frame.shape[1], frame.shape[0])

out = cv2.VideoWriter('12.mov', cv2.VideoWriter_fourcc(*'MJPG'), 10, size, 0)

while True:

    validation, frame = my_video.read()

    if validation is not True:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    white_mask = cv2.inRange(frame_gray, 190, 255)
    gray_mask = cv2.inRange(frame_gray, 80, 189)
    black_mask = cv2.inRange(frame_gray, 0, 79)

    x = 100
    y = 100
    w = 100
    h = 100

    cv2.rectangle(frame_gray, (x, y), (x + w, y + h), (0, 0, 0), 8)
    detector = frame_gray[x:x+w, y:y+h]
    frame_gray = cv2.blur(frame_gray, (49, 49))
    frame_gray[x:x+w, y:y+h] = detector
    color = np.average(detector)

    if color <= 90:
        cv2.putText(frame_gray, "Black", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 1)
    elif color >= 180:
        cv2.putText(frame_gray, "White", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 1)
    else:
        cv2.putText(frame_gray, "Gray", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 1)

    out.write(frame_gray)

    cv2.imshow('output', frame_gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

my_video.release()
out.release()
cv2.destroyAllWindows()

print("The video was successfully saved")
