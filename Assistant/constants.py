from os import environ
import os
from dotenv import load_dotenv
import pyttsx3
import platform

import shutil
import psutil
import string
from Assistant.exts.networks import localInfo, weather, internetConnection              # noqa
from Assistant.exts.workWithFiles import contactInfo                                    # noqa


__all__ = ["Client", "Contacts", "ERROR_REPLIES", "NEGATIVE_REPLIES", "POSITIVE_REPLIES",
           "Storage"]

load_dotenv()



def Storage():
    """ Function to get total harder storage as per the drive """
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
    return totalStorage, freeStorage, usedStorage



storageInfo = Storage()
engine = pyttsx3.init()
localInformation = localInfo()
userSystem = platform.uname()
try:
    battery = psutil.sensors_battery()
except Exception:
    battery = None


class Client:
    AssistantName = environ.get("AssistantName", "Alice")
    intro = f"Hey There! Now me to introduce myself, I am {AssistantName}. A virtual desktop assistant and I'm here to assist you with a verity of tasks as best as I can. 24 Hours a day, seven days a week, Importing all preferences from home interface, system is now initializing!"
    aliceInfo = "I am written in python by Abhinav, My birthday is 21 December of 2020."


    # Author Info
    author = "Abhinav(Brodevil)"
    contact = "brodevil89@gmail.com"
    github_assistant_repo = "https://github.com/Brodevil/Alice"
    DiscordId = "Brodevil#5822"


    # Client Choice to Alice
    voices = [engine.id for engine in engine.getProperty("voices")]                                               # noqa
    voiceRate = int(environ.get("VoiceRate", 175))
    voice = int(environ.get("VoiceNumber", 1))
    if voice > len(voices):
        raise Exception(f"There are just {len(voices)} available in your system and you had choice the {voice} number of voice! please Change it in .env file")


    # Few Computer status
    storage = {"Total": storageInfo[0], "Used": storageInfo[1], "Free": storageInfo[2]}  # values are in GB
    memory_status = psutil.virtual_memory().percent  # Used memory in percentage
    cpu_status = psutil.cpu_percent()  # cpu uses in percentage
    internet = internetConnection()
    computerInfo = {"System": userSystem.system, "Node name": userSystem.node, "Release": userSystem.release,
                    "Version": userSystem.version, "Machine": userSystem.machine, "Processor": userSystem.processor}


    # Few user Info :
    musicDirectory = environ.get("MUSIC", r"C:\Users\ADMIN\Music")  # Music directory should be without space
    favouriteMusic = environ.get("FavMusic", None)
    ApplicationShortcutPath = os.getcwd().replace(r"\Alice\Assistant", r"\Alice\Application")          # Application folder where all the using application shortcuts will available to the user
    userGithub = environ.get("GITHUB", "Brodevil")


    if battery is not None:
        battery_status = battery.percent
        battery_plugged = battery.power_plugged


    # Networks infos
    if localInformation is not None and weather() is not None:
        city = localInformation[0]
        location = localInformation[1]['country'], localInformation[1]["regionName"], localInformation[1]["city"]
        network = localInformation[1]["isp"]
        weatherInfo = weather()


class Contacts:
    files = os.listdir()
    if "contactinfo.xlsx" in files:
        contactsFile = os.getcwd().replace(r"Alice\Assistant\constants.py", "Alice\Contacts.xlsx")
    else:
        contactsFile = os.getcwd().replace(r"Alice\Assistant\constants.py", "Alice\constants.py")

    emails = {name: email[0] for name, email in contactInfo(contactsFile).items()}
    contactNumber = {name: contactNumber[1] for name, contactNumber in contactInfo("contactinfo.xlsx").items()}





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

if __name__ == "__main__":
    # print(Client.storage)
    pass
