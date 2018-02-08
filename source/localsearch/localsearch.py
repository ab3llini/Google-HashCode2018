def localsearch(neighborhood, best, solutionsequaity, startingsolution, iterations = -1):
    initsol = startingsolution
    iternumber = 1
    while True:
        nextsolution = best(neighborhood(initsol))
        if solutionsequaity(initsol, nextsolution) or iternumber == iterations:
            return nextsolution
        iternumber += 1
        initsol = nextsolution