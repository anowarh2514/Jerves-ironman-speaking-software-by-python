import pyttsx3
import speech_recognition as sr
import datetime
# import pyaudio
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[-1].id)
engine.setProperty('voice',voices[0].id)
# engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\SPEECH\Voices\Tokens\MSTTS_V110_enUS_MarkM')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")
    else:
        speak("Good Evening !")

    speak("Hello Sir,"
          " I am Fryda ."
          "Welcome to your lab."
          " Sir."
          "Please tell me, "
          "how may I help you. "
          "what should I do?")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, Language='en-in')
        print("User said:",query)
        # print(f"User said:{query}")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email address','your password')
    server.sendmail('your email address',to,content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir ='D:\\MP3'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            # speak("Sir,the time is",strTime)
            speak(f"Sir,the time is {strTime}")
            print(strTime)
        elif 'open code' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1\\bin\\pycharm64.exe"
            os.startfile(codePath)
        elif 'Send Email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to ="email address where you send email"
                sendEmail(to,content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("Sorry Brother I can't able to send the email")