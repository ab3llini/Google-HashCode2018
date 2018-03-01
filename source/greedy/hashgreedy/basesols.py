from hash2018 import reader
from hash2018 import writer
from text_parser import conventions
import numpy as np

def perctime(ride):
    return abs(ride[2][0] - ride[1][0]) + abs(ride[2][1] - ride[1][1])


def percasstart(ride):
    return ride[1][0] + ride[1][1]


def reachableasfirst(ride):
    return percasstart(ride) < ride[3][1] - perctime(ride)


def compatible(ride1, ride2):
    return ride1[3][1] + abs(ride1[2][0] - ride2[1][0]) + abs(ride1[2][1] - ride2[1][1]) + perctime(ride2) < ride2[3][1]

set = conventions.HIGHBONUS

data = reader.read_in(set)

ncars = data[reader.FLEET]

ris = []

rides = data[reader.DATA]
nrides = len(rides)
used = np.zeros([nrides])
for _ in range(ncars):
    carsol = []
    first = True
    for i in range(nrides):
        if used[i] == 0 and first:
            if reachableasfirst(rides[i]):
                carsol.append(i)
                used[i] = 1
                first = False
        else:
            if used[i] == 0 and not first:
                if compatible(rides[carsol[len(carsol)-1]], rides[i]):
                    carsol.append(i)
                    used[i] = 1
    ris.append(carsol)

writer.write_sol(set, "highbonfirst", ris)
