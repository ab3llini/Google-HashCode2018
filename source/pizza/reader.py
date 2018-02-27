from text_parser.parser import *

import os.path as path


MUSH = 'M'
TOM = 'T'

def read_problem_instance(fname):
    with Parser(fname) as p:
        r, c, l, h = p.read_line()
        outmat = p.read_matrix(rows=r, cols=c,
                               column_splitter=lambda s: s.split(),
                               mapper= lambda e: e)
        return l, h, outmat


print(read_problem_instance())