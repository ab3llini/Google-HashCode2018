from text_parser.resources import *

EXAMPLE = 'example'
SMALL = 'small'
MEDIUM = 'medium'
BIG = 'big'

IN_EXT = ".in"
SOL_EXT = ".sol"


def get_dir(id):
    return res_path(id)


def get_in(id):
    return os.path.join(get_dir(id), get_in_name(id))


def get_sol(id, name):
    return os.path.join(get_dir(id), name + SOL_EXT)


def get_in_name(id):
    return id + IN_EXT