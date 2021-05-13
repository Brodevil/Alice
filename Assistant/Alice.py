import requests
import json
import datetime
import pyttsx3
import pprint



class Alice:
    def __init__(self, username, location):
        super().__init__()
        self.name = username
        self.city = location.lower()
        self.intro = "Now me to introduce myself, I m Alice. A virtual desktop assistant and I'm here to assist you with a verity of tasks \
                    as best as I can. 24 Hours a day seven days a week, Importing all preferences from home, interface system are now \
                    fully operational, Sir!"
        self.workDo = "I guess there are several things I can do as i m acting as a package and for more info about my commands and works you can just checkout the README file of this project"
        
        self.voice = "richard"
        self.voiceSpeed = 175

        

    def speak(self, audio):
        engine = pyttsx3.init('sapi5')

        if self.voice.lower() == "david":
            engine.setProperty('voice', engine.getProperty('voices')[0].id)
        elif self.voice.lower() == "ravi":
            engine.setProperty('voice', engine.getProperty('voices')[1].id)
        elif self.voice.lower() == "richard":
            engine.setProperty('voice', engine.getProperty('voices')[2].id)
        elif self.voice.lower() == "zira":
            engine.setProperty('voice', engine.getProperty('voices')[3].id)

        engine.setProperty("rate", self.voiceSpeed)
        engine.say(audio)
        engine.runAndWait()
    

    def intro(self):
        hour = int(datetime.datetime.now().hour)
        if hour == 0 or hour < 12:
            speak(f"Good Morning {self.name} Sir!")

        elif hour == 12 or hour < 18:
            speak(f"Good Afternon {self.name} Sir!")

        else:
            speak(f"Good Evening {self.name} Sir!")

        speak("Now me to introduce myself, I m Alice. A virtual desktop assistant and I'm here to assist you with a verity of tasks \
            as best as I can. 24 Hours a day, seven days a week, Importing all preferences from home Interface, System are now \
            fully operational!")



