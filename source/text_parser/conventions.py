from text_parser.resources import *

EXAMPLE = 'example'
SHOULDBEEASY = 'shouldbeeasy'
NOHURRY = 'nohurry'
METROPOLIS = 'metropolis'
HIGHBONUS = 'highbonus'

IN_EXT = ".in"
SOL_EXT = ".txt"


def get_dir(id):
    return res_path(id)


def get_in(id):
    return os.path.join(get_dir(id), get_in_name(id))


def get_sol(id, name):
    return os.path.join(get_dir(id), name + SOL_EXT)


def get_in_name(id):
    return id + IN_EXT


def get_sol_names_list(id):
    base = get_dir(id)
    sols = []
    for file in os.listdir(base):
        name, ext = os.path.splitext(file)
        if ext == SOL_EXT:
            sols.append(name)
    return sols
