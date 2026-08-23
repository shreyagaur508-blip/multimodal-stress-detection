# Multimodal Stress Detection

An AI-based multimodal stress detection system that uses machine learning models to predict a person's stress level in real time by analyzing **live facial expressions** and **live voice recordings**.

## 🧠 Overview

This project combines **facial emotion recognition** and **voice emotion recognition** into a single fusion model to estimate stress levels. It captures live video (for facial expression analysis) and live audio (for voice tone/emotion analysis), processes both streams through trained ML models, and fuses the results to produce a final stress prediction.

## 📂 Repository Structure

```
multimodal-stress-detection/
├── .devcontainer/              # Dev container configuration
├── templates/                  # HTML templates for the web app
├── .gitignore
├── app.py                      # Main application entry point (likely Flask app)
├── face_detect.py              # Face detection logic
├── face_train.py               # Training script for the facial emotion model
├── final_multimodal.py         # Final combined multimodal pipeline
├── fusion.py                   # Fusion logic combining face + voice predictions
├── live_face_emotion.py        # Real-time facial emotion detection
├── live_voice_emotion.py       # Real-time voice emotion detection
├── multimodal_fusion.py        # Multimodal fusion model/logic
├── requirements.txt            # Python dependencies
├── runtime.txt                 # Python runtime version (for deployment)
├── temp.jpg                    # Temporary/sample image asset
├── voice_detect.py             # Voice activity/emotion detection
├── voice_emotion_model.pkl     # Trained voice emotion classification model
├── voice_train.py              # Training script for the voice emotion model
└── README.md
```

## ✨ Features

- **Real-time facial emotion detection** via webcam (`live_face_emotion.py`, `face_detect.py`)
- **Real-time voice emotion detection** via microphone (`live_voice_emotion.py`, `voice_detect.py`)
- **Multimodal fusion** combining facial and vocal emotion signals for a more robust stress prediction (`fusion.py`, `multimodal_fusion.py`, `final_multimodal.py`)
- **Pre-trained voice emotion model** included (`voice_emotion_model.pkl`)
- **Trainable pipelines** for both face and voice models (`face_train.py`, `voice_train.py`)
- **Web interface** via Flask-style `app.py` and `templates/`
- **Dev Container support** for a consistent development environment

## 🛠️ Tech Stack

- **Python** (69.3%) – core ML pipelines, model training, and inference
- **HTML** (30.7%) – web UI templates
- Likely libraries (see `requirements.txt`): OpenCV, TensorFlow/Keras or PyTorch, librosa (audio processing), scikit-learn, Flask

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/shreyagaur508-blip/multimodal-stress-detection.git
cd multimodal-stress-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Then open the app in your browser (default Flask port is usually `http://localhost:5000`).

## 📋 Requirements

- Python (version specified in `runtime.txt`)
- Webcam (for facial emotion capture)
- Microphone (for voice emotion capture)
- Dependencies listed in `requirements.txt`

## 🎯 How It Works

1. **Face module** – Captures live video, detects the face, and classifies emotion using a trained facial emotion model.
2. **Voice module** – Records live audio, extracts features, and classifies emotion using `voice_emotion_model.pkl`.
3. **Fusion module** – Combines both predictions (`fusion.py` / `multimodal_fusion.py`) to compute an overall stress level.
4. **Web app** – `app.py` serves the interface (via `templates/`) to display live results to the user.

## 🤝 Contributing

Contributions and suggestions are welcome via issues or pull requests.

## 📄 License

No license specified yet — consider adding one (e.g., MIT) if you'd like others to reuse this code freely.

## 👤 Author

**Shreya V Gaur** ([@shreyagaur508-blip](https://github.com/shreyagaur508-blip))
