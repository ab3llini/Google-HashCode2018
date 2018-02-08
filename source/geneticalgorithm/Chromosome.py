class Chromosome:

    def __init__(self):
        """initialization of a FEASIBLE chromosome"""
        pass

    def getfitness(self):
        """Directly returns the fitness if it was already calculated.
        Calculates and returns the fitness if it has never been calculated.
        This is to avoid the fitness being calculated multiple times uselessly."""
        if hasattr(self, "fitness"):
            return self.fitness
        self.fitness = self.calculatefitness()
        return self.fitness

    def calculatefitness(self):
        """fitness MUST be positive in order to work properly with all selection methods
        furthermore, you should project a fitness function that needs to be maximized"""
        pass

    def crossover(self, parent2):
        """MUST return a Chromosome that is crossover of this and parent2.
        Basically this is where you define crossover"""
        pass

    def mutation(self):
        """MUST return a Chromosome that is mutation of this.
        Basically this is where you define mutation"""
        pass

    def feasible(self):
        """MUST return True if and ony if this is a feasible solution for the problem."""
        pass

    def randomize(self):
        """Transforms this chromosome into a random solution. Returns northing"""
        pass
