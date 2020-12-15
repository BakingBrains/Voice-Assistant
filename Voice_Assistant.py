import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            speak = listener.recognize_google(voice)
            speak = speak.lower()
            if 'alexa' in speak:
                speak = speak.replace('alexa', '')
                print(speak)

    except:
        pass
    return speak


def runAlexa():
    speak = takeCommand()
    print(speak)
    if 'play' in speak:
        song = speak.replace('play', '')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in speak:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'who is' in speak:
        person = speak.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in speak:
        talk('I am Busy')
    elif 'joke' in speak:
        talk(pyjokes.get_joke())
    else:
        talk('Please say it again')


while True:
    runAlexa()