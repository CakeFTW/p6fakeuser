from os import *
import shutil
from sys import argv
import datetime


def call_openpose_on_folder(path):
    out_dir = getcwd()

    try:
        folders_to_call_on = listdir(argv[1])
    except:
        print("no folder path provided")

    try:
        mkdir(argv[1] + "_poses")
    except:
        print("folder already exists")

    chdir(r"D:\Openpose\openpose-master")

    pose_path = r'build-old\x64\Release\openposedemo.exe'
    

    #pose_flags = r' --display 0 --render_pose 0'
    pose_flags = r""


    for folder in folders_to_call_on:
        pose_media = "--image_dir " + out_dir + "/" + argv[1]+ "/" + folder
        output_dest = "--write_json " + out_dir + "/" + argv[1] + "_poses/" +folder

        try:
            system("{} {} {} {}".format(pose_path, pose_media, output_dest, pose_flags))
        except:
            print("error trying to start open pose")
            exit()


call_openpose_on_folder(argv)





