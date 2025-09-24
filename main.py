from modules import emotion_detection_function, get_user_data, get_labels
import os
import json

def main():

    use_terminal = True

    user_name, user_location, user_age, favorite_color, ideal_movie, ideal_meal, current_mood = get_user_data.get_user_data(use_terminal)

    detected_emotion = emotion_detection_function.detect_emotion()
    user_data = {
        "name": user_name,
        "location": user_location,
        "age": user_age,
        "favorite_color": favorite_color,
        "ideal_movie": ideal_movie,
        "ideal_meal": ideal_meal,
        "current_mood": current_mood
    }
    
    with open(os.path.join("data", "labels.json"), "r") as f:
        labels = json.load(f)
    
    confidence_scores = get_labels.get_labels(user_data, detected_emotion, labels)
    
    with open(os.path.join("data", "output_labels.json"), "w") as f:
        json.dump(confidence_scores, f, indent=4)
    
    print(f"\nRecommendation complete! Check 'data/output_labels.json' for the personalized music labels.")

if __name__ == "__main__":
    main()