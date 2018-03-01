from hash2018 import reader
from hash2018 import writer
from text_parser import conventions
from random import *
import numpy as np

def perctime(ride):
    return abs(ride[2][0] - ride[1][0]) + abs(ride[2][1] - ride[1][1])


def percasstart(ride):
    return ride[1][0] + ride[1][1]

def bonusnotfirst(ride1, ride2):
    return abs(ride1[2][0]-ride2[1][0]) + abs(ride1[2][1]-ride2[1][1]) < ride2[3][0]


def reachableasfirst(ride):
    return percasstart(ride) < ride[3][1] - perctime(ride)


def compatible(ride1, ride2):
    return ride1[3][1] + abs(ride1[2][0] - ride2[1][0]) + abs(ride1[2][1] - ride2[1][1]) + perctime(ride2) < ride2[3][1]


def main(n):
    set = conventions.HIGHBONUS

    data = reader.read_in(set)
    data_copy = reader.read_in(set)

    ncars = data[reader.FLEET]

    ris = []

    rides = data[reader.DATA]
    rides_copy = data_copy[reader.DATA]
    nrides = len(rides)
    used = np.zeros([nrides])
    times = np.zeros([ncars])
    max_time = data[reader.SIMTIME]
    carnum = 0
    for _ in range(ncars):
        carsol = []
        first = True
        for i in range(nrides):
            if times[carnum] < max_time:
                if used[i] == 0 and first:
                    if reachableasfirst(rides[rides_copy[i][0]]):
                        carsol.append(i)
                        used[i] = 1
                        first = False
                        times[carnum] = max([rides[rides_copy[carsol[i]][0]][3][1] for i in range(len(carsol))])
                else:
                    if used[i] == 0 and not first:
                        nparrides = len(carsol)
                        for ridesolind in range(nparrides):
                            if nparrides == 1:
                                if compatible(rides[carsol[ridesolind]], rides[rides_copy[i][0]]):
                                    carsol.append(i)
                                    used[i] = 1
                                    times[carnum] = max([rides[rides_copy[carsol[i]][0]][3][1] for i in range(len(carsol))])
                            else:
                                if ridesolind != nparrides - 1:
                                    if bonusnotfirst(rides[carsol[ridesolind]], rides[rides_copy[i][0]]) and \
                                            bonusnotfirst(rides[rides_copy[i][0]], rides[carsol[ridesolind +1]]):
                                        carsol.append(i)
                                        used[i] = 1
                                        times[carnum] = max([rides[rides_copy[carsol[i]][0]][3][1] for i in range(len(carsol))])
                                else:
                                    if compatible(rides[carsol[ridesolind]], rides[rides_copy[i][0]]):
                                        carsol.append(i)
                                        used[i] = 1
                                        times[carnum] = max(
                                            [rides[rides_copy[carsol[i]][0]][3][1] for i in range(len(carsol))])
        ris.append(carsol)
        carnum += 1

    writer.write_sol(set, "highbonfirst" + str(n), ris)


if __name__ == '__main__':
    main(102)
