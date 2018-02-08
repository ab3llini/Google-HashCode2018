import math
from source.localsearch.localsearch import localsearch
# find the local maxima of a function at using local search starting from x=0

initsol = 0


#Example with sin(x)
def func(x):
    return math.sin(x)

def best(list):
    max = list[0]
    for i in range(0, len(list)):
        if(func(list[i])>func(max)):
            max = list[i]
    return max


def neighborhood(sol, precision=0.01, step=0.2):
    i = -step
    res = []
    while i <= step:
        res.append(sol+i)
        i += precision
    return res


def equal(sol1,sol2):
    return sol1 == sol2

print("EXPECTED: ", math.asin(1))
final = localsearch(neighborhood, best, equal, initsol)
print("FOUND:    ", final, "-> VALUE: ", func(final))
