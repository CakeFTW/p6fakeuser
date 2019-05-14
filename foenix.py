from sys import argv
from os import *
import keyboard as kb
from keras.models import load_model
import datetime
import _thread
from time import sleep,time

#script for running open pose with the arguments
#1 path to the model to use
#2 to use controls or not

control = False
try:
    if "control" in argv[2]:
        control = True
except:
    pass

# try:
#     model = load_model(argv[1])
# except:
#     print("Could not find model at:", argv[1])
#     exit()

#open openpose webcam and set output
openpose_folder = r"C:\Users\Rasmus\Downloads\openpose-1.4.0-win64-gpu-binaries_recommended\openpose-1.4.0-win64-gpu-binaries" #has to be set by user

openpose_path = r"bin\OpenPoseDemo.exe"
timestamp = str(int(datetime.datetime.now().timestamp()))

json_dir = openpose_folder+ "/model_test" + timestamp + "/"

chdir(openpose_folder)
print(getcwd())

def start_open_pose():
    system("{} {}".format(openpose_path,"--write_json " + json_dir))


pose_thread = _thread.start_new_thread( start_open_pose , ())

#wait for the folder to be created
while True:
    sleep(0.1)
    if json_dir in listdir():
        break


while True:
    sleep(0.095)
    for file in listdir():
        if time() - path.getctime(file) > 2:
            print("deleting:", file)
            remove(file) 


