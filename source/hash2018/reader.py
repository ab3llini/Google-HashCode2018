from text_parser.conventions import *
from text_parser.parser import *

def read_in(id):
    path = get_in(id)
    with Parser(path) as p:
        pass