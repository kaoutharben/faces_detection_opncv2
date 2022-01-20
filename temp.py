# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#to capture video from our laptop webcam
cap = cv2.VideoCapture(0)

while True:
    
    # Read the frame
    _, img = cap.read()
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect the faces
    faces = faceCascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    # Display
    cv2.imshow('img', img)
    
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    
# Release the VideoCapture object
cap.release()
