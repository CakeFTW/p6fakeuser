
#imports
import sys
import pyautogui as gui
import time
import keyboard as kb
from numpy import std

print("okay, sending input")

file = open("keyboard.txt","r")
headertype = file.readline()
data1 = file.readline().split(',')[0:-1]
data2 = file.readline().split(',')[0:-1]
data3 = file.readline().split(',')[0:-1]

def pythonread(key: str = '', timeOfAction: float = 0.0, delay = 0):
    "inputs keys captured from python, format is - keys, time since begining, delay until starting to play"
    time.sleep(3)

    timeNow = time.time()

    for k,t in zip(key,timeOfAction):
        gui.keyDown(k, _pause=False)
        while time.time() < timeNow + t + delay:
            pass
        gui.keyUp(k, _pause=False)

def unityread(key: str = '', timeOfAction: float = 0.0, action: bool = False, delay = 0.0):
    "inputs keys captured from unity, format is - keys, time since begining, up or down, delay until starting to play"
    timeStart = time.time() + delay

    for k,t,a in zip(key,timeOfAction,action):
        #wait until time stamp
        
        while time.time() < (timeStart + t):    
            pass
        print(time.time() - (timeStart +t))
        
        #perform the correct action
        if a:
            gui.keyDown(k, _pause=False)
        else:
            gui.keyUp(k, _pause=False)

def keyboard_read(key: int = 0, timeOfAction: float = 0.0, action: bool = False, delay = 0.0):
    "inputs keys captured from keyboard, format is - keys, time since begining, up or down, delay until starting to play"
    time.sleep(delay)


    time_dif = []
    state = kb.stash_state()
    a = kb.start_recording()
    kb.stop_recording()
    timeStart = time.time()
    last_time = None
    for k,t,a in zip(key,timeOfAction,action):
        sleep_until = float(timeStart+ t)
        while time.time() < sleep_until:
            pass
        kb.press(k) if a == True else kb.release(k)
        time_dif.append(time.time() - float(timeStart+ t))

    kb.restore_modifiers(state)
    return time_dif

#call corresponsing functions depending on file header
if "UNITY" in headertype:
    unityread(data1, [float(x) for x in data2], [1 if b in "True" else 0 for b in data3],3.0)

elif "PYTHON" in headertype:
    pythonread(data1, [float(x) for x in data2])

elif "KEYBOARD" in headertype:
    totals = []
    for i in range(1):
        totals.append(keyboard_read([int(x) for x in data1], [float(x) for x in data2], [1 if b in "1" else 0 for b in data3],0))

    means = [std([col[i] for col in totals])/len(totals) for i in range(len(totals[0]))]

    print(means)

else:
    print("Header not supported")

