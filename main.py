

from utils.functions import speak, listen, get_time, open_website, tell_joke, get_weather, calculate

def main():
    speak("Hello! I am your voice assistant. Say 'Hey Assistant' to wake me up.")
    
    while True:
        print("Waiting for wake word...")
        command = listen().lower()
        if "hey assistant" in command:
            speak("I am listening.")
            command = listen().lower()

            if "time" in command:
                current_time = get_time()
                speak(f"The current time is {current_time}")

            elif "open google" in command:
                open_website("google")

            elif "open youtube" in command:
                open_website("youtube")

            elif "open github" in command:
                open_website("github")

            elif "joke" in command:
                tell_joke()

            elif "weather" in command:
                # You can ask for city by voice, but for now use default
                get_weather()

            elif "calculate" in command:
                # Remove the word 'calculate' from command and pass the rest
                expr = command.replace("calculate", "").strip()
                calculate(expr)

            elif "exit" in command or "quit" in command:
                speak("Goodbye!")
                break

            else:
                speak("Sorry, I didn't understand that command.")
        else:
            continue  # Ignore if wake word not detected

if __name__ == "__main__":
    main()
