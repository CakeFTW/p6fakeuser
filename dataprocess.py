"This module contains the data_processing scrips"

import numpy as np



def circle_scale(data : np.ndarray):
    """Sets all key points relative to the center but scale 0-1 using screen dimensions"""
    if data.shape[1] != 75:
        print("wrong dimensions, DUDE! should be 75 MAAAAN")
        exit()
    #scale according to hips
    hip_index = data[:,24]
    hip_indey = data[:,25]
    for i in range(25):
        data[:,i*3] = data[:,i*3] - hip_index
        data[:,(i*3)+1] = data[:,(i*3)+1] - hip_indey

    #do min-max scaling but using the screen
    for i in range(25):
        total = np.sqrt( np.square(data[:,i*3]) + np.square(data[:,(i*3)+1]))
        data[:,i*3] = data[:,i*3]/total*100
        data[:, (i*3)+1] = data[:,(i*3)+1]/total*100
    data = np.nan_to_num(data)
    return data