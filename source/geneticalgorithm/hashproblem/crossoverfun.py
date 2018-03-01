def crossoverfun(sched1, sched2, ts_split, ridesdata):
    newsched = []
    for car in sched1:
        partsol = []
        for ind in car:
            if ridesdata[ind][3][1] < ts_split:
                partsol.append(ind)
        newsched.append(partsol)
    num = len(sched2)
    for i in range(0, num):
        car = sched2[i]
        for ind in car:
            if ridesdata[ind][3][1] < ts_split:
                newsched[car].append(ind)
