from geneticalgorithm.EndCondition import EndCondition


class EpochsEndCondition(EndCondition):
    """Extension of EndCondition, using this end condition will make the algorithm end after a certain
    amount of generations."""

    def __init__(self, maxepoch: int):
        """Initialization of the end condition."""
        self.actepoch=0
        self.maxepoch = maxepoch

    def isSatisfied(self):
        """This is the condition checked at the beginning of each loop of the algorithm.
                If True, the algorithm will stop and return the best chromosome"""
        return self.actepoch==self.maxepoch

    def update(self):
        """This is executed at the end of each loop. It updates the epoch number"""
        self.actepoch+=1