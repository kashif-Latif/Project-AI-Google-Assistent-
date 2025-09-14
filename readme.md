🎙️ Voice-Controlled AI Assistant

This project is a voice-activated desktop assistant built with Python. It can understand your voice commands and perform a variety of tasks like opening websites, fetching news, playing music, and even answering general questions using Google's Gemini AI.

✨ Features

🎧 Voice Activation using the keyword "Google"

🌐 Web Browsing — Opens popular websites like Google, YouTube, Facebook, etc.

🎵 Play Music — Plays a song from a predefined library

🗞️ Get News — Fetches the latest Business news using the NewsAPI

🧠 AI-Powered Chat — Uses Gemini (Google Generative AI) for answering complex queries

🗣️ Text-to-Speech responses using pyttsx3

🧠 How It Works
🔊 Voice Activation

The assistant listens for the keyword "Google". Once heard, it activates and begins listening for further commands.

if "google" in command.lower():
    speak("Hello, how may I assist you?")

🧾 Command Processing

The assistant can:

Open websites like Google, Facebook, YouTube, Instagram, GitHub

Play songs from a music_library dictionary

Fetch and read the latest business news headlines

Answer any other query using Gemini AI

elif command.startswith("play"):
    # Plays a song from the music library
elif command.lower().startswith("news"):
    # Fetches latest business news
else:
    # Sends query to Gemini and speaks the response

🤖 Google Gemini AI Integration

You can ask the assistant any general question, and it will use Gemini’s generate_content() method to get the response.

response = model.generate_content(prompt)


💡 Note: Replace the placeholder API key with your own Gemini API key
.

🔁 Continuous Listening

Once activated, the assistant keeps listening for commands until you say:

"exit", "stop", "quit", or "bye"

🧩 Dependencies

Install the required Python packages:

pip install speechrecognition pyttsx3 requests google-generativeai


Make sure you also install pyaudio correctly (may require additional setup depending on your OS).

🔐 API Keys
Integerated with the Gemini API key 

📁 Project Structure
.
├── main.py
├── music_library.py   # Contains a dictionary of song names and URLs
└── README.md

🚀 Usage

Clone the repository

Add your API keys

Run the script:

python main.py


Say "Google" to activate, and you're ready to go!

📄 License

This project is open-source under the MIT License.