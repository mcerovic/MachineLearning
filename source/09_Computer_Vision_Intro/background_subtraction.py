import numpy as np
import cv2

cap = cv2.VideoCapture('../../data/09_CV/vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((2, 2), np.uint8)

while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    # res = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    res = fgmask

    cv2.imshow('frame', res)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
