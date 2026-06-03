 # 🎭 MoodFace — AI-Powered Mood-Based Music Recommender

> A real-time emotion detection system that recommends Spotify playlists based on facial expressions using a custom-trained CNN model.

## 🌐 Live Demo
**[moodface.streamlit.app](https://moodface.streamlit.app)**

---

## Overview

MoodFace combines computer vision and music recommendation to create a seamless mood-based listening experience. The system captures a photo via webcam, detects the user's facial expression using a trained deep learning model, and surfaces relevant Spotify playlists — all in under 3 seconds.

---

## Features

- Real-time face detection via OpenCV
- Custom CNN model trained on FER2013 dataset (35,000+ images, 7 emotion classes)
- Spotify playlist recommendations via Spotipy API
- One-click redirect to Spotify
- Deployed on Streamlit Cloud

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend & App | Streamlit |
| Face Detection | OpenCV (Haar Cascade) |
| Emotion Classification | TensorFlow / Keras CNN |
| Music API | Spotify Web API (Spotipy) |
| Deployment | Streamlit Cloud |
| Language | Python 3.10 |

---

## Project Structure
Moodface-Music-Suggestor/
├── app.py                    # Streamlit application entry point
├── moodface/
│   ├── detector.py           # Face detection module (OpenCV)
│   ├── music_suggester.py    # Spotify API integration
│   └── mood_model.h5         # Trained CNN model weights
├── data/                     # FER2013 training data
├── requirements.txt
└── README.md
---

## Quick Start

**Prerequisites:** Python 3.10+

```bash
git clone https://github.com/24051081-dotcom/Moodface-Music-Suggestor
cd Moodface-Music-Suggestor
pip install -r requirements.txt
streamlit run app.py
```

App runs at `http://localhost:8501`

---

## Model

- **Dataset:** FER2013 — 35,887 labeled facial expression images
- **Architecture:** Custom CNN (Conv2D → MaxPooling → Dropout → Dense)
- **Input:** 48×48 grayscale face crop
- **Output:** 7 classes — Angry, Disgust, Fear, Happy, Neutral, Sad, Surprise
- **Framework:** TensorFlow / Keras

---

## Emotion → Playlist Mapping

| Emotion | Spotify Query |
|---------|--------------|
| Happy | happy upbeat pop |
| Sad | sad emotional songs |
| Angry | rock intense angry |
| Fear | calm ambient relaxing |
| Surprise | bollywood party |
| Disgust | alternative indie |
| Neutral | chill acoustic |

---

## Team

| Name | Responsibility |
|------|---------------|
| Alka Singh | CNN model training, emotion classification pipeline |
| Shriya Singh | Face detection, Streamlit app, Spotify integration |

---

## Notes

- Camera input is processed client-side — no images are stored or transmitted
- Spotify API uses Client Credentials flow (read-only playlist search)