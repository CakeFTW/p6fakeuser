import os
import keyboard as kb
import cv2
from time import time
from sys import argv as arg

recording_delay = 0.08

try:
    file_name = "participant"+ str(arg[1])
except:
    file_name = "participant_nothing"

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
cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
n=0



def save_frame (label, file_name, out_folder):
    res, frame = cap.read()
    imageName = file_name+"_"+str(label)+"_"+str(n)+".png"
    try:
        os.mkdir(out_folder+ "/" + str(label))
    except:
        pass
    cv2.imwrite(out_folder + "/" + str(label) + "/" + imageName,frame)


while True:
    time_to_check_key = time() + recording_delay
    while time() < time_to_check_key:
        pass
    key = kb.read_event()
    n=n+1
    print(key.scan_code)
    a = time()
    save_frame( key.scan_code, file_name, total_path)
    print(a - last_frame)
    last_frame = a

def record_keyboard(path_to_save):
    pass

