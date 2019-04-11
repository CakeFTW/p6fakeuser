
#imports
import sys
import pyautogui as gui
import time


print("press 'escape' to quit...")

file = open("unitydata.txt","r")
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
    timeStart = time.time()

    for k,t,a in zip(key,timeOfAction,action):
    
        #wait until time stamp
        while time.time() < timeStart + t+delay:
            pass
        
        #perform the correct action
        if a:
            gui.keyDown(k, _pause=False)
        else:
            gui.keyUp(k, _pause=False)

#call corresponsing functions depending on file header
if "UNITY" in headertype:
    unityread(data1, [float(x) for x in data2], [1 if b in "True" else 0 for b in data3])

elif "PYTHON" in headertype:
    pythonread(data1, [float(x) for x in data2])

else:
    print("Header not supported")