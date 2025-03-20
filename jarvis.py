import pyttsx3  
import speech_recognition as sr
import datetime
import os
import sys
import cv2
import requests

# Initialize the pyttsx3 engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[-1].id)
engine.runAndWait()
    
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio = r.listen(source,timeout=10,phrase_time_limit=7)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-In')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say again please...")
        print(e)
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning sir!!")
    elif hour>=12 and hour<=18:
        speak("good afternoon sir!!")
    else:
        speak("good evening sir!!")
    speak("I am jarvis, please tell me sir how can I help you!!")
    
if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()
        if "open notepad" in query:
            speak("Okay sir I try to opening notepad")
            notepadpath = "c:\\Windows\\notepad"
            os.startfile(notepadpath)
           
        elif "open chrome" in query:
            speak("Okay sir I try to opening chrome")
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)
       
        elif "quite jarvis" in query or "sleep" in query or "bye" in query:
            speak("Good bye sir take care!!")
            sys.exit(0)

        elif "open camera" in query:
            speak("Okay sir I try to opening camera")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitkey(50)
                if k==27:
                  break;
                cap.release()
                cv2.distroyAllWindows()

        elif "IP Address" in query:
            speak("Okay sir I try to finding IP Address")
            ip = requests("https://api.ipify.org").text
            speak(f"Your IP Address is {ip}")
