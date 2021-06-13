import datetime
import os
import time
import keyboard
import random
import sys
import webbrowser

import psutil
from playsound import playsound
import multiprocessing as mp
import subprocess
import pywhatkit

from Assistant.exts import alarm  # noqa
from Assistant.exts import networks  # noqa
from Assistant.constants import Contacts, ERROR_REPLIES, NEGATIVE_REPLIES, POSITIVE_REPLIES, Client  # noqa

from Assistant.utils import login  # noqa
from Assistant.Alice import alice  # noqa
from Assistant.exts import keyactivities  # noqa
from Assistant.exts import workWithFiles  # noqa

__all__ = ["logic"]

# reminder list, contain the multiprocessing object of reminding tasks
side_reminder = list()


# load_dotenv()


def logic(queary: str, taskMultiProcessing: mp.Process = None) -> None:
    """This is the logic of the Program as it will be matching several query and do the programmed task """

    # fetching info from INTERNET_CONNECTION

    if 'search' in queary and 'on wikipedia' in queary:
        try:
            queary = queary.split("search")[-1].split("on wikipedia")[0]
        except ValueError:
            pass
        else:
            alice.speak("Searching Wikipedia...")
            alice.speak(networks.wiki(queary))



    elif 'search' in queary and 'on google' in queary:
        try:
            queary = queary.split("search ")[-1].split("on google")[0]
        except:
            alice.speak("Sir, I didn't get that can you type that in the terminal.")
            queary = input(f"Enter the your Google Search {Client.GENDER}: \t")
        finally:
            alice.speak(f"Fetching the related queary in Google...")
            pywhatkit.search(queary)



    elif "on youtube" in queary and "play" in queary:
        try:
            queary = queary.split("play ")[-1].split("on youtube")[0]
            alice.speak("Fetching Data...")
            pywhatkit.playonyt(queary)
        except Exception:
            alice.speak(f"No results found on {queary} on youtube")  # noqa


    elif "search" in queary and "on youtube" in queary:
        try:
            queary = queary.split("search")[-1].split("on youtube")[0]
            alice.speak("Fetching results...")
            alice.edge(f"https://www.youtube.com/results?search_query={queary}")
        except Exception:
            alice.speak("Sir, I didn't get that can you type that in the interminal.")
            queary = input(f"Enter the your YouTube Search {Client.GENDER}: \t")
            alice.edge(f"https://www.youtube.com/results?search_query={queary}")



    # quiting the program
    elif "bye" in queary or 'kill yourself' in queary or 'quit' in queary:
        alice.speak("That's it, I m quiting....")
        taskMultiProcessing.terminate()
        try:
            for reminder in globals()['side_reminder']:
                reminder.terminate()
        except Exception:
            pass
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


    elif 'your code' in queary:
        alice.speak("Opening Github repository.....")
        alice.edge("github.com/Brodevil/Alice")


    elif 'open github' in queary:
        alice.speak("Opening Github.....")
        alice.edge(f"https://github.com/{Client.USER_GITHUB}")


    elif 'open discord' in queary:
        alice.speak("Opening Discord in Browser.....")
        alice.edge("https://discord.com/channels/@me")


    elif 'open instagram' in queary:
        alice.speak("Opening Instagram.....")
        alice.edge("https://www.instagram.com")


    elif 'open whatsapp' in queary:
        alice.speak("Opening Whatsapp.....")
        alice.edge("https://web.whatsapp.com/")



    elif 'open spotify' in queary:
        alice.speak("Opening Spotify.....")
        alice.edge('https://open.spotify.com/')


    elif 'open twitter' in queary:
        alice.speak("Opening Twitter...")
        alice.edge("https://twitter.com/")


    elif 'pep8' in queary:
        alice.edge("https://www.python.org/dev/peps/pep-0008/")


    elif 'open gmail' in queary or 'show' in queary and 'inbox' in queary:
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
        alice.speak("Shutting down pc....")
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


    elif 'close this website' in queary or 'close the webpage' in queary:
        keyboard.press_and_release("ctrl+w")



    # reminder        
    elif 'remind me after' in queary or "wake up me after" in queary:
        queary = queary.split("remind me after " if 'remind me after' in queary else "wake up me after")[1]
        magnitude = int(queary.split()[0])
        unit = queary.split()[1]
        alice.speak(f"Okay {Client.GENDER}! I will be reminding you after {magnitude} {unit}!")
        try:
            # if reason is there, then it will going to replace the sentence "I will back to my work again" to "you will back to your work again"
            pourpose = queary.split("so that ")[1].replace("i", "you").replace('my', 'your')
        except Exception:  # the user can give the reason as a option
            pourpose = "You didn't told the pourpose for reminding, Its might be some thing secret \U0001F923"

        globals()['side_reminder'].append(mp.Process(target=alarm.reminderAlarm, args=(magnitude, unit, pourpose)))
        globals()['side_reminder'][-1].start()





    # music
    elif "play" in queary and "music" in queary or "song" in queary and "music" in queary:
        music = os.listdir(Client.MUSIC_DIRECTORY)
        os.startfile(os.path.join(Client.MUSIC_DIRECTORY, random.choice(music)))
        alice.speak("Playing Music...")


    elif 'brown munde' in queary:  # this function is just for my self i.e. For Abhinav personal songs
        try:
            os.startfile(
                r"E:\ADMIN\Music\BRODEVIL\Hollywood_song\sunna_hai_kya\BROWN MUNDE.mp3")
        except FileNotFoundError:
            pass


    elif "play my" in queary and "song" in queary or "play my" in queary and "music" in queary:
        if Client.FAVOURITE_MUSIC is not None:
            coolMusic = mp.Process(target=playsound, args=(Client.FAVOURITE_MUSIC,))
            coolMusic.start()
        else:
            alice.speak(f"{Client.GENDER}! Please run the documentation of Alice and then ")


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
        alice.speak(f"Hello {Client.GENDER}! {random.choice(POSITIVE_REPLIES)}")


    elif 'hello' in queary or queary == "alice":
        alice.speak(f"Hello {Client.GENDER}! how may I can help you.")


    elif 'good' in queary and 'afternoon' in queary or 'evening' in queary or 'morning' in queary:
        wish = alice.goodWish
        if wish.lower() in queary:
            alice.speak(f"{wish} {Client.GENDER}!")
        else:
            alice.speak(f"{Client.GENDER}! Its {wish.split()[1]} Right now!")


    elif "time" in queary:
        alice.speak(f"Its {datetime.datetime.now().strftime('%I:%M %p')} {Client.GENDER}!")


    elif "date" in queary:
        alice.speak(
            f"Its {datetime.datetime.now().day} of {datetime.date(1900, datetime.datetime.now().month, 1).strftime('%B')} {datetime.datetime.now().year}")


    elif 'who are you' in queary or "introduction" in queary:
        alice.INTRO()


    elif "what's my name" in queary or "what is my name" in queary or "who i am" in queary:
        alice.speak(f"You are {alice.name} {Client.GENDER}!, But why did you are asking this?")


    elif "to kaise hain aap log" in queary:  # just for ha
        alice.speak("Hum thik hai bhai, Tum batao!..")


    elif "yalghar" in queary:
        alice.edge("https://www.youtube.com/watch?v=zzwRbKI2pn4")


    elif 'voices' in queary or "change your voice" in queary:
        alice.severalVoices(voicesId=Client.VOICES)


    elif 'pause' in queary or "stop for" in queary or "sleep for" in queary:
        try:
            period = int(queary.split("for")[-1].split()[0])
        except ValueError:
            try:
                alice.speak(
                    f"Sorry {Client.GENDER}! I didn't get that, Can you type the number of minutes I should sleep for in terminal ")
                period = int(input("Enter the number of minutes I should sleep :\t"))
            except ValueError:
                alice.speak("Wrong Input, I should be a number. Try again")
                return

        alice.speak(f"Okay {Client.GENDER}! I will be wake up after {period} minutes.")  # noqa
        time.sleep(60 * period)

        alice.speak(f"{alice.goodWish} {Client.GENDER}!, I wake up after {period} minutes, Lets back to work.")
        del period



    elif 'thank you' in queary or 'thanks' in queary:
        alice.speak(f"Your most welcome {Client.GENDER}!")


    elif 'how are you' in queary:
        alice.speak("I am quite fine sir, What about you ?")


    elif 'alice info' in queary or 'your info' in queary:
        alice.speak(
            f"I am written in Python by {Client.AUTHOR}Sir!. To CONTACT him you can email at ({Client.CONTACT}), Check out his GitHub Profile You will know more about my sir")
        print(
            f"Alice : Mr. Abhinav's  Email:{Client.CONTACT}. Github link :{Client.ALICE_GITHUB_REPOSITORY}. Discord Id : {Client.DISCORD_ID}")



    # System features :
    elif 'cpu' in queary or 'processor' in queary or 'processing' in queary:
        alice.speak(f"CPU used : {psutil.cpu_percent()}%")


    elif 'battery' in queary:
        try:
            battery = psutil.sensors_battery()
        except Exception:
            battery = None

        if battery is not None:
            alice.speak(
                f"Battery is {Client.BATTERY_STATUS}% Charged!, " + "And its still in charging." if Client.BATTERY_PLUGGED else "",
                f"{Client.GENDER}! I guess you should plug out the charger now!" if Client.BATTERY_STATUS >= 95 and Client.BATTERY_PLUGGED else "",
                f"{Client.GENDER}! Its very low battery, Please plug in to charge" if Client.BATTERY_STATUS >= 30 and not Client.BATTERY_PLUGGED else "")
        else:
            alice.speak(f"Something went wrong {random.choice(ERROR_REPLIES)}. I think you are in desktop")


    elif 'memory' in queary or 'ram' in queary.split():
        alice.speak(f"Memory Used : {psutil.virtual_memory().percent}%")


    elif 'storage' in queary or 'hard drive' in queary:
        alice.speak(
            f"Total Usable Storage : {Client.STORAGE['Total']} GB, Used : {Client.STORAGE['Used']} GB, Free : {Client.STORAGE['Free']} GB")


    elif "internet speed" in queary or "network speed" in queary or "download" in queary and 'speed' in queary or "upload" in queary and 'speed' in queary:
        alice.speak("Wait a while sir, Internet speed test might take time")
        speed = networks.internet_speed()
        alice.speak(f"Internet speed from nearest Server : {speed}")
        del speed

    elif "internet info" in queary or "network info" in queary:
        try:
            alice.speak("Internet is connected! with", Client.NETWORK)
        except NameError:
            alice.speak(random.choice(ERROR_REPLIES), "Some thing went wrong!")


    elif 'internet' in queary:
        if Client.INTERNET_CONNECTION:
            alice.speak(f"Yes {Client.GENDER}! Internet is connected")
        else:
            alice.speak(
                f"No {Client.GENDER}! Internet is not connected, But I don't know How I am working without INTERNET CONNECTION, lol\nActive INTERNET CONNECTION is needed to run Alice")


    elif 'system' in queary or 'computer info' in queary:
        alice.speak(
            f"Its a {Client.COMPUTER_INFO['System']} {Client.COMPUTER_INFO['Release']}, A {Client.COMPUTER_INFO['Machine'][-3:-1]} bit Machine, Version {Client.COMPUTER_INFO['Version']}, Admin user is {Client.COMPUTER_INFO['Node name']}. {Client.COMPUTER_INFO['Processor']} Processor.")


    elif "active" in queary and "pc" in queary or "computer" in queary:
        try:
            minutes, unit = queary.split("for ")[-1].split()
            if unit == "hours" or unit == "hour":
                minutes = minutes * 60
        except Exception:
            alice.speak(
                f"{Client.GENDER}! Please Enter how many minutes in numbers, I should keep active your windows machine.")
            minutes = int(input("Enter the number of Minutes :\t"))
        finally:
            alice.speak(
                f"Okay {Client.GENDER}, I will be keep your windows machine active for next {minutes} Minutes!, "  # noqa
                f"Till that time you can grape a cup of coffee.")
            #
            alice.activePC(minutes)
            del minutes, unit



    # work with git just for Abhinav :-
    elif 'push the code' in queary or "git commit" in queary:
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
    elif 'say' in queary or 'speak' in queary:
        queary = queary.split("say" if 'say' in queary else "speak")[-1]
        alice.speak(queary)

    elif 'start following m' in queary:             # m as be me or my voice
        alice.speak("I will be now following your while repeating yourself, say stop to quit this")
        sentence = str()
        while "stop" not in sentence and "quit" not in sentence and "break" not in sentence:
            if sentence != "None":
                alice.speak(sentence)
            sentence = alice.takeCommand()
        del sentence


    elif 'spell' in queary:
        alice.speak(f"Enter what I should spell in terminal {Client.GENDER}!")
        queary = input("Enter what I should spell :\t")
        alice.speak(queary)



    # make Alice to type, Keyboard features

    elif 'open' in queary and "windows" in queary or "close" in queary and 'windows' in queary:
        keyboard.press_and_release("win")


    elif 'close this applications' in queary:
        keyboard.press_and_release("alt+f4")

    elif "type that" in queary or "send that" in queary:
        queary = queary.split("that")[-1]
        keyactivities.typeWrite(queary)
        keyboard.press("enter")


    elif 'start' in queary and 'typ' in queary:
        alice.speak(f"{Client.GENDER}! You start to speak I will type that And then to quit plz say quite or close.")
        string = str()
        while "stop" not in string.lower() and 'quit' not in string.lower() and 'close' not in string.lower():
            if string != "None":
                keyactivities.typeWrite(string)
            string = alice.takeCommand()
        del string


    elif 'record keyboard' in queary:
        alice.speak(
            f"Okay {Client.GENDER}! Note that, your keyboard actives will be recording till you press Escape button on your keyboard")
        globals()['keyRecorded'] = keyactivities.keyboardRecord()



    elif 'play the keyboard recording' in queary:
        try:
            globals()["keyRecorded"]
        except NameError:
            alice.speak(f"{Client.GENDER}! there is no keyboard Activity available till now")
        else:
            alice.speak(
                f"Okay {Client.GENDER}! Playing the keyboard Activity recording, Note that have to put the cursor where you want to play it.")
            time.sleep(7)
            keyactivities.playKeyboard(globals()["keyRecorded"])




    # local info work with INTERNET_CONNECTION :
    elif "what's my location" in queary or 'where am i' in queary or 'where i am' in queary:
        alice.speak(
            f" You are in the Country {Client.LOCATION[0]} and near by {Client.LOCATION[2]} which is in {Client.LOCATION[1]} Region {Client.GENDER}!")


    elif 'news' in queary:
        topTen = login.news()
        if topTen is not None:
            for index, articles in enumerate(topTen):
                alice.speak("Moving On " + "a" if index == 0 else "another" + " fresh news!")
                alice.speak(
                    f" {articles['title']}. \n{articles['description']}. " + f" {articles['content']}\n" if articles[
                                                                                                                'content'] is not None else "")
                print(f"For more info... Go to ==>>> {articles['url']}\n\n")

            alice.speak("Thank you for listening")
        else:
            alice.speak(f"{random.choice(ERROR_REPLIES)}, Check your INTERNET_CONNECTION connection {Client.GENDER}!")


    elif 'weather report of' in queary:
        place = queary.split("of")[1]
        alice.speak(networks.weather(place))


    elif "temperature" in queary or "weather report" in queary:
        try:
            alice.speak(Client.WEATHER_INFO)
        except:
            alice.speak(random.choice(ERROR_REPLIES))



    # work with lodging file : i.e.work with E commerce websites accounts
    elif 'send' in queary and "email" in queary:
        alice.speak("To whom you want to send the email")
        try:
            userName = alice.takeCommand().lower()  # here taking the name as a input and featuring it in our contacts
            for i in Contacts.emails.keys():
                if userName.split()[0] in i.lower().split():
                    userEmail = Contacts.emails[i]
                    break
            else:
                alice.speak(
                    f"Sorry {Client.GENDER}! I didn't got {userName} in your contacts. Please type the email Address in the terminal!")
                userEmail = input("Enter the Email Address :\t")

            alice.speak("What's the subject...")
            subject = alice.takeCommand()
            alice.speak("What's the content...")
            content = alice.takeCommand()
            result = login.sendEmail(userEmail, subject, content)

            if result is False:
                alice.speak(f"Some thing went wrong! Unable to send Email")
            else:
                alice.speak(f"Email send successfully to {userEmail}!")

        except Exception:
            alice.speak(f"{random.choice(ERROR_REPLIES)}, Some thing went Wrong")



    elif "read book" in queary or "audio book" in queary or "speak pdf" in queary or "read pdf" in queary:
        alice.speak(f"{Client.GENDER} select the pdf file which you want to make read!")
        audioFile = alice.audioBook()
        if audioFile is not None:
            try:
                alice.speak(f"{Client.GENDER}! The audio file had created in that same path with same name.")
                os.startfile(audioFile)
            except FileNotFoundError:
                pass



    # Launching the software stuffs

    elif "open file explorer" in queary or "this pc" in queary:
        subprocess.Popen('explorer')
        alice.speak("Opening File Explorer...")
        alice.speak("Some thing went Wrong")


    elif 'open' in queary or 'launch' in queary:
        applicationName = queary.split("open" if "open" in queary else "launch")[1]
        # the second argument is the related path of the folder where all the used or usable software shortcuts are available by the user
        app = workWithFiles.openApplication(applicationName, Client.APPLICATIONS_SHORTCUTS_PATH)
        if app is not None:
            alice.speak(f"Launching {app} Application...")
        else:
            # alice.speak(f"Sorry! {applicationName} shortcut didn't got in the Application folder. Please put the shortcuts of all the application do \
            # you use in day to day life in Application folder, Which is in this project folder.")
            pass


if __name__ == '__main__':
    while True:
        command = input()
        logic(command)
