import cv2
import numpy as np
from os import system


def pixel_to_ascii(px):
    asci_array = list(" .:-=+*#%@")
    return asci_array[np.rint(px*10/255-1).astype(np.int64)]


def array_to_ascii(array):
    ascii_array = ""
    for i in array:
        ascii_array += pixel_to_ascii(i)
    return ascii_array


def print_ascii_result(frame):
    picture_ascii = ""
    for i in frame:
        picture_ascii += array_to_ascii(i) + "\n"

    system('cls')
    print(picture_ascii)


def start_camera():
    camera = cv2.VideoCapture(0)

    while True:
        _, frame = camera.read()
        frame = cv2.resize(frame, (180, 60))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print_ascii_result(frame)
        if cv2.waitKey(1) == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    start_camera()
