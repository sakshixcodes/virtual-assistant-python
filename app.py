import streamlit as st
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

st.set_page_config(page_title="Echo - Virtual Assistant", layout="centered")
st.title("🤖 Echo Assistant")
st.markdown("**Type or click '🎙 Speak' to give a command.**")

# Command processor
def process_command(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://www.google.com")
        return "✅ Opened Google"
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "✅ Opened YouTube"
    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"🕒 Current time is {now}"
    elif "joke" in command:
        return pyjokes.get_joke()
    elif "search" in command:
        query = command.replace("search", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            return f"🔎 Searched for: {query}"
        else:
            return "❌ What should I search?"
    else:
        return "🤷 Sorry, I didn’t understand that."

# Voice recognizer
def listen_to_microphone():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("🎤 Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio, language="en-IN")
            return command
        except sr.WaitTimeoutError:
            return "❌ No voice detected."
        except sr.UnknownValueError:
            return "❌ Could not understand voice."
        except sr.RequestError:
            return "❌ Voice service unavailable."

# Text input
text_command = st.text_input("⌨️ Type your command")

# Voice input
if st.button("🎙 Speak"):
    voice_command = listen_to_microphone()
    st.write(f"🗣 You said: **{voice_command}**")
    if "❌" not in voice_command:
        st.success(process_command(voice_command))
    else:
        st.error(voice_command)

# Process typed command
if text_command:
    st.success(process_command(text_command))
