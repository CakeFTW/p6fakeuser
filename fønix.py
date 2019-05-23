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
import dataprocess as dp
import pickle
#script for running open pose with the arguments
#1 path to the model to use
#2 to use controls or not

control = False

model_path1 = "knn_final.sav"
model_path2 = "dt.pkl"

try:
    if "control" in argv[2]:
        control = True
except:
    pass

model1 = pickle.load(open(model_path1, 'rb'))
model2 = pickle.load(open(model_path2, 'rb'))


#open openpose webcam and set output
openpose_folder = r"D:\Openpose\openpose-master" #has to be set by user

openpose_path = r"build-old\x64\Release\OpenPoseDemo.exe"
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
    sleep(0.01)
    #print(listdir())
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
    key_codes = [16,17,23,31,36,37,38]
    kb._listener.start_if_necessary()
    try:
        f = open(newest_file, 'r')
        #load newsest file
        try:
            data = json.load(f)["people"][0]["pose_keypoints_2d"]
            #print(data)
            try:
                arrayz = np.zeros((1,75))
                arrayz[0] = data
                data_transformed = dp.circle_scale(arrayz) 
                class_number = model1.predict(data_transformed)
                # down_detector = model2.predict(data_transformed)
                # if down_detector[0][5] == 1 & control:
                #     kb.press_and_release(37)
                #     print("down detector")

                pred_key = np.argmax(class_number[0])
                print(pred_key, "with probability " , class_number[0,pred_key])

                if(class_number[0,pred_key] > 0.6):
                    if(control):
                        kb.press_and_release(key_codes[pred_key])


                

            except Exception as ex:
                print(ex)
                print("problem with model")
        except:
            print("can't open newest file")
    except:
        print("can't open newest file")
    

