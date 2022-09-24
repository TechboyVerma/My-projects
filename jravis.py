import os
import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
from requests import get
import wikipedia
import pywhatkit as kit
import sys
import selenium as sl


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[1].id)

#text to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

#TO recognize voice into text
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        

    except Exception as e:
        speak("speak again dad...")
        return "none"
    return query





#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning verma")
    elif hour>12 and hour<18:
        speak("good afternoon verma")
    else:
        speak("good evening verma")
    speak("i am your son sir. please tell me what i do")


if __name__ == '__main__':
    wish()
    while True:

        query = takecommand().lower()

        #logic building for tasks
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query , sentences=2)
            speak("According t wikipedia")
            print(results)
            speak(results)
#to open yotube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
#to open google
        elif 'open google' in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif 'play gaana' in query:
            music_dir = 'D:\\non critical\\songs\\Favorite songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = '"C:\\Users\\QAZI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codePath)

        elif"ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"tera address yo s kaka {ip}")

        elif "play music on youtube" in query:
            webbrowser.open("youtube.com")

        elif "open whatsapp" in query:
            whatsappPath = '"C:\\Users\\QAZI\\AppData\\Local\\WhatsApp\\WhatsApp.exe"'
            os.startfile(whatsappPath)

        elif "open SPOTIFY" in query:
            speak("which song i play for you dad")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "play song on youtube" in  query:
            speak("which song i play for you verma")
            cm = takecommand().lower()
            kit.playonyt(f"{cm}")

        elif "i love you"in query:
            speak(" i love you too sir")
            speak("what happend sir")
            cm = takecommand().lower()
            speak("i can play song for you because i think you are sad today ")
            cm = takecommand().lower()
            speak("which song i play for you")
            cm = takecommand().lower()
            kit.playonyt(f"{cm}")

        elif "addition" in query:
            speak("tell me the values")
            cm = takecommand().lower()
            speak("okh sir")
            cm = takecommand().lower()
            sum("a+b")
            print(sum)
            speak("sum")
            
            
        elif"bye bye" in query:
            speak("thanks for using me ,Have nice day verma")
            sys.exit()
