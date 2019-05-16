"This module contains the data_processing scrips"

import numpy as np



def circle_scale(data : np.ndarray, joint = 24):
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

def circle_scale_all(data : np.ndarray):
    ln = data.shape[1]
    out_1 = circle_scale(data.copy())
    out_2 = circle_scale(data.copy())
    out_3 = circle_scale(data.copy())
    out_1 = np.append(out_1,out_2, axis=1)
    out_1 = np.append(out_1,out_3, axis=1)
    return out_1
