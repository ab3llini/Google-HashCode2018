import os
import re
import numpy as np


def _robust_str_int_cast(in_str):
    """

    Parse a single string token to int
    making sure to clean any non-digit char.
    :return: the int obtained by concatenated all digits in in_str,
    None if no digits are present.
    """
    clean = re.sub('[^0-9-]+', '', in_str)
    if clean != '':
        return int(clean)
    return None


def _map(in_lst, mapper):
    """
    Perform a mapping of all elements in the list according to a mapper

    :param in_lst:  iterable list of elements to be mapped
    :param mapper:  function that maps the single token in the list,
                    must output None if a token is unwanted
    :return:    the list of the outputs of the mapper with regards to the in_lst,
                in the same order of appearance.
    """
    ret = []
    for elem in in_lst:
        r = mapper(elem)
        if r is not None:
            ret.append(r)
    return ret


def _space_splitter(in_str):
    return in_str.split(' ')


class Parser:
    def __init__(self, in_f):
        self.__filein = in_f
        self.__in = None

    def __enter__(self):
        """
        Called when entering a with context. Opens the input file.
        """
        self.start()
        return self

    def __exit__(self, tp, value, traceback):
        """
        Called when terminating a with context. Closes the input file.
        """
        self.close()

    def close(self):
        self.__in.close()

    def start(self):
        self.__in = open(self.__filein)

    def read_line(self, reducer=lambda *x: x, splitter=_space_splitter, mapper=_robust_str_int_cast):
        """
        Perform a single line map-reduce parsing:
        1) the next line is read from the file (until a \n is found. \n is NOT included)
        2) the line is separated into tokens, based on the splitter function.
        3) the tokens are mapped according to the mapper function
        4) the list of mapped tokens is reduced through the reducer. Tokens are passed as varargs
        :param reducer: reduction applied at step 4. By default, output inputs as a tuple
        :param splitter: the function used to split the line into tokens. Space-split by default
        :param mapper: the function to map string tokens to useful elements. A robust cast to int by default
        :return: the result of the reduction of step 4, whatever it is.
        """
        tokens = splitter(self.__in.readline()[:-1])
        return reducer(*_map(tokens, mapper))

    def read_matrix(self, rows, cols, column_splitter=_space_splitter, mapper=_robust_str_int_cast):
        """
        Read multiple lines in order to directly extract a matrix of tokens
        :param rows: expected rows of the matrix.
        :param cols: expected cols of the matrix.
        :param column_splitter: splitter used to separate a row in the file
                        into its component tokens. Space-split by default
        :param mapper: the function to map string tokens to useful elements.
                        A robust cast to int by default
        :return: a numpy matrix containing rows * cols tokens read from the input file
        """
        mat = []
        warned = False
        for _ in range(rows):
            row = self.read_line(reducer=lambda *x: list(x), mapper=mapper, splitter=column_splitter)
            if not warned and len(row) != cols:
                print("Warning: row with unexpected number of tokens has been found")
                warned = True
            mat.append(row)
        return np.array(mat)
