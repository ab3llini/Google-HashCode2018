import numpy as np
from hash2018.reader import *
from hash2018.writer import *
from hash2018.utility import *
import random


data = read_in(SHOULDBEEASY)

BONUS = data[BONUS]

UNBOUNDED = "0"
REACHING_RIDE = "1"
EXECUTING_RIDE = "2"

class Simulation:
    def __init__(self):

        self.time = 0
        self.end = data[SIMTIME]

        self.cars = []
        for i in range(data[FLEET]):
            self.cars.append(Car())
        self.rides = data[DATA]

        #print("Number of cars = %d", len(self.cars))

    def simulate(self):
        while self.time < self.end and len(self.rides) > 0:
            #print("CURRENT TIME = %s" % self.time)
            for i, car in enumerate(self.cars):
                #print("SIMULATING CAR #%s" % i)
                car.simulate(self.time, self.rides)

            self.time = self.time + 1



class Car:
    def __init__(self):
        self.id = random.randint(1,101)
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
            #print("%s ::: Ride reached, Current loc = %s" % (self.id, self.loc))
            self.status = EXECUTING_RIDE
            return

        if self.status is EXECUTING_RIDE:
            #print("%s ::: Ride executed" % (self.id))
            self.history.append(self.current_ride)
            self.current_ride = None
            self.status = UNBOUNDED

    def simulate(self, time, rides):

        if len(rides) == 0:
            return

        if self.status is not UNBOUNDED:

            #print("%s ::: Current loc = %s" % (self.id, self.loc))

            if self.status is REACHING_RIDE:
                #print("%s ::: Moving towards ride %s..." % (self.id, start_point(self.current_ride)))
                self.move_towards_point(start_point(self.current_ride))
            else:
                #print("%s ::: Executing ride..." % self.id)
                self.move_towards_point(end_point(self.current_ride))

        else:
            # assign the best ride
            best_idx = 0
            best_utility = 0
            for i, ride in enumerate(rides):
                u = utility(self.loc, time, BONUS, ride)
                if u > best_utility:
                    best_idx = i
                    best_utility = u

            #print("%s ::: Best utility = %s" % (self.id, best_utility))
            self.current_ride = rides.pop(best_idx)

            #print("%s ::: Assigned ride #%s" % (self.id, best_idx))
            self.status = REACHING_RIDE
            self.simulate(time, rides)


s = Simulation()
s.simulate()


#print("Computing solution:")

sol = []

for car in s.cars:
    res = []
    for ride in car.history:
        res.append(ride[0])
    sol.append(res)

write_sol(EXAMPLE, "albi2", sol)


