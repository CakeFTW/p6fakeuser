import os
from sys import argv
import json
from time import time
import pandas

start_time = time()
try:
    dirs =  os.listdir(argv[1])
except:
    print("no folder provided")

origin = os.getcwd()

paths_to_folders = []

data = []
labels = []
for path in dirs:
    os.chdir(origin + "/" + argv[1] + "/" + path)
    files = os.listdir()
    for file in files:
        f = open(os.getcwd() + "/"+file, "r")
        tmp_store = json.load(f)["people"]
        if len(tmp_store) != 1:
            break
        data.append(tmp_store[0]["pose_keypoints_2d"])
        labels.append(path)
    print("loaded :", path)

out_data = pandas.DataFrame(data)
out_labels = pandas.DataFrame(labels)

os.chdir(origin)
# out_put = file("")
# file_data = open("dataframe_keypoint",'a')
# file_labels = open("dataframe_labels", 'a')
# json.dump()

out_data.to_csv("dataframe_data.csv",index=False)
out_labels.to_csv("dataframe_labels.csv", index=False)


print(out_data.head())
print(out_labels.head())
print("done in", (time() - start_time), " seconds")


