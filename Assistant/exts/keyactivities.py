import keyboard
import pyautogui

__all__ = ("typeWrite", "keyboardRecord", "playKeyboard")


def typeWrite(string) -> None:
    for i in string.split():
        if i.lower() == "enter" or i.lower() == "send":
            keyboard.press("enter")
        elif i.lower() == "next" or i.lower() == "new":
            keyboard.press_and_release("shift+enter")
        else:
            keyboard.write(f"{i} ")


def keyboardRecord() -> object:
    """The functions records the keyboard activity and can be just written by using another recordedKeyboardType() functions"""
    record = keyboard.record(until='Esc')
    # keyboard.play(record, speed_factor=5)
    return record


def playKeyboard(record) -> None:
    """Function to type the recorded keyboard activity which is recorded by keyboardRecord() functions"""
    keyboard.play(record, speed_factor=5)


def volume_control(how_much, increase=False, decrease=False, mute=False) -> None:
    for _ in range(how_much//2):
        if increase:
            pyautogui.press("volumeup")
        elif decrease:
            pyautogui.press("volumedown")

    if mute:
        pyautogui.press("volumemute")


