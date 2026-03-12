import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Dropout, Flatten
from tensorflow.keras.utils import to_categorical

# LOAD DATASET (CORRECT PATH)
data = pd.read_csv("datasets/images/fer2013/fer2013.csv")

pixels = data['pixels'].tolist()

faces = []

for pixel_sequence in pixels:
    face = [int(pixel) for pixel in pixel_sequence.split()]
    face = np.asarray(face).reshape(48,48)
    faces.append(face)

faces = np.asarray(faces)

# NORMALIZE
faces = faces / 255.0

# RESHAPE
faces = faces.reshape(-1,48,48,1)

# EMOTION LABELS
emotions = to_categorical(data['emotion'])

# BUILD MODEL
model = Sequential()

model.add(Conv2D(32,(3,3),activation='relu',input_shape=(48,48,1)))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D(2,2))

model.add(Flatten())

model.add(Dense(128,activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(7,activation='softmax'))

# COMPILE MODEL
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("Training Started...")

# TRAIN MODEL
model.fit(faces, emotions, epochs=40, batch_size=64)

# SAVE MODEL
model.save("face_emotion_model.h5")

print("Model Saved Successfully")