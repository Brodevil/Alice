from Assistant.exts.networks import internetConnection
from Assistant.utils.exceptions import InternetException

if internetConnection() is False:
    raise InternetException("Alice works with INTERNET, Please get connected with INTERNET.")

import multiprocessing
from os import getcwd, startfile, path
import Assistant
from Assistant import alice
from Assistant.exts.workWithFiles import DailyWorksExel
from Assistant.constants import Client


__all__ = ["queary", ]
__authors__ = ("Abhinav", "Brodevil")  # Both are the same person lol


tasks = DailyWorksExel(getcwd().replace("\\Alice", "\\Alice\\DailyWorks.xlsx"))
DailyTasks = multiprocessing.Process(target=alice.dailyTaskReminder, args=(tasks,))



# Running part of the Alice Program
if __name__ == "__main__":
    """
    The Alice just suppose to take the Voice from the user and convert the voice into text
    Then by word to word matching and checking the queary 
    The tasks, works and much more things get executed!
    """

    alice.intro()               # Introduction of Alice
    DailyTasks.start()          # daily task reminding will start here using Multiprocessing


    # The program will be going to run on Infinite loop
    while True:
        queary = alice.takeCommand().lower()

        if 'sleep' in queary or 'take a break' in queary:
            alice.speak(f"{Client.GENDER}! I am going to sleep while you don't wake up me")
            startfile(path.join(Client.ALICE_PATH, "Media//Ribbons.scr"))

            while 'wake up' not in queary and 'back to work' not in queary:
                queary = alice.takeCommand()
            else:
                alice.speak(f"{alice.goodWish} {Client.GENDER}! How May I can help you!")

        # Logic of Program
        if queary != "none" and 'skip this one' not in queary or "leave this one" or "leave that one":
            Assistant.logic(queary, DailyTasks)
