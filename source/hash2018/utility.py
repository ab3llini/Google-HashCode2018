import numpy as np

def manhattan_dist(p1, p2):
    return np.abs(p1[0] - p2[0]) + np.abs(p1[1] - p2[1])

def start_time(ride):
    return ride[3][0]

def end_time(ride):
    return ride[3][1]

def start_point(ride):
    return [ride[1][0], ride[1][1]]

def end_point(ride):
    return [ride[2][0], ride[2][1]]