import numpy as np
from hash2018.reader import *
from hash2018.utility import *


data = read_in(EXAMPLE)


UNBOUNDED = "0"
REACHING_RIDE = "1"
EXECUTING_RIDE = "2"

class Simulation:
    def __init__(self):

        self.time = 0
        self.end = data[SIMTIME]
        self.cars = [Car()] * data[FLEET]
        self.rides = data[DATA]

    def simulate(self):
        while self.time < self.end:
            for car in self.cars:
                car.simulate(self.time, self.rides)


class Car:
    def __init__(self):
        self.loc = [0, 0]
        self.status = UNBOUNDED
        self.current_ride = None
        self.history = []


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


    def assign_ride(self, ride):
        self.current_ride = ride

    def move_towards_point(self, p):
        if (self.loc[0] < p[0]):
            self.loc[0] = self.loc[0] + 1
            return
        if (self.loc[1] < p[1]):
            self.loc[1] = self.loc[1] + 1
            return
        if (self.loc[0] > p[0]):
            self.loc[0] = self.loc[0] - 1
            return
        if (self.loc[1] > p[1]):
            self.loc[1] = self.loc[1] - 1
            return

        # If we got here we reached the point
        if self.status is REACHING_RIDE:
            self.status = EXECUTING_RIDE

        if self.status is EXECUTING_RIDE:
            self.history.append(self.current_ride)
            self.current_ride = None
            self.status = UNBOUNDED

    def simulate(self, time, rides):
        if self.status is not UNBOUNDED:
            if self.status is REACHING_RIDE:
                self.move_towards_point(start_point(self.current_ride))
            else:
                self.move_towards_point(end_point(self.current_ride))

        else:
            # assign the best ride
            best_idx = 0
            best_utility = 0
            for i, ride in enumerate(rides):
                utility = self.utility(ride, time)
                if utility > best_utility:
                    best_idx = i
                    best_utility = utility

            print("Best utility = %s" % utility)

            self.current_ride = rides.pop(best_idx)


s = Simulation()
s.simulate()