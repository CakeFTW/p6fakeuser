from sys import argv
import os
import cv2
import keyboard as kb
from time import time, sleep
import _thread
import json

#this is hopefully the final recording script

number_of_frames = []

#set the name to save the data under
try:
    sample_name = "participant" + argv[1]
except:
    print("participant number provided, -- saving as participant nothing")
    sample_name = "participant_nothing"


vid_folder = "data_cap"
rec_folder = "data_rec"

try:
    os.mkdir(vid_folder)
except:
    pass

try:
    os.mkdir(rec_folder)
except:
    pass

if sample_name == "participant_nothing":
    pass
else:
    a = os.listdir(rec_folder)
    for path in a:
        if sample_name in path:
            print("that participant number already exists -- try properly now")
            exit()

print("started recording for ", sample_name)

def record_webcam(path_to_save, frame_counter):
    "records the webcam and updates the frame counter"

    print("Opening webcam")
    cap = cv2.VideoCapture(0)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(path_to_save,fourcc, fps, (int(width),int(height)))
    local_frame_counter = 0

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            if frame_counter == []:
                frame_counter.append(0)
            local_frame_counter = local_frame_counter + 1
            frame_counter[0] = local_frame_counter
            out.write(frame)
            cv2.imshow('frame',frame)
            if cv2.waitKey(2) & 0xFF == ord('\x1b'):
                print("video: got escape char")
                break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

web_thread = _thread.start_new_thread(record_webcam, (vid_folder + "/" + sample_name + ".avi",number_of_frames,))

#now initialize the recording lists, while webcam is staring up
header = "ENDGAME"
keys = []
times = []
up_downs = []
frames = []

kb.start_recording
recording_delay = 0.08

while number_of_frames == []:
    pass

start_time = time()
while True:
    time_to_check_key = time() + recording_delay
    sleep(time_to_check_key - time())
    key_event = kb.read_event()
    keys.append(key_event.scan_code)
    times.append(key_event.time)
    up_downs.append(key_event.event_type)
    frames.append(number_of_frames[0])
    if key_event.scan_code == 1:
        print("got escape key")
        break

#adjust time stamps to be based of start time
times = [x - start_time for x in times]

#start writing file
totals = [header,keys,times,up_downs,frames]
print(totals)
file = open(rec_folder+"/"+ sample_name + ".json","a")
json.dump(totals, file)
file.close()




