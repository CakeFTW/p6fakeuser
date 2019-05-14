from sys import argv
from os import chdir, listdir, remove, getcwd, system, path
import keyboard as kb
from keras.models import load_model
import datetime
import _thread
from time import sleep,time
import json
from keras.models import Sequential
import numpy as np

#script for running open pose with the arguments
#1 path to the model to use
#2 to use controls or not

control = False
try:
    if "control" in argv[2]:
        control = True
except:
    pass

try:
    model = load_model(argv[1])
except:
    print("Could not find model at:", argv[1])
    exit()

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

kb.start_recording
#wait for the folder to be created
while True:
    try:
        sleep(1)
        chdir(json_dir)
        break
    except:
        print("waiting for json folder to be created")

print("found the folder")



while True:
    sleep(0.095)
    print(listdir())
    #delete old files
    newest_file = ""
    largest_time = 0
    for file in listdir():
        time_of_file = path.getctime(file)

        #if file is newer than the newest file, it is the newest
        if time_of_file > largest_time:
            newest_file = file
            largest_time = time_of_file

        #delete file if folder than two seconds
        if time() - time_of_file > 3:
            remove(file) 
            pass
    
    data = []
    key_codes = [17,23,31,36,17,38]
    try:
        f = open(newest_file, 'r')
        #load newsest file
        try:
            data = json.load(f)["people"][0]["pose_keypoints_2d"]
            #print(data)
            try:
                arrayz = np.zeros((1,75))
                arrayz[0] = data
                class_number = model.predict_classes(arrayz)
                if(control):
                    kb.press(key_codes[class_number[0]])
                else:
                    print(key_codes[class_number[0]])

            except Exception as ex:
                print(ex)
                print("problem with model")
        except:
            print("can't open newest file")
    except:
        print("can't open newest file")
    

