import Assistant
from Assistant import alice



__all__ = ["queary", ]
__authors__ = ("Abhinav", "Brodevil")       # Both are the same person lol



if __name__ == "__main__":
    # Running part of the Alice Program
    alice.intro()       # Introduction
    while True:     # The program will be going to run on Infinite loop
        queary = alice.takeCommand().lower()
        if queary != "none":
            if 'skip this' not in queary:
                Assistant.logic(queary)     # Logic for execution task based on query

