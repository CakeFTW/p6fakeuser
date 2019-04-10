
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

def pythonread(key: str = '', timeOfAction: float = 0.0, action: bool = False):
    pass

def unityread(key: str = '', timeOfAction: float = 0.0, action: bool = False):
    timeStart = time.time()

    print(action)


    for k,t,a in zip(key,timeOfAction,action):
    
        #wait until time stamp
        while time.time() < timeStart + t:
            pass
        
        #perform the correct action
        if a:
            gui.keyDown(k, _pause=False)
        else:
            gui.keyUp(k, _pause=False)


if "UNITY" in headertype:
    unityread(data1, [float(x) for x in data2], [1 if b in "True" else 0 for b in data3])
    #unity interpret
    pass
elif "PYTHON" in headertype:
    #python interpret
    pass
else:
    print("Header not supported")




# keys = file.readline().split(',')[0:-1]
# b = file.readline().split(',')[0:-1]
# keyTime = [float(x) for x in b]

# file.close()
# del(file)

# time.sleep(3)

# timeNow = time.time()

# for k,t in zip(keys,keyTime):
#     gui.keyDown(k, _pause=False)
#     while time.time() < timeNow + t:
#         pass
#     gui.keyUp(k, _pause=False)

