import Assistant
from Assistant import alice



if __name__ == "__main__":
    # Running part of the Alice Program
    alice.intro()       # Introdunction


    while True:     # The program will be going to run on INfinate loop
        queary = alice.takeCommand().lower()
        if queary != "none":
            Assistant.logic(queary)     # Logic for executin task based on query