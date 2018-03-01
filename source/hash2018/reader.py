from text_parser.conventions import *
from text_parser.parser import *


ROWS = 'r'
COLS = 'c'
FLEET = 'f'
RIDES = 'n'
BONUS = 'b'
SIMTIME = 't'
DATA = 'd'


def read_in(id):
    path = get_in(id)
    ret = {}
    with Parser(path) as p:
        R, C, F, N, B, T = p.read_line()
        ret[ROWS] = R
        ret[COLS] = C
        ret[FLEET] = F
        ret[RIDES] = N
        ret[BONUS] = B
        ret[SIMTIME] = T
        data = []
        for idx in range(N):
            ride = p.read_line()
            data.append([idx, [ride[0], ride[1]], [ride[2], ride[3]], [ride[4], ride[5]]])
        ret[DATA] = data
        return ret


def read_sol(id, name):
    path = get_sol(id, name)
    sol = []
    with Parser(path) as p:
        tokens = (0,)
        while len(tokens) != 0:
            tokens = p.read_line()
            if len(tokens) != 0:
                sol.append(np.array(tokens[1:]))
    return np.array(sol)


def read_all_solutions(id):
    names = get_sol_names_list(id)
    ret = []
    for n in names:
        ret.append(read_sol(id, n))
    return ret
