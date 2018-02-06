import random

from source.geneticalgorithm.Population import Population

"""**************************END CONDITIONS****************************"""

def epochsend(gen, maxgen):
    """This is the condition checked at the beginning of each loop of the algorithm.
            If True, the algorithm will stop and return the best chromosome"""
    return gen == maxgen


"""**********************SELECTION METHODS********************************"""

def rankselection(population):
    """returns an element of the population according to the hereby defined method, that is that
    each Chromosome has a probability to be chosen proportional to its rank (position in the list of
    chromosomes ordered by fitness), compared to others'."""
    dim = population.getDimension()
    sum = dim * (dim + 1) / 2
    partial = .0
    rand = random.uniform(0, 1)
    for i in range(0, dim):
        partial += (dim - i) / sum
        if rand < partial:
            return population.chromosomes[i]
    return population.chromosomes[population.getDimension() - 1]


def roulettewheelselection(population: Population):
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


"""*************************ALGORITHM STRUCTURE*****************************"""

def start(pop):
    """Intructions executed before starting the loop."""
    pop.sort()


def mutation(chromosome, probability):
    """Does mutation with a probability that was given when the algorithm was started"""
    numb = random.uniform(0,1)
    if numb < probability :
        return chromosome.mutation()
    return chromosome


def crossover(parent1, parent2, probability):
    """Does crossover with a probability that was given when the algorithm was started"""
    numb = random.uniform(0, 1)
    if numb < probability:
        return parent1.crossover(parent2)
    return parent1


def execute(list, elitism, selmethod, endcondition, crossoverprob, mutationprob, stop, generations):
    """This is what must be called to execute the genetic algorithm with the parameters specified at the moment.
     Returns, at the end, the best chromosome"""
    pop = Population(list)
    start(pop)
    result = loop(pop, elitism, selmethod, endcondition, crossoverprob, mutationprob, generations)
    stop(pop)
    return result


def applyElitism(newgen, pop, elitism):
    """Used by the loop. It applies Elitism, that means that it copies in the new generation
    a certain number of chromosomes."""
    i = 0
    while i < elitism:
        newgen.chromosomes.append(pop.chromosomes[i])
        i += 1
    return newgen


def generateOffSpring(newgen, pop, selmethod, crossoverprob, mutationprob):
    """Used by the loop. It generates new offspring, that means that it selects two parents basing on the selection
     method that was defined when the algorithm was started and:
     - performs crossover with the probability defined when the algorithm was started;
     - performs mutation with the probability defined when the algorithm was started.
     Returns the new offspring. If no offspring was created, returns the first parent (eventually mutated)"""
    parent1 = selmethod(pop)
    parent2 = selmethod(pop)
    while parent1 == parent2:
        parent2 = selmethod(pop)
    offspring = crossover(parent1, parent2, crossoverprob)
    offspring = mutation(offspring, mutationprob)
    if offspring.feasible():
        offspring.getfitness()
        newgen.chromosomes.append(offspring)
    return newgen


def loop(pop, elitism, selmethod, endcondition, crossoverprob, mutationprob, generations):
    """This is the loop of the algorithm."""
    gen=0
    while True:
        """If condition is satisfied, it stops and returns the best chromosome."""
        if endcondition(gen,generations):
            return pop.getbest()
        """Applies elitism to copy a certain number of chromosomes to the new generation, 'newgen' """
        newgen = applyElitism(Population([]), pop, elitism)
        """Generated new offspring a certain number of times, to have a new generation as numerous as the 
        previous one."""
        while newgen.getDimension() < pop.getDimension():
            newgen = generateOffSpring(newgen, pop, selmethod, crossoverprob, mutationprob)

        """Sort the new generation by fitness, decreasing order."""
        newgen.sort()
        """Uses the new generation as current population"""
        pop = newgen
        gen += 1
        print (pop.getbest().getfitness())

