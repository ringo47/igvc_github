import cv2
import numpy as np
import serial


arduino = serial.Serial('COM17', 9600, timeout=.1)
video = cv2.VideoCapture("igvc_unsw.mp4")
glare=0
while True:
    arduino.flushInput()
    data = arduino.readline()[:-2]
    if data:
        try:
            glare=int(data)
            print(glare)
        except ValueError:
            continue
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture("igvc_unsw.mp4")
        continue
    orig_frame=cv2.imread('cap1.jpg')
##    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
##    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_yellow = np.array([18, 94, 140])
    up_yellow = np.array([48, 255, 255])

    mask = cv2.inRange(orig_frame, low_yellow, up_yellow)
    for glare in range(80):
        edges = cv2.Canny(orig_frame, glare, glare*3)
        cv2.imshow("edges", edges)

##    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=50)
##    if lines is not None:
##        for line in lines:
##            x1, y1, x2, y2 = line[0]
##            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

##    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)

    key = cv2.waitKey(1)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()
