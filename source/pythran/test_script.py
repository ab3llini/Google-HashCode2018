from pythran import *
from timeit import timeit


def run():
    return pi_approximate(10000000)


def run2():
    foo2(1000000)


a = run()
print(str(a) + ' calculated 10 times in ' + str(timeit(run, number=10)) + ' seconds')
print(timeit(run2, number=10))
