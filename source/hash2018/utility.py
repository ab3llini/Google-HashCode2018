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
    return (bns + ttrav) if flag else 0, (ttr + ttrav + wait), flag


def get_end_stats(schedule, bonus):
    pos = [0, 0]
    ts = 0
    pts = 0
    for ride in schedule:
        p, ts, _ = get_stats(pos, ts, bonus, ride)
        pos = end_point(ride)
        pts += p
    return pos, ts, pts


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


def takes_bonus(posstart, tstart, ride):
    ttr = manhattan_dist(posstart, start_point(ride))
    ttrav = travtime(ride)
    if tstart + ttr + ttrav >= end_time(ride):
        return False
    wait = start_time(ride) - tstart - ttrav
    if wait >= 0:
        return True
    return False


def schedule_car(posstart, tsstart, avrides: list, bonus, norm=True):
    avrides = avrides[:]
    chrides = []
    uts = [utility(posstart, tsstart, bonus, ride) for ride in avrides if norm or takes_bonus(posstart, tsstart, ride)]
    chosen = int(np.argmax(uts))
    chut = uts[chosen]
    while chut > 0:
        chrides.append(avrides[chosen][0])
        tsstart += get_stats(posstart, tsstart, bonus, avrides[chosen])[1]
        posstart = end_point(avrides[chosen])
        avrides.pop(chosen)
        uts = [utility(posstart, tsstart, bonus, ride) for ride in avrides if norm or takes_bonus(posstart, tsstart, ride)]
        if len(uts) > 0:
            chosen = np.argmax(uts)
            chut = uts[chosen]
        else:
            chut = 0
    return chrides, avrides
