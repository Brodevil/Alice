from plyer import notification
import time
from Assistant.Alice import alice
import winsound


__all__ = ["notifier", "reminderAlarm"]


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
    if unit.lower() == "myounute" or unit.lower() == "myounutes":  # this is actually the computer sense word to minutes as a myounutes     #noqa
        remindTime = int(magnitude * 60 + time.time())
        while True:
            presentTime = int(time.time())
            if presentTime == remindTime:
                notifier(
                    reason=pourpose,
                    string="Alice : Time Out Sir!",
                    ico=r"Assistant\media\time-out.ico"
                )
                winsound.Beep(frequency=2500, duration=4000)
                alice.speak("Time Out Sir!")
                break

    elif unit.lower() == "hours" or unit.lower() == "hour":
        remindTime = int(magnitude * 60 * 60 + time.time())
        while True:
            presentTime = int(time.time())
            if presentTime == remindTime:
                notifier(
                    reason=pourpose,
                    string="Alice : Time Out Sir!",
                    ico=r"Assistant\media\time-out.ico"
                )
                winsound.Beep(frequency=2500, duration=4000)
                alice.speak("Time Out Sir!")
                break

