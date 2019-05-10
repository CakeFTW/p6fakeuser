from os import *
import shutil
from sys import argv
import datetime

try:
    a = listdir(argv[1])
except:
    print("no path provided as first argument")
    exit()
main_folder = argv[1]

out_dir = "imgs_from_" + str(int(datetime.datetime.now().timestamp()))
mkdir(out_dir)

list_of_files = []
dir_to_check = [x for x in a if "participant" in x]
print(main_folder)
print(dir_to_check)
for participants in dir_to_check:
    action_folder = listdir("{}/{}".format(main_folder,participants))
    for action in action_folder:
        #try to make the folder the we need to move the images to
        try:
            mkdir("{}/{}".format(out_dir,action))
        except:
            pass
        images = listdir("{}/{}/{}".format(main_folder,participants,action))
        for img in images:

            img_path = "{}/{}/{}/{}".format(main_folder,participants,action,img)
            list_of_files.append(img_path)

            dest_path = "{}/{}".format(out_dir,action)

            shutil.copy(img_path, dest_path)




    print("--------- {} of {} processed: {}".format(dir_to_check.index(participants)+1,len(dir_to_check),participants))

print("renaming 36 to 38, and 38 to 36")

name = listdir(out_dir)
if "36" in name:
    rename(out_dir + "/" + "36", out_dir + "/" + "tmp")
if "38" in name:
     rename(out_dir + "/" + "38", out_dir + "/" + "36")
name = listdir(out_dir)
if "tmp" in name:
    rename(out_dir + "/" + "tmp", out_dir + "/" + "38")

print("it is done my brother!!!")