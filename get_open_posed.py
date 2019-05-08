import sys
import os
import datetime
import cv2

delay = 0.0

def save_frame (frame, label, n, capture, file_name, out_folder):
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame)
    res, frame = capture.read()
    imageName = file_name+"_"+str(label)+"_"+str(n)+".png"
    try:
        os.mkdir(out_folder+ "/" + str(label))
    except:
        pass

    cv2.imwrite(out_folder + "/" + str(label) + "/" + imageName,frame)

def save_everything(path_vid, path_key,output_folder):
    #open video
    cap = cv2.VideoCapture(path_vid)
    fps = cap.get(cv2.CAP_PROP_FPS)
    #open keylogger file corresponding to video
    file = open(path_key,"r")
    headertype = file.readline()
    data1 = file.readline().split(',')[0:-1]
    data2 = file.readline().split(',')[0:-1]
    data3 = file.readline().split(',')[0:-1]

    key = [int(x) for x in data1]
    timeOfAction = [float(x) for x in data2]
    action = [1 if b in "1" else 0 for b in data3]

    for k,t,a,n in zip(key[-2:],timeOfAction[-2:],action[-2:],range(2)):
        if a==True:
            save_frame((t + delay)*fps,k,n,cap,path_vid[5:-4],output_folder)
            print(t + delay)


#setting variables
folder = ""
if(len(sys.argv)>1):
    folder = sys.argv[1]
else:
    print("no folder provided")
    exit()

try:
    delay = float(sys.argv[2])
except:
    pass
print("""running function on folder: "{}" with video time shift of {} secs """.format(folder, str(delay)))
#create folder for folding the ouput

#getting file paths in order
os.chdir(sys.argv[1])
out_folder =  "sorted_frames_" + str(int(datetime.datetime.now().timestamp())) + ".data"
os.mkdir(out_folder)
folder = os.listdir()
txt = folder.index('txt')
vid = folder.index('vid')


txt_files = [(folder[txt]+ "//" + file_name) for file_name in os.listdir(folder[txt])]
vid_files = [(folder[vid]+ "//" + file_name) for file_name in os.listdir(folder[vid])]

i = 0
total = len(vid_files)
for path_vid,path_key in zip(vid_files,txt_files):
    save_everything(path_vid,path_key,out_folder)
    i = i + 1
    print("-------------" ,i, "of", total, "-----------", path_vid)
