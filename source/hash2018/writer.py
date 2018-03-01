from text_parser.conventions import *
from text_parser.writer import *


def write_sol(id, name, sol):
    path = get_sol(id, name)
    print(sol)
    with TextWriter(path) as tw:
        for ride in sol:
            print(ride)
            out = [len(ride)]
            out.extend(ride)
            print(out)
            tw.write_line(out)
