from sys import argv
import os
import datetime
import cv2
import json

origin = os.getcwd()


#create output destination 
out_folder =  "frames" + str(int(datetime.datetime.now().timestamp()))
os.mkdir(out_folder)
out_folder = origin + "/" + out_folder

try:
    os.chdir(argv[1])
    folder =os.getcwd()
except:
    print("no folder provided")
    exit()

try:
    frameskip = int(argv[2])
except:
    frameskip = 0



def save_frame (frame, label, n, capture, file_name, out_folder):
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame)
    res, frame = capture.read()
    imageName = file_name+"_"+str(label)+"_"+str(n)+".png"
    try:
        os.mkdir(out_folder+ "/" + file_name)
    except:
        pass

    try:
        os.mkdir(out_folder+ "/" + file_name +"/"+ str(label))
    except:
        pass

    cv2.imwrite(out_folder + "/" +file_name+ "/"+ str(label) + "/" + imageName,frame)






subfolders = os.listdir()

#for all subfolder loop through them, load and save the corresponding frames
for participant in subfolders:
    names = os.listdir(participant)
    print(names)
    vid_pos = ['.avi' in x for x in names]
    if True not in vid_pos:
        print("missing either json or avi file")
    json_pos = ['.json' in x for x in names]
    if True not in json_pos:
        print("missing either json or avi file")
    
    file = open(participant + "/" + names[json_pos.index(True)], 'r')
    rec = json.load(file)

    cap = cv2.VideoCapture(participant + "/" + names[vid_pos.index(True)])

    print("----processing",participant,"---")
    for n in range(len(rec[1])):
        
        save_frame(rec[4][n]+frameskip,rec[1][n],n,cap,participant,out_folder)

    

os.chdir(origin)


