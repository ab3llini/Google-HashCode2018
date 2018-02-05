import random

from source.geneticalgorithm.geneticalgorithm.Chromosome import Chromosome


class Mutation:

    def __init__(self, probability: float):
        """Here's defined mutation probability"""
        self.probability=probability

    def mutation(self, chromosome: Chromosome) -> Chromosome:
        """Does mutation with a probability that was given when the object was created"""
        numb = random.uniform(0,1)
        if numb < self.probability :
            return chromosome.mutation()
        return chromosome