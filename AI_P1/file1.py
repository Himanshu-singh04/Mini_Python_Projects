from email.mime import audio
from logging import exception
import re
from unittest import result
import pyttsx3
import datetime
from sklearn.utils import resample
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        speak("Good Morning Sir")
    elif (hour>=12 and hour<18):
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    
    speak("I am the computer talking to you, how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        print("Recognitizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    except exception as e:
        speak("Say that again please")
        return "None"
    return query

        # print(e)



if __name__ == "__main__":
    wishMe()
    n = True
    while n == True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            query = query.replace("youtube","")
            webbrowser.open(f"https://www.youtube.com/{query}")
        
        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(str_time)
            speak(f"the time now is {str_time}")

        elif 'vs code' in query:
            code_Path = "C:\\Users\\Himanshu Singh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_Path)

        elif 'whatsapp' in query:
            whatsapp = "C:\\Users\\Himanshu Singh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp\\WhatsApp"
            os.startfile(whatsapp)

        elif 'random number' in query:
            num = random.randint(0,10)
            print (num)

        elif 'spotify' in query:
            spotify = "C:\\Users\\Himanshu Singh\\OneDrive\\Desktop\\Spotify.lnk"
            os.startfile(spotify)
        elif 'quit' in query:
            speak("thank you sir")
            break
            n == False
