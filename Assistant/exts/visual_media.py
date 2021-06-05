from cv2 import *
import datetime



class VisualMedia:
    def __init__(self):
        self.cam = VideoCapture(0)      # initialize the camera


    def photos(self):
        # initialize the camera
        s, img = self.cam.read()
        if s:    # frame captured without any errors
            namedWindow("Alice", 500)
            imshow("Alice", img)
            waitKey(0)
            imwrite(f"Alice({datetime.time().strftime('%b-%d-%Y')}).jpg", img)
            destroyAllWindows()


    def video_recorder(self):
        pass


    def screen_recorder(self):
        pass


    def CCTV_mood(self):
        pass


    def voice_recorder(self):
        pass



if __name__ == '__main__':
    pass
