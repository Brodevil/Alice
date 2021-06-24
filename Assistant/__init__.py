import datetime
import os
import time
import keyboard
import random
import sys
import pyjokes
from tkinter import Tk

import psutil
from playsound import playsound
import multiprocessing as mp
import pywhatkit
from tkinter.filedialog import askopenfilename
from pywikihow import search_wikihow
import screen_brightness_control as sbc

from Assistant.exts import alarm
from Assistant.exts import networks
from Assistant.constants import Contacts, ERROR_REPLIES, NEGATIVE_REPLIES, POSITIVE_REPLIES, WELCOME, Client
from Assistant.exts.visual_media import VisualMedia

from Assistant.utils import login
from Assistant.Alice import alice
from Assistant.exts import keyactivities
from Assistant.exts import workWithFiles

__all__ = ["logic"]

# reminder & Alarm list, contain the multiprocessing object of reminding tasks
side_reminder = list()
side_alarm = list()




def logic(queary: str) -> None:
    """This is the logic of the Program as it will be matching several query and do the programmed task """

    # ---------------------- fetching info from INTERNET ---------------------------------------
    if 'search' in queary and 'on wikipedia' in queary:
        try:
            queary = queary.split("search")[-1].split("on wikipedia")[0]
        except ValueError:
            pass
        else:
            alice.speak("Searching Wikipedia...")
            alice.speak(networks.wiki(queary))



    elif 'search' in queary and 'on google' in queary:
        queary = queary.split("search ")[-1].split("on google")[0]
        if "type" in queary:
            alice.speak(f"{Client.GENDER}! You can ofcourse type the message on your own in the terminal!")
            queary = input(f"Enter the your Google Search {Client.GENDER}: \t")

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
        queary = queary.split("search")[-1].split("on youtube")[0]
        if "type" in queary:
            alice.speak(f"{Client.GENDER}! You can ofcourse type the message on your own in the terminal!")
            queary = input(f"Enter the your YouTube Search {Client.GENDER}: \t")

        alice.speak("Fetching results...")
        alice.edge(f"https://www.youtube.com/results?search_query={queary}")



    elif 'search' in queary:  # this is just a quick google search, return the result
        queary = queary.replace("search ", "")
        alice.speak(networks.quick_google_search(queary))


    elif 'how to ' in queary:
        queary = queary.split("how to ")[-1]
        steps = search_wikihow(queary, max_results=1)
        steps[0].print()
        alice.speak(steps[0].summary, _print=False)



    # ---------------------------------------- quiting the program -----------------------------------
    elif "bye" in queary or 'kill yourself' in queary or 'quit' in queary:
        alice.speak("That's it, I m quiting....")

        alice.remind_daily_task = False         # terminate the daily task reminder thread
        try:
            # terminating all the side alarms while closing alice
            for reminder in globals()['side_reminder']:
                reminder.terminate()
                
            # terminating all the side alarms while closing alice
            for reminder in globals()["side_alarm"]:
                reminder.terminate()
        except Exception:
            pass

        sys.exit(0)



    # --------------------------------------- Opening websites -------------------------------------------
    elif 'open youtube studio' in queary:
        alice.speak("Opening youtube studio...")
        alice.edge("https://studio.youtube.com/")


    elif 'open youtube' in queary:
        alice.speak("Opening youtube...")
        alice.edge("https://www.youtube.com")


    elif 'open google' in queary:
        alice.speak("Opening google...")
        alice.edge("https://www.google.com")


    elif 'open stack overflow' in queary:
        alice.speak("Opening stackoverflow...")
        alice.edge("https://stackoverflow.com")

    elif 'open krunker' in queary:
        alice.speak("Opening Krunker...")
        alice.edge("https://https://krunker.io/")

    elif 'your code' in queary:
        alice.speak("Opening Github repository.....")
        alice.edge("https://github.com/Brodevil/Alice")


    elif 'open github' in queary:
        alice.speak("Opening Github.....")
        alice.edge(f"https://github.com/{Client.USER_GITHUB}")


    elif 'open discord' in queary:
        alice.speak("Opening Discord in Browser.....")
        alice.edge("https://discord.com/channels/@me")


    elif 'open instagram' in queary:
        alice.speak("Opening Instagram.....")
        alice.edge("https://www.instagram.com")


    elif 'open facebook' in queary:
        alice.speak("Opening FaceBook...")
        alice.edge("https://www.facebook.com")


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




    # --------------------------------------------work with GUI or windows :-----------------------------------------
    elif 'desktop' in queary:
        keyboard.press_and_release("win+d")


    elif 'lock pc' in queary or "lock the pc" in queary:
        os.system("rundll32.exe user32.dll, LockWorkStation")  # noqa
        sys.exit(0)


    elif 'shutdown pc' in queary:
        try:
            os.startfile(r"C:\Windows\System32\SlideToShutDown.exe")
        except FileNotFoundError:
            os.system("shutdown /s /t 1")

        finally:
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


    elif 'volume' in queary:
        if queary.isalnum():
            rate = sum([_ for _ in queary.split() if _.isnumeric()])
        else:
            rate = 10

        if 'up' in queary or 'increase' in queary:
            keyactivities.volume_control(how_much=rate, increase=True)

        elif 'down' in queary or 'decrease' in queary:
            keyactivities.volume_control(how_much=rate, decrease=True)


    elif 'mute' in queary:
        keyactivities.volume_control(how_much=0, mute=True)


    elif 'screen' in queary and 'bright' in queary:
        try:
            if queary.isalnum():
                rate = [_ for _ in queary.split() if _.isnumeric()][0]
            else:
                rate = 10

            current_brightness = sbc.get_brightness()

            if 'increase' in queary or 'more' in queary:
                sbc.set_brightness(current_brightness + rate)

            elif 'decrease' in queary or 'less' in queary:
                sbc.set_brightness(current_brightness - rate)

        except Exception:
            alice.speak(random.choice(ERROR_REPLIES), "Something went Wrong!")




    # ----------------------- make Alice to type, Keyboard features, working with keyboards------------------------------

    elif 'close this website' in queary or 'close the webpage' in queary:
        keyboard.press_and_release("ctrl+w")

    elif 'open' in queary and "windows" in queary or "close" in queary and 'windows' in queary:
        keyboard.press_and_release("win")

    elif 'close this applications' in queary:
        keyboard.press_and_release("alt+f4")


    elif "type" in queary:
        queary = queary.split("type")[-1]
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



    elif 'play' in queary and 'keyboard' in queary and 'record':  # play my recorded keyboard/play keyboard recording/etc
        try:
            globals()['keyRecorded'] = globals()['keyRecorded']  # noqa
        except NameError:
            alice.speak(f"{Client.GENDER}! there is no keyboard Activity available till now")
        else:
            alice.speak(
                f"Okay {Client.GENDER}! Playing the keyboard Activity recording, Note that have to put the cursor where you want to play it.")
            time.sleep(3)
            keyactivities.playKeyboard(globals()['keyRecorded'])


    elif 'record' in queary and 'keyboard':
        alice.speak(
            f"Okay {Client.GENDER}! Note that, your keyboard activities will be recording till you press Escape button on your keyboard")
        globals()['keyRecorded'] = keyactivities.keyboardRecord()





    # -------------------------------------Music---------------------------------------------------
    elif "play" in queary and "music" in queary or "song" in queary and "music" in queary:
        music = os.listdir(Client.MUSIC_DIRECTORY)
        music = os.path.join(Client.MUSIC_DIRECTORY, random.choice(music))
        if music.endswith(".mp3"):
            os.startfile(music)
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




    # ---------------------------------------  working with files : ---------------------------------------
    elif 'delete unwanted files' in queary:
        alice.speak("Deleting unwanted files...")
        workWithFiles.deleteUnwantedFiles()


    elif 'alice path' in queary:
        os.startfile("")


    # --------------------------------------- Natural Talks/ Fun commands : ----------------------------
    elif 'testing' in queary or 'is i am audio able' in queary:
        alice.speak(f"Hello {Client.GENDER}! {random.choice(POSITIVE_REPLIES)}")

    elif 'hello' in queary or queary == "alice" or "your" in queary and "name" in queary:
        alice.speak(
            f"{'Hello' if random.randint(1, 2) == 1 else alice.goodWish} {Client.GENDER}! I am Alice, how may I can help you.")


    elif 'good afternoon' in queary or 'good evening' in queary or 'good morning' in queary:
        wish = alice.goodWish
        if wish.lower() in queary:
            alice.speak(f"{wish} {Client.GENDER}!")
        else:
            alice.speak(f"{Client.GENDER}! Its {wish.split()[1]} Right now!")


    elif 'time of' in queary or "time in" in queary:
        place = queary.split("of " if "of" in queary else "in ")[-1].split()[0]
        alice.speak(f"The Current Time Of {place} is {networks.quick_google_search(f'Current time of {place}')}")


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


    elif 'thank you' in queary or 'thanks' in queary:
        alice.speak(random.choice(WELCOME))


    elif 'how are you' in queary:
        alice.speak("I am quite fine sir, What about you ?")


    elif 'alice info' in queary or 'your info' in queary:
        alice.speak(
            f"I am written in Python by {Client.AUTHOR}Sir!. To CONTACT him you can email at ({Client.CONTACT}), Check out his GitHub Profile You will know more about my sir")
        print(
            f"Alice : Mr. Abhinav's  Email:{Client.CONTACT}. GitHub Profile :{Client.ALICE_GITHUB_REPOSITORY}. Discord Id : {Client.DISCORD_ID}")


    elif 'idle mood' in queary:
        os.startfile(os.path.join(Client.ALICE_PATH, "Assistant\\resources\\images\\Ribbons.scr"))



    # ------------------------------------- Work with System, Info, features :------------------------------------------
    elif 'cpu' in queary or 'processor' in queary or 'processing' in queary:
        alice.speak(f"CPU used : {psutil.cpu_percent()}%")


    elif 'battery' in queary:
        try:
            battery = psutil.sensors_battery()
        except Exception:
            battery = None

        if battery is not None:
            alice.speak(f"Battery is {Client.BATTERY_STATUS}% Charged! ",
                        "And its still in charging. " if Client.BATTERY_PLUGGED else " ")
            if Client.BATTERY_STATUS >= 95 and Client.BATTERY_PLUGGED:
                alice.speak(f"{Client.GENDER}! I guess you should plug out the charger now!")

            elif Client.BATTERY_STATUS <= 35 and not Client.BATTERY_PLUGGED:
                alice.speak(f"{Client.GENDER}! You should Plug in the changer because Currently its very low battery!")
        else:
            alice.speak(f"Something went wrong {random.choice(ERROR_REPLIES)}. I think you are in desktop")


    elif 'memory' in queary or 'ram' in queary.split():
        alice.speak(f"Memory Used : {psutil.virtual_memory().percent}%")


    elif 'storage' in queary or 'hard drive' in queary:
        alice.speak(
            f"Total Usable Storage : {Client.STORAGE['Total']} GB, Used : {Client.STORAGE['Used']} GB, Free : {Client.STORAGE['Free']} GB")


    elif "internet speed" in queary or "network speed" in queary or "download" in queary and 'speed' in queary or "upload" in queary and 'speed' in queary:
        alice.speak("Wait a while sir, Internet speed test might take time")
        try:
            speed = speed  # noqa
        except NameError:
            speed = networks.internet_speed()
        finally:
            alice.speak(f"Internet speed from nearest Server : {speed}")



    elif "internet" in queary or "network" in queary:
        try:
            if Client.INTERNET_CONNECTION:
                alice.speak(f"Internet is connected! with {Client.NETWORK}")
            else:
                alice.speak(
                    f"No {Client.GENDER}! Internet is not connected, But I don't know How I am working without INTERNET CONNECTION, lol\nActive INTERNET CONNECTION is needed to run Alice")
        except NameError:
            alice.speak(random.choice(ERROR_REPLIES), "Some thing went wrong!")



    elif 'ip' in queary and 'address' in queary:
        alice.speak(f"{Client.GENDER}! You Current IPv4 Address is : {networks.ip_address()}")


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



    # ------------------------------------- work with git just for Abhinav :-----------------------------
    elif 'push the code' in queary or "git commit" in queary:
        alice.speak("Commit and then pushing the code in github repository....")
        login.initialCommit(os.getcwd())


    elif 'git status' in queary:
        os.system("git status")



    # ---------------------------------- make Alice to speak, Test to Speech features --------------------------------
    elif 'speak' in queary:
        queary = queary.split("say" if 'say' in queary else "speak")[-1]
        alice.speak(queary)


    elif 'start following m' in queary or "repeat my self" in queary:  # start following me or my voice both starts from m
        alice.speak("I will be now following your while repeating yourself, say stop to quit this")
        sentence = str()
        while "stop" not in sentence and "quit" not in sentence and "break" not in sentence:
            if sentence != "None":
                alice.speak(sentence)
            sentence = alice.takeCommand()
        del sentence


    elif 'spell' in queary and 'text' in queary or 'speak' in queary and 'text' in queary:
        alice.speak(f"Enter what I should spell in terminal {Client.GENDER}!")
        queary = input("Enter what I should spell :\t")
        alice.speak(queary)


    elif "read book" in queary or "audiobook" in queary or "speak pdf" in queary or "read pdf" in queary:
        alice.speak(f"{Client.GENDER} select the pdf file which you want to make read!")

        root = Tk()
        root.withdraw()
        root.update()
        pdfPath = askopenfilename(mode='r', defaultextension=".pdf")
        root.destroy()

        audioFile = alice.audioBook(pdfPath)
        if audioFile is None:
            alice.speak("Something Went Wrong!")


    elif "how many voices" in queary:
        alice.severalVoices(voicesId=Client.VOICES)


    elif 'change' in queary and "voice" in queary:
        if Client.VOICE <= len(Client.VOICES) - 1:
            Client.VOICE += 1
        else:
            Client.VOICE = 1
        alice.speak(f"Hey {Client.GENDER}! How did you like this voice, Is this okay.")


    elif 'voice' in queary and 'speed' in queary:
        alice.takeCommand(f"Current speed is {Client.VOICE_RATE}")

        if 'increase' in queary or 'more' in queary or "add" in queary:
            rate = alice.takeCommand("Please tell How much should I increase the Voice Rate!")
        
        elif 'decrease' in queary or "less" in queary and "slow":
            rate = alice.takeCommand("Please tell How much should I decrease my Voice Rate!")

        else:
            return 
        
        if not rate.isalnum():
            alice.speak(f"{Client.GENDER}! You should just speak number for Voice Rate for changes")
            return
        
        rate = sum([_ for _ in rate.split() if _.isnumeric()])
        Client.VOICE_RATE += rate

        alice.speak("How did you like this speed!")               

    # ------------------------------------------ local info work with INTERNET and APIs -----------------------------
    elif "my location" in queary or 'where am i' in queary or 'where i am' in queary:
        alice.speak(
            f" You are in the Country {Client.LOCATION[0]} and near by {Client.LOCATION[2]} which is in {Client.LOCATION[1]} Region {Client.GENDER}!")
        alice.speak(f"{Client.GENDER}! You can also ask for exact location")


    elif 'exact location' in queary:
        alice.speak(f"Showing your Exact location {Client.GENDER}!")
        alice.edge("https://www.google.com/maps/search/my+locations/")


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


    elif "weather report" in queary:
        alice.speak(Client.WEATHER_INFO)


    elif 'temperature' in queary:
        place = queary.split("of ")[-1].split()[0] if "of" in queary else ""
        temp = networks.quick_google_search(f'Current temperature {place}')
        alice.speak(f"The Current Temperature " + f"of {Client.CITY}" if not len(place) else "" + f" is {temp}")


    elif 'joke' in queary:
        alice.speak("Alright, I will make a joke that definitely make you laugh!")
        alice.speak(f"{pyjokes.get_joke()}\n Ha Ha Ha")


    elif 'corona' in queary:
        country = alice.takeCommand("Please tell the country name which you want to get the corona cases")
        result = networks.corona_virus(country)
        alice.speak(
            f"The Total cases in {country} is {result[0]}, Total {result[1]} death cases and {result[2]} recovered cases")



    # ------------------------------------------ reminders & Alarms ----------------------------------------------
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


    elif 'alarm' in queary:
        alice.speak(f"{Client.GENDER}! Please enter the alarm time in 24 hour format in terminal!")
        alarm_time = input("Enter the Alarm time in 24 hour Format : \t")
        if ":" not in alarm_time:
            alice.speak(f"")
        alice.speak(f"Successfully set the Alarm of {alarm_time}, remind you soon {Client.GENDER}")
        globals()["side_alarm"].append(mp.Process(target=alarm.alarm, args=(alarm_time, )))
        globals()["side_alarm"][-1].start()



    # --------------------------------- work with login folder : i.e.work with E commerce websites accounts ------------
    elif 'send' in queary and "email" in queary:
        try:
            userName = alice.takeCommand("To whom you want to send the email").lower()
            for i in Contacts.emails.keys():
                if userName.split()[0] in i.lower().split():
                    userEmail = Contacts.emails[i]
                    if userEmail is None:
                        alice.speak(
                            f"{Client.GENDER}! {i}'s Email Address had not been there in your contact Exel file!")
                        return
                    break
            else:
                alice.speak(
                    f"Sorry {Client.GENDER}! I didn't got {userName} in your contacts. Please type the email Address in the terminal!")
                userEmail = input("Enter the Email Address :\t")

            subject = alice.takeCommand("What's the subject...")

            content = alice.takeCommand("What's the content...")

            if content == "None" or "let me" in content and "typ":
                alice.speak(
                    "Sorry, I didn't get that!, Can you please type the message in the terminal!" if content == "None" else f"Okay {Client.GENDER}! You can ofcourse type the message on your own in the terminal!")
                content = input(f"Enter the Message/Content of the Email {Client.GENDER}! : \t")

            result = login.sendEmail(userEmail, subject, content)

            if result is False:
                alice.speak(f"Some thing went wrong! Unable to send Email")
            else:
                alice.speak(f"Email send successfully to {userEmail}!")

        except Exception:
            alice.speak(f"{random.choice(ERROR_REPLIES)}, Some thing went Wrong")



    elif 'whatsapp' in queary and 'send' in queary:
        try:
            userName = alice.takeCommand("To whom you want to send the Whatsapp Message!")
            for _ in Contacts.contactNumber.keys():
                if userName.split()[0] in _.split():
                    contact_num = Contacts.contactNumber[_]
                    if contact_num is None:
                        alice.speak(f"{Client.GENDER}! {_}'s Phone number had not been there in your contact Exel file!")
                        return
                    break

            else:
                alice.speak(
                    f"{Client.GENDER}! We didn't got {userName} in your contacts Exel file. Enter his phone number including  (+ and country code)")
                contact_num = input("Enter the Contact Number including Country code  :\t")

            if "+" not in contact_num:
                alice.speak(
                    f"Sorry {Client.GENDER}! The contact number is invalid, Format should be like (+ and country Code and numbers)")
                return

            content = alice.takeCommand("What's the message!")

            if content == "None" or "let me" in content and "typ":
                alice.speak(
                    "Sorry, I didn't get that!, Can you please type the message in the terminal!" if content == "None" else f"Okay {Client.GENDER}! You can ofcourse type the message on your own in the terminal!")
                contact_num = input(f"Enter the Message/Content of the Email {Client.GENDER}! : \t")

            pywhatkit.sendwhatmsg_instantly(contact_num.replace(" ", ""), content, wait_time=1)
            time.sleep(8)
            keyboard.press("enter")
        except Exception:
            alice.speak(f"{random.choice(ERROR_REPLIES)}, Some thing went Wrong")
        else:
            alice.speak(f"Whatsapp Messages SuccessFully Send to {contact_num}")




    # ----------------------------  Launching the software stuffs --------------------------------------------------

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


    elif 'close' in queary:
        queary = queary.split("close ")[-1]
        alice.closeApps(application=queary)


    # --------------------------------------------- Media -------------------------------------------------------------

    elif "screenshot" in queary:
        name = alice.takeCommand("By which name I should save the file!")
        if 'default' in name:
            name = None
        VisualMedia.screen_shorts(name=name)
        alice.speak("ScreenShot Saved! In Media folder of Alice Project.")
