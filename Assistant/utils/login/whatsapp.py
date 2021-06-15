import pywhatkit
import pyautogui as pg
import time

__all__ = ("sendWhatsappMessage", "readWhatsappMessage")


def sendWhatsappMessage(number:str, message:str) -> None:
    pywhatkit.sendwhatmsg_instantly(number, message, wait_time=1)
    time.sleep(3)
    pg.press("enter")


def readWhatsappMessage():
    pass


if __name__ == '__main__':
    print("here!")
    sendWhatsappMessage("+918975057675", "Test 0, by Alice")
