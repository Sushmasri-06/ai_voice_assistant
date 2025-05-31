# 🧠 AI Voice Assistant (Python)

A beginner-friendly voice assistant built using Python. It can answer questions, tell jokes, report the weather, open websites, and more — all with your voice.

---

## 🎯 Features

- 🔊 **Speech Recognition** (understands your voice)
- 🗣️ **Text-to-Speech** using `pyttsx3`
- 🌐 **Opens websites** like YouTube and Google
- 🕒 **Tells current time**
- 🌤️ **Reports weather** for a chosen city
- 😂 **Tells random jokes**
- ➗ **Performs basic calculations**
- ❌ **Listens for “exit” to quit**

---

## 🛠️ Tech Stack

- Python 3
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [PyAudio](https://pypi.org/project/PyAudio/)
- [Requests](https://pypi.org/project/requests/)
- OpenWeatherMap API

---

## 📁 Project Structure

ai_voice_assistant/
├── main.py
├── requirements.txt
├── README.md
└── utils/
└── functions.py
## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/Sushmasri-06/ai_voice_assistant.git
cd ai_voice_assistant

### 2. Create a Virtual Environment

python3 -m venv venv
source venv/bin/activate  # for Mac/Linux

### 3. Install Requirements

pip install -r requirements.txt

### 4. Add Your OpenWeatherMap API Key

Open functions.py and replace:
api_key = "YOUR_API_KEY_HERE"
with your actual key from https://openweathermap.org/

🧪 Run the Assistant

python3 main.py
Say “Hey Assistant” to activate it, then try commands like:

“What’s the time?”

“Open YouTube”

“Tell me a joke”

“What’s the weather?”

“Exit”


📌 Notes:

Ensure your microphone works and is not muted

Tested on macOS with Python 3.9+

You can expand it with more features like Wikipedia search, reminder setting, or even Spotify control!

say “Hey Assistant” before every command. That’s because the assistant is listening for the wake word "hey assistant" to know when you're actually giving a command.

So yes — even to exit, you need to say:

“Hey Assistant”
“Exit”

Why it's built this way-
  *It helps avoid reacting to random background noise or unintended speech.

  *It mimics how real assistants like Alexa or Siri work: they wait for a wake word before processing.



👩‍💻 Author
Sushma Sri
🔗 GitHub
