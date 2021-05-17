import keyboard


__all__ = ("", "")


def typeWrite(str):
    keyboard.write(str) 
    

def keyboardRecord():
    """The functions records the keybaord activity and can be just written by using another recordedKeyboardType() functions"""
    record = keyboard.record(until ='Esc')
    # keyboard.play(record, speed_factor=5)
    return record


def recordedKeyboardType(record):
    """Function to type the recorded keyboard activity which is recorded by keyboardRecord() functions"""
    keyboard.play(record, speed_factor = 5)


