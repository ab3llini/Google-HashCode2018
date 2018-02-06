from source.geneticalgorithm.Chromosome import Chromosome


def getfitness(c:Chromosome):
    return c.getfitness()


class Population:

    def __init__(self, chromoList: list):
        """Initializes with a list of chromosomes. All the generation will be of the same dimension"""
        self.chromosomes = chromoList

    def sort(self):
        """Sorts the population by fitness, decreasing order"""
        self.chromosomes= sorted(self.chromosomes, reverse=True, key=getfitness)

    def getbest(self):
        """Returns the best chromsome, that is the first one because the population is constantly kept sorted."""
        return self.chromosomes[0]

    def getDimension(self) -> int:
        """returns the dimension of the population"""
        return len(self.chromosomes)
