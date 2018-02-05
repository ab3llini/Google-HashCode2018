from geneticalgorithm.Chromosome import Chromosome
from geneticalgorithm.Crossover import Crossover
from geneticalgorithm.Elitism import Elitism
from geneticalgorithm.EndCondition import EndCondition
from geneticalgorithm.Mutation import Mutation
from geneticalgorithm.Population import Population
from geneticalgorithm.SelectionMethod import SelectionMethod


class Genetic:

    def __init__(self, pop: Population, elitism: Elitism, selmethod: SelectionMethod, endcondition: EndCondition, crossover: Crossover, mutation: Mutation):
        self.pop = pop
        self.selmethod = selmethod
        self.endcondition=endcondition
        self.mutation=mutation
        self.crossover=crossover
        self.elitism=elitism

    def start(self):
        """Intructions executed before starting the loop."""
        self.pop.sort()

    def stop(self):
        """Intructions executed before after the termination. Must be defined by the user."""
        pass

    def execute(self) -> Chromosome:
        """This is what must be called to execute the genetic algorithm with the parameters specified when the object
        was created. Returns, at the end, the best chromosome"""
        self.start()
        self.result = self.loop()
        self.stop()
        return self.result

    def applyElitism(self, newgen: Population) -> Population:
        """Used by the loop. It applies Elitism, that means that it copies in the new generation
        a certain number of chromosomes."""
        i=0
        while i<self.elitism.elitesnumber:
            newgen.chromosomes.append(self.pop.chromosomes[i])
            i+=1
        return newgen

    def generateOffSpring(self, newgen: Population) -> Population:
        """Used by the loop. It generated new offspring, that means that it selects two parents basing on the selection
         method that was defined when this object was created and:
         - performs crossover with the probability defined when the object was created;
         - performs mutation with the probability defined when the object was created.
         Returns the new offspring. If no offspring was created, returns the first parent (eventually mutated)"""
        parent1 = self.pop.select(self.selmethod)
        parent2 = self.pop.select(self.selmethod)
        while parent1 == parent2:
            parent2 = self.pop.select(self.selmethod)
        offspring= self.crossover.crossover(parent1,parent2)
        offspring=self.mutation.mutation(offspring)
        if(offspring.feasible()):
            offspring.getfitness()
            newgen.chromosomes.append(offspring)
        return newgen


    def loop(self) -> Chromosome:
        """This is the loop of the algorithm."""
        while True:
            """If condition is satisfied, it stops and returns the best chromosome."""
            if self.endcondition.isSatisfied():
                return self.pop.getbest()
            """Applies elitism to copy a certain number of chromosomes to the new generation, 'newgen' """
            newgen = self.applyElitism(Population([]))
            """Generated new offspring a certain number of times, to have a new generation as numerous as the 
            previous one."""
            while(newgen.getDimension() < self.pop.getDimension()):
                newgen = self.generateOffSpring(newgen)

            """Sort the new generation by fitness, decreasing order."""
            newgen.sort()
            """Updates end condition"""
            self.endcondition.update()
            """Uses the new generation as current population"""
            self.pop = newgen


