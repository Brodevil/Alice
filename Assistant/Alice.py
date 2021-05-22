import requests
import json
import datetime
import time

from os import environ
import PyPDF2                                                                   # noqa
import pprint
import webbrowser 


from dotenv import load_dotenv
import speech_recognition as sr 
import pyttsx3
from tkinter.filedialog import *


from Assistant.exts.networks import localInfo                                                 # noqa                                                                
from Assistant.constants import Contacts, ERROR_REPLIES, NEGATIVE_REPLIES, POSITIVE_REPLIES, Client             # noqa




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
        self.Assistantname = Client.Assistantname
        if gender == "male":
            self.gender = "Sir"
        elif gender == "female":
            self.gender = "Mam"
        else:
            raise ValueError("In .env file GENDER= always should  be 'male or female!' which will your gender")


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
        print(f"{self.Assistantname} : {audio}\n")
        engine.say(audio)
        engine.runAndWait()
    


    def takeCommand(self):
        '''
        The not having any parameter but it taking the input form the microphone of the user 
        and return the string object that the user says
        '''
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(f"{self.Assistantname}: Listening....")
            r.pause_threshold = 1
            r.energy_threshold = 100
            audio = r.listen(source)

        try:
            print(f"{self.Assistantname} : Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"{self.name} : {query}\n")

        except Exception as e:
            print("Alice : Sorry! I didn't get that...\n")
            return "None"

        return query



    @property
    def goodWish(self):
        presentHour = int(datetime.datetime.now().hour)
        if presentHour == 0 or presentHour < 12:
            return "Good Morning"

        elif presentHour == 12 or presentHour < 18:                                                       # noqa
            return "Good Afternoon"

        else:
            return "Good Evening"



    def intro(self):
        self.speak(Client.intro)
        self.speak(f"Its {datetime.datetime.now().strftime('%I:%M %p')}, and todays date is {datetime.datetime.now().day} of {datetime.date(1900, datetime.datetime.now().month, 1).strftime('%B')} {datetime.datetime.now().year} ")
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
        

    @staticmethod
    def edge(url):
        edgePath = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edgePath))
        webbrowser.get('edge').open(url)



    def audioBook(self, fromPageNo=0):
        """ Funtion to read the pdf and save the audio in a mp3 file at the same directory where the pdf locatied """
        pdfPath=askopenfilename()
        print(pdfPath)
        full_Text = str()
        if ".pdf" not in pdfPath:       
            return None

        with open(pdfPath, "rb") as book:
            try:
                reader = PyPDF2.PdfFileReader(book)
                audio_reader = pyttsx3.init('sapi5')
                audio_reader.setProperty("rate", 170)
                audio_reader.setProperty("voice", Client.voices[Client.voice-1])
                
                for page in range(fromPageNo, reader.numPages):
                    next_page = reader.getPage(page)
                    content = next_page.extractText()
                    full_Text+=content
                    

                audiofile = pdfPath.replace(".pdf", ".mp3")
                
                #  To save the voice in a mp3 file, but the problem is that, the large books are not able to be save to file 
                # audio_reader.save_to_file(content, audiofile)

                # this will say to voice at the current time. While the program will be paused and just book will be readed
                audio_reader.say(content)
                audio_reader.runAndWait()
            except Exception:
                return None
        return audiofile





alice = Alice()     # Object for the Alice class  


if __name__ == "__main__":      # Testing part, just for testing pourposes
    test0 = Alice()
    # test0.intro()
    # print(environ.get("GENDER"))
    # queary = test0.takeCommand()
    # test0.speak(queary)
    # test0.edge("https://github.com/Brodevil")
    # test0.audioBook(r"Assistant\media\Machine Learning.pdf")
    test0.intro()
    pass
