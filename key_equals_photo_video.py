import os
import keyboard as kb
import cv2
from time import time, sleep
from sys import argv as arg
import _thread

recording_delay = 0.08

try:
    file_name = str(arg[1])
except:
    print("no file")
    exit()



time_to_check_key = 0
kb.start_recording
last_frame = 0

cap = cv2.VideoCapture(file_name)

file_name=file_name[:-4]
cv2.waitKey(500)
fps = cap.get(cv2.CAP_PROP_FPS)
delay = 1000 / 33
n=0

try:
    os.mkdir(file_name)
except:
    print("participant already exist, renaming to paricipant_allready_exist")
    exit()
    
print(" started recording for", file_name)

keypresses = []


def display_frame (stack):
    while (cap.isOpened()):
        res, frame = cap.read()
        if res == True:
            cv2.imshow("poopity scoop",frame)
            if stack != []:
                label = stack.pop()
                imageName = file_name+"_"+str(label)+"_"+str(n)+".png"
                try:
                    os.mkdir(file_name+ "/" + str(label))
                except:
                    pass
                cv2.imwrite(file_name + "/" + str(label) + "/" + imageName,frame)
        cv2.waitKey(30)


t1=_thread.start_new_thread(display_frame,(keypresses,))

while True:
    time_to_check_key = time() + recording_delay
    sleep(time_to_check_key - time())
    key = kb.read_event()
    n=n+1
    print(key.scan_code)
    a = time()
    keypresses.append(key.scan_code)
    print(a - last_frame)
    last_frame = a
    pass

