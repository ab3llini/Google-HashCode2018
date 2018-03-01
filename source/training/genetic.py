from geneticalgorithm.Chromosome import Chromosome
from random import shuffle
from random import randint
import time
import source.geneticalgorithm.geneticalgorithm as lib


import numpy as np

N = 10
D = 50
b = np.random.random_integers(0, D,size=(N,N))
distances = np.array((b + b.T)/2)

for i in range(N):
    distances[i, i] = 0

print(distances)


class PathChromosome(Chromosome):

    def __init__(self, n, genes = None):
        self.n = n

        if genes is None:
            self.genes = [i for i in range(n)]
            shuffle(self.genes)
        else:
            self.genes = genes


    def calculatefitness(self):
        sum = 0;
        for i in range(self.n):
            sum = sum + distances[i, (i + 1) % self.n]

        return 10000 - sum

    def crossover(self, parent2):
        genes = self.genes[0:10]
        genes.append(parent2.genes[10:])
        return PathChromosome(n=self.n, genes=genes)

    def mutation(self):
        idx1 = randint(0, self.n - 1)
        idx2 = randint(0, self.n - 1)
        t = self.genes[idx1]
        self.genes[idx1] = self.genes[idx2]
        self.genes[idx2] = t

    def feasible(self):
        return True

    def randomize(self):
        shuffle(self.genes)


c = PathChromosome(N)

print(c.genes)


def stop(pop):
    for i in range(0,pop.getDimension()):
        print(pop.chromosomes[i].positions, " ", pop.chromosomes[i].getfitness())
    print()
    print(pop.getbest().positions)
    print(pop.getbest().getfitness())


lst = []
for i in range(0, 50):
    c = PathChromosome(N)
    lst.append(c)

start = time.time()

result = lib.execute(lst, 5, lib.roulettewheelselection, lib.epochsend, 0.999, 0.2, stop, 35000, np.inf)
end = time.time()

print((end-start)/60)

