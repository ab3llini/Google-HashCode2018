from text_parser.conventions import *
from text_parser.writer import *


def write_sol(id, name, sol):
    path = get_sol(id, name)
    with TextWriter(path) as tw:
        for ride in sol:
            out = [len(ride)]
            out.extend(ride)
            tw.write_line(out)
