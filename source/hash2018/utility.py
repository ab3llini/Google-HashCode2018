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


def travtime(ride):
    return manhattan_dist(end_point(ride), start_point(ride))


def get_stats(posstart, tstart, bonus, ride):
    ttr = manhattan_dist(posstart, start_point(ride))
    ttrav = travtime(ride)
    flag = True
    if tstart + ttr + ttrav >= end_time(ride):
        flag = False
    bns = 0
    wait = start_time(ride) - tstart - ttrav
    if wait >= 0:
        bns = bonus
    else:
        wait = 0
    return (bns + ttrav), (ttr + ttrav + wait), flag

def utility(posstart, tstart, bonus, ride):
    ttr = manhattan_dist(posstart, start_point(ride))
    ttrav = travtime(ride)
    if tstart + ttr + ttrav >= end_time(ride):
        return 0
    bns = 0
    wait = start_time(ride) - tstart - ttrav
    if wait >= 0:
        bns = bonus
    else:
        wait = 0
    return (bns + ttrav)/(ttr + ttrav + wait)


def schedule_car(posstart, tsstart, avrides: list, bonus):
    avrides = avrides[:]
    chrides = []
    uts = [utility(posstart, tsstart, bonus, ride) for ride in avrides]
    chosen = int(np.argmax(uts))
    while uts[chosen] > 0:
        chrides.append(avrides[chosen][0])
        avrides.pop(chosen)
        tsstart += get_stats(posstart, tsstart, bonus, chrides[-1])[1]
        posstart = end_point(chrides[-1])
        uts = [utility(posstart, tsstart, bonus, ride) for ride in avrides]
        chosen = np.argmax(uts)
    return chrides, avrides
