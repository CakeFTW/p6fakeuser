import keyboard
import cv2
import _thread
import time
import sys


def record_webcam(flag, path_to_vid):
    print("Opening webcam")

    cap = cv2.VideoCapture(path_to_vid)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_delay = int(1000/fps)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            if flag == []:
                flag.append(True)
            cv2.imshow('frame',frame)
            cv2.waitKey(frame_delay)
            if cv2.waitKey(2) & 0xFF == ord('\x1b'):
                print("video: got escape char")
                break
        else:
            break
    # Release everything if job is finished
    cap.release()
    cv2.destroyAllWindows()


def record_keyboard(save_name):
    print("starting recording")
    startTime = time.time()
    record = keyboard.record()


    keys, times, up_down = [],[],[]

    for e in record:
        keys.append(e.scan_code)
        times.append(e.time)
        up_down.append(e.event_type)

    #set times to be relative to starting time
    times = [x - startTime for x in times]
    print(times)
    print(keys)


    file = open(save_name,"a")
    file.write('KEYBOARD\n')
    [file.write(str(x) + ',') for x in keys]
    file.write('\n')
    [file.write(str(x) + ',') for x in times]
    file.write('\n')
    [file.write(str(1)+',' if x in 'down' else str(0) + ',') for x in up_down]


print("starting program")
vid_path, key_path = "",""
if( len(sys.argv) > 1):
    print("participant number: " ,sys.argv[1])
    key_path = sys.argv[1][:-4] + ".txt"
    vid_path =  sys.argv[1]
else:
    exit()

webcam_recording = []
play_thread = _thread.start_new_thread(record_webcam, (webcam_recording,vid_path,))
while webcam_recording == []:
    pass
record_keyboard(key_path)

print("done recording")

