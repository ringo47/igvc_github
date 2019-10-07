import cv2
import numpy as np

cv2.namedWindow("edges");
def funcCan():
    threshold_low = cv2.getTrackbarPos('thresh1', 'edges')
    threshold_high = cv2.getTrackbarPos('thresh2', 'edges')
    edge = cv2.Canny(orig_frame, threshold_low, threshold_high)
    print(threshold_low)
    print(threshold_high)
    cv2.imshow('edges', edge)
    
glare=0
orig_frame=cv2.imread('cap1.jpg')
edges = cv2.Canny(orig_frame, glare//6, glare//2)


cv2.createTrackbar('thresh1','edges',0,255,funcCan)
cv2.createTrackbar('thresh2','edges',0,255,funcCan)
while(1):
    
    funcCan()

    key = cv2.waitKey(1)
    if key == 27:
        video.release()
        cv2.destroyAllWindows()
    

