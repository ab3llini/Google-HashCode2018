from text_parser.conventions import *
from text_parser.writer import *


def write_sol(id, name):
    path = get_sol(id, name)
    with TextWriter(path) as tw:
        pass

