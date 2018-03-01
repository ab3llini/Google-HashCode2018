from hash2018.utility import *
from text_parser.conventions import *
from hash2018.reader import *
from hash2018.writer import *


inst = METROPOLIS

if __name__ == '__main__':
    problem = read_in(inst)
    avrides = problem[DATA][:]
    chrides = []
    pts = 0
    nottakingbonus = [False for _ in range(problem[FLEET])]
    ended = [False for _ in range(problem[FLEET])]
    for index in range(problem[FLEET]):
        if ended[index]:
            continue
        ch, av = schedule_car((0, 0), 0, avrides, problem[BONUS], nottakingbonus[index])
        if len(ch) == 0:
            if nottakingbonus[index]:
                ended[index] = True
            else:
                nottakingbonus[index] = True
            if all(ended):
                break
        chrides.append(ch)
        avrides = av
        # pts += get_end_stats([problem[DATA][i] for i in chrides[-1]], problem[BONUS])[2]
        if len(avrides) == 0:
            break
        print("%d/%d" % (index, problem[FLEET]))
    while True:
        for index in range(problem[FLEET]):
            if ended[index]:
                continue
            sts = get_end_stats(chrides[index], problem[BONUS])
            ch, av = schedule_car(sts[0], sts[1], avrides, problem[BONUS], nottakingbonus[index])
            if len(ch) == 0:
                if nottakingbonus[index]:
                    ended[index] = True
                else:
                    nottakingbonus[index] = True
                if all(ended):
                    break
            chrides[index].extend(ch)
            avrides = av
            # pts += get_end_stats([problem[DATA][i] for i in chrides[-1]], problem[BONUS])[2]
            if len(avrides) == 0:
                break
            print("%d/%d" % (index, problem[FLEET]))
    # print(pts)
    write_sol(inst, "greedyL", chrides)
