import pyttsx3
import datetime
import requests
import json
import pprint
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import keyboard
import time
import random
import psutil
import subprocess
from exts import reminder
from exts import apis


engine = pyttsx3.init('sapi5')


introduction = "Now me to introduce myself, I m Alice. A virtual desktop assistant and I'm here to assist you with a verity of tasks \
        as best as I can. 24 Hours a day seven days a week, Importing all preferences from home, interface system are now \
        fully operational, Sir!"


def speakDavid(audio):
    engine.setProperty('voice', engine.getProperty('voices')[0].id)
    print(engine.getProperty('voices'))
    engine.setProperty("rate", 175)
    engine.setProperty('volume', 50)
    print(f"Alice : {audio}\n")
    engine.say(audio)
    engine.runAndWait()


def speakRavi(audio):
    engine.setProperty('voice', engine.getProperty('voices')[1].id)
    engine.setProperty("rate", 170)
    engine.setProperty('volume', 50)
    print(f"Alice : {audio}\n")
    engine.say(audio)
    engine.runAndWait()


def speakZira(audio):
    engine.setProperty('voice', engine.getProperty('voices')[3].id)
    engine.setProperty("rate", 170)
    engine.setProperty('volume', 50)
    print(f"Alice : {audio}\n")
    engine.say(audio)
    engine.runAndWait()
    

def speakRichard(audio):
    engine.setProperty('voice', engine.getProperty('voices')[2].id)
    engine.setProperty("rate", 170)
    engine.setProperty('volume', 50)
    print(f"Alice : {audio}\n")
    engine.say(audio)
    engine.runAndWait()


def goodWish():
    presentHour = int(datetime.datetime.now().hour)
    if presentHour == 0 or presentHour < 12:
        return "Good Morning"

    elif presentHour == 12 or presentHour < 18:
        return "Good Afternoon"

    else:
        return "Good Evening"


def typing(str):
    pass



def keyboardRecord():
    """The functions records the keybaord activity and can be just written by using another recordedKeyboardType() functions"""
    record = keyboard.record(until ='Esc')
    # keyboard.play(record, speed_factor=5)
    return record


def recordedKeyboardType(record):
    """Function to type the recorded keyboard activity which is recorded by keyboardRecord() functions"""
    keyboard.play(record, speed_factor = 5)
    


def edge(url):
    edgePath = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edgePath))
    webbrowser.get('edge').open(url)


def intro():
    speakRichard("Now me to introduce myself, I m Alice. A virtual desktop assistant and I'm here to assist you with a verity of tasks as best as I can. 24 Hours a day, seven days a week, Importing all preferences from home Interface, System are now fully operational!")
    speakRichard(f"{goodWish()} Sir!")
    speakRichard(f"Its {datetime.datetime.now().hour}:{datetime.datetime.now().minute}, and todays date is {datetime.datetime.now().day} of {datetime.date(1900, datetime.datetime.now().month, 1).strftime('%B')} {datetime.datetime.now().year} ")

    temperature = apis.weather()    # seem to give location as a argument
    if temperature != None:
        speakRichard(f"Its feels like approximately {temperature} degree celsius outside the door")
    

def initialCommit(path):
    os.chdir(path)
    os.system("git add .")
    os.system('git commit -m "inital commit by Alice"')
    os.system("git push -u origin main")


