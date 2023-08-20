# 3rd STEP IS EXTENDED LOOP OF STEP 2
# MAIN LOOP IT WILL RUN ALL THE UNLESS
# AND UNTIL THE PROGRAM IS BEING KILLED
# BY THE USER
while True:
    null, frame = cap.read()
    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector(gray_scale)
    
    for face in faces :
        face_landmarks = dlib_facelandmark(gray_scale, face)
        leftEye = []
        rightEye = []

        # THESE ARE THE POINTS ALLOCATION FOR THE
        # LEFT EYE IN .DAT FILE THAT ARE FROM 42 TO 47
        for n in range(42 , 48 ):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            rightEye.append((x,y))
            next_point = n+1
            if n == 47:
                next_point = 42
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame , (x, y), (x2, y2), (0, 255, 0), 1)
    
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

        # STEP - 3
        # CALCULATING THE ASPECT RATIO FOR LEFT
        # AND RIGHT EYE
        right_Eye = Detect_Eye(rightEye)
        left_Eye  = Detect_Eye(leftEye)
        Eye_Rat   = (left_Eye+right_Eye)/2

        # NOW ROUND OF THE VALUE OF AVERAGE MEAN
        # OF RIGHT AND LEFT EYE
        Eye_Rat = round(Eye_Rat, 2)

        # THIS VALUE OF 0.25 WILL DECIDE
        # WHETHER THE PERSON'S EYES ARE 
        # CLOSE OR NOT
        if Eye_Rat < 0.20:
            cv2.putText(frame, "DROWSINESS DETEECTED", (50, 100), 
                        cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)
            cv2.putText(frame, "Alert!!! WAKE UP DUDE", (50, 450), 
                        cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 212), 3)
        
            # CALLING THE AUDIO FUNCTION OF TEXT TO AUDIO 
            # FOR ALERTING THE PERSON
            engine.say("Alert!!! Wake UP Dude")
            engine.runAndWait()
