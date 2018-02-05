class Elitism:

    def __init__(self, n: int):
        """ n is the number of the best elements from the population that will directly be copied
        to the next generation
        :type n: int"""
        self.elitesnumber=n

    @property
    def getelitesnumber(self) -> int:
        """returns the number of elements that will directly be copied to the next generation"""
        return self.elitesnumber