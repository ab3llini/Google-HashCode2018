import numpy as np
from hash2018.reader import *
from hash2018.utility import *


data = read_in(EXAMPLE)
rides = data[DATA]

class Simulation:
    def __init__(self, start, end):

        self.time = start
        self.end = end

    def simulate(self):
        while self.time < self.end:



class Car:
    def __init__(self):
        self.loc = [0, 0]

    def __str__(self):
        return "x=%d, y=%s" % (self.x, self.y)

    def utility(self, ride, now):

        timetoreach = manhattan_dist(ride[1], self.loc)
        ridestart = start_time(ride)

        bonus = 0

        if (ridestart - now) == timetoreach:
            bonus = data[BONUS];

        gain = manhattan_dist(ride[2], ride[1])

        timetowait = 0

        if (ridestart - now) >= 0:
            timetowait = start_time(ride) - timetoreach - now

        timetotravel = gain

        return (gain + bonus) / (timetoreach + timetowait + timetotravel)

