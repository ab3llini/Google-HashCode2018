from source.geneticalgorithm.geneticalgorithm.Crossover import Crossover
from source.geneticalgorithm.geneticalgorithm.Elitism import Elitism
from source.geneticalgorithm.geneticalgorithm.EpochsEndCondition import EpochsEndCondition
from source.geneticalgorithm.geneticalgorithm.Genetic import Genetic
from source.geneticalgorithm.geneticalgorithm.Mutation import Mutation
from source.geneticalgorithm.geneticalgorithm.Population import Population
from source.geneticalgorithm.geneticalgorithm.RankSelection import RankSelection
from source.geneticalgorithm.testgeneticalgorithm.MyChromosome import MyChromosome
import time


class MyGenetic(Genetic):

    def stop(self):
        print(self.result.positions)
        print(self.result.fitness)


poplist = []
i = 0
while i < 50:
    chromo = MyChromosome()
    chromo.randomize()
    chromo.getfitness()
    poplist.append(chromo)
    i += 1
pop = Population(poplist)

print()
for c in pop.chromosomes:
    print(c.positions, " ", c.fitness)

genetic = MyGenetic(pop, Elitism(5), RankSelection(), EpochsEndCondition(70000), Crossover(0.8), Mutation(0.1))
start = time.time()
genetic.execute()
end = time.time()

print()
for c in genetic.pop.chromosomes:
    print(c.positions, " ", c.fitness)

print((end - start) / 60)
