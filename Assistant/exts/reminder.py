from plyer import notification
import pyttsx3
import time
from Assistant.Alice import alice



def notifier(reason, string, ico):
    notification.notify(
                    title = string,
                    message = reason,
                    app_icon = ico,
                    timeout = 12
                )
            

def reminder(magnitude, unit, pourpose):
    print("bhai atlest function me ghuss gaya hu me")
    if unit.lower() == "myounute" or unit.lower() == "myounutes":     # this is actually the computer sense word to minutes as a myournutes     #noqa
        remindTime = int(magnitude*60 + time.time())
        print("in program")
        while True:
            presentTime = int(time.time())
            if presentTime == remindTime:
                print('wah bete moj kr di')
                alice.speak("Time Out Sir!")
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
                alice.speak("Time Out Sir!")
                notifier(
                    reason=pourpose,
                    string="Alice : Time Out Sir!",
                    ico=r"Assistant\media\time-out.ico"
                )
                break


if __name__ == "__main__":
    reminder(1, "minutes", "Test 0")
