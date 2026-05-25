import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from moodface.detector import FaceDetector
from moodface.music_suggester import suggest_music

st.set_page_config(
    page_title="MoodFace 🎭",
    page_icon="🎭",
    layout="wide"
)

st.title("🎭 MoodFace - Music Suggester")
st.subheader("Let AI detect your mood and suggest perfect music!")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model('moodface/mood_model.h5')

model = load_model()
detector = FaceDetector()

MOODS = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

def predict_mood(face):
    face = cv2.resize(face, (48, 48))
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    face = face / 255.0
    face = face.reshape(1, 48, 48, 1)
    prediction = model.predict(face, verbose=0)
    return MOODS[np.argmax(prediction)]

col1, col2 = st.columns(2)

with col1:
    st.header("📷 Camera")
    camera = st.camera_input("Take a photo")

with col2:
    st.header("🎵 Results")
    if camera is not None:
        bytes_data = camera.getvalue()
        frame = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        face, bbox = detector.detect_face(frame)

        if face is not None:
            mood = predict_mood(face)

            mood_emojis = {
                'happy': '😊', 'sad': '😢', 'angry': '😠',
                'surprise': '😲', 'fear': '😨', 'neutral': '😐', 'disgust': '🤢'
            }
            emoji = mood_emojis.get(mood, '😐')
            st.success(f"Detected Mood: {emoji} **{mood.upper()}**")

            st.subheader("🎵 Suggested Playlists:")
            playlists = suggest_music(mood)

            if playlists:
                for playlist in playlists:
                    if playlist:
                        name = playlist.get('name', 'Unknown')
                        url = playlist.get('url', '#')
                        st.markdown(f"### 🎵 {name}")
                        st.markdown(f"[▶ Open in Spotify]({url})")
            else:
                st.info("No playlists found!")
        else:
            st.warning("No face detected! Please try again.")