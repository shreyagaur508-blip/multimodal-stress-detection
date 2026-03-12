import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("face_emotion_model.h5")

emotion_labels = ["Angry","Disgust","Fear","Happy","Sad","Surprise","Neutral"]

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_face_image(image_path):

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:

        face = gray[y:y+h, x:x+w]
        face = cv2.resize(face,(48,48))
        face = face/255.0
        face = face.reshape(1,48,48,1)

        prediction = model.predict(face)

        return emotion_labels[np.argmax(prediction)]

    return "No Face"