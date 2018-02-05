from greedy.elementList import ElementList


def greedy(element_list):
    if issubclass(element_list, ElementList):
        raise TypeError

    solution = []
    element_list.sort()
    while not element_list.is_empty():
        e = element_list.best()
        if element_list.ind(e):
            solution.append(e)

    return solution
