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
        self.__in = open(in_f)

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

    def close(self):
        """
        remember to close the file!
        """
        self.__in.close()


# just test... but you will need to produce a file first!
fin = os.path.abspath('/home/luca/Scrivania/test.txt')
print("--- Input file content: ---\n")
with open(fin) as f:
    for line in f:
        print(line, end='')
print("--- end of file content ---\n\n")
p = Parser(fin)


def reduce_sum(*args):
    s = 0
    for i in args:
        s += i
    return s


def alternative_mapper(token):
    clean = re.sub("[^0-9-.]+", '', token)
    if clean != '':
        return float(clean)
    return None


class ATestClass:
    def __init__(self, a, b):
        self.prod = a * b
        self.sum = a + b

    def __str__(self):
        return "I am the test class.\nproduct: " + str(self.prod) + "\nsum: " + str(self.sum)


# Test basic matrix reading:
print(p.read_matrix(rows=3, cols=3))
# Test custom-splitter matrix reading:
print(p.read_matrix(rows=4, cols=3, column_splitter=lambda s: list(s), mapper=lambda t: t))
# Test a custom robust reducer
print(p.read_line(reducer=reduce_sum))
# Test the default reducer
print(p.read_line())
# Note: here we are testing non-robust reducers: this constructor wants exactly 2 integers.
# Should raise an exception if more than 2 are given.
print(p.read_line(reducer=ATestClass))
# Test also with a different mapper
print(p.read_line(reducer=reduce_sum, mapper=alternative_mapper))
print(p.read_line())
print(p.read_line())
# Again a test with the most elementary and non-robust reducer, only one argument.
print(p.read_line(reducer=lambda x: x))
print(p.read_line(reducer=reduce_sum))
p.close()
