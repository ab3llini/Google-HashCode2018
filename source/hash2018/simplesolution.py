import numpy as np
from hash2018.reader import *
from hash2018.utility import *


data = read_in(EXAMPLE)
rides = data[DATA]

class Simulation:
    def __init__(self, start, end):

        self.time = start
        self.end = end

    def


class Car:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return "x=%d, y=%s" % (self.x, self.y)

    def utility(self, ride, now):

        timetoreach = np.abs(ride[1][0] - self.x) + np.abs(ride[1][1] - self.y)
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




for car in cars:
    print(car)
print(rides)

