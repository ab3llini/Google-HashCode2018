from geneticalgorithm.Crossover import Crossover
from geneticalgorithm.Elitism import Elitism
from geneticalgorithm.EpochsEndCondition import EpochsEndCondition
from geneticalgorithm.Genetic import Genetic
from geneticalgorithm.Mutation import Mutation
from geneticalgorithm.Population import Population
from geneticalgorithm.RouletteWheelSelection import RouletteWheelSelection
from geneticalgorithm.RankSelection import RankSelection
from testgeneticalgorithm.MyChromosome import MyChromosome


class MyGenetic(Genetic):

    def stop(self):
        print(self.result.positions)
        print(self.result.fitness)


poplist = []
i=0
while (i<50):
    chromo = MyChromosome()
    chromo.randomize()
    chromo.getfitness()
    poplist.append(chromo)
    i += 1
pop = Population(poplist)
print()
for c in pop.chromosomes:
    print(c.positions, " ", c.fitness)

genetic = MyGenetic(pop,Elitism(5), RankSelection(), EpochsEndCondition(60000), Crossover(0.5), Mutation(0.02))
genetic.execute()

print()
for c in genetic.pop.chromosomes:
    print(c.positions, " ", c.fitness)