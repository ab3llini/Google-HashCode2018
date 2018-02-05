from abc import abstractmethod

from source.geneticalgorithm.geneticalgorithm.Chromosome import Chromosome



class SelectionMethod:

    @abstractmethod
    def selectFrom(self, population, gen: int) -> Chromosome:
        """returns an element of the population according to the hereby defined method"""
        raise NotImplementedError

