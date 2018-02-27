from text_parser.parser import *
from text_parser.conventions import *

MUSH = 'M'
TOM = 'T'

HIGH = 'h'
LOW = 'l'
DATA = 'd'


def read_problem_instance(id):
    fname = get_in(id)
    with Parser(fname) as p:
        r, c, l, h = p.read_line()
        outmat = p.read_matrix(rows=r, cols=c,
                               column_splitter=lambda e: list(e),
                               mapper=lambda e: e)
        return {
            LOW: l,
            HIGH: h,
            DATA: outmat
        }


def read_problem_solution(id, name):
    fname = get_sol(id, name)
    with Parser(fname) as p:
        l = p.read_line()[0]
        sol = []
        for i in range(l):
            a, b, c, d = p.read_line()
            sol.append(np.array([[a, b], [c, d]]))
        return np.array(sol)


def read_all_solutions(id):
    names = get_sol_names_list(id)
    ret = []
    for n in names:
        ret.append(read_problem_solution(id, n))
    return ret
