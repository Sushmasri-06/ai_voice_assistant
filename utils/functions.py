import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import requests
import random

# Initialize the speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to the user's voice and return it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was a problem with the speech recognition service.")
        return ""

def get_time():
    """Return the current time as a string."""
    return datetime.datetime.now().strftime("%I:%M %p")

def open_website(site):
    """Open a known website."""
    urls = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://www.github.com"
    }
    if site in urls:
        webbrowser.open(urls[site])
        speak(f"Opening {site}")
    else:
        speak("Sorry, I don't know that website.")


def tell_joke():
    """Tell a random joke."""
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I told my computer I needed a break, and it said 'No problem, I'll go to sleep.'",
        "Why did the math book look sad? Because it had too many problems."
    ]
    joke = random.choice(jokes)
    speak(joke)

def get_weather(city="Hyderabad"):
    api_key = "be7c338baf577da5107002d0b4686fda"  # Replace with your real API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        # Print the full JSON response for debugging
        print("Full API response:", data)

        if data.get("cod") != 200:
            speak(f"Sorry, I couldn't find the weather for {city}. Reason: {data.get('message', 'No message')}")
            return

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        speak(f"The weather in {city} is {description} with a temperature of {temp} degrees Celsius.")
    except Exception as e:
        speak("Sorry, I couldn't retrieve the weather information.")
        print("Error:", e)


def calculate(expression):
    """Calculate a simple math expression (like '2 plus 2')."""
    try:
        # Replace words with symbols
        expression = expression.lower()
        expression = expression.replace("plus", "+").replace("minus", "-")
        expression = expression.replace("times", "*").replace("multiplied by", "*")
        expression = expression.replace("divided by", "/").replace("over", "/")
        result = eval(expression)
        speak(f"The result is {result}")
    except Exception:
        speak("Sorry, I couldn't calculate that.")
