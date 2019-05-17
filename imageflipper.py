import cv2
import os
from sys import argv

try:
    folder = argv[1]
except:
    print("no folder provided")
    exit()

origin = os.getcwd()

os.chdir(folder)

action_folder = os.listdir()

for actions in action_folder:
    os.chdir(actions)
    images = os.listdir()
    print(images)
    for image in images:
        img = cv2.imread(image)
        fliped_img = cv2.flip(img,1)

        cv2.imwrite("flipped_"+image, fliped_img)
    
    os.chdir("..")


