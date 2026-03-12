def stress_level(face,voice):

    if face==voice:
        return "Low Stress"

    if face in ["Sad","Angry"] and voice in ["Sad","Angry"]:
        return "High Stress"

    if face=="Neutral":
        return "Normal"

    return "Medium Stress"