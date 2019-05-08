import keyboard as kb
import cv2
from time import time

recording_fps = 10
recording_delay = 1/recording_fps

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

    #cv2.imwrite(out_folder + "/" + str(label) + "/" + imageName,frame)
    cv2.imwrite("testing.png",frame)
while True:

    time_to_check_key = time() + recording_delay
    while time() < time_to_check_key:
        pass
    key = kb.read_event()
    n=n+1
    print(key.scan_code)
    a = time()
    save_frame( key.scan_code, "test", "output_folder")
    print(a - last_frame)
    last_frame = a


def record_keyboard(path_to_save):
    pass