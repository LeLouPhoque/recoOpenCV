import cv2
import numpy as np
import time
import os


# Chargement du modèle d'entraînement
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('/home/usersio/work/test.yml')

# Chargement du classificateur de visages
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialisation du flux vidéo
cap = cv2.VideoCapture(0)

# Initialisation des variables pour le renforcement de la confiance
current_id = 'kilian'
confidence_threshold = 70
confidence_counter = 0
name = 'Inconnu'
time_start = time.time()
path = 'image'
names = {}
pasreconnu = True
id=0

for subdir in os.listdir(path):
    names[id]=subdir
    id+=1

while pasreconnu:
    # Lecture de l'image depuis le flux vidéo
    ret, img = cap.read()

    # Conversion en niveaux de gris
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Détection des visages dans l'image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    # Reconnaissance des visages détectés
    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        label, confidence = recognizer.predict(roi)
        if confidence < confidence_threshold:
            name = "Personne {}".format(names[label])
            if current_id == names[label]:
                confidence_counter += 1
                print (confidence_counter)
                if confidence_counter >= 5:
                    pasreconnu = False

        else:
            name = 'Inconnu'
        # Affichage du nom de la personne reconnue sur l'image
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Affichage de l'image avec les résultats de reconnaissance de visages
    cv2.imshow('Reconnaissance de visages', img)

    # Vérification de la limite de temps
    time_current = time.time()
    if (time_current - time_start) > 60:
        pasreconnu = False

    # Sortie de la boucle infinie si l'utilisateur appuie sur la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pasreconnu = False

# Arrêt du flux vidéo
cap.release()
cv2.destroyAllWindows()
