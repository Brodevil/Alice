import pyttsx3
import datetime
import requests
import json
import pprint
import speech_recognition as sr 


introduction = "Now me to introduce myself, I m Alice. A virtual desktop assistant and I'm here to assist you with a verity of tasks \
        as best as I can. 24 Hours a day seven days a week, Importing all preferences from home, interface system are now \
        fully operational, Sir!"


def speak(audio):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    engine.setProperty("rate", 175)
    engine.say(audio)
    engine.runAndWait()


def tell(audio):
    engine = pyttsx3.init('sapi5')
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.setProperty("rate", 180)
    engine.say(audio)
    engine.runAndWait()


def intro():
    hour = int(datetime.datetime.now().hour)
    if hour == 0 or hour < 12:
        tell("Good Morning Sir!")

    elif hour == 12 or hour < 18:
        tell("Good Afternon Sir!")

    else:
        tell("Good Evening Sir!")

    speak("Now me to introduce myself, I m Alice. A virtual desktop assistant and I'm here to assist you with a verity of tasks \
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
    with sr.Microphone as source:
        print("Alice is Listening....")
        r.pause_threshold = 1
        # r.energy_threshold = 300
        audio = r.listen(source)
    
    try:
        print("Alice is Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User : {query:>20}")
    
    except Exception as e:
        print("Sorry! I didn't get")
        return "None"


if __name__ == "__main__":
    intro()
    # temperature()
    takeCommand()
