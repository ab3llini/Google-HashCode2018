import os
import re


def _robust_str_int_cast(in_str):
    """

    Parse a single string token to int
    making sure to clean any non-digit char.
    :return: the int obtained by concatenated all digits in in_str,
    None if no digits are present.
    """
    clean = re.sub('[^0-9]+', '', in_str)
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


class Parser:
    def __init__(self, in_f):
        self.__in = open(in_f)

    def read_line(self, reducer=lambda *x: x, separator=' ', mapper=_robust_str_int_cast):
        """
        Perform a single line map-reduce parsing:
        1) the next line is read from the file (until a \n is found. \n is INCLUDED)
        2) the line is separated into tokens, based on the separator char.
        3) the tokens are mapped according to the mapper function
        4) the list of mapped tokens is reduced through the reducer. Tokens are passed as varargs
        :param reducer: reduction applied at step 4. By default, output inputs as a tuple
        :param separator: the character used to separate tokens in the line. Space by default
        :param mapper: the function to map string tokens to useful elements. A robust cast to int by default
        :return: the result of the reduction of step 4, whatever it is.
        """
        tokens = self.__in.readline().split(separator)
        return reducer(*_map(tokens, mapper))

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


class ATestClass:
    def __init__(self, a, b):
        self.prod = a * b
        self.sum = a + b

    def __str__(self):
        return "I am the test class.\nproduct: "+str(self.prod)+"\nsum: "+str(self.sum)


print(p.read_line(reducer=reduce_sum))
print(p.read_line())
print(p.read_line(reducer=ATestClass))
print(p.read_line(reducer=reduce_sum))
print(p.read_line())
print(p.read_line(reducer=lambda x: x))
print(p.read_line(reducer=reduce_sum))
p.close()