def takeCommand():
    '''
    The not having any parameter but it taking the input form the microphone of the user 
    and return the string object that the user says
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Alice : Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 100
        audio = r.listen(source)
    
    try:
        print("Alice : Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"User : \t{query}\n")
    
    except Exception as e:
        print("Alice : Sorry! I didn't get that...\n")
        return "None"

    return query


def logic(queary):
    """This is the logic of the Program as it will be matching several queary and do the programmed task """

    if 'wikipedia' in queary:
            speakRavi("Searching Wikipedia...")
            queary = queary.replace("wikipedia", "")
            try:
                results = wikipedia.summary(queary, sentences=2)
                speakRavi(f"According to wikipedia. {results}")
            except Exception:
                speakRichard("Sorry! I didn't got that stuff in wikipedia")
        

    elif 'quit' in queary:
        speakRichard("That's it, I am quiting")
        exit()


    elif 'search' in queary:
        queary = queary.replace("search", "")
        edge("https://www.google.com")
        speakRichard(f"Searching {queary} in Google")
        time.sleep(4)
        keyboard.write(queary)
        keyboard.press_and_release('enter')


    elif 'open youtube studio' in queary:
        speakRichard("Opening youtube studio...")
        edge("https://studio.youtube.com/")

    
    elif 'open youtube' in queary:
        speakRichard("Opening youtube...")
        edge("youtube.com")
    
    
    elif 'open google' in queary:
        speakRichard("Opening google...")
        edge("google.com")
    
    
    elif 'open stack overflow' in queary:
        speakRichard("Opening stackoverflow...")
        edge("stackoverflow.com")
    
    
    elif 'reveal your code' in queary:
        speakRichard("Opening Github repositor.....")
        edge("github.com/Brodevil/Alice")


    elif 'open github' in queary:
        speakRichard("Opening Github.....")
        edge("https://github.com/Brodevil")
    

    elif 'open discord' in queary:
        speakRichard("Opening Discord in Browser.....")
        edge("https://discord.com/channels/@me")


    elif 'open instagram' in queary:
        speakRichard("Opening Instagram.....")
        edge("https://www.instagram.com")


    elif 'open whatsapp' in queary:
        speakRichard("Opening  Whatsapp.....")
        edge("https://web.whatsapp.com/")


    # elif 'open'

    elif 'open spotify' in queary:
        speakRichard("Opening Spotify.....")
        edge('https://open.spotify.com/')
    

    elif 'pep8' in queary:
        edge("https://www.python.org/dev/peps/pep-0008/")   
    

    elif 'is i am audio able' in queary:
        speakRichard("Yes sir you are Audio able!")
    

    elif 'hello alice' in queary:
        speakRichard("Hello sir! how may I can help you.")


    elif 'good morning' in queary or 'good afternoon' in queary or 'good evening' in queary:
        wish = goodWish()
        if wish.lower() in queary:
            speakRichard(f"{wish} Sir!")
        else:
            speakRichard(f"Sir! Its {wish.split()[1]} Right now!")
    

    elif "what's the time" in queary:
        speakRichard(f"Its {datetime.datetime.now().strftime('%H:%M:%S')} Sir!")
    

    elif "what's the date" in queary:
        speakRichard(f"Its {datetime.datetime.now().day} of {datetime.date(1900, datetime.datetime.now().month, 1).strftime('%B')} {datetime.datetime.now().year}")


    elif 'who are you' in queary:
        intro()
    

    elif 'desktop' in queary:
        keyboard.press_and_release("win+d")


    elif 'lock pc' in queary:   
        os.system("rundll32.exe user32.dll, LockWorkStation")
        exit()


    elif 'shutdown pc' in queary:
        os.startfile(r"C:\Windows\System32\SlideToShutDown.exe")
        speakRichard("Shuting down pc....")
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


    elif 'open visual studio code' in queary:
        speakRichard("Opening vs code...")
        os.startfile(r"E:\Programe File (x83)\Microsoft VS Code\Code.exe")


    elif 'open sublime text' in queary:
        speakRichard("Opening Sublime Text")
        os.startfile(r"E:\Programe File (x83)\Sublime Text 3\sublime_text.exe")


    elif "open discord application" in queary:
        try:
            os.startfile(r"E:\Programe File (x83)\Discord\app-0.0.309\Discord.exe")
            speakRichard("Opening Discord Application")
        except Exception:
            speakRichard("Some thing went wrong! It might be a wrong path or you had not Installed that application")
        
    
    elif "open file explorer" in queary:
        try:
            subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')
            speakRichard("Opening File Explorer...")
        except Exception:
            speakRichard("Some thing went Wrong")

    elif "open rapid typing" in queary:
        try:
            os.startfile(r"E:\Programe File (x83)\Typing Course\RapidTyping.exe")
            speakRichard("Opening Rapid Typing...")
        except Exception:
            speakRichard("Some thing went wrong! It might be a wrong path or you had not Installed that application")


        
    elif 'remind me after' in queary:
        queary = queary.replace("remind me after", "")
        queary = queary.replace("i" , "you")
        magnitude = int(queary.split()[0])
        unit = queary.split()[1]
        print(unit)
        speakRichard(f"Okay Sir! I will be reminding you after {magnitude} {unit}!")
        try:
            pourpose = queary.split("so that ")[1]

        except Exception:      # the user can give the reason as a option

            pourpose = "You didn't told the pourpose for reminding, Its might be some thing secret \U0001F923"
        
        finally :
            reminder.reminder(magnitude, unit, pourpose)



    elif 'play music' in queary or 'play another music' in queary:
        music = os.listdir(r"E:\ADMIN\Music\BRODEVIL\Hollywood song\sunna hai kya")
        os.startfile(os.path.join(r"E:\ADMIN\Music\BRODEVIL\Hollywood song\sunna hai kya", random.choice(music)))
        speakRichard("Playing Music...")


    elif 'brown munde' in queary:
        os.startfile(r"E:\ADMIN\Music\BRODEVIL\Hollywood song\sunna hai kya\BROWN MUNDE - AP DHILLON GURINDER GILL SHINDA KAHLON GMINXR.mp3")


    elif 'play my music' in queary:
        os.startfile(r"E:\ADMIN\Music\BRODEVIL\Hollywood song\sunna hai kya\AUD-20210421-WA0103 - Copy (2).mp3")


    elif 'delete unwanted files' in queary:
        speakRichard("Deleting unwanted files...")
        unwantedFiles = [r"C:\Windows\Temp", r"C:\Users\ADMIN\AppData\Local\Temp", r"C:\Windows\Prefetch"]
        for f in unwantedFiles:
            for file in os.listdir(f):
                try:
                    os.remove(os.path.join(f , file))  
                except PermissionError:
                    pass


    elif "to kaise hain aap log" in queary:
        speakRichard("Hum thik hai bhai, Tum batao!..")


    elif 'push the code' in queary:
        speakRichard("Commit and then pushing the code in github repository....")
        initialCommit(os.getcwd())
    

    elif "what's the temperature" in queary:
        temperature = apis.weather()    # wanna back on this
        if temperature != None:
            speakRichard(f"Its seemed to be approximately {temperature} degree celsius outside the door")


    elif "bye" in queary or 'kill yourself' in queary:
        speakRichard("That's it, I m quiting....")
        exit()


    elif 'say' in queary:
        queary = queary.replace("say ", "")
        speakRichard(queary)

    
    elif "type that" in queary:
        queary = queary.replace("type that", "")
        typing(queary)
    

    elif 'record keyboard' in queary:
        speakRichard("Okay Sir! Note that, your keyboard activies will be recording till you prese Escap button on your keyboard")
        keyboardActivities = keyboardRecord()


    elif 'play the keyboard recording' in queary:
        try:
            keyboardActivities
        except NameError:
            speakRichard("Sir! there is no keyboard Activity available till now")
        else:
            speakRichard("Okay Sir! Playing the keyboard Activiy recording, Note that have to put the cursor where you want to play it.")
            time.sleep(7)
            recordedKeyboardType(keyboardActivities)



    elif 'location' in queary:
        pass


    elif 'wheter report' in queary:
        pass


    elif 'todays news' in queary:
        pass

    
    elif 'contact' in queary:
        pass


    elif 'repeat my self' in queary:
        speakRichard("Okay Sir! Start to tell I will be follwing you")
        while queary == "quite" or queary == "stop":
            queary = takeCommand().lower()
            speakRichard(queary)


if __name__ == "__main__":
    intro()
    # if 1:
    while True:
        queary = takeCommand().lower()
        logic(queary)     # Logic for executin task based on query
        