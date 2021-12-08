import cv2
import numpy as np

def jpgtohsv(img_path):
    img = cv2.imread(img_path)

    if img is None:
        print("Image invalid")
        return

    lwr = np.array([0, 0, 69])
    upr = np.array([180, 255, 255])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    msk = cv2.inRange(hsv, lwr, upr)
    
    cv2.imshow('Original image',img)
    cv2.imshow('HSV image', msk)

    cv2.waitKey(0)
    cv2.destroyAllWindows()