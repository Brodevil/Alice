import datetime
import os
import time
import keyboard
import random
import sys
import webbrowser

import psutil
from playsound import playsound
import pywhatkit
import multiprocessing as mp
import subprocess

from Assistant.exts import reminder                                                        # noqa
from Assistant.exts import networks                                                        # noqa
from Assistant.constants import Contacts, ERROR_REPLIES, NEGATIVE_REPLIES, POSITIVE_REPLIES, Client  # noqa

from Assistant.resources.login import login                                                 # noqa
from Assistant.Alice import alice                                                           # noqa
from Assistant.exts import keyactivities                                                    # noqa
from Assistant.exts import workWithFiles                                                    # noqa



__all__ = ["logic"]

# load_dotenv()
try:
    battery = psutil.sensors_battery()
except Exception:
    battery = None


def logic(queary):
    """This is the logic of the Program as it will be matching several query and do the programmed task """

    # fetching info from internet

    if 'wikipedia' in queary:
        alice.speak("Searching Wikipedia...")
        queary = queary.replace("wikipedia", "")
        alice.speak(networks.wiki(queary))


    elif 'search' in queary and 'google' in queary:
        queary = queary.replace("search", "")
        queary = queary.replace("google", "")
        alice.speak(f"Fetching the related queary in Google")
        pywhatkit.search(queary)



    elif "youtube" in queary and "search" in queary:
        try:
            search = queary.split("youtube")[-1]
            alice.speak("Fetching Data....")
            pywhatkit.playonyt(search)
        except Exception:
            alice.speak(f"No results found on {search} on youtube")



    # quiting the program
    elif "bye" in queary or 'kill yourself' in queary or 'quit' in queary:
        alice.speak("That's it, I m quiting....")
        sys.exit(0)



    # Opening websites
    elif 'open youtube studio' in queary:
        alice.speak("Opening youtube studio...")
        alice.edge("https://studio.youtube.com/")


    elif 'open youtube' in queary:
        alice.speak("Opening youtube...")
        webbrowser.open("youtube.com")


    elif 'open google' in queary:
        alice.speak("Opening google...")
        alice.edge("google.com")


    elif 'open stack overflow' in queary:
        alice.speak("Opening stackoverflow...")
        alice.edge("stackoverflow.com")


    elif 'reveal your code' in queary or 'your code' in queary:
        alice.speak("Opening Github repository.....")
        alice.edge("github.com/Brodevil/Alice")


    elif 'open github' in queary:
        alice.speak("Opening Github.....")
        alice.edge(f"https://github.com/{Client.userGithub}")


    elif 'open discord' in queary:
        alice.speak("Opening Discord in Browser.....")
        alice.edge("https://discord.com/channels/@me")


    elif 'open instagram' in queary:
        alice.speak("Opening Instagram.....")
        alice.edge("https://www.instagram.com")


    elif 'open whatsapp' in queary:
        alice.speak("Opening  Whatsapp.....")
        alice.edge("https://web.whatsapp.com/")



    elif 'open spotify' in queary:
        alice.speak("Opening Spotify.....")
        alice.edge('https://open.spotify.com/')


    elif 'pep8' in queary:
        alice.edge("https://www.python.org/dev/peps/pep-0008/")


    elif 'gmail' in queary:
        alice.speak("Opening Gmail...")
        alice.edge("https://gmail.com")



    # work with GUI or windows :
    elif 'desktop' in queary:
        keyboard.press_and_release("win+d")


    elif 'lock pc' in queary or "lock the pc" in queary:
        os.system("rundll32.exe user32.dll, LockWorkStation")
        sys.exit(0)


    elif 'shutdown pc' in queary:
        os.startfile(r"C:\Windows\System32\SlideToShutDown.exe")
        alice.speak("Shuting down pc....")
        time.sleep(1)
        keyboard.press_and_release("enter")


    elif 'restart pc' in queary:
        os.system("Shutdown.exe -r -t 00")


    elif 'switch tab' in queary:
        keyboard.press_and_release("alt+tab")


    elif 'switch window right' in queary:
        keyboard.press_and_release("ctrl+win+right")


    elif 'switch window left' in queary:
        keyboard.press_and_release("ctrl+win+left")




    # reminder        
    elif 'remind me after' in queary or "wake up me after" in queary:
        queary = queary.split("remind me after " if "remind me after" in queary else "wake up me after ")[-1]
        queary = queary.replace("i", "you")
        magnitude = int(queary.split()[0])
        unit = queary.split()[1]
        alice.speak(f"Okay {alice.gender}! I will be reminding you after {magnitude} {unit}!")
        try:
            pourpose = queary.split("so that ")[1]
        except Exception:  # the user can give the reason as a option
            pourpose = "You didn't told the pourpose for reminding, Its might be some thing secret \U0001F923"

        side_reminder = mp.Process(target=reminder.reminder, args=(magnitude, unit, pourpose))
        side_reminder.start()

    



    # music
    elif 'play music' in queary or "play another music" in queary or "play another song" in queary or "play song" in queary or "play" in queary and "random" in queary and "music" in queary:
        music = os.listdir(Client.musicDirectory)
        os.startfile(os.path.join(Client.musicDirectory, random.choice(music)))
        alice.speak("Playing Music...")


    elif 'brown munde' in queary:  # this function is just for my self i.e. For Abhinav personal songs
        try:
            os.startfile(
                r"E:\ADMIN\Music\BRODEVIL\Hollywood_song\sunna_hai_kya\BROWN MUNDE.mp3")
        except Exception:
            pass


    elif "play my music" in queary or "play my song" in queary or "i am feeling bad" in queary or "sad" in  queary  and "feeling" in queary or "unhappy" in queary and "feeling" in queary:
        coolMuisc = mp.Process(target=playsound, args=(Client.favouriteMusic, ))
        coolMuisc.start()


    elif 'play' in queary:
        queary = queary.split("play ")[-1]
        alice.speak(f"Showing related results to {queary}")
        alice.edge(f"https://music.youtube.com/search?q={queary}")



    # working with files :
    elif 'delete unwanted files' in queary:
        alice.speak("Deleting unwanted files...")
        workWithFiles.deleteUnwantedFiles()



        # Natural Talks/ Fun commands :
    elif 'is i am audio able' in queary:
        alice.speak(random.choice(POSITIVE_REPLIES))


    elif 'testing' in queary:
        alice.speak(f"Hello {alice.gender}! {random.choice(POSITIVE_REPLIES)}")


    elif 'hello' in queary or "hello alice" in queary or queary == "alice":
        alice.speak(f"Hello {alice.gender}! how may I can help you.")


    elif 'good morning' in queary or 'good afternoon' in queary or 'good evening' in queary:
        wish = alice.goodWish
        if wish.lower() in queary:
            alice.speak(f"{wish} {alice.gender}!")
        else:
            alice.speak(f"{alice.gender}! Its {wish.split()[1]} Right now!")


    elif "time" in queary:
        alice.speak(f"Its {datetime.datetime.now().strftime('%I:%M %p')} {alice.gender}!")


    elif "date" in queary:
        alice.speak(
            f"Its {datetime.datetime.now().day} of {datetime.date(1900, datetime.datetime.now().month, 1).strftime('%B')} {datetime.datetime.now().year}")


    elif 'who are you' in queary or "introduction" in queary:
        alice.intro()


    elif "what's my name" in queary or "what is my name" in queary or "who i am" in queary:
        alice.speak(f"You are {alice.name} {alice.gender}!, But why did you are asking this?")


    elif "to kaise hain aap log" in queary:  # just for ha
        alice.speak("Hum thik hai bhai, Tum batao!..")


    elif "yalghar" in queary:
        alice.edge("https://www.youtube.com/watch?v=zzwRbKI2pn4")


    elif 'voices' in queary or "change your voice" in queary:
        alice.severalVoices(voicesId=Client.voices)


    elif 'pause' in queary or "stop for" in queary:
        try:
            period = int(queary.split("for")[-1].split()[0])
        except Exception:
            alice.speak(f"{alice.gender} For how many minutes I should stop or sleep")
            try:
                period = int(alice.takeCommand())
            except ValueError:
                try:
                    alice.speak(
                        f"Sorry {alice.gender}! I didn't get that, Can you type the number of minutes in terminal ")
                    period = int(input("Enter the number of minutes I should sleep :\t"))
                except ValueError:
                    pass

        alice.speak(f"Okay {alice.gender}! I will be wake up after {period} minutes.")  # noqa
        time.sleep(60 * period)

        alice.speak(f"{alice.goodWish} {alice.gender}!, I wake up after {period} minutes, Lets back to work.")
        del period



    elif 'thank you' in queary or 'thanks' in queary:
        alice.speak(f"Your most welcome {alice.gender}!")


    elif 'how are you' in queary:
        alice.speak("I am quite fine sir, What about you ?")


    elif 'alice' in queary and 'info' in queary or "your" in queary and "info" in queary:
        alice.speak(
            f"I am written in Python by {Client.author}Sir!. To contact him you can email at ({Client.contact}), Check out his GitHub Profile You will know more about my sir")
        print(
            f"Alice : Mr. Abhinav's  Email:{Client.contact}. Github link :{Client.github_assistant_repo}. Discord Id : {Client.DiscordId}")



    # System features :
    elif 'cpu' in queary or 'processor' in queary or 'processing' in queary:
        alice.speak(f"CPU used : {psutil.cpu_percent()}%")


    elif 'battery' in queary:

        if battery is not None:
            alice.speak(
                        f"Battery is {battery.percent}% Charged! " + "And its still in charging." if battery.power_plugged else "")
        else:
            alice.speak(f"Something went wrong {random.choice(ERROR_REPLIES)}. I think you are in desktop")


    elif 'memory' in queary or 'ram' in queary.split():
        alice.speak(f"Memory Used : {psutil.virtual_memory().percent}%")


    elif 'storage' in queary or 'hard drive' in queary:
        alice.speak(
            f"Total Usable Storage : {Client.storage['Total']} GB, Used : {Client.storage['Used']} GB, Free : {Client.storage['Free']} GB")


    elif 'internet' in queary:
        if Client.internet:
            alice.speak(f"Yes {alice.gender}! Internet is connected")
        else:
            alice.speak(
                f"No {alice.gender}! Internet is not connected, But I don't know How I am working without internet, lol")



    elif 'system' in queary or 'computer info' in queary:
        alice.speak(
            f"Its a {Client.computerInfo['System']} {Client.computerInfo['Release']}, A {Client.computerInfo['Machine'][-3:-1]} bit Machine, Version {Client.computerInfo['Version']}, Admin user is {Client.computerInfo['Node name']}. {Client.computerInfo['Processor']} Processor.")


    elif "active" in queary and "pc" in queary or "active" in queary and "computer" in queary:
        try:
            minutes, unit = queary.split("for ")[-1].split()
            if unit == "hours" or unit == "hour":
                minutes = minutes * 60

        except Exception:
            alice.speak(
                f"{alice.gender}! Please Enter how many minutes in numbers, I should keep active your windows machine.")
            minutes = int(input("Enter the number of Minutes :\t"))
        finally:
            alice.speak(
                f"Okay {alice.gender}, I will be keep your windows machine active for next {minutes} Minutes!, "    # noqa
                f"Till that time you can grape a cup of coffee.")
            #
            alice.activePC(minutes)
            del minutes, unit



    # work with git just for Abhinav :-
    elif 'push the code' in queary:
        try:
            alice.speak("Commit and then pushing the code in github repository....")
            login.initialCommit(os.getcwd())
        except Exception:
            alice.speak(f"Something went wrong! {random.choice(ERROR_REPLIES)}")


    elif 'git status' in queary:
        try:
            os.system("git status")
        except Exception:
            alice.speak(f"Something went wrong! {random.choice(ERROR_REPLIES)}")




    # make Alice to speak features
    elif 'say' in queary:
        queary = queary.replace("say ", "")
        alice.speak(queary)


    elif 'spell' in queary:
        alice.speak(f"Enter what I should spell in terminal {alice.gender}!")
        queary = input("Enter what I should spell :\t")
        alice.speak(queary)




    # make Alice to type, Keyboard features

    elif 'open' in queary and 'windows' in queary or "close" in queary and "windows" in queary:
        keyboard.press("win")


    elif "type that" in queary or "send that" in queary:
        queary = queary.split("that")[-1]
        keyactivities.typeWrite(queary)
        keyboard.press("enter")


    elif 'start' in queary and 'typ' in queary:
        alice.speak(f"{alice.gender}! You start to speak I will type that And then to quit plz say quite or close.")
        string = str()
        while "stop" not in string.lower():
            string = alice.takeCommand()
            if string is not None:
                keyactivities.typeWrite(string)
                print(string)



    elif 'record keyboard' in queary:
        alice.speak(
            f"Okay {alice.gender}! Note that, your keyboard activies will be recording till you prese Escap button on your keyboard")
        globals()['keyRecorded'] = keyactivities.keyboardRecord()



    elif 'play the keyboard recording' in queary:
        try:
            globals()["keyRecorded"]
        except NameError:
            alice.speak(f"{alice.gender}! there is no keyboard Activity available till now")
        else:
            alice.speak(
                f"Okay {alice.gender}! Playing the keyboard Activity recording, Note that have to put the cursor where you want to play it.")
            time.sleep(7)
            keyactivities.recordedKeyboardType(globals()["keyRecorded"])




    # local info work with internet :
    elif "what's my location" in queary or 'where am i' in queary or 'where i am' in queary:
        alice.speak(
            f" You are in the Country {Client.location[0]} and near by {Client.location[2]} which is in {Client.location[1]} Region {alice.gender}!")


    elif 'news' in queary:
        topTen = networks.news()
        if topTen is not None:
            for index, articles in enumerate(topTen):
                alice.speak("Moving On " + "a" if index == 0 else "another" + " fresh news!")
                alice.speak(
                    f" {articles['title']}. \n{articles['description']}. " + f" {articles['content']}\n" if articles['content'] is not None else "")
                print(f"For more info... Go to ==>>> {articles['url']}\n\n")

            alice.speak("Thank you for listening")


    elif 'weather report of' in queary:
        place = queary.split("of")[1]
        alice.speak(networks.weather(place))


    elif "temperature" in queary or "weather report" in queary:
        try:
            alice.speak(Client.weatherInfo)
        except:
            alice.speak(random.choice(ERROR_REPLIES))



    # work with lodging file : i.e.work with E commerce websites accounts
    elif 'send' in queary and "email" in queary:
        alice.speak("To whom you want to send the email")
        try:
            userEmail = alice.takeCommand().lower()  # here taking the name as a input and featuring it in our contacts
            for i in Contacts.emails.keys():
                if i.split()[0].lower() == userEmail.split()[0]:
                    userEmail = Contacts.emails[i]
                    break
            else:
                alice.speak(
                    f"{alice.gender}! We didn't got {userEmail} in your contact. Can you tell the email address!")
                userEmail = alice.takeCommand()  # taking email address by speak function
                if userEmail != "None":
                    userEmail = userEmail.replace(" ", "").lower()
                else:
                    alice.speak(
                        f"Sorry {alice.gender}! I didn't get that. Please type the email Address in the terminal!")
                    userEmail = input("Enter the Email Address :\t")
        except Exception:
            alice.speak(f"{random.choice(ERROR_REPLIES)}, Some thing went Wrong")

        alice.speak("What's the subject...")
        subject = alice.takeCommand()
        alice.speak("What's the content...")
        content = alice.takeCommand()
        result = login.sendEmail(userEmail, subject, content)  # noqa

        if result is False:
            alice.speak(f"{random.choice(ERROR_REPLIES)}, Some thing went Wrong")
        else:
            alice.speak(f"Email send successfully to {userEmail}!")



    elif "read book" in queary or "audio book" in queary or "speak pdf" in queary or "read pdf" in queary:
        alice.speak(f"{alice.gender} select the pdf file which you want to make read!")
        audioFile = alice.audioBook()
        if audioFile is None:
            alice.speak(
                "Some thing went wrong!, It might be not a pdf file or the pdf file content will be in images form.")
        try:
            alice.speak(f"{alice.gender}! The audio file had created in that same path with same name.")
            os.startfile(audioFile)
        except Exception:
            pass



    # Launching the software stuffs


    elif "open file explorer" in queary or "this pc" in queary:
        try:
            subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')
            alice.speak("Opening File Explorer...")
        except Exception:
            alice.speak("Some thing went Wrong")



    elif 'open' in queary or 'launch' in queary:
        applicationName = queary.split("open" if "open" in queary else "launch")[-1].split()[0]

        # the second argument is the related path of the folder where all the used or usable software shortcuts are available by the user
        app = workWithFiles.openApplication(applicationName, Client.ApplicationShortcutPath)

        if app is not None:
            alice.speak(f"Launching {app} Application...")
        else:
            # alice.speak(f"Sorry! {applicationName} shortcut didn't got in the Application folder. Please put the shortcuts of all the application do \
            # you use in day to day life in Application folder, Which is in this project folder.")
            pass






if __name__ == "__main__":
    while True:
        command = input("Enter the command for Alice :\t")
        logic(command)

