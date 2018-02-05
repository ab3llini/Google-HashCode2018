class EndCondition:
    """This class defines the end condition of the genetic algorithm"""


    def isSatisfied(self):
        """This is the condition checked at the beginning of each loop of the algorithm.
        If True, the algorithm will stop and return the best chromosome"""
        pass

    def update(self):
        """This is executed at the end of each loop. Leave empty if unnecesary"""
        pass