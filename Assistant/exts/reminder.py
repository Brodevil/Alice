from plyer import notification
import pyttsx3
import time


def speakRichard(audio):
    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[2].id)
    engine.setProperty("rate", 170)
    engine.setProperty('volume', 50)
    print(f"Alice : {audio}\n")
    engine.say(audio)
    engine.runAndWait()


def notifier(reason, string, ico):
    notification.notify(
                    title = string,
                    message = reason,
                    app_icon = ico,
                    timeout = 12
                )
            

def reminder(magnitude, unit, pourpose):
    if unit.lower() == "myournutes" or unit.lower() == "myounutes":     # this is actually the computer sence word to minutes as a myournutes
        remindTime = int(magnitude*60 + time.time())
        while(True):
            presentTime = int(time.time())
            if presentTime == remindTime:
                speakRichard("Time Out Sir!")
                notifier(
                    reason=pourpose,
                    string="Alice : Time Out Sir!",
                    ico=r"Assistant\media\time-out.ico"
                )
                break

    elif unit.lower() == "hours" or unit.lower() == "hour":
        remindTime = int(magnitude*60*60 + time.time())
        while(True):
            presentTime = int(time.time())
            if presentTime == remindTime:
                speakRichard("Time Out Sir!")
                notifier(
                    reason=pourpose,
                    string="Alice : Time Out Sir!",
                    ico=r"Assistant\media\time-out.ico"
                )
                break


if __name__ == "__main__":
    reminder(1, "minutes", "Test 0")
