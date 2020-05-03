import cv2
import numpy as np
import serial

#arduino = serial.Serial('COM17', 9600, timeout=.1)
video = cv2.VideoCapture("igvc_unsw.mp4")

while True:
    data=1
    #data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:
        print(data)
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture("igvc_unsw.mp4")
        continue

    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    low_white = np.array([200, 200, 200])
    up_white = np.array([255, 255, 255])
    mask = cv2.inRange(orig_frame, low_white, up_white)
    edges = cv2.Canny(mask, 75, 150)
    image_canny = cv2.Canny(edges, 50, 150)
    # ROI
    vertices = np.array([[(0,650),(300,300), (900, 300), (1150,650)]], dtype=np.int32)
    #vertices = np.array([[(20,460),(340, 300), (460, 300), (740,460)]], dtype=np.int32)    
    mask = np.zeros_like(image_canny)
    cv2.fillPoly(mask, vertices, 255)
    masked_image = cv2.bitwise_and(image_canny, mask)

    lines = cv2.HoughLinesP(masked_image, 2, np.pi/180, 40, np.array([]), 100, 50)
        
    line_image = np.zeros((masked_image.shape[0], masked_image.shape[1], 3), dtype=np.uint8)

    try:
        for line in lines:
            for x1,y1,x2,y2 in line:      
                cv2.line(line_image, (x1, y1), (x2, y2), [255, 0, 0], 20)
    except TypeError:
        continue

    α = 1
    β = 1
    γ = 0    
    # Resultant weighted image is calculated as follows: original_img * α + img * β + γ
    Image_with_lines = cv2.addWeighted(orig_frame, α, line_image, β, γ)

    cv2.imshow("frame", frame)
    cv2.imshow("EDGES", Image_with_lines)

    key = cv2.waitKey(1)
    if key == 27:
        break

video.release()
cv2.destroyAllWindows()
arduino.close()
