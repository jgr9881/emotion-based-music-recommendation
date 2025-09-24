import tkinter as tk
from tkinter import messagebox, font

def get_user_data(use_terminal=True):
    """
    Collects user data either through terminal or GUI based on the parameter.
    
    Args:
        use_terminal (bool): If True, uses terminal input. If False, uses GUI.
        
    Returns:
        tuple: (name, location, age, favorite_color, ideal_movie, ideal_meal, current_mood)
    """
    if use_terminal:
        return get_terminal_data()
    else:
        return get_gui_data()

def get_terminal_data():
    """Gets user data through terminal prompts"""
    print("\n\nWelcome to the Emotion-Based Music Recommendation System!\n")
    print("==============================================\n\n")

    user_name = input("Hey, I'm EmoReco! What's your name?\n\n")
    print(f"\nCool! Nice to meet you, {user_name}!\n\n")

    user_location = input("\nWhere are you from?\n\n")

    print(f"\nAwesome, {user_name}! I love {user_location}!\n\n")

    user_age = input(f"\nNow... how old are you, {user_name}?\n\n")
    while True:
        try:
            user_age = int(user_age)
            if 0 < user_age < 120:
                break
            else:
                user_age = input(f"Please enter a valid age between 1 and 120, {user_name}.\n")
        except ValueError:
            user_age = input(f"Please enter a valid age (a number) between 1 and 120, {user_name}.\n")

    print("\n\n==============================================\n\n")
    print(f"Now let me ask you some more personal questions, {user_name}!\n\n")
    print("==============================================\n\n")

    favorite_color = input("\nWhat's your favorite color?\n\n")
    print(f"\n{favorite_color} is a beautiful color!\n\n")

    ideal_movie = input("\nWhat movie would you love to watch right now? (because of its particular ambiance, emotional impact, or just pick a movie you like)\n\n")
    print(f"\nGreat choice!")

    ideal_meal = input("\nWhat would be your ideal meal right now? (it could be a snack, a full meal, or just a type of cuisine)\n")
    print(f"\nYummy! {ideal_meal} sounds delicious!\n\n")

    print("==============================================\n\n")
    print("Now, let me ask you one last question before we proceed to the emotion detection!\n\n")
    current_mood = input("\nHow are you feeling right now? (you can describe your mood in a few words or phrases - tell me everything, I'll figure it out!)\n\n")

    print(f"\nThanks for sharing, {user_name}! I appreciate your honesty.\n\n")
    print("==============================================\n\n")
    print("Now, let's move on to the emotion detection part!\n\n")

    return user_name, user_location, user_age, favorite_color, ideal_movie, ideal_meal, current_mood

