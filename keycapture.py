import sys
import msvcrt
import subprocess
import time



stuff = []
stuffTime = []

print("press 'escape' to quit...")

while 1:
    if(msvcrt.kbhit() == True):
        char = msvcrt.getch()
        char = char.decode()
        if char == '\x1b':
            break
        stuff.append(char)
        stuffTime.append(time.time())
        print(stuff)


#adjust time stamps
stuffTime = [x-stuffTime[0] for x in stuffTime]


print(sys.argv)
path = sys.argv[0]

file = open("pythondata.txt","w")
file.write('PYTHON\n')
[file.write(x + ',') for x in stuff]
file.write('\n')
[file.write(str(x) + ',') for x in stuffTime]


