from text_parser.conventions import *
from text_parser.parser import *


def read_in(id):
    path = get_in(id)
    with Parser(path) as p:
        pass


def read_sol(id, name):
    path = get_sol(id, name)
    with Parser(path) as p:
        pass


def read_all_solutions(id):
    names = get_sol_names_list(id)
    ret = []
    for n in names:
        ret.append(read_sol(id, n))
    return ret
