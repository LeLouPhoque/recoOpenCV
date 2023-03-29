import cv2
import sys
import os
import time

i = 0
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

path = '/home/usersio/work/image'
while True:
    if not video_capture.isOpened():
        print("error")
        break
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    frame1 = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(80, 80),
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if i < 50 :
            cv2.imwrite(os.path.join(path, 'image'+str(i)+'.png'),frame1[y:y+h, x:x+w])
            i = i+1
    # Display the resulting frame
    
    cv2.imshow('Video', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(2)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
