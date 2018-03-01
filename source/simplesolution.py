import numpy as np
from hash2018.reader import *


data = read_in(EXAMPLE)
rides = data[DATA]

class Simulation:
    def __init__(self):
        self.time = 0


class Car:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return "x=%d, y=%s" % (self.x, self.y)

    def utility(self, ride, time):
        distance = np.abs(ride[1][0] - self.x) + np.abs(ride[1][1] - self.y)

        ridestart = ride[3][0]

        if (ridestart - time) < distance:
            return 0
        else:
            gain = np.abs(ride[2][0] - ride[1][0]) + np.abs(ride[1][1] - ride[1][1])


cars = [Car()] * data[FLEET]

for car in cars:
    print(car)
print(rides)

