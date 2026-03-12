import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import numpy as np
import pickle

# record voice
fs = 22050
seconds = 3

print("Speak now...")

recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

write("recorded.wav", fs, recording)

print("Recording complete")

# load model
model = pickle.load(open("voice_emotion_model.pkl","rb"))

def extract_feature(file):

    audio, sr = librosa.load(file, duration=3)

    mfcc = np.mean(librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=40
    ).T, axis=0)

    return mfcc


feature = extract_feature("recorded.wav")

feature = feature.reshape(1,-1)

prediction = model.predict(feature)

print("Predicted Emotion:", prediction)