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

from Assistant.resources.login import login                                                                            # noqa
from Assistant.Alice import alice                                                                           # noqa
from Assistant.exts import keyactivities                                                                    # noqa
from Assistant.exts import workWithFiles                                                                    # noqa



__all__ = ("logic")

# load_dotenv()
try:
    battery = psutil.sensors_battery()
except Exception:
    battery = None


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


    elif "youtube" in queary and "search" in queary:
        search = queary.split("youtube")[-1]
        alice.edge(f"https://www.youtube.com/results?search_query={search.replace(' ', '+')}")
        

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




    # reminder        
    elif 'remind me after' in queary:
        queary = queary.replace("remind me after", "")
        queary = queary.replace("i" , "you")
        magnitude = int(queary.split()[0])
        unit = queary.split()[1]
        alice.speak(f"Okay {alice.gender}! I will be reminding you after {magnitude} {unit}!")
        try:
            pourpose = queary.split("so that ")[1]
        except Exception:      # the user can give the reason as a option
            pourpose = "You didn't told the pourpose for reminding, Its might be some thing secret \U0001F923"
        finally :
            reminder.reminder(magnitude, unit, pourpose)





    # music
    elif 'play music' in queary or "play another music" in queary or "play another song" in queary or "play song" in queary or "play" in queary and "random" in queary:
        music = os.listdir(Client.musicDirectory)
        os.startfile(os.path.join(Client.musicDirectory, random.choice(music)))
        alice.speak("Playing Music...")


    elif 'brown munde' in queary:       # this function is just for my self i.e. For Abhinav personal songs
        try:
            os.startfile(r"E:\ADMIN\Music\BRODEVIL\Hollywood_song\sunna_hai_kya\BROWN MUNDE - AP DHILLON GURINDER GILL SHINDA KAHLON GMINXR.mp3")
        except Exception:
            pass


    elif "play my music" in queary or "play my song" in queary: 
        print("contition satifiding here!")
        os.startfile(Client.favorateMusic)




    # working with files :
    elif 'delete unwanted files' in queary:
        alice.speak("Deleting unwanted files...")
        workWithFiles.deleteUnwantedFiles() 



    
    # Natural Talks/ Fun dommands :
    
    elif 'is i am audio able' in queary:
        alice.speak(random.choice(POSITIVE_REPLIES))
    

    elif 'testing' in queary:
        alice.speak(f"Hello {alice.gender}! {random.choice(POSITIVE_REPLIES)}")


    elif 'hello' in queary:
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
        alice.speak(f"Its {datetime.datetime.now().day} of {datetime.date(1900, datetime.datetime.now().month, 1).strftime('%B')} {datetime.datetime.now().year}")


    elif 'who are you' in queary or "introduction" in queary:
        alice.intro()

    
    elif "what's my name" in queary or "what is my name" in queary or "who i am" in queary:
        alice.speak(f"You are {alice.name} {alice.gender}!, But why did you are asking this?")


    elif "to kaise hain aap log" in queary:     # just for ha
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
                    alice.speak(f"Sorry {alice.gender}! I didn't get that, Can you type the number of minutes in terminal ")
                    period = int(input("Enter the number of minutes I should sleep :\t"))
                except ValueError:
                    pass

        alice.speak(f"Okay {alice.gender}! I will be wake up after {period} minutes.")
        time.sleep(60*period)

        alice.speak(f"{alice.goodWish} {alice.gender}!, I wake up after {period} minutes, Lets back to work.")
        del period


    elif 'thank you' in queary or 'thanks' in queary:
        alice.speak(f"Your most welcome {alice.gender}!")


    elif 'how are you' in queary:
        alice.speak("I am quite fine sir, What about you ?")



    # System features :
    elif 'cpu' in queary or 'processor' in queary or 'processing' in queary:
        alice.speak(f"CPU used : {psutil.cpu_percent()}%")


    elif 'battery' in queary:
        if battery != None:
            try:
                alice.speak(f"Battery is {battery.percent}% Charged! " + ("And its still in charging." if battery.power_plugged else ""))
            except Exception:
                alice.speak(f"Something went wrong {random.choice(ERROR_REPLIES)}. I think you are in desktop")


    elif 'memory' in queary or 'ram' in queary.split():
        alice.speak(f"Memory Used : {psutil.virtual_memory().percent}%")


    elif 'storage' in queary or 'hard drive' in queary:
        alice.speak(f"Total available Storage : {Client.storage['Total']} GB, Used : {Client.storage['Used']} GB, Free : {Client.storage['Free']} GB")


    elif 'internet' in queary:
        if Client.internet:
            alice.speak(f"Yes {alice.gender}! Internet is connected")
        else:
            alice.speak(f"No {alice.gender}! Internet is not connected, But I don't know How I am working without internet, lol")

            

    elif 'system' in queary or 'computer info' in queary:
        alice.speak(f"Its a {Client.computerInfo['System']} {Client.computerInfo['Release']}, A {Client.computerInfo['Machine'][-3:-1]} bit Machine, Version {Client.computerInfo['Version']}, Admin user is {Client.computerInfo['Node name']}. {Client.computerInfo['Processor']} Processor.")


    elif "active" in queary and "pc" in queary or "active" in queary and "computer" in queary:
        try:
            time, unit = queary.split("for ")[-1].split()
            if unit == "hours" or unit == "hour": 
                time = time*60

        except Exception:
            alice.speak(f"{alice.gender}! Please Enter how many minutes in numbers, I should keep active your windows machine.")
            time = int(input("Enter the number of Minutes :\t"))
        finally:
            alice.speak(f"Okay {alice.gender}, I will be keep your windows machine active for next {time} Minutes!, Till that time you can grap a cup of coffee.")
            alice.activePC(time)


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
        alice.speak(f"Okay {alice.gender}! Note that, your keyboard activies will be recording till you prese Escap button on your keyboard")
        keyboardActivities = keyactivities.keyboardRecord()


    elif 'play the keyboard recording' in queary:
        try:
            keyboardActivities
        except NameError:
            alice.speak(f"{alice.gender}! there is no keyboard Activity available till now")
        else:
            alice.speak(f"Okay {alice.gender}! Playing the keyboard Activiy recording, Note that have to put the cursor where you want to play it.")
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
                alice.speak(f"{alice.gender}! We didn't got {userEmail} in your contact. Can you tell the email address!")
                userEmail = alice.takeCommand()     # taking email address by speak function
                if userEmail != "None":
                    userEmail = userEmail.replace(" ", "").lower()
                else:
                    alice.speak(f"Sorry {alice.gender}! I didn't get that. Please type the email Adress in the terminal!")
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


    
    elif "read book" in queary or "audio book" in queary or "speak pdf" in queary or "read pdf" in queary:
        alice.speak(f"{alice.gender} select the pdf file which you want to make read!")
        audioFile = alice.audioBook()
        if audioFile is None:
            alice.speak("Some thing went wrong!, It might be not a pdf file or the pdf file content will be in images form.")
        try:
            alice.speak(f"{alice.gender}! The audio file had created in that same path with same name.")
            os.startfile(audioFile)
        except Exception:
            pass



    # Launching the softwares stuffs

    elif 'open' in queary or 'launch' in queary:
        if "open" in queary:
            applicationName = queary.split("open ")
        elif 'launch' in queary:
            applicationName = queary.split("launch ")


            # the second argument is the releated path of the folder where all the used or usale software shortcuts are avaialbe by the user
        app = workWithFiles.openApplication(applicationName, "Application") 
        if app != None:
            alice.speak(f"Launching {app} Application...")     
        else:
            alice.speak(f"Sorry! {applicationName} shortcut didn't got in the Application folder. Please put the shortcuts of all the application do \
            you use in day to day life in Application folder, Which is in this project folder.")



    elif "open file explorer" in queary or "this pc" in queary:
        try:
            subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')
            alice.speak("Opening File Explorer...")
        except Exception:
            alice.speak("Some thing went Wrong")



if __name__ == "__main__":
    command = input("Enter the command for Alice :\t")
    logic(command)