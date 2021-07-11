import time

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from pygame import mixer

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and  hour<12:
        speak("goodmorning!")

    elif hour>=12 and hour<18:
        speak("goodafternoon!")

    elif hour>=18 and hour<20:
        speak("goodevening!")
    else:
        speak("goodnight!")
    speak("I am Suvan's robo Speed 1 teraherz")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print("user said:",query)
    except Exception as e:
        print(e)
        print("can you please say it again")
        return "none"
    return query
def sendemail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com","yourpassword")
    server.sendmail("youremail@gmail.com",to,content)
    server.close()


if __name__ == '__main__':
     wishme()
     while(True):
         query=takecommand().lower()
         if "wikipedia"in query:
             speak("searching")
             query=query.replace("wikipedia","")
             results=wikipedia.summary(query,sentences=2)
             speak("according to wikipedia")
             speak(results)


         elif "youtube" in query:
             webbrowser.open("youtube.com")
         elif "google" in query:
            webbrowser.open("google.com")
         elif "share this" in query:
             webbrowser.open("www.github.com")

         elif "music" in query:
             speak("which music should i play sir")
             music=takecommand()
             songsdir=["D:\\myplaylist\\religious.mp3","D:\\myplaylist\\romantic.mp3"]
             if "religious" in music:
                 mixer.init()
                 mixer.music.load(songsdir[0])
                 mixer.music.play()
                 time.sleep(1)
             elif "romantic" in music:
                 mixer.init()
                 mixer.music.load(songsdir[1])
                 mixer.music.play()
                 time.sleep(1)
         elif "stop" in query:
                mixer.music.stop()






         elif "time" in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")
         elif "email" in query:
             try:
               speak("what should i say")
               content=takecommand()
               to="towhomyouwanttosend@gmail.com"
               sendemail(to,content)
               speak("the email has been sent")
             except Exception as e:
                 print(e)
                 speak("the email could not be sent")









