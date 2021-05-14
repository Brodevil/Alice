import requests
import json
import datetime
import pyttsx3
from os import environ
import pprint
from dotenv import load_dotenv
from exts.networks import localInfo
from constants import Contacts, ERROR_REPLIES, NEGATIVE_REPLIES, POSITIVE_REPLIES, Client


load_dotenv()


class Alice:
    """ 
    Alice Assitant:

    This class contain the Function of the Alice program and also with the Assitant Data
    """

    def __init__(self):
        super().__init__()
        self.name = environ.get("UserName", "Abhinav")

        gender = environ.get("GENDER", 'male')
        if gender == "male" or gender == "boy":
            self.gender = "Sir"
        elif gender == "female" or gender == "girl":
            self.gender == "Mam"

        
        self.city = environ.get("location", localInfo())
        
        self.voice = pass
        self.voiceSpeed = Client.voiceRate
        
    @staticmethod
    def severalVoices(voicesId):
        """ This is the function to show the user how many voices are available in his/her system 
        So that the user will able to choose his own liked voice """

        engine = pyttsx3.init("sapi5")
        for index, voice in enumerate(voicesId):
            engine.setProperty("voice", voice)
            engine.setProperty("rate", 170)
            if index == 0:
                engine.say(f"Hey there! My voice name is {voice.split('Tokens')[1].replace('_', ' ')}")
                engine.say(f"Hey there! I am {index+1}st voice of your system ")
            elif index == 1:
                engine.say(f"Hey there! I am {index+1}nd voice of your system ")
            elif index == 2:
                engine.say(f"Hey there! I m {index+1}rd voice of your system ")
            else:
                engine.say(f"Hey there! I am {index+1}th voice of your system ")

            engine.runAndWait()


    def speak(self, audio):
        """ Speak function as per the selected voice """
        
        engine = pyttsx3.init('sapi5')
        try:


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




if __name__ == "__main__":
    print(Client.voices)
    Alice.severalVoices(Client.voices)