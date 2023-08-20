# Drowsiness-Detection-Using_Python
<div align="center">
    <img src="https://github.com/222Aryan/Drowsiness-Detection-Using_Python/blob/main/gif.gif" alt="Alt Text" />
</div>

Project Description:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
The project involves creating a real-time system that can continuously analyze a person's facial features, especially the eyes, to determine if they are showing signs of drowsiness. Drowsiness detection is crucial to prevent accidents, especially in scenarios where the person's attention is required, such as driving a vehicle or operating heavy machinery.

Key Components and Steps:
-------------------------

1. Face Detection: The project starts by using a pre-trained face detection model to identify and locate the face within a given frame or image. This is typically done using libraries like OpenCV.

2. Eye Tracking: Once the face is detected, the project focuses on tracking the person's eyes. This is essential because drowsiness is often characterized by slow or closed eye movements. The eyes' movement patterns are analyzed to determine if the person's eyes are closing or blinking at an unusual rate.

3. Feature Extraction: The project extracts relevant features from the eyes, such as the eye aspect ratio (EAR). The EAR is a measure of how open or closed the eyes are. It's calculated using the distances between various eye landmarks.

4. Drowsiness Detection Algorithm: Based on the extracted features, a drowsiness detection algorithm is implemented. This algorithm typically sets threshold values for the EAR and tracks its changes over time. If the EAR falls below a certain threshold, it indicates that the person's eyes are closing, and they might be drowsy.

5. Alert Mechanism: When drowsiness is detected, the system issues an alert to the user. This can be done using audio warnings, visual cues, or vibrations, depending on the application.

Possible Extensions:
---------------------
-> Integration with an alarm system in vehicles: If the driver is detected as drowsy, an alarm could sound in the vehicle to alert the driver and prevent an accident.

-> Real-time monitoring: The project can run in real-time, continuously analyzing the person's behavior and providing immediate warnings if drowsiness is detected.

-> Machine learning: Advanced versions of the project might incorporate machine learning techniques to improve drowsiness detection accuracy over time.


Benefits:
---------

-> Improved road safety: The project helps prevent accidents caused by drowsy driving.
Increased productivity: It can also be used in workplaces to prevent accidents caused by drowsiness while operating machinery.
Challenges:

-> Variability in people's behavior: Different people may exhibit different drowsiness patterns, making it challenging to set universal thresholds.
Environmental factors: Lighting conditions, camera quality, and other environmental factors can affect the accuracy of the system.

Challenges:
------------
-> Variability in people's behavior: Different people may exhibit different drowsiness patterns, making it challenging to set universal thresholds.

-> Environmental factors: Lighting conditions, camera quality, and other environmental factors can affect the accuracy of the system.

Steps Performed:
----------------

Step 1 – Take image as input from a camera.
<div align="center">
    <img src="https://github.com/222Aryan/Drowsiness-Detection-Using_Python/blob/main/Step%201%20Drowsiness%20detector.jpg" alt="Alt Text" />
</div>

Step 2 – Detect the face  and eye in the image and create a Region of Interest (ROI) and feed it to the classifier.
<div align="center">
    <img src="https://github.com/222Aryan/Drowsiness-Detection-Using_Python/blob/main/Step%202%20Drowsiness%20detector.jpg" alt="Alt Text" />
</div>

Step 3 – Classifier will categorize whether eyes are open or closed and calculate Aspect Ratio to check whether the person is Drowsy or Not .
<div align="center">
    <img src="https://github.com/222Aryan/Drowsiness-Detection-Using_Python/blob/main/Step%203%20Drowsiness%20detector.jpg" alt="Alt Text" />
</div>

File Required:
--------------
https://raw.githubusercontent.com/davisking/dlib-models/master/shape_predictor_68_face_landmarks.dat.bz2

Reference :
-----------
https://www.geeksforgeeks.org/python-opencv-drowsiness-detection/
