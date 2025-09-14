import speech_recognition as sr
import pyttsx3
import webbrowser
import music_library
import requests
import google.generativeai as genai

genai.configure(api_key="AIzaSyC-NcRKyp0YsU_IRqjqKZOHe-y_vF6BPjM")  # Replace with your actual API key

# Load the model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # Or gemini-1.5-pro

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("Gemini error:", e)
        return None


    
# ----------- text and All modules setup.... -----------
engine = pyttsx3.init()
newsapi="5dd660193a89410684ecc6deb1857b5e"
engine.setProperty('rate', 200)    
engine.setProperty('volume', 1.0)  

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# ----------- Command giving section..... -----------
def process(command):
    command = command.lower()

    if command == "open google":
        webbrowser.open("https://www.google.com")
    elif command == "open facebook":
        webbrowser.open("https://www.facebook.com")
    elif command == "open youtube":
        webbrowser.open("https://www.youtube.com")
    elif command == "open instagram":
        webbrowser.open("https://www.instagram.com/accounts/login/?hl=en")
    elif command == "open github":
        webbrowser.open("https://github.com/signup?source=login")
    elif command.startswith("play"):
            song = command.split(" ", 1)[1]
            speak(f"Playing {song}")
            webbrowser.open(music_library.music[song])  
    elif command.lower().startswith("news"):
        try:
            speak("Fetching the latest business news...")
            url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=5dd660193a89410684ecc6deb1857b5e"
            response = requests.get(url)
            data = response.json()

            if data["status"] == "ok":
                articles = data["articles"]
                top_articles = articles[:5]

                for i, article in enumerate(top_articles, start=1):
                    headline = article["title"]
                    speak(f"News {i}: {headline}")
            else:
                speak("Sorry, I couldn't fetch the news.")
        except Exception as e:
            speak("There was an error getting the news.")
            print(f"News error: {e}")
    elif command in ["exit", "stop", "quit", "bye"]:
        speak("Goodbye! Exiting active mode.")
        return "exit"

    else:
        speak("Let me think...")
        response = ask_gemini(command)
        if response:
            speak(response)
        else:
            speak("Sorry, I couldn't get a response from Gemini.")


# ----------- Main listening...... -----------
speak("Initializing Google Assistant...")

recognizer = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening for the keyword 'Google'...")
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")

            if "google" in command.lower():
                speak("Hello, how may I assist you?")
        while True:
            try:
                with sr.Microphone() as source:
                    print("GOOGLE IS ACTIVE ... Listening for command...")
                    audio = recognizer.listen(source, timeout=4, phrase_time_limit=3)
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")

                    # Process command and check for exit signal
                    result = process(command)
                    if result == "exit":   # If process returns "exit", break the loop
                        break

            except sr.WaitTimeoutError:
                print("Timeout: No speech detected. Listening again...")
            except sr.UnknownValueError:
                print("Didn't understand!!...Please repeat.")
            except Exception as e:
                print(f"Unexpected error: {e}")

    except sr.WaitTimeoutError:
        print("Timeout: No speech detected.")
    except sr.UnknownValueError:
        print("Didn't understand. Try again.")
    except Exception as e:
        print(f"Unexpected error: {e}")
