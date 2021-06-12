from os import environ
import os
from dotenv import load_dotenv
import pyttsx3
import platform

import shutil
import psutil
import string
from Assistant.exts.networks import localInfo, weather, internetConnection  # noqa
from Assistant.exts.workWithFiles import contactInfo  # noqa
from Assistant.utils.exceptions import EnvFileValueError  # noqa

__all__ = ["Client", "Contacts", "ERROR_REPLIES", "NEGATIVE_REPLIES", "POSITIVE_REPLIES",
           "Storage"]

load_dotenv()


def Storage():
    """ Function to get total harder STORAGE as per the drive """
    totalStorage = 0
    usedStorage = 0
    freeStorage = 0
    for i in list(string.ascii_lowercase):
        try:
            storeInfo = list(map(lambda x: x // 2 ** 30, shutil.disk_usage(f"{i}:\\")))
            totalStorage += storeInfo[0]
            usedStorage += storeInfo[1]
            freeStorage += storeInfo[2]
        except Exception:
            pass
    return totalStorage, usedStorage, freeStorage


storageInfo = Storage()
engine = pyttsx3.init()
LOCAL_INFORMATION = localInfo()
userSystem = platform.uname()
try:
    BATTERY = psutil.sensors_battery()
except Exception:
    BATTERY = None


class Client:
    ASSISTANT_NAME = environ.get("ASSISTANT_NAME", "Alice")
    INTRO = f"Hey There! Now me to introduce myself, I am {ASSISTANT_NAME}. A virtual desktop assistant and I'm here to assist you with a verity of tasks as best as I can. 24 Hours a day, seven days a week, Importing all preferences from home interface, system is now initializing!"
    ALICE_INFO = "I am written in python by Abhinav, My birthday is 21 December of 2020."

    # Author Info
    AUTHOR = "Abhinav(Brodevil)"
    CONTACT = "brodevil89@gmail.com"
    ALICE_GITHUB_REPOSITORY = "https://github.com/Brodevil/Alice"
    DISCORD_ID = "Brodevil#5822"
    GENDER = environ.get("GENDER")
    if GENDER == "male":
        GENDER = "Sir"
    elif GENDER == "female":
        GENDER = "Mam"
    else:
        raise EnvFileValueError("In .env file GENDER= always should  be 'male or female!' which will your GENDER")

    # Client Choice to Alice
    VOICES = [engine.id for engine in engine.getProperty("voices")]                 # noqa
    VOICE_RATE = int(environ.get("VoiceRate", 175))
    VOICE = int(environ.get("VoiceNumber", 1))
    if VOICE > len(VOICES):
        raise EnvFileValueError(
            f"There are just {len(VOICES)} available in your system and you had choice the {VOICE} number of voice! please Change it in .env file")

    # Few Computer status
    STORAGE = {"Total": storageInfo[0], "Used": storageInfo[1], "Free": storageInfo[2]}  # values are in GB
    MEMORY_STATUS = psutil.virtual_memory().percent  # Used memory in percentage
    CPU_STATUS = psutil.cpu_percent()  # cpu uses in percentage
    COMPUTER_INFO = {"System": userSystem.system, "Node name": userSystem.node, "Release": userSystem.release,
                     "Version": userSystem.version, "Machine": userSystem.machine, "Processor": userSystem.processor}
    INTERNET_CONNECTION = internetConnection()

    # Few user Info :
    MUSIC_DIRECTORY = environ.get("MUSIC", r"C:\Users\ADMIN\Music")  # Music directory should be without space
    FAVOURITE_MUSIC = environ.get("FavMusic", None)
    APPLICATIONS_SHORTCUTS_PATH = os.getcwd().replace("\\Alice",
                                                      "\Alice\Applications")  # Application folder where all the using application shortcuts will available to the user
    ALICE_PATH = "".join([os.getcwd().split("\\Alice")[0], "\\Alice\\"])
    USER_GITHUB = environ.get("GITHUB", "Brodevil")

    if BATTERY is not None:
        BATTERY_STATUS = BATTERY.percent
        BATTERY_PLUGGED = BATTERY.power_plugged

    # Networks infos
    if LOCAL_INFORMATION is not None and weather() is not None:
        CITY = LOCAL_INFORMATION[0]
        LOCATION = LOCAL_INFORMATION[1]['country'], LOCAL_INFORMATION[1]["regionName"], LOCAL_INFORMATION[1]["city"]
        NETWORK = LOCAL_INFORMATION[1]["isp"]
        WEATHER_INFO = weather()


class Contacts:
    files = os.listdir(Client.ALICE_PATH)
    if "contactinfo.xlsx" in files:
        contactsFile = os.path.join(Client.ALICE_PATH, "contactinfo.xlsx")
    else:
        contactsFile = os.path.join(Client.ALICE_PATH, "Contact.xlsx")
    emails = {name: email[0] for name, email in contactInfo(contactsFile).items()}  # noqa
    contactNumber = {name: contactNumber[1] for name, contactNumber in contactInfo(contactsFile).items()}  # noqa


ERROR_REPLIES = [
    "Please don't do that.",
    "You have to stop.",
    "Do you mind?",
    "In the future, don't do that.",
    "That was a mistake.",
    "You blew it.",
    "You're bad at computers.",
    "Are you trying to kill me?",
    "Noooooo!!",
    "I can't believe you've done this",
]

NEGATIVE_REPLIES = [
    "Noooooo!!",
    "Nope.",
    "I'm sorry Dave, I'm afraid I can't do that.",
    "I don't think so.",
    "Not gonna happen.",
    "Out of the question.",
    "Huh? No.",
    "Nah.",
    "Naw.",
    "Not likely.",
    "No way, José.",
    "Not in a million years.",
    "Fat chance.",
    "Certainly not.",
    "NEGATORY.",
    "Nuh-uh.",
    "Not in my house!",
]

POSITIVE_REPLIES = [
    "Yep.",
    "Absolutely!",
    "Can do!",
    "Affirmative!",
    "Yeah okay.",
    "Sure.",
    "Sure thing!",
    "You're the boss!",
    "Okay.",
    "No problem.",
    "I got you.",
    "Alright.",
    "You got it!",
    "ROGER THAT",
    "Of course!",
    "Aye aye, cap'n!",
    "I'll allow it.",
]
