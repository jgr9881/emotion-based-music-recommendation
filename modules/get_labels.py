from modules import emotion_detection_function, get_user_data
import json
import os
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def get_labels(user_data, detected_emotion, labels):
    """
    Process labels using LangChain and OpenAI to generate confidence scores
    """
    template = """
    You are an AI assistant that associates music-related labels to users, based on user emotions and preferences.
    
    User Information:
    - Name: {name}
    - Location: {location}
    - Age: {age}
    - Favorite Color: {favorite_color}
    - Movie They Want to Watch Right Now: {ideal_movie}
    - Ideal Meal Right Now: {ideal_meal}
    - Current Mood (in their words): {current_mood}
    - Detected Emotion: {detected_emotion}
    
    Available Music Labels/Genres:
    {labels}
    
    Based on this information, assign a confidence score between 0 and 1 for each label/genre 
    that would be appropriate for this person's current emotional state and preferences.
    Only include labels with a confidence score of 0.85 or higher. Include exactly 1 BPM group label.
    
    Your response should be a valid JSON object with labels as keys and confidence scores as values:
    {{
        "label1": 0.95,
        "label2": 0.82,
        ...
    }}
    """
    
    prompt = PromptTemplate(
        input_variables=["name", "location", "age", "favorite_color", "ideal_movie", 
                         "ideal_meal", "current_mood", "detected_emotion", "labels"],
        template=template,
    )
    
    llm = OpenAI(temperature=0.7)
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    response = chain.run(
        name=user_data["name"],
        location=user_data["location"],
        age=user_data["age"],
        favorite_color=user_data["favorite_color"],
        ideal_movie=user_data["ideal_movie"],
        ideal_meal=user_data["ideal_meal"],
        current_mood=user_data["current_mood"],
        detected_emotion=detected_emotion,
        labels=", ".join(labels)
    )
    
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        print("Error: API response is not valid JSON. Using fallback method.")
        import re
        json_match = re.search(r'({[\s\S]*})', response)
        if json_match:
            try:
                return json.loads(json_match.group(1))
            except:
                pass
        
        # if all else fails, return a default response
        return {"default": 0.7}