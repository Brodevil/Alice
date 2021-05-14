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


def goodWish():
    presentHour = int(datetime.datetime.now().hour)
    if presentHour == 0 or presentHour < 12:
        return "Good Morning"

    elif presentHour == 12 or presentHour < 18:
        return "Good Afternoon"

    else:
        return "Good Evening"


class Alice:
    """ 
    Alice Assitant:

    This class contain the Function of the Alice program and also with the Assitant Data
    """

    def __init__(self):
        super().__init__()
        self.name = environ.get("UserName", "Abhinav")      # this is the user name of the person who suppose to use this program : Data From (.env)
        self.gender = environ.get("GENDER", 'male')          # Gender of the user, Data From (.env)
        if gender == "male" or gender == "boy":
            self.gender = "Sir"
        elif gender == "female" or gender == "girl":
            self.gender == "Mam"

        self.city = environ.get("location", localInfo())    # Data From (.env)
        self.voice = Client.voice
        self.voiceSpeed = Client.voiceRate
        


    def severalVoices(self, voicesId=Client.voices):
        """ This is the function to show the user how many voices are available in his/her system 
        So that the user will able to choose his own liked voice """

        engine = pyttsx3.init("sapi5")
        for index, voice in enumerate(voicesId):
            engine.setProperty("voice", voice)
            engine.setProperty("rate", 170)
            if index == 0:
                engine.say(f"Hey there! I am {index+1}st voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file")
                print(f"{Client.name} : Hey there! I am {index+1}st voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file\n")
            elif index == 1:
                engine.say(f"Hey there! I am {index+1}nd voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file")
                print(f"{Client.name} : Hey there! I am {index+1}nd voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file\n")
            elif index == 2:
                engine.say(f"Hey there! I m {index+1}rd voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file")
                print(f"{Client.name} : Hey there! I am {index+1}rd voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file\n")
            else:
                engine.say(f"Hey there! I am {index+1}th voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file")
                print(f"{Client.name} : Hey there! I am {index+1}th voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file\n")
            engine.runAndWait()


    def speak(self, audio):
        """ Speak function as per the selected voice """
        
        engine = pyttsx3.init('sapi5')
        engine.setProperty("voice", Client.voices[self.voice])
        engine.setProperty("rate", self.voiceSpeed)
        print(f"{Client.name} :  {audio}\n")
        engine.say(audio)
        engine.runAndWait()
    

    def intro(self):
        speak(Client.intro)
        speak(f"{goodWish()} {self.name} {self.gender}!")
        speak()
        




if __name__ == "__main__":
    test0 = Alice()
    print(test0.city)
    test0.severalVoices()