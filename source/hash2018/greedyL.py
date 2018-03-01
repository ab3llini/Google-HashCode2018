from hash2018.utility import *
from text_parser.conventions import *
from hash2018.reader import *
from hash2018.writer import *


inst = METROPOLIS

if __name__ == '__main__':
    problem = read_in(inst)
    avrides = problem[DATA][:]
    chrides = [[] for _ in range(problem[FLEET])]
    pts = [0 for _ in range(problem[FLEET])]
    pos = [(0, 0) for _ in range(problem[FLEET])]
    ts = [0 for _ in range(problem[FLEET])]
    ended = [False for _ in range(problem[FLEET])]
    while not all(ended):
        for index in range(problem[FLEET]):
            if ended[index]:
                continue
            ch, av = schedule_car(pos[index], ts[index], avrides, problem[BONUS])
            stats = get_end_stats(chrides[index], bonus=problem[BONUS])
            if len(ch) == 0:
                ended[index] = True
            pts[index] = stats[2]
            pos[index] = stats[0]
            ts[index] = stats[1]
            chrides[index].extend(ch)
            avrides = av
            # pts += get_end_stats([problem[DATA][i] for i in chrides[-1]], problem[BONUS])[2]
            if len(avrides) == 0:
                break
            print("%d/%d" % (index, problem[FLEET]))
    # print(pts)
    write_sol(inst, "greedyL", chrides)
