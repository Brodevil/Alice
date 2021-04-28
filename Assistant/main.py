import pyttsx3
import datetime
import requests
import json
import pprint


engine = pyttsx3.init('sapi5')
engine.setProperty('voice', engine.getProperty('voices')[0].id)
engine. setProperty("rate", 150)

intoduction = "Now me to introduce myself, I m Alice. A virtual desktop assitant and I'm here to assit you with a veriety of tasks \
        as best as I can. 24 Hours a day seven days a week, Importing all preferences from home, interface system are now \
        fully operational, Sir!"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def intro():
    hour = int(datetime.datetime.now().hour)
    if hour == 0 and hour < 12:
        speak("Good Morning Sir!")
    
    elif hour == 12 and hour < 18:
        speak("Good Afternon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("Now me to introduce myself, I m Alice. A virtual desktop assistant and I'm here to assit you with a veriety of tasks \
        as best as I can. 24 Hours a day, seven days a week, Importing all preferences from home Interface, System are now \
        fully operational!")



def temperature():
    try:
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=thane&appid=c04f06f6ac189dc5401ecf14a257adc7")
        respons = json.load(response.text)
        pprint.pprint(response)
    except ConnectionError:
        return 



if __name__ == "__main__":
    # intro()
    temperature()

