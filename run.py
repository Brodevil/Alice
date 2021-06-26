from Assistant.exts.networks import internetConnection
from Assistant.utils.exceptions import InternetException

if internetConnection() is False:
    raise InternetException("Alice works with INTERNET, Please get connected with INTERNET.")

import threading
from os import startfile, path
import Assistant
from Assistant import alice            # noqa
from Assistant.exts.workWithFiles import DailyWorksExel
from Assistant.constants import Client

__authors__ = ("Abhinav", "Brodevil")  # Both are the same person lol

tasks = DailyWorksExel(path.join(Client.ALICE_PATH,  "DailyWorks.xlsx"))
DailyTasks = threading.Thread(target=alice.dailyTaskReminder, args=(tasks,))



# Running part of the Alice Program
if __name__ == "__main__":
    """
    The Alice just suppose to take the Voice from the user and convert the voice into text
    Then by word to word matching and checking the queary 
    Then the tasks or works get executed as per the queary!
    """

    if Client.ALICE_PASSWORD is not None:
        password = str()

        alice.speak("Alice is password Protected, Kindly Please type the Password To Access Alice!")
        while password != Client.ALICE_PASSWORD:
            alice.speak("Incorrect Password, Access not Granted! Please Try Again.") if password != "" else None
            password = input("Enter the password of Alice : \t")
        else:
            alice.speak("Access Granted.")

    alice.intro()           # Introduction of Alice
    DailyTasks.start()      # daily task reminding will start here using Multiprocessing

    # The program will be going to run on Infinite loop
    while True:
        queary = alice.takeCommand().lower()

        if 'sleep' in queary or 'break' in queary or "rest" in queary:
            alice.speak(f"Okay {Client.GENDER}! I am going for sleep, Call me any time for any help!")
            startfile(path.join(Client.ALICE_PATH, "Assistant//resources//images//Ribbons.scr"))

            while 'wake up' not in queary and 'back to work' not in queary:
                queary = alice.takeCommand()
            else:
                alice.speak(f"{alice.goodWish} {Client.GENDER}! How May I can help you!")

        # Logic of Program
        if queary != "none" and 'skip this one' not in queary or "leave this one" or "leave that one":
            Assistant.logic(queary)
