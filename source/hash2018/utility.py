import numpy as np

def manhattan_dist(p1, p2):
    np.abs(p1[0] - p2[0]) + np.abs(p1[1] - p2[1])

def start_time(ride):
    return ride[3][0]

def end_time(ride):
    return ride[3][1]