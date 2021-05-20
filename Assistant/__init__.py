import datetime
import os
import time
import keyboard
import random
import sys 

import psutil
import smtplib
import subprocess
from dotenv import load_dotenv


from Assistant.exts import reminder                                                                         # noqa
from Assistant.exts import networks                                                                         # noqa
from Assistant.constants import Contacts, ERROR_REPLIES, NEGATIVE_REPLIES, POSITIVE_REPLIES, Client         # noqa

from Assistant.exts import login                                                                            # noqa
from Assistant.Alice import alice                                                                           # noqa
from Assistant.exts import keyactivities                                                                    # noqa
from Assistant.exts import workWithFiles                                                                    # noqa



__all__ = ("logic")

# load_dotenv()


def logic(queary):
    """This is the logic of the Program as it will be matching several queary and do the programmed task """


    # fetching info from intrnet
    if 'wikipedia' in queary:
            alice.speak("Searching Wikipedia...")
            queary = queary.replace("wikipedia", "")
            alice.speak(networks.wiki())


    elif 'search' in queary:
        queary = queary.replace("search", "")
        alice.speak(f"Searching {queary} in Google")
        queary = queary.replace(" ", "%20")
        alice.edge(f"https://www.google.com/search?q={queary}")
        


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
        alice.edge("youtube.com")
    
    
    elif 'open google' in queary:
        alice.speak("Opening google...")
        alice.edge("google.com")
    
    
    elif 'open stack overflow' in queary:
        alice.speak("Opening stackoverflow...")
        alice.edge("stackoverflow.com")
    
    
    elif 'reveal your code' in queary:
        alice.speak("Opening Github repositor.....")
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
        alice.edge("https://www.python.org/dev/peps/pep-0008/")   \
    

    # work with GUI or windows :
    elif 'desktop' in queary:
        keyboard.press_and_release("win+d")


    elif 'lock pc' in queary or "lock the pc" in queary:   
        os.system("rundll32.exe user32.dll, LockWorkStation")
        sys.exit(0)


    elif 'shutdown pc' in queary:
        os.startfile(r"C:\Windows\System32\SlideToShutDown.exe")
        alice.speak("Shuting down pc....")
        time.sleep(2)
        keyboard.press_and_release("enter")


    elif 'restart pc' in queary:
        os.system("Shutdown.exe -r -t 00")


    elif 'switch tab' in queary:
        keyboard.press_and_release("alt+tab")


    elif 'switch window right' in queary:
        keyboard.press_and_release("ctrl+win+right")


    elif 'switch window left' in queary:
        keyboard.press_and_release("ctrl+win+left")



    # Launching the softwares stuffs

    elif 'open visual studio code' in queary:
        try:
            alice.speak("Opening vs code...")
            os.startfile(r"E:\Programe File (x83)\Microsoft VS Code\Code.exe")
        except Exception:
            alice.speak("Some thing went wrong! It might be a wrong path or you had not Installed that application")


    elif 'open sublime text' in queary:     # this command is also just for Abhinav, as He have sublime text
        try:
            alice.speak("Opening Sublime Text")
            os.startfile(r"E:\Programe File (x83)\Sublime Text 3\sublime_text.exe")
        except Exception:
            alice.speak("Some thing went wrong! It might be a wrong path or you had not Installed that application")


    elif "open discord application" in queary:
        try:
            os.startfile(r"E:\Programe File (x83)\Discord\app-0.0.309\Discord.exe")
            alice.speak("Opening Discord Application")
        except Exception:
            alice.speak("Some thing went wrong! It might be a wrong path or you had not Installed that application")
        
    
    elif "open file explorer" in queary:
        try:
            subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')
            alice.speak("Opening File Explorer...")
        except Exception:
            alice.speak("Some thing went Wrong")


    elif "open rapid typing" in queary:
        try:
            os.startfile(r"E:\Programe File (x83)\Typing Course\RapidTyping.exe")
            alice.speak("Opening Rapid Typing...")
        except Exception:
            alice.speak("Some thing went wrong! It might be a wrong path or you had not Installed that application")



    # reminder        
    elif 'remind me after' in queary:
        queary = queary.replace("remind me after", "")
        queary = queary.replace("i" , "you")
        magnitude = int(queary.split()[0])
        unit = queary.split()[1]
        alice.speak(f"Okay Sir! I will be reminding you after {magnitude} {unit}!")
        try:
            pourpose = queary.split("so that ")[1]
        except Exception:      # the user can give the reason as a option
            pourpose = "You didn't told the pourpose for reminding, Its might be some thing secret \U0001F923"
        finally :
            reminder.reminder(magnitude, unit, pourpose)



    # music
    elif 'play music' in queary or 'play another music' in queary or 'play song' in queary or 'play any song' in queary:
        music = os.listdir(Client.musicDirectory)
        os.startfile(os.path.join(Client.musicDirectory, random.choice(music)))
        alice.speak("Playing Music...")


    elif 'brown munde' in queary:       # this function is just for my self i.e. For Abhinav personal songs
        os.startfile(r"E:\ADMIN\Music\BRODEVIL\Hollywood_song\sunna_hai_kya\BROWN MUNDE - AP DHILLON GURINDER GILL SHINDA KAHLON GMINXR.mp3")


    elif 'play my music' in queary: 
        os.startfile(Client.favorateMusic)


    # working with files :
    elif 'delete unwanted files' in queary:
        alice.speak("Deleting unwanted files...")
        workWithFiles.deleteUnwantedFiles() 



    # fun commands :

    elif 'is i am audio able' in queary:
        alice.speak(random.choice(POSITIVE_REPLIES))
    

    elif 'testing' in queary:
        alice.speak(f"Hello sir! {random.choice(POSITIVE_REPLIES)}")


    elif 'hello' in queary:
        alice.speak("Hello sir! how may I can help you.")


    elif 'good morning' in queary or 'good afternoon' in queary or 'good evening' in queary:
        wish = alice.goodWish
        if wish.lower() in queary:
            alice.speak(f"{wish} Sir!")
        else:
            alice.speak(f"Sir! Its {wish.split()[1]} Right now!")
    

    elif "time" in queary:
        alice.speak(f"Its {datetime.datetime.now().strftime('%H:%M:%S')} Sir!")
    

    elif "date" in queary:
        alice.speak(f"Its {datetime.datetime.now().day} of {datetime.date(1900, datetime.datetime.now().month, 1).strftime('%B')} {datetime.datetime.now().year}")


    elif 'who are you' in queary:
        alice.intro()

    
    elif "what's my name" in queary or "what is my name" in queary or "who i am" in queary:
        alice.speak(f"You are {alice.name} {alice.gender}!, But why did you are asking this?")


    elif "to kaise hain aap log" in queary:     # just for ha
        alice.speak("Hum thik hai bhai, Tum batao!..")



    # Hardware Features:
    elif 'cpu' in queary or "cpu status" in queary or 'processor' in queary or 'processing' in queary:
        alice.speak(f"CPU used : {Client.cpu_status}%")


    elif 'battery' in queary:
        try:
            alice.speak(f"Battery is {Client.battery_status}% Charged! " + ("And its still in charging." if Client.battery_pugged else ""))
        except Exception:
            alice.speak(f"Something went wrong {random.choice(ERROR_REPLIES)}. I think you are in desktop")


    elif 'memory' in queary or 'ram' in queary:
        alice.speak(f"Memory Used : {Client.memory_status}%")


    elif 'storage' in queary or 'hard drive' in queary:
        alice.speak(f"Total available Storage : {Client.storage['Total']} GB, Used : {Client.storage['Used']} GB, Free : {Client.storage['Free']} GB")


    elif 'internet' in queary:
        if Client.internet:
            alice.speak("Yes sir! Internet is connected")\


    elif 'system' in queary or 'computer info' in queary:
        alice.speak(f"Its a {Client.computerInfo['System']} {Client.computerInfo['Release']}, A {Client.computerInfo['Machine'][-3:-1]} bit Machine, Version {Client.computerInfo['Version']}, Admin user is {Client.computerInfo['Node name']}. {Client.computerInfo['Processor']} Processor.")




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
    elif "type that" in queary or "send that" in queary:
        queary = queary.split("that")[1]
        keyactivities.typeWrite(queary)
        keyboard.press("enter")
    

    elif 'record keyboard' in queary:
        alice.speak("Okay Sir! Note that, your keyboard activies will be recording till you prese Escap button on your keyboard")
        keyboardActivities = keyactivities.keyboardRecord()


    elif 'play the keyboard recording' in queary:
        try:
            keyboardActivities
        except NameError:
            alice.speak("Sir! there is no keyboard Activity available till now")
        else:
            alice.speak("Okay Sir! Playing the keyboard Activiy recording, Note that have to put the cursor where you want to play it.")
            time.sleep(7)
            keyactivities.recordedKeyboardType(keyboardActivities)



    # local info work with internet :
    elif 'whats my location' in queary or 'where am i' in queary or 'where i am' in queary:
        alice.speak(f" You are in the Country {Client.location[0]} and near by {Client.location[2]} which is in {Client.location[1]} Region {alice.gender}!")


    elif 'news' in queary:
        topTen = networks.news()
        if topTen is not None:
            for articles in topTen:
                print(f"For more info... Go to ==>>> {articles['url']}\n")
                alice.speak(f"Title; {articles['title']}. \nDiscription; {articles['description']}. Actually; {articles['content']}\n")
                alice.speak("Moving On next news!")
            alice.speak("Thank you for listening")
    

    elif 'weather report of' in queary:
        place = queary.split("of")[1]
        alice.speak(networks.weather(place))
    

    elif "temperature" in queary or "weather report" in queary:
        try:
            alice.speak(Client.weatherInfo)
        except:
            alice.speak(random.choice(ERROR_REPLIES))
    


    # work with loging file : i.e.work with E commerce websites accounts 
    elif 'send email' in queary:
        alice.speak("To whom you want to send the email")
        try:
            userEmail = alice.takeCommand().lower()     # here taking the name as a input and featuring it in our contacts
            for i in Contacts.emails.keys():
                if i.split()[0].lower() == userEmail.split()[0]:
                    userEmail = Contacts.emails[i]
                    break
            else:
                alice.speak(f"Sir! We didn't got {userEmail} in your contact. Can you tell the email address!")
                userEmail = alice.takeCommand()     # taking email address by speak function
                if userEmail != "None":
                    userEmail = userEmail.replace(" ", "").lower()
                else:
                    alice.speak("Sorry sir! I didn't get that. Please type the email Adress in the terminal!")
                    userEmail = input("Enter the Email Adress :\t")  
        except Exception as e:
            alice.speak(f"{random.choice(ERROR_REPLIES)}, Some thing went Wrong")


        alice.speak("What's the subject...")
        subject = alice.takeCommand()
        alice.speak("Whats the content...")
        content = alice.takeCommand()
        result = login.sendEmail(userEmail, subject, content)
        if result == False:
            alice.speak(f"{random.choice(ERROR_REPLIES)}, Some thing went Wrong")
        else:
            alice.speak(f"Email send succefully to {userEmail}!")


















