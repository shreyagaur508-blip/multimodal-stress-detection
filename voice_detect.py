import librosa
import numpy as np
import pickle

model = pickle.load(open("voice_emotion_model.pkl","rb"))

def detect_voice_audio(file):

    audio, sr = librosa.load(file, duration=3)

    mfcc = np.mean(
        librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40).T,
        axis=0
    )

    feature = mfcc.reshape(1,-1)

    prediction = model.predict(feature)

    return prediction[0]