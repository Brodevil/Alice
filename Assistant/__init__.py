import pyttsx3
import datetime
import requests
import json
import pprint
import speech_recognition as sr 
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')


introduction = "Now me to introduce myself, I m Alice. A virtual desktop assistant and I'm here to assist you with a verity of tasks \
        as best as I can. 24 Hours a day seven days a week, Importing all preferences from home, interface system are now \
        fully operational, Sir!"


def speakDavid(audio):
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    print(engine.getProperty('voices'))
    engine.setProperty("rate", 175)
    engine.say(audio)
    engine.runAndWait()


def speakRavi(audio):
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.setProperty("rate", 170)
    engine.say(audio)
    engine.runAndWait()


def speakZira(audio):
    engine.setProperty('voice', engine.getProperty('voices')[3].id)
    engine.setProperty("rate", 170)
    engine.say(audio)
    engine.runAndWait()
    

def speakRichard(audio):
    engine.setProperty('voice', engine.getProperty('voices')[2].id)
    engine.setProperty("rate", 170)
    engine.say(audio)
    engine.runAndWait()


def intro():
    hour = int(datetime.datetime.now().hour)
    if hour == 0 or hour < 12:
        speakRichard("Good Morning Sir!")

    elif hour == 12 or hour < 18:
        speakRichard("Good Afternon Sir!")

    else:
        speakRichard("Good Evening Sir!")

    speakRichard("Now me to introduce myself, I m Alice. A virtual desktop assistant and I'm here to assist you with a verity of tasks \
        as best as I can. 24 Hours a day, seven days a week, Importing all preferences from home Interface, System are now \
        fully operational!")


def temperature():
    try:
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=thane&appid=c04f06f6ac189dc5401ecf14a257adc7")
        response = json.load(response.text)
        pprint.pprint(response)
    except ConnectionError:
        return


def takeCommand():
    '''
    The not having any parameter but it taking the input form the microphone of the user 
    and return the string object that the user says
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Alice : Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)
    
    try:
        print("Alice : Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User : \t{query}\n")
    
    except Exception as e:
        print("Alice : Sorry! I didn't get\n")
        return "None"

    return query

    
if __name__ == "__main__":
    # intro()
    # temperature()
    while True:
        queary = takeCommand().lower()
        # LOgic for executin task based on query


        if 'wikipedia' in queary:
            print("Alice : Searching Wikipedia...")
            speakRavi("Searching Wikipedia...")
            queary = queary.replace("wikipedia", "")
            try:
                results = wikipedia.summary(queary, sentences=2)
                print(f"Alice : According to wikipedia. {results}\n")
                speakRavi(f"According to wikipedia. {results}")
            except Exception:
                speakRichard("Sorry! I didn't got that stuff in wikipedia")
        
        elif 'quit' in queary:
            print("Alice : That's it, I am quiting")
            speakRavi("That's it, I am quiting")
            exit()

        elif 'open youtube' in queary:
            webbrowser.open("youtube.com", new=2)

        elif 'open google' in queary:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in queary:
            webbrowser.open("stackoverflow.com")
        
        elif 'open github' in queary:
            webbrowser.get('C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe').open("github.com/Brodevil")
        
        elif 'open github this repository' in queary:
            webbrowser.open("github.com/Brodevil/Alice")
        
        elif 'is i am audio able' in queary:
            print("Alice : Yes sir you are Audio able!\n")
            speakRichard("Yes sir you are Audio able!")
        
        elif 'hello alice' in queary:
            print("Alice : Hello sir! how may I can help you.\n")
            speakRichard("Hello sir! how may I can help you.")