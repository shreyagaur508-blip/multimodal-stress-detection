def detect_stress(face_emotion, voice_emotion):

    # High stress conditions
    if face_emotion in ["Angry", "Sad", "Fear"] and voice_emotion in ["angry", "sad"]:
        return "High Stress"

    # Low stress condition
    elif face_emotion == "Happy" and voice_emotion == "happy":
        return "Low Stress"

    # Medium stress
    else:
        return "Medium Stress"