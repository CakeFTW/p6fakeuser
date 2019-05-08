import os
import keyboard as kb
import cv2
from time import time
from sys import argv as arg
import _thread

recording_delay = 0.08

try:
    file_name = str(arg[1])
except:
    print("no file")
    exit()
folder_path = "recordings"
try:
    os.mkdir(folder_path)
except:
    pass

try:
    os.mkdir(folder_path + "/" + file_name)
except:
    print("participant already exist, renaming to paricipant_allready_exist")
    os.mkdir(folder_path + "/participant_already_exists")
    file_name = "participant_already_exists"

total_path = folder_path + "/" +file_name
print(" started recording for", file_name)

time_to_check_key = 0
kb.start_recording
last_frame = 0
frame = 0
cap = cv2.VideoCapture(file_name)
file_name=file_name[:-4]
fps = cap.get(cv2.CAP_PROP_FPS)
delay = 1000 / fps
n=0

keypresses = []


def displayFrame ():
    res, frame = cap.read()
    cv2.imshow()
    if keypresses != []:
        label = keypresses.pop()
        imageName = file_name+"_"+str(label)+"_"+str(n)+".png"
        try:
            os.mkdir(file_name+ "/" + str(label))
        except:
            pass
        cv2.imwrite(file_name + "/" + str(label) + "/" + imageName,frame)

    cv2.waitKey(delay)

t1=_thread.start_new_thread(displayFrame,())

while True:
    time_to_check_key = time() + recording_delay
    while time() < time_to_check_key:
        pass
    key = kb.read_event()
    n=n+1
    print(key.scan_code)
    a = time()
    keypresses.append(key.scan_code)
    print(a - last_frame)
    last_frame = a


def record_keyboard(path_to_save):
    pass

