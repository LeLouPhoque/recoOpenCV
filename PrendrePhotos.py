import cv2
import sys
import os
import time

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

path = '/home/usersio/Raspberry-AP4-main/Images_Reco'

try:
    print("Identifiant de l'infirmière")
    fn_name = input()
    if len(fn_name)==0:
        print("Vous devez fournir un identifiant valide !")
        sys.exit(0)
except:
    print("Erreur de saisie !")
    sys.exit(0)

path = os.path.join(path, fn_name)

if not os.path.isdir(path):
    os.mkdir(path)
i=0 
pause = 0
while i < 50 :
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
        minSize=(100, 100),
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        if pause == 0:
            cv2.imwrite(os.path.join(path, 'image'+str(i)+'.png'),frame1[y:y+h, x:x+w])
            print("image"+str(i))
            pause = 1
            i = i+1
    # Display the resulting frame
    
    cv2.imshow('Video', frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if(pause > 0):
        pause = (pause + 1) % 5
print("fin")
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()