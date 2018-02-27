from text_parser.writer import *
from text_parser.conventions import *
import numpy as np


def write_solution(id, name, solution):
    path = get_sol(id, name)
    with TextWriter(path) as tw:
        tw.write_line([np.shape(solution)[0]])
        for line in solution:
            tokens = np.reshape(line, (4,))
            tw.write_line(tokens)

