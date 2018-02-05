import random
from source.geneticalgorithm.geneticalgorithm.Chromosome import Chromosome
from source.geneticalgorithm.geneticalgorithm.Population import Population
from source.geneticalgorithm.geneticalgorithm.SelectionMethod import SelectionMethod


class RankSelection(SelectionMethod):

    def selectFrom(self, population: Population) -> Chromosome:
        """returns an element of the population according to the hereby defined method, that is that
        each Chromosome has a probability to be chosen proportional to its rank (position in the list of
        chromosomes ordered by fitness), compared to others'."""
        dim = population.getDimension()
        sum = dim*(dim+1)/2
        partial = .0
        rand = random.uniform(0, 1)
        for i in range(0,dim):
            partial += (dim-i) / sum
            if rand < partial:
                return population.chromosomes[i]
        return population.chromosomes[population.getDimension() - 1]