import keyboard as kb
import cv2 as cv
from time import time

recording_fps = 10
recording_delay = 1/recording_fps

time_to_check_key = 0
kb.start_recording
last_frame = 0
frame = 0

while True:

    time_to_check_key = time() + recording_delay
    while time() < time_to_check_key:
        pass
    print(kb.read_event().scan_code)
    a = time()
    print(a - last_frame)
    last_frame = a


def record_keyboard(path_to_save):
    pass

