import time
import winsound  # noqa
import pyttsx3
import datetime

from os import environ, path
from dotenv import load_dotenv
from plyer import notification

from Assistant.constants import Client

load_dotenv()

__all__ = ["speak", "notifier", "reminderAlarm"]


def speak(string: str) -> None:
    """
    speak function for reminding the user from voice also
    """
    engine = pyttsx3.init("sapi5")
    engine.setProperty("voice", engine.getProperty("voices")[int(environ.get("VoiceNumber", 1)) - 1].id)
    print(f"{Client.ASSISTANT_NAME} : {string}", "\n")
    engine.say(string)
    engine.runAndWait()


def notifier(reason: str, string: str, ico: str) -> None:
    """
    take the reason, long string and icon file as a argument
    and make a notification in windows 10 for reminding the user in any task or work
    """
    try:
        notification.notify(
            title=string,
            message=reason,
            app_icon=ico,
            timeout=12
        )
    except Exception:
        pass


def reminderAlarm(magnitude: int, unit: str, pourpose: str) -> None:
    """
    The function is just a reminder not a alarm
    this will remind after specific time, by beeping and notifying
    All the process will be placed in background.
    """
    if unit.lower() == "minute" or unit.lower() == "minutes":
        remindTime = int(magnitude * 60 + time.time())
        is_hour = False

    elif unit.lower() == "hours" or unit.lower() == "hour":
        remindTime = int(magnitude * 60 * 60 + time.time())
        is_hour = True
    else:
        return

    while True:
        presentTime = int(time.time())
        if presentTime == remindTime:  # noqa
            notifier(
                reason=f"Here's your reminder : {pourpose}",
                string="Alice : Time Out Sir!",
                ico=path.join(Client.ALICE_PATH, "Assistant\\resources\\Images\\time-out.ico")
            )
            winsound.Beep(frequency=2500, duration=4000)
            speak(
                f"Time Up, You had told me to remind you after {magnitude}" " hours " if is_hour else " minutes" +  # noqa
                                                                                                      "Now its time to remind you, Wake up.")

            break


def alarm(time_unit: str):
    """
    Alarm function to remind at the specific time like at 19:05/02:00
    """

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == time_unit:
            notifier(
                reason=f"Alarm of {time_unit}",
                string="Time has arrived!",
                ico=path.join(Client.ALICE_PATH, "Assistant\\resources\\Images\\time-out.ico")
            )
            winsound.Beep(frequency=2500, duration=4000)
            speak(f"The Alarm of {time_unit} had Been Arrived!")
            break


