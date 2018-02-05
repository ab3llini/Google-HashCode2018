import random

from source.geneticalgorithm.geneticalgorithm.Chromosome import Chromosome


class Crossover:

    def __init__(self, probability: float):
        """Here's defined crossover probability"""
        self.probability = probability

    def crossover(self, parent1: Chromosome, parent2: Chromosome):
        """Does crossover with a probability that was given when the object was created"""
        numb = random.uniform(0, 1)
        if numb < self.probability:
            return parent1.crossover(parent2)
        return parent1


