import speech_recognition as sr
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("How can I help you?")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {command}")
        except Exception as e:
            print("Sorry, could not understand.")
            speak("Sorry, I didn't catch that.")
            return "None"
        
        return command.lower()

# Test run
if __name__ == "__main__":
    while True:
        query = listen()
        if 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break
        elif 'hello' in query:
            speak("Hello! I am your assistant.")
        elif 'your name' in query:
            speak("My name is Echo, your voice assistant.")
        else:
            speak("I heard you say " + query)
