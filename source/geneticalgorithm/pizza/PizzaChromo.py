import math
import numpy as np
from copy import deepcopy

from source.geneticalgorithm.Chromosome import Chromosome
import random

class PizzaChromo(Chromosome):

    def __init__(self, lista, nrows, ncols, matr, miningr, maxcells):
        self.slices = len(lista)
        self.sliceslist = lista
        self.ncols = ncols
        self.nrows = nrows
        self.matr = matr
        self.miningr = miningr
        self.maxcells = maxcells
        self.feasibilitymatrix = np.zeros(shape=[nrows, ncols], dtype=np.uint8)
        for slice in lista:
            for i in range(slice[0][0], slice[1][0]+1):
                for j in range(slice[0][1], slice[1][1]+1):
                    self.feasibilitymatrix[i][j] = 1

    def calculatefitness(self):
        return np.sum(self.feasibilitymatrix)

    def addable(self, slice):
        portion = self.feasibilitymatrix[slice[0][0]:slice[1][0]+1, slice[0][1]:slice[1][1]+1]
        return np.sum(portion) == 0

    def crossover(self, parent2):
        slicesoff = []
        for i in range(0, len(self.sliceslist)):
            slicesoff.append(deepcopy(self.sliceslist[i]))
        for i in range(0, len(parent2.sliceslist)):
            if self.addable(parent2.sliceslist[i]):
                slicesoff.append(deepcopy(parent2.sliceslist[i]))
        return PizzaChromo(slicesoff, self.nrows, self.ncols, self.matr, self.miningr, self.maxcells)


    def slicesfeasible(self, slices):
        return True


    def mutation(self):
        which=random.uniform(0,1)
        if which < 0.8:
            return self.addslice()
        if which < 0.9:
            return self.modifyslice()
        return self.removeslice()

    def addslice(self):
        lista= deepcopy(self.sliceslist)
        n1 = math.floor(random.uniform(0, self.nrows - 1))
        n2 = math.floor(random.uniform(n1, n1 + self.maxcells))
        c1 = math.floor(random.uniform(0, self.ncols - 1))
        c2 = math.floor(random.uniform(c1, c1 + self.maxcells))
        if not singleslicefeasible([[n1, c1], [n2, c2]], self.maxcells, self.miningr, self.nrows, self.ncols, self.matr):
            return self
        if not self.addable([[n1, c1], [n2, c2]]):
            return self
        lista.append([[n1, c1], [n2, c2]])
        return PizzaChromo(lista, self.nrows, self.ncols, self.matr, self.miningr, self.maxcells)

    def removeslice(self):
        lista = deepcopy(self.sliceslist)
        elim = math.floor(random.uniform(0,len(lista)))
        lista.remove(lista[elim])
        return PizzaChromo(lista,self.nrows,self.ncols,self.matr,self.miningr,self.maxcells)

    def modifyslice(self):
        lista = deepcopy(self.sliceslist)
        mod = math.floor(random.uniform(0, len(lista)))
        which = math.floor(random.uniform(0, 2))
        which2 = math.floor(random.uniform(0, 2))
        what = math.floor(random.uniform(-1, 2))
        modified = deepcopy(lista[mod])
        lista.remove(modified)
        modified[which][which2] += what
        modif = PizzaChromo(lista,self.nrows,self.ncols,self.matr,self.miningr,self.maxcells)
        if singleslicefeasible(modified, self.maxcells, self.miningr, self.nrows, self.ncols, self.matr) and modif.addable(modified):
            lista.append(modified)
            return PizzaChromo(lista,self.nrows,self.ncols,self.matr,self.miningr,self.maxcells)
        return self

    def feasible(self):
        return self.slicesfeasible(self.sliceslist)

def randomize(nrows, ncols, matr, miningr, maxcells):
    while True:
        n1 = math.floor(random.uniform(0, nrows - 1))
        n2 = math.floor(random.uniform(n1, ncols))
        c1 = math.floor(random.uniform(0, ncols - 1))
        c2 = math.floor(random.uniform(c1, ncols))
        lista = [[[n1, c1], [n2, c2]]]
        if singleslicefeasible(lista[0], maxcells, miningr, nrows, ncols, matr):
            return PizzaChromo(lista, nrows, ncols, matr, miningr, maxcells)


def singleslicefeasible(slice, maxcells, miningr, nrows, ncols, matr):
    sum1 = 0
    sum2 = 0
    slice = np.array(slice)
    if slice[0][0] >= nrows or slice[1][0] >= nrows or slice[0][0] < 0 or slice[1][0] < 0:
        return False
    if slice[0][1] >= ncols or slice[1][1] >= ncols or slice[0][1] < 0 or slice[1][1] < 0:
        return False
    if (slice[1][0] - slice[0][0] +1) * (slice[1][1] - slice[0][1] +1) > maxcells:
        return False
    for i in range(slice[0][0], slice[1][0]):
        for j in range(slice[0][1], slice[1][1]):
            sum1 += matr[i][j]
            sum2 += 1 - matr[i][j]
    if sum1 < miningr or sum2 < miningr:
        return False
    return True
