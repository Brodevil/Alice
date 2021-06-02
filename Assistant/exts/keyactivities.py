import keyboard


__all__ = ("typeWrite", "keyboardRecord", "recordedKeyboard")


def typeWrite(string):
    for i in string.split():
        if i.lower() == "enter" or i.lower() == "send":
            keyboard.press("enter")
        elif i.lower() == "next" or i.lower() == "new":
            keyboard.press_and_release("shift+enter")
        else:
            keyboard.write(f"{i} ") 
    

def keyboardRecord():
    """The functions records the keyboard activity and can be just written by using another recordedKeyboardType() functions"""
    record = keyboard.record(until='Esc')
    # keyboard.play(record, speed_factor=5)
    return record


def recordedKeyboard(record):
    """Function to type the recorded keyboard activity which is recorded by keyboardRecord() functions"""
    keyboard.play(record, speed_factor = 5)


