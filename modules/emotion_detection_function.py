import cv2
import numpy as np
import os
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D

# possible emotions
EMOTIONS = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]

def create_emotion_model():
    model = Sequential()
    
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1), name='conv2d_1'))
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', name='conv2d_2'))
    model.add(MaxPooling2D(pool_size=(2, 2), name='max_pooling2d_1'))
    model.add(Dropout(0.25, name='dropout_1'))
    
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu', name='conv2d_3'))
    model.add(MaxPooling2D(pool_size=(2, 2), name='max_pooling2d_2'))
    model.add(Conv2D(128, kernel_size=(3, 3), activation='relu', name='conv2d_4'))
    model.add(MaxPooling2D(pool_size=(2, 2), name='max_pooling2d_3'))
    model.add(Dropout(0.25, name='dropout_2'))
    
    model.add(Flatten(name='flatten_1'))
    model.add(Dense(1024, activation='relu', name='dense_1'))
    model.add(Dropout(0.5, name='dropout_3'))
    model.add(Dense(7, activation='softmax', name='dense_2'))  # 7 emotions

    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../data/emotion_model.h5')
    model.load_weights(model_path)
    
    return model

def detect_emotion():
    """
    Captures video from webcam, detects faces and emotions.
    Returns the last detected emotion when 'q' is pressed.
    
    Returns:
        str: The last detected emotion or None if no emotion was detected
    """
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    try:
        emotion_model = create_emotion_model()
        emotion_detection = True
        print("Emotion model created and weights loaded successfully!")
    except Exception as e:
        print(f"Error creating model: {e}")
        emotion_detection = False
    
    cap = cv2.VideoCapture(0)
    
    last_emotion = None
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
                if emotion_detection:
                    try:
                        face_roi = gray[y:y+h, x:x+w]
                        
                        face_roi = cv2.resize(face_roi, (48, 48))
                        face_roi = face_roi.astype("float") / 255.0
                        face_roi = np.expand_dims(face_roi, axis=0)
                        face_roi = np.expand_dims(face_roi, axis=-1)
                        
                        preds = emotion_model.predict(face_roi)[0]
                        emotion_idx = np.argmax(preds)
                        emotion = EMOTIONS[emotion_idx]
                        
                        # update the last detected emotion
                        last_emotion = emotion
                    except Exception as e:
                        print(f"Error predicting emotion: {e}")
                        emotion = "Error"
                else:
                    emotion = "Face Detected"
                
                cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
            cv2.imshow('Emotion Detection', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    finally:
        # Clean up resources
        cap.release()
        cv2.destroyAllWindows()
    
    return last_emotion