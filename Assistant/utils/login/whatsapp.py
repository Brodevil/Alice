import pywhatkit
import pyautogui as pg
import time

__all__ = ("sendWhatsappMessage", "readWhatsappMessage")


def sendWhatsappMessage(number, message):
    pywhatkit.sendwhatmsg_instantly("+918975057675", "Hey", wait_time=5)
    time.sleep(4)
    pg.press("enter")


def readWhatsappMessage():
    pass


if __name__ == '__main__':
    sendWhatsappMessage(None, None)