def get_gui_data():
    """Gets user data through a GUI interface"""
    user_data = {
        "name": "",
        "location": "",
        "age": 0,
        "favorite_color": "",
        "ideal_movie": "",
        "ideal_meal": "",
        "current_mood": ""
    }
    
    def finish_data_collection():
        root.quit()
    
    def validate_age():
        try:
            age = int(age_entry.get())
            if 0 < age < 120:
                user_data["age"] = age
                show_frame(personal_frame)
            else:
                messagebox.showerror("Invalid Age", "Please enter a valid age between 1 and 120.")
        except ValueError:
            messagebox.showerror("Invalid Age", "Please enter a valid age (a number) between 1 and 120.")
    
    def show_frame(frame):
        frame.tkraise()
    
    def save_name_location():
        user_data["name"] = name_entry.get()
        user_data["location"] = location_entry.get()
        if user_data["name"] and user_data["location"]:
            greeting_label.config(text=f"Cool! Nice to meet you, {user_data['name']}!\nNow, how old are you?")
            show_frame(age_frame)
        else:
            messagebox.showerror("Missing Information", "Please enter your name and location.")
    
    def save_preferences():
        user_data["favorite_color"] = color_entry.get()
        user_data["ideal_movie"] = movie_entry.get()
        user_data["ideal_meal"] = meal_entry.get()
        
        if user_data["favorite_color"] and user_data["ideal_movie"] and user_data["ideal_meal"]:
            mood_greeting.config(text=f"Thanks for sharing, {user_data['name']}!\nHow are you feeling right now?")
            show_frame(mood_frame)
        else:
            messagebox.showerror("Missing Information", "Please fill in all fields.")
    
    def save_mood_and_finish():
        user_data["current_mood"] = mood_entry.get()
        if user_data["current_mood"]:
            messagebox.showinfo("Complete", f"Thanks for sharing, {user_data['name']}! Now we'll move to emotion detection.")
            finish_data_collection()
        else:
            messagebox.showerror("Missing Information", "Please describe your current mood.")
    
    root = tk.Tk()
    root.title("Emotion-Based Music Recommendation")
    root.geometry("600x400")
    
    title_font = font.Font(family="Arial", size=14, weight="bold")
    normal_font = font.Font(family="Arial", size=12)
    
    container = tk.Frame(root)
    container.pack(fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    
    intro_frame = tk.Frame(container)
    age_frame = tk.Frame(container)
    personal_frame = tk.Frame(container)
    mood_frame = tk.Frame(container)
    
    for frame in (intro_frame, age_frame, personal_frame, mood_frame):
        frame.grid(row=0, column=0, sticky="nsew")
    
    # ===== Intro Frame =====
    tk.Label(intro_frame, text="Welcome to the Emotion-Based Music Recommendation System!", 
             font=title_font, pady=10).pack()
    
    tk.Label(intro_frame, text="What's your name?", font=normal_font, pady=10).pack()
    name_entry = tk.Entry(intro_frame, font=normal_font, width=30)
    name_entry.pack(pady=5)
    
    tk.Label(intro_frame, text="Where are you from?", font=normal_font, pady=10).pack()
    location_entry = tk.Entry(intro_frame, font=normal_font, width=30)
    location_entry.pack(pady=5)
    
    tk.Button(intro_frame, text="Next", font=normal_font, command=save_name_location).pack(pady=20)
    
    # ===== Age Frame =====
    greeting_label = tk.Label(age_frame, text="", font=normal_font, pady=10)
    greeting_label.pack()
    
    age_entry = tk.Entry(age_frame, font=normal_font, width=30)
    age_entry.pack(pady=5)
    
    tk.Button(age_frame, text="Next", font=normal_font, command=validate_age).pack(pady=20)
    
    # ===== Personal Preferences Frame =====
    tk.Label(personal_frame, text="Let me ask you some more personal questions!", 
             font=title_font, pady=10).pack()
    
    tk.Label(personal_frame, text="What's your favorite color?", font=normal_font, pady=5).pack()
    color_entry = tk.Entry(personal_frame, font=normal_font, width=30)
    color_entry.pack(pady=5)
    
    tk.Label(personal_frame, text="What movie would you love to watch right now?", font=normal_font, pady=5).pack()
    movie_entry = tk.Entry(personal_frame, font=normal_font, width=30)
    movie_entry.pack(pady=5)
    
    tk.Label(personal_frame, text="What would be your ideal meal right now?", font=normal_font, pady=5).pack()
    meal_entry = tk.Entry(personal_frame, font=normal_font, width=30)
    meal_entry.pack(pady=5)
    
    tk.Button(personal_frame, text="Next", font=normal_font, command=save_preferences).pack(pady=20)
    
    # ===== Mood Frame =====
    mood_greeting = tk.Label(mood_frame, text="", font=normal_font, pady=10)
    mood_greeting.pack()
    
    tk.Label(mood_frame, text="How are you feeling right now?\n(describe your mood in a few words or phrases)", 
             font=normal_font, pady=5).pack()
    
    mood_entry = tk.Entry(mood_frame, font=normal_font, width=40)
    mood_entry.pack(pady=5)
    
    tk.Button(mood_frame, text="Continue to Emotion Detection", font=normal_font, 
              command=save_mood_and_finish).pack(pady=20)
    
    show_frame(intro_frame)
    
    root.mainloop()
    
    return user_data["name"], user_data["location"], user_data["age"], user_data["favorite_color"], user_data["ideal_movie"], user_data["ideal_meal"], user_data["current_mood"]

if __name__ == "__main__":
    result = get_user_data(use_terminal=False)
    print(result)