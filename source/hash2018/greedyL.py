from hash2018.utility import *
from text_parser.conventions import *
from hash2018.reader import *
from hash2018.writer import *


inst = EXAMPLE

if __name__ == '__main__':
    problem = read_in(inst)
    avrides = problem[DATA]
    chrides = []
    for _ in range(problem[FLEET]):
        ch, av = schedule_car((0, 0), 0, avrides, problem[BONUS])
        chrides.append(ch)
        avrides = av
        if len(avrides) == 0:
            break

    write_sol(inst, "greedyL", chrides)