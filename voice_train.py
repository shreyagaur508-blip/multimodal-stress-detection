import librosa
import numpy as np
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def extract_feature(file):
    audio, sr = librosa.load(file, duration=3)
    mfcc = np.mean(librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40).T, axis=0)
    return mfcc

features = []
labels = []

dataset_path = "datasets/audio"

for emotion in os.listdir(dataset_path):

    emotion_path = os.path.join(dataset_path, emotion)

    for file in os.listdir(emotion_path):

        file_path = os.path.join(emotion_path, file)

        feature = extract_feature(file_path)

        features.append(feature)
        labels.append(emotion)

X = np.array(features)
y = np.array(labels)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()

model.fit(X_train,y_train)

accuracy = model.score(X_test,y_test)

print("Accuracy:",accuracy)

pickle.dump(model,open("voice_emotion_model.pkl","wb"))

print("Voice Model Saved")