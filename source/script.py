from pizza.reader import *
from text_parser.conventions import *

pizza = read_problem_instance(BIG)

kernels = [
    [14, 0],
    [0, 14],
    [13, 0],
    [0, 13],
    [12, 0],
    [0, 12],
    [6, 2],
    [2, 6],
    [4, 3],
    [3, 4]
]

def check_conditions(solution):
    m, t = 0, 0
    for elem in pizza[DATA][solution[0, 0] : solution[1, 0], solution[0, 1] : solution[1, 1]]:
        if elem == MUSH:
            m = m+1
        else:
            t = t+1
    if m > pizza[LOW] and t > pizza[LOW] and t + m <= pizza[HIGH]:
        return True
    return False

def check(solutions, kernel, point):
    solution = point, (kernel[0] + point[0], kernel[1] + point[1])
    if check_conditions(solution) and check_overlap(solutions, solution):
        solutions.append(solution)
        return True
    return False



def check_overlap(solutions, solution):


def foo(solution, suggestions):
    for sug in suggestions:
