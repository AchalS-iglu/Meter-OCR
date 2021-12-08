import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract

from modules.jpgtohsv import jpgtohsv


path = "./images/"
files = [file for file in os.listdir(path) if file.endswith('.jpg')]
#print(sorted(files))

custom_config = r'--oem 3 --psm 6'
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract"
TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'

while True:
    for image in files:
        #jpgtohsv(("./images/" + image))
        img = cv2.imread("./images/" + image)
        if img is None:
            print('Invalid Image')
            continue
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_edge = cv2.Canny(img, 70, 120)    

        cv2.imshow('image window1', img)
        cv2.imshow('image window2',img_edge)

        contours, hierarchy = cv2.findContours(img_edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
        cv2.imshow('Contours', img)
        
        reading = pytesseract.image_to_string(img_edge, config=custom_config)
        print(reading)
    
        key = cv2.waitKey(30000)
        if key == ord('q') or key == 27:
            continue

    break