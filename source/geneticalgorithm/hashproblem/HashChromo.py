from source.geneticalgorithm.Chromosome import Chromosome
import numpy as np
from source.geneticalgorithm.hashproblem.crossoverfun import crossoverfun
from hash2018.reader import *
import random

class HashChromo(Chromosome):

    def __init__(self, sol, ridesdict):
        self.sol = np.array(sol)
        self.checked = np.ones([len(sol)], dtype=np.uint8)
        self.ridesdict = ridesdict
        self.bonusachieved = np.zeros(self.sol.shape, dtype=np.uint8)
        self.assignedride = np.zeros([self.ridesdict[RIDES]])
        for car in self.sol:
            for ind in car:
                self.assignedride[ind] = 1


    def calculatefitness(self):
        fitness = np.sum(self.bonusachieved)*self.ridesdict[BONUS]
        rides = self.ridesdict[DATA]
        for car in self.sol:
            for ind in car:
                fitness += rides[car]
        return fitness


    def crossover(self, parent2):
        ts_split = random.uniform(0, SIMTIME)
        new_sched = crossoverfun(self.sol, parent2.sol, ts_split, self.ridesdict[DATA])
        nc = HashChromo(new_sched, self.ridesdict)
        if nc.feasible():
            return nc
        return self



    def mutation(self):
        pass #must returns chromo



    def perctime(self, ride):
        return abs(ride[2][0]-ride[1][0]) + abs(ride[2][1]-ride[1][1])

    def percasstart(self, ride):
        return ride[1][0] + ride[1][1]

    def reachableasfirst(self, ride):
        return self.percasstart(ride) < ride[3][1] - self.perctime(ride)

    def bonusfirst(self, ride):
        return self.percasstart(ride) < ride[3][0]

    def bonusnotfirst(self, ride1, ride2):
        return abs(ride1[2][0]-ride2[1][0]) + abs(ride1[2][1]-ride2[1][1]) < ride2[3][0]

    def compatible(self, ride1, ride2):
        return abs(ride1[2][0]-ride2[1][0]) + abs(ride1[2][1]-ride2[1][1]) + self.perctime(ride2) < ride2[3][1]

    def feasible(self):
        rides = self.ridesdict[DATA]
        num = len(self.sol)
        for j in range(0, num):
            car = self.sol[j]
            if self.checked[j] != 0:
                ride = rides[car[0]]
                if not self.reachableasfirst(ride):
                    return False
                if self.bonusfirst(ride):
                    self.bonusachieved[j][0] = 1
                rnum = len(car)
                for i in range(0, rnum-1):
                    if not self.compatible(rides[car[i]], rides[car[i+1]]):
                        return False
                    if self.bonusnotfirst(rides[car[i]], rides[car[i+1]]):
                        self.bonusachieved[j][i+1] = 1
        return True
