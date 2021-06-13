import datetime
import time
from os import environ, getcwd

import PyPDF2
import webbrowser
import pyautogui
import winsound

import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from tkinter.filedialog import askopenfilename 

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
        self.name = environ.get("UserName",
                                "Abhinav")  # this is the user name of the person who suppose to use this program : Data From (.env)
        self.AssistantName = Client.ASSISTANT_NAME

        self.city = environ.get("LOCATION", localInfo())  # Data From (.env)
        self.voice = Client.VOICE
        self.voiceSpeed = Client.VOICE_RATE

    @staticmethod
    def severalVoices(voicesId=Client.VOICES):
        """ This is the function to show the user how many VOICES are available in his/her system
        So that the user will able to choose his own liked VOICE
        """

        engine = pyttsx3.init("sapi5")
        for index, voice in enumerate(voicesId):
            engine.setProperty("voice", voice)
            engine.setProperty("rate", 170)

            if index == 0:
                print(
                    f"{Client.ASSISTANT_NAME} : Hey there! I am {index + 1}st VOICE of your system {Client.GENDER}! You can select VOICE as a default by putting my VoiceNumber={index + 1} in .env file\n")
                engine.say(
                    f"Hey there! I am {index + 1}st VOICE of your system {Client.GENDER}! You can select VOICE as a default by putting my VoiceNumber={index + 1} in .env file")
                engine.runAndWait()

            elif index == 1:
                print(
                    f"{Client.ASSISTANT_NAME} : Hey there! I am {index + 1}nd VOICE of your system {Client.GENDER}! You can select VOICE as a default by putting my VoiceNumber={index + 1} in .env file\n")
                engine.say(
                    f"Hey there! I am {index + 1}nd VOICE of your system {Client.GENDER}! You can select VOICE as a default by putting my VoiceNumber={index + 1} in .env file")
                engine.runAndWait()

            elif index == 2:
                print(
                    f"{Client.ASSISTANT_NAME} : Hey there! I am {index + 1}rd VOICE of your system {Client.GENDER}! You can select VOICE as a default by putting my VoiceNumber={index + 1} in .env file\n")
                engine.say(
                    f"Hey there! I m {index + 1}rd VOICE of your system {Client.GENDER}! You can select VOICE as a default by putting my VoiceNumber={index + 1} in .env file")
                engine.runAndWait()

            else:
                print(
                    f"{Client.ASSISTANT_NAME} : Hey there! I am {index + 1}th VOICE of your system {Client.GENDER}! You can select VOICE as a default by putting my VoiceNumber={index + 1} in .env file\n")
                engine.say(
                    f"Hey there! I am {index + 1}th VOICE of your system {Client.GENDER}! You can select VOICE as a default by putting my VoiceNumber={index + 1} in .env file")
                engine.runAndWait()

    def speak(self, *args):
        """ Speak function as per the selected VOICE by the user in .env file

         argument : string
         work : spoke the string in the user's selected VOICE by default speaker
         return : None

         """

        engine = pyttsx3.init('sapi5')
        engine.setProperty("voice", Client.VOICES[self.voice - 1])
        engine.setProperty("rate", self.voiceSpeed)
        print("{0} : {1:}\n".format(self.AssistantName, *args))
        engine.say(" ".join(args))
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
        """
        the function will run at the startup of the program, after the Alice get initialized

        introduction of Alice as follow:
        1. How is Alice?
        2. Time and Date
        3. Total usable STORAGE, Memory used, CPU used
        4. Location
        5. If BATTERY is there then its changed percentage and charging status with suggestion
        6. Its own LOCATION's weather, which had tracked by ip and weather by api
        7. Good Wish = Morning/ Afternoon/ Evening as per the time
        """

        self.speak(Client.INTRO)
        self.speak(
            f"Its {datetime.datetime.now().strftime('%I:%M %p')}, and today's date is {datetime.datetime.now().day} of {datetime.date(1900, datetime.datetime.now().month, 1).strftime('%B')} {datetime.datetime.now().year} ")
        self.speak(
            f"Usable Storage : {Client.STORAGE['Total']} GB, Memory Used : {Client.MEMORY_STATUS}%,  CPU Used : {Client.CPU_STATUS}%")
        self.speak(
            f"You are in the Country {Client.LOCATION[0]} and near by {Client.LOCATION[2]} which is in {Client.LOCATION[1]} Region {Client.GENDER}!. ")

        try:
            self.speak(f"Battery is {Client.BATTERY_STATUS}% Charged!, " + "And its still in charging." if Client.BATTERY_PLUGGED else "", f"{Client.GENDER}! I guess you should plug out the charger now!" if Client.BATTERY_STATUS >= 95 and Client.BATTERY_PLUGGED else "", f"{Client.GENDER}! Its very low battery, Please plug in to charge" if Client.BATTERY_STATUS >= 30 and not Client.BATTERY_PLUGGED else "")
        except NameError:
            pass

        self.speak(Client.WEATHER_INFO)  # Trying to say the weather report ond the client local area'
        self.speak(
            f"{self.goodWish} {self.name} {Client.GENDER}!, System is now fully Operational. How Can I help you {Client.GENDER}")

    @staticmethod
    def edge(url):
        """Edge is my Favorite Browser so this function initialize the edge browser
        Argument: url of the website
        process : opine that url or website in the edge browser
         """
        edgePath = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edgePath))
        webbrowser.get('edge').open(url)

    @staticmethod
    def activePC(minutes):
        """
        The function to keep pc active while it will just do some activities like moving mouse and click shif
        so that your pc will active for number of minutes
        """

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
                audio_reader.setProperty("rate", 175)
                audio_reader.setProperty("voice", Client.VOICES[Client.VOICE - 1])

                for page in range(fromPageNo, reader.numPages):
                    next_page = reader.getPage(page)
                    content = next_page.extractText()
                    full_Text += content

                '''commented part, if the pdf file is small then we can just created .mp3 file and save the VOICE in it
                but the big pdf files will not able to convert into mp3 so we can directly speak by audio_reader.say()'''
                # To save the VOICE in a mp3 file, but the problem is that, the large books are not able to be save to file
                # audioFile = asksaveasfile(mode='w', defaultextension=".mp3")
                # if audioFile is None:
                #     return None
                # audio_reader.save_to_file(content, audioFile)

                # this will say to VOICE at the current time. While the program will be paused and just book will be read
                audio_reader.say(content)
                audio_reader.runAndWait()
            except Exception:
                return None
        # return audioFile

    def dailyTaskReminder(self, task: dict):
        """
        Function using multi processing runs in the background while program to remind the user
        the user can able to write his time and task in the exel file so that the program will be going
        to remind user whole day
        """
        while True:
            for exelTime, work in task.items():
                currentTime = datetime.time(int(datetime.datetime.now().strftime("%H")),
                                            int(datetime.datetime.now().strftime("%M")))
                if exelTime == currentTime:
                    notifier(work,
                             f"{Client.ASSISTANT_NAME} :  I am reminding you {Client.GENDER} for your Following task",
                             getcwd().replace("\\Alice", "\\Alice\\Assistant\\resources\\Images\\time-out.ico"))

                    winsound.Beep(frequency=2500, duration=4000)
                    self.speak(
                        f"{Client.GENDER}! You had a task that, {work.replace('i', 'you').replace('my', 'your')}")
                    time.sleep(62)


# Object for the Alice class
alice = Alice()


