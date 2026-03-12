from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    face_emotions = ["Happy","Sad","Angry","Neutral"]
    voice_emotions = ["Calm","Stressed","Happy"]

    face = random.choice(face_emotions)
    voice = random.choice(voice_emotions)

    if face == "Angry" or voice == "Stressed":
        stress = "High"
    else:
        stress = "Low"

    return jsonify({
        "face": face,
        "voice": voice,
        "stress": stress
    })


if __name__ == "__main__":
    app.run(debug=True)