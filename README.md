# Emotion-Based Music Recommendation

A Python application that recommends music genres and styles based on your detected facial emotion, personal preferences, and current mood.

## Overview

This project combines computer vision, deep learning, and natural language processing to create personalized music recommendations. It:

1. Collects personal information through an interactive interface
2. Captures your facial expression through your webcam
3. Analyzes your emotion using a pre-trained CNN model
4. Processes all data using an LLM
5. Generates a subset of recommended labels with confidence scores (all possible labels can be defined in labels.json)

## How It Works

### 1. User Data Collection
The system collects information about you through a series of questions, either through a terminal interface or a graphical user interface (GUI). This includes:
- Basic demographics (name, location, age)
- Personal preferences (favorite color, ideal movie, ideal meal)
- Current mood (in your own words)

### 2. Emotion Detection
- Activates your webcam to capture video
- Uses OpenCV's Haar Cascade classifier to detect faces
- Processes the detected face through a pre-trained CNN model
- Identifies your emotion from 7 categories: Angry, Disgust, Fear, Happy, Sad, Surprise, or Neutral

### 3. Music Genre Recommendation
- Combines all collected data (user information + detected emotion)
- Sends this data to OpenAI's language model through LangChain
- Analyzes which music genres would best match your current emotional state and preferences
- Outputs a JSON file with recommended genres and their confidence scores

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jgr9881/emotion-based-music-recommendation.git
   cd emotion-based-music-recommendation
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up OpenAI API key**
   - Create a .env file in the project root with:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```
   - You can get an API key from the [OpenAI platform](https://platform.openai.com/account/api-keys)

## Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Choose input method**
   - Open main.py and set `use_terminal = False` for GUI input, or `use_terminal = True` for terminal input

3. **Answer the questions** about yourself and your preferences

4. **Allow webcam access** for emotion detection
   - Position your face in frame
   - Express the emotion you're feeling
   - Press 'q' to capture and process the emotion

5. **Check your recommendations**
   - Once the process completes, the recommendations are saved in output_labels.json
   - The file contains music genres with confidence scores (higher scores = stronger recommendations)

## File Structure

- main.py - Main application script
- modules
  - `emotion_detection_function.py` - Facial emotion detection using CNN
  - `get_user_data.py` - Collects user information (terminal/GUI)
  - `get_labels.py` - Processes data and gets recommendations from OpenAI
- data
  - `emotion_model.h5` - Pre-trained emotion recognition model
  - `labels.json` - Available music genres and styles
  - `output_labels.json` - Generated recommendations

## Tools used

- **OpenCV** - Computer vision for face detection
- **TensorFlow/Keras** - Deep learning framework for emotion recognition
- **Tkinter** - GUI for input collection
- **LangChain** - Framework for LLM application development
- **OpenAI API** - Natural language processing for recommendation generation
- **Python-dotenv** - Environment variable management

## Sample Output

With a simple set of labels (common genres, subgenres and bpm groups), the result could be the following if the user seems calm and a bit under the weather :

```json
{
    "sad songs": 0.95,
    "blues": 0.92,
    "lo-fi": 0.91,
    "slow-tempo (60-90 BPM)": 0.89,
    "acoustic": 0.87,
    "ambient": 0.86
}
```

## Customization

- **Add new genres**: Edit labels.json to include additional music genres
- **Adjust confidence threshold**: Modify the threshold in `get_labels.py` (default is 0.85)
- **Change prompt**: Edit the template in `get_labels.py` to change how recommendations are generated

## Limitations and Future Improvements

- Emotion detection works best in good lighting conditions
- Currently only uses a single frame for emotion detection
- Future versions could:
  - Include Spotify API integration for actual song recommendations
  - Implement continuous emotion tracking over time
  - Add multi-face support for group recommendations

## Requirements

- Python 3.7+
- Webcam
- OpenAI API key
- Dependencies listed in requirements.txt
