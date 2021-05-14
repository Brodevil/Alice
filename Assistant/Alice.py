import requests
import json
import datetime
import pyttsx3
from os import environ
import pprint
from dotenv import load_dotenv
from exts.networks import location
from constants import Client


load_dotenv()


class Alice:
    """ 
    Alice Assitant:

    This class contain the Function of the Alice program and also with the Assitant Data
    """

    def __init__(self):
        super().__init__()
        self.name = environ.get("UserName", "Abhinav")
        if gender == "male" or gender == "boy":
            self.gender = "Sir"
        elif gender == "female" or gender == "girl":
            self.gender == "Mam"
        self.city = environ.get("location", location())
        
        self.voice = Client.voices
        self.voiceSpeed = Client.voiceRate
        
    
    def severalVoices(self, voicesId):
        """ This is the function to show the user how many voices are available in his/her system 
        So that the user will able to choose his own liked voice"""

        engine = pyttsx3.init("sapi5")
        for voice in voicesId:
            engine.setProperty("voice", voice)
            engine.say(f"Hey there! My voice name is {voice.split('Tokens\\')[1].replace('_', ' ')}")
            engine.runAndWait()


    def speak(self, audio):
        """ Speak function as per the selected voice """
        
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
            speak(f"Good Morning {self.name} {self.gender}")

        elif hour == 12 or hour < 18:
            speak(f"Good Afternon {self.name} {self.gender}")

        else:
            speak(f"Good Evening {self.name} {self.gender}")

        speak(Client.intro)




