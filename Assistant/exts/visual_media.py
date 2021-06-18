from pyautogui import screenshot
from os.path import join
from subprocess import Popen
from Assistant.constants import Client
import datetime


__all__ = ["VisualMedia"]


class VisualMedia:
    def __init__(self):
        pass

    @staticmethod
    def screen_shorts(name=None) -> None:
        if name is None:
            name = f"Alice Screenshot ({datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')})"

        image = screenshot()
        file_path = join(Client.ALICE_PATH, f"Media\\Images\\{name}.png")
        image.save(file_path)
        Popen(f'explorer , "{file_path}"')



    def photos(self):
        pass

    def video_recorder(self):
        pass

    def screen_recorder(self):
        pass

    def CCTV_mood(self):
        pass

    def voice_recorder(self):
        pass


if __name__ == '__main__':
    VisualMedia.screen_shorts()
