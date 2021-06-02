from cv2 import *
import datetime


def photos():
    # initialize the camera
    cam = VideoCapture(0)   # 0 -> index of camera
    s, img = cam.read()
    if s:    # frame captured without any errors
        namedWindow("Alice", 500)
        imshow("Alice", img)
        waitKey(0)
        imwrite(f"Alice({datetime.time().strftime('%b-%d-%Y')}).jpg", img)
        destroyAllWindows()

    else:
        return None


if __name__ == '__main__':
    photos()