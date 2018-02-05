import random
from geneticalgorithm.Chromosome import Chromosome
from geneticalgorithm.Population import Population
from geneticalgorithm.SelectionMethod import SelectionMethod


class RouletteWheelSelection(SelectionMethod):

    def selectFrom(self, population: Population) -> Chromosome:
        """returns an element of the population according to the hereby defined method, that is that
        each Chromosome has a probability to be chosen proportional to its fitness, compared to others'."""
        sum = .0
        partial = .0
        for c in population.chromosomes:
            sum += c.getfitness()
        rand = random.uniform(0, 1)
        for c in population.chromosomes:
            partial += c.getfitness() / sum
            if rand < partial:
                return c
        return population.chromosomes[len(population.chromosomes) - 1]