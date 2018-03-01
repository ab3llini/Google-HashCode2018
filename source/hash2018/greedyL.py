from hash2018.utility import *
from text_parser.conventions import *
from hash2018.reader import *
from hash2018.writer import *


inst = HIGHBONUS

if __name__ == '__main__':
    problem = read_in(inst)
    avrides = problem[DATA][:]
    chrides = []
    pts = 0
    for index in range(problem[FLEET]):
        ch, av = schedule_car((0, 0), 0, avrides, problem[BONUS])
        chrides.append(ch)
        avrides = av
        pts += get_end_stats([problem[DATA][i] for i in chrides[-1]], problem[BONUS])[2]
        if len(avrides) == 0:
            break
        print("%d/%d" % (index, problem[FLEET]))
    print(pts)
    write_sol(inst, "greedyL%d" % pts, chrides)
