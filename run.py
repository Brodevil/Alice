from Assistant.exts.networks import internetConnection
from Assistant.utils.exceptions import InternetException

if internetConnection() is False:
    raise InternetException("Alice works with INTERNET, Please get connected with INTERNET.")

import multiprocessing
from os import getcwd
import Assistant
from Assistant import alice
from Assistant.exts.workWithFiles import DailyWorksExel

__all__ = ["queary", ]
__authors__ = ("Abhinav", "Brodevil")  # Both are the same person lol

tasks = DailyWorksExel(getcwd().replace("\\Alice", "\\Alice\\DailyWorks.xlsx"))
DailyTasks = multiprocessing.Process(target=alice.dailyTaskReminder, args=(tasks,))

# Running part of the Alice Program
if __name__ == "__main__":
    alice.intro()  # Introduction
    DailyTasks.start()

    while True:  # The program will be going to run on Infinite loop
        queary = alice.takeCommand().lower()
        if 'sleep' in queary or 'take a break' in queary:
            alice.speak("I am going to sleep while you don't wake up me")
            while 'wake up' not in queary and 'back to work' not in queary:
                queary = alice.takeCommand()
                
        if queary != "none":
            if 'skip this one' not in queary or "leave this one" or "leave that one":
                Assistant.logic(queary, DailyTasks)  # Logic for execution task based on query
