from plyer import notification
import time
import winsound
import pyttsx3
from os import environ, getcwd
from dotenv import load_dotenv

load_dotenv()

__all__ = ["notifier", "reminderAlarm"]


def speak(str):
    engine = pyttsx3.init("sapi5")
    engine.setProperty("voice", engine.getProperty("voices")[int(environ.get("VoiceNumber", 1)) - 1].id)
    engine.say(str)
    engine.runAndWait()


def notifier(reason, string, ico):
    try:
        notification.notify(
            title=string,
            message=reason,
            app_icon=ico,
            timeout=12
        )
    except Exception:
        pass


def reminderAlarm(magnitude, unit, pourpose):
    if unit.lower() == "myounute" or unit.lower() == "myounutes" or unit.lower() == "minute" or unit.lower() == "minutes":  # this is actually the computer sense word to minutes as a myounutes     #noqa
        remindTime = int(magnitude * 60 + time.time())
        is_hour = False

    elif unit.lower() == "hours" or unit.lower() == "hour":
        remindTime = int(magnitude * 60 * 60 + time.time())
        is_hour = True
    else:
        reminderTime = None

    while True:
        presentTime = int(time.time())
        if presentTime == remindTime:  # noqa
            notifier(
                reason=pourpose,
                string="Alice : Time Out Sir!",
                ico=getcwd().replace("\\Alice\\Assistant\\exts", "\\Alice\\Assistant\\media\\time-out.ico")
            )
            winsound.Beep(frequency=2500, duration=4000)
            speak(
                f"Time Up, You had told me to remind your after {magnitude}" " hours " if is_hour else " minutes" +                         # noqa
                                                                                                       "Now its time to remind you, Wake up.")
            break
