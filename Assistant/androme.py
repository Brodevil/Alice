import pyttsx3
import datetime


engine = pyttsx3.init('sapi5')
engine.setProperty('voice', engine.getProperty('voices')[0].id)

intoduction = "Now me to introduce myself, I m Alice. A virtual desktop assitant and I'm here to assit you with a veriety of tasks \
        as best as I can. 24 Hours a day seven days a week, Importing all preferences from home, interface system are now \
        fully operational, Sir!"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def intro():
    hour = int(datetime.datetime.now().hour())
    if hour == 0 and hour < 12:
        speak("Good Morning Sir!")
    
    elif hour == 12 and hour < 18:
        speak("Good Afternon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("Now me to introduce myself, I m Alice. A virtual desktop assitant and I'm here to assit you with a veriety of tasks \
        as best as I can. 24 Hours a day seven days a week, Importing all preferences from home, interface system are now \
        fully operational, Sir!")


if __name__ == "__main__":
    speak("Abhinav is the good boy!")
    

