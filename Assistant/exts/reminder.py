import datetime
from plyer import notification
from Assistant.__init__ import speakRichard 


def notifier(reason, string, ico):
    notification.notify(
                    title = string,
                    message = reason,
                    app_icon = ico,
                    timeout = 12
                )
            

def reminder(magnitude, unit, pourpose=None):
    if unit.lower() == "minutes":
        remindTime = magnitude + int(datetime.datetime.now().minute)
        while(True):
            presentTime = int(datetime.datetime.now().minute)
            if presentTime == remindTime:
                speakRichard("Time Out Sir!")
                notifier(
                    reason=pourpose,
                    string="Alice : Time Out Sir!",
                    ico=r"Assistant\media\time-out.svg"
                )

    elif unit.lower() == "hours":
        remindTime = magnitude + int(datetime.datetime.now().hours)
        while(True):
            presentTime = int(datetime.datetime.now().hours)
            if presentTime == remindTime:
                speakRichard("Time Out Sir!")
                notifier(
                    reason=pourpose,
                    string="Alice : Time Out Sir!",
                    ico=r"Assistant\media\time-out.svg"
                )


if __name__ == "__main__":
    pass
