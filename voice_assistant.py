"""
Simple Voice Assistant
Requires: pip install SpeechRecognition pyttsx3
Run: python voice_assistant.py
"""
import speech_recognition as sr, pyttsx3, webbrowser, datetime

engine=pyttsx3.init()
def say(t): engine.say(t); engine.runAndWait()

r=sr.Recognizer()
with sr.Microphone() as source:
    say("Listening...")
    audio=r.listen(source)
try:
    cmd=r.recognize_google(audio).lower()
    if "time" in cmd:
        say("The time is "+datetime.datetime.now().strftime("%H:%M"))
    elif "google" in cmd:
        webbrowser.open("https://google.com"); say("Opening Google")
    else:
        say("I heard "+cmd)
except Exception as e:
    say("Sorry, I couldn't understand")
