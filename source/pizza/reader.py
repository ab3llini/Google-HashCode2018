from text_parser.parser import *
from text_parser.resources import *
from text_parser.conventions import *

import os.path as path


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



print(read_problem_instance(res_path(path.join("datasets", "small.in"))))