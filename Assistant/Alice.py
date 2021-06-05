import datetime
import time
from os import environ

import PyPDF2  # noqa
import webbrowser
import pyautogui
import winsound

import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from tkinter.filedialog import *

from Assistant.exts.networks import localInfo  # noqa
from Assistant.exts.alarm import notifier  # noqa
from Assistant.constants import Contacts, ERROR_REPLIES, NEGATIVE_REPLIES, POSITIVE_REPLIES, Client  # noqa

__all__ = ("Alice", "alice")

load_dotenv()


class Alice:
    """ 
    Alice Assistant:

    This class contain the Function of the Alice program and also with the Assistant Data
    """

    def __init__(self):
        super().__init__()
        gender = str(environ.get("GENDER", 'male'))
        self.name = environ.get("UserName",
                                "Abhinav")  # this is the user name of the person who suppose to use this program : Data From (.env)
        self.AssistantName = Client.AssistantName
        if gender == "male":
            self.gender = "Sir"
        elif gender == "female":
            self.gender = "Mam"
        else:
            raise ValueError("In .env file GENDER= always should  be 'male or female!' which will your gender")

        self.city = environ.get("location", localInfo())  # Data From (.env)
        self.voice = Client.voice
        self.voiceSpeed = Client.voiceRate

    def severalVoices(self, voicesId=Client.voices):
        """ This is the function to show the user how many voices are available in his/her system 
        So that the user will able to choose his own liked voice 
        """

        engine = pyttsx3.init("sapi5")
        for index, voice in enumerate(voicesId):
            engine.setProperty("voice", voice)
            engine.setProperty("rate", 170)

            if index == 0:
                print(
                    f"{Client.AssistantName} : Hey there! I am {index + 1}st voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index + 1} in .env file\n")
                engine.say(
                    f"Hey there! I am {index + 1}st voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index + 1} in .env file")


            elif index == 1:
                print(
                    f"{Client.AssistantName} : Hey there! I am {index + 1}nd voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index + 1} in .env file\n")
                engine.say(
                    f"Hey there! I am {index + 1}nd voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index + 1} in .env file")

            elif index == 2:
                print(
                    f"{Client.AssistantName} : Hey there! I am {index + 1}rd voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index + 1} in .env file\n")
                engine.say(
                    f"Hey there! I m {index + 1}rd voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index + 1} in .env file")

            else:
                print(
                    f"{Client.AssistantName} : Hey there! I am {index + 1}th voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index + 1} in .env file\n")
                engine.say(
                    f"Hey there! I am {index + 1}th voice of your system {self.gender}! You can select voice as a default by putting my VoiceNumber={index + 1} in .env file")
        engine.runAndWait()

    def speak(self, audio):
        """ Speak function as per the selected voice by the user in .env file
         
         argument : string
         work : spoke the string in the user's selected voice by default speaker
         return : None
         
         """

        engine = pyttsx3.init('sapi5')
        engine.setProperty("voice", Client.voices[self.voice - 1])
        engine.setProperty("rate", self.voiceSpeed)
        print(f"{self.AssistantName} : {audio}\n")
        engine.say(audio)
        engine.runAndWait()

    def takeCommand(self):
        """
        The not having any parameter but it taking the input form the microphone of the user
        and return the string object that the user says

        takes : audio from the default mic
        return :  the sentence spoke by the user return it as a string

        behind the seen the function takes google's api to recognize the audio,
        so indirectly Alice will needed to be online for working properly.
        """

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(f"{self.AssistantName}: Listening....")
            r.pause_threshold = 1
            r.energy_threshold = 300
            audio = r.listen(source)

        try:
            print(f"{self.AssistantName} : Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"{self.name} : {query}\n")
        except Exception:
            print(f"{self.AssistantName} : Sorry! I didn't get that...\n")
            return "None"
        else:
            return query

    @property
    def goodWish(self):
        presentHour = int(datetime.datetime.now().hour)
        if presentHour == 0 or presentHour < 12:
            return "Good Morning"

        elif presentHour == 12 or presentHour < 18:  # noqa
            return "Good Afternoon"

        else:
            return "Good Evening"

    def intro(self):
        self.speak(Client.intro)
        self.speak(
            f"Its {datetime.datetime.now().strftime('%I:%M %p')}, and today's date is {datetime.datetime.now().day} of {datetime.date(1900, datetime.datetime.now().month, 1).strftime('%B')} {datetime.datetime.now().year} ")
        self.speak(
            f"Usable Storage : {Client.storage['Total']} GB, Memory Used : {Client.memory_status}%,  CPU Used : {Client.cpu_status}%")
        try:
            self.speak(
                f"You are in the Country {Client.location[0]} and near by {Client.location[2]} which is in {Client.location[1]} Region {self.gender}!. "
                f"Battery is {Client.battery_status}% Charged!, " + "And its still in charging." if Client.battery_plugged else "")

            self.speak(Client.weatherInfo)  # Trying to say the weather report ond the client local area'
        except Exception:
            pass

        self.speak(
            f"{self.goodWish} {self.name} {self.gender}!, System is now fully Operational. How Can I help you {self.gender}")

        if not Client.internet:
            self.speak(
                f"{self.gender}! Internet is not connected. I going to work with Internet, Please get connect with internet.")
            exit()

    @staticmethod
    def edge(url):
        edgePath = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edgePath))
        webbrowser.get('edge').open(url)

    @staticmethod
    def activePC(minutes):
        pyautogui.FAILSAFE = False
        presentTime = int(time.time())
        while presentTime + minutes * 60 >= int(time.time()):
            time.sleep(3 * 60)
            for i in range(50, 100):
                pyautogui.moveTo(500, i * 5)
            for i in range(0, 5):
                pyautogui.press("shift")

    @staticmethod
    def audioBook(fromPageNo=0):
        """ Function to read the pdf and save the audio in a mp3 file at the same directory where the pdf located """
        pdfPath = askopenfilename(mode='r', defaultextension=".pdf")
        full_Text = str()
        if pdfPath is None:  # this condition happened when the user will click cancel
            return None

        with open(pdfPath, "rb") as book:
            try:
                reader = PyPDF2.PdfFileReader(book)
                audio_reader = pyttsx3.init('sapi5')
                audio_reader.setProperty("rate", 170)
                audio_reader.setProperty("voice", Client.voices[Client.voice - 1])

                for page in range(fromPageNo, reader.numPages):
                    next_page = reader.getPage(page)
                    content = next_page.extractText()
                    full_Text += content

                '''commented part, if the pdf file is small then we can just created .mp3 file and save the voice in it
                but the big pdf files will not able to convert into mp3 so we can directly speak by audio_reader.say()'''
                # To save the voice in a mp3 file, but the problem is that, the large books are not able to be save to file
                # audioFile = asksaveasfile(mode='w', defaultextension=".mp3")
                # if audioFile is None:
                #     return None
                # audio_reader.save_to_file(content, audioFile)

                # this will say to voice at the current time. While the program will be paused and just book will be read
                audio_reader.say(content)
                audio_reader.runAndWait()
            except Exception:
                return None
        # return audioFile

    def dailyTaskReminder(self, task: dict):
        print("function me paunch gaye bhai")
        while True:
            for exelTime, work in task.items():
                currentTime = datetime.time(int(datetime.datetime.now().strftime("%H")),
                                            int(datetime.datetime.now().strftime("%M")))
                if exelTime == currentTime:
                    notifier(work, f"{Client.AssistantName} :  I am reminding you sir for your Following task",
                             r"Assistant/utils/time-out.ico")
                    winsound.Beep(frequency=2500, duration=4000)
                    self.speak(f"{self.gender}! You had a task that, {work.replace('i', 'you')}")
                    time.sleep(62)



# Object for the Alice class
alice = Alice()
