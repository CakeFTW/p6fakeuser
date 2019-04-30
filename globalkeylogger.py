import keyboard
import cv2
import _thread
import time


def record_webcam(flag):
    print("Opening webcam")

    cap = cv2.VideoCapture(0)
    fps = cap.get(cv2.cv2.CAP_PROP_FPS)
    width = cap.get(cv2.cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.cv2.CAP_PROP_FRAME_HEIGHT)
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi',fourcc, fps, (int(width),int(height)))
    print(flag)
    flag.append(True)
    print(flag)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(2) & 0xFF == ord('\x1b'):
                print("video: got escape char")
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()


def record_keyboard():
    print("starting recording")
    startTime = time.time()
    record = keyboard.record()

    #get rid of escape input
    record.pop()

    keys = []
    times = []
    up_down = []
    for e in record:
        keys.append(e.scan_code)
        times.append(e.time)
        up_down.append(e.event_type)

    #set times to be relative to starting time
    times = [x - startTime for x in times]
    print(times)
    print(keys)


    file = open("keyboard1.txt","w")
    file.write('KEYBOARD\n')
    [file.write(str(x) + ',') for x in keys]
    file.write('\n')
    [file.write(str(x) + ',') for x in times]
    file.write('\n')
    [file.write(str(1)+',' if x in 'down' else str(0) + ',') for x in up_down ]


print("starting program")
webcam_recording = []
web_thread = _thread.start_new_thread(record_webcam, (webcam_recording,))
while webcam_recording == []:
    pass

print("got okay to start recording")
record_keyboard()

print("done recording")

