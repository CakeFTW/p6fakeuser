"This module contains the data_processing scrips"

import numpy as np



def circle_scale(data : np.ndarray, joint = 24):
    """Sets all key points relative to the center but scale 0-1 using screen dimensions"""
    if data.shape[1] != 75:
        print("wrong dimensions, DUDE! should be 75 MAAAAN")
        exit()

    print(data.shape)
    #remove confidence intervals



    # #scale according to hips
    # x_index = data[:,joint]
    # y_indey = data[:,joint + 1]
    # for i in range(25):
    #     data[:,i*3] = data[:,i*3] - x_index
    #     data[:,(i*3)+1] = data[:,(i*3)+1] - y_indey

    # #do min-max scaling but using the screen
    # for i in range(25):
    #     total = np.sqrt( np.square(data[:,i*3]) + np.square(data[:,(i*3)+1]))
    #     data[:,i*3] = data[:,i*3]/total
    #     data[:, (i*3)+1] = data[:,(i*3)+1]/total

    #remove confidence intervals
    data = np.nan_to_num(data)

    data_nci = np.delete(data,[3*x+2 for x in range(75)], 1)

    #remove unsued joints
    unused_joints = [0,10,13,11,14,15,16,17,18,19,20,21,22,23,24]

    unused_joints = [2*x for x in unused_joints]

    unused_joints = unused_joints + [x+1 for x in unused_joints]

    data_new = np.delete(data_nci, unused_joints, 1)

    return data_new

def circle_scale_all(data : np.ndarray):
    ln = data.shape[1]
    out_1 = circle_scale(data.copy())
    out_2 = circle_scale(data.copy())
    out_3 = circle_scale(data.copy())
    out_1 = np.append(out_1,out_2, axis=1)
    out_1 = np.append(out_1,out_3, axis=1)
    return out_1

def circle_scale_old(data : np.ndarray, joint = 24):
    """Sets all key points relative to the center but scale 0-1 using screen dimensions"""
    if data.shape[1] != 75:
        print("wrong dimensions, DUDE! should be 75 MAAAAN")
        exit()
    #scale according to hips
    x_index = data[:,joint]
    y_indey = data[:,joint + 1]
    for i in range(25):
        data[:,i*3] = data[:,i*3] - x_index
        data[:,(i*3)+1] = data[:,(i*3)+1] - y_indey

    #do min-max scaling but using the screen
    for i in range(25):
        total = np.sqrt( np.square(data[:,i*3]) + np.square(data[:,(i*3)+1]))
        data[:,i*3] = data[:,i*3]/total
        data[:, (i*3)+1] = data[:,(i*3)+1]/total
    data = np.nan_to_num(data)
    return data