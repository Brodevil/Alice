import requests
import json
import datetime
import pyttsx3
from os import environ
import pprint
from dotenv import load_dotenv
from exts.networks import localInfo                                                                   # noqa
from constants import Contacts, ERROR_REPLIES, NEGATIVE_REPLIES, POSITIVE_REPLIES, Client             # noqa


__all__ = ("Alice", "alice")


load_dotenv()



class Alice:
    """ 
    Alice Assitant:

    This class contain the Function of the Alice program and also with the Assitant Data
    """


    def __init__(self):
        super().__init__()
        gender=str(environ.get("GENDER", 'male'))
        self.name = environ.get("UserName", "Abhinav")      # this is the user name of the person who suppose to use this program : Data From (.env)
        self.gender = ("Sir" if gender == "male" else "Mam")


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
                print(f"{Client.name} : Hey there! I am {index+1}st voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file\n")
                engine.say(f"Hey there! I am {index+1}"+"st"+ " voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file")
                
           
            elif index == 1:
                print(f"{Client.name} : Hey there! I am {index+1}nd voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file\n")
                engine.say(f"Hey there! I am {index+1}nd voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file")

            elif index == 2:
                print(f"{Client.name} : Hey there! I am {index+1}rd voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file\n")
                engine.say(f"Hey there! I m {index+1}rd voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file")
            
            else:
                print(f"{Client.name} : Hey there! I am {index+1}th voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file\n")
                engine.say(f"Hey there! I am {index+1}th voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index+1} in .env file")
            
        engine.runAndWait()

    

    def speak(self, audio):
        """ Speak function as per the selected voice """
        
        engine = pyttsx3.init('sapi5')
        engine.setProperty("voice", Client.voices[self.voice-1])
        engine.setProperty("rate", self.voiceSpeed)
        print(f"{Client.Assistantname} :  {audio}\n")
        engine.say(audio)
        engine.runAndWait()
    

    @property
    @staticmethod
    def goodWish():
        presentHour = int(datetime.datetime.now().hour)
        if presentHour == 0 or presentHour < 12:
            return "Good Morning"

        elif presentHour == 12 or presentHour < 18:                                                       # noqa
            return "Good Afternoon"

        else:
            return "Good Evening"


    def intro(self):
        self.speak(Client.intro)
        self.speak(f"Storage : {Client.storage['Total']} GB, Memory Used : {Client.memory_status}%,  CPU Used : {Client.cpu_status}%")
        try:
            self.speak(f"Battery is {Client.battery_status}% Charged!, You are in the Country {Client.location[0]} and near by {Client.location[2]} which is in {Client.location[1]} Region {self.gender}!")
            self.speak(Client.weatherInfo)   # Tring to say the weather report ond the client local area'
        except Exception:
            pass
        self.speak(f"{self.goodWish} {self.name} {self.gender}!, System is now fully Operational. How Can I help you {self.gender}")
        if Client.internet == False:
            self.speak(f"{self.gender}! Internet is not connected. I going to work with Internet, Please get connect with internet.")
            exit()
        

alice = Alice()     # Object for the Alice class  


if __name__ == "__main__":
    test0 = Alice()
    test0.intro()
    # print(environ.get("GENDER"))