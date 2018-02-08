import math
from source.localsearch.localsearch import localsearch
# find the local maxima of a function at using local search starting from x=0

initsol = 0


#Example with sin(x)
def func(x):
    return math.sin(x)*math.cos(x)


def best(lista):
    max = lista[0]
    for i in range(0, len(lista)):
        if(func(lista[i])>func(max)):
            max = lista[i]
    return max


def neighborhood(sol, precision=0.001, window=0.2):
    i = -window
    res = [sol]
    while i <= window:
        res.append(sol+i)
        i += precision
    return res


def equal(sol1,sol2):
    return sol1 == sol2

final = localsearch(neighborhood, best, equal, initsol)
print("FOUND:    ", final, "-> VALUE: ", func(final))
