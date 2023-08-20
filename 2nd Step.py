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

face_detector = dlib.get_frontal_face_detector()

# PUT THE LOCATION OF .DAT FILE (FILE
# FOR PREDICTING THE LANDMARKS ON FACE )
dlib_facelandmark = dlib.shape_predictor("D:\Drowsiness Detection using python\shape_predictor_68_face_landmarks.dat")

# FUNCTION CALCULATING THE ASPECT RATIO 
# FOR THE EYE BY USING EUCLIDEAN DISTANCE
# FUNTION
def Detect_Eye(eye):
    poi_A =  distance.euclidean(eye[1], eye[5])
    poi_B =  distance.euclidean(eye[2], eye[4])
    poi_C =  distance.euclidean(eye[0], eye[3])
    aspect_ratio_Eye = (poi_A + poi_B)/(2*poi_C)
    return aspect_ratio_Eye


# MAIN LOOP IT WILL RUN ALL THE UNLESS
# AND UNTIL THE PROGRAM IS BEING KILLED
# BY THE USER
while True:
    null, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector(gray_scale)
    
    for face in faces:
        face_landmarks = dlib_facelandmark(gray_scale, face)
        leftEye = []
        rightEye = []
 
        # THESE ARE THE POINTS ALLOCATION FOR THE
        # LEFT EYES IN .DAT FILE THAT ARE FROM 42 TO 47
        for n in range(42, 48):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            rightEye.append((x, y))
            next_point = n+1
            if n == 47:
                next_point = 42
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)
    
        # THESE ARE THE POINTS ALLOCATION FOR THE 
        # RIGHT EYE IN .DAT FILE THAT ARE FROM 36 TO 41
        for n in range(36,42):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            leftEye.append((x,y))
            next_point = n+1
            if n == 41:
                next_point = 36
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (255, 255,0), 1)

    cv2.imshow("Drowsiness DETECTOR IN OPENCV2", frame)
    key = cv2.waitKey(9)
    if key == 20:
        break
cap.release()
cv2.destroyAllWindows