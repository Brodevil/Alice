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
        self.askGender = "Actually As per Abhinav sir, He think that to being a male will the best option for me but as per your demand I can change my gender, Should I change my gender!"
        self.gender = "male"
        self.voiceSpeed = 175


        try:
            response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=thane&appid=c04f06f6ac189dc5401ecf14a257adc7")
            respons = json.load(response.text)
            pprint.pprint(response)
        except ConnectionError:
            return None
        

    def temperature(self):
        pass


    def speak(self, audio):
        engine = pyttsx3.init('sapi5')
        if self.gender == "male":
            engine.setProperty('voice', engine.getProperty('voices')[0].id)
        elif self.gender == "female":
            engine.setProperty('voice', engine.getProperty('voices')[1].id)
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



