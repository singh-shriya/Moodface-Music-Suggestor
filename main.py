import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import cv2
import numpy as np
import tensorflow as tf
from moodface.detector import FaceDetector
from moodface.music_suggester import suggest_music

# Load trained model
model = tf.keras.models.load_model('moodface/mood_model.h5')

# Mood labels
MOODS = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Initialize face detector
detector = FaceDetector()

def predict_mood(face):
    face = cv2.resize(face, (48, 48))
    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    face = face / 255.0
    face = face.reshape(1, 48, 48, 1)
    prediction = model.predict(face, verbose=0)
    mood = MOODS[np.argmax(prediction)]
    return mood

def main():
    cap = cv2.VideoCapture(0)
    print("Press 'q' to quit, 's' to detect mood and suggest music")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        face, bbox = detector.detect_face(frame)
        
        if face is not None:
            mood = predict_mood(face)
            cv2.putText(frame, f'Mood: {mood}', (50, 50),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow('MoodFace', frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s') and face is not None:
            mood = predict_mood(face)
            suggest_music(mood)
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()