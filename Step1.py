import cv2
import dlib
import pyttsx3 
from scipy.spatial import distance

# INITIATING THE pyttsx3 So TTAT
# ALERT AUDIO MESSAGE CAN BE DELIVERED
engine = pyttsx3.init()

# SETTING UP OF CAMERA FOR DRIVER
cap = cv2.VideoCapture(0)
# DETECTING FACE AND EYE CANDIDATES 
# FROM IMAGE USING DLIB HOG FEATURES

# MAIN LOOP IT WILL RUN ALL THE UNLESS
# AND UNTIL THE PROGRAM IS BEING KILLED
# BY THE USER
while True:
    null, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Drowsiness DETECTOR IN OPENCV2", frame)
    key = cv2.waitKey(9)
    if key == 20:
        break
cap.release()
cv2.destroyAllWindows
