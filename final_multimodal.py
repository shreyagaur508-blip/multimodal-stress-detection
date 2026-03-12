def multimodal_result(face,voice):

    if face == voice:
        return face

    elif face == "Sad" and voice == "Angry":
        return "Stressed"

    else:
        return face


face_emotion = "Sad"
voice_emotion = "Angry"

result = multimodal_result(face_emotion,voice_emotion)

print("Final Emotion:",result)