import time
import numpy as np

import source.geneticalgorithm.geneticalgorithm as lib
from source.geneticalgorithm.MyChromosome import MyChromosome


def stop(pop):
    for i in range(0,pop.getDimension()):
        print(pop.chromosomes[i].positions, " ", pop.chromosomes[i].getfitness())
    print()
    print(pop.getbest().positions)
    print(pop.getbest().getfitness())


lst = []
for i in range(0, 50):
    c = MyChromosome()
    c.randomize()
    lst.append(c)

start = time.time()

result = lib.execute(lst, 5, lib.roulettewheelselection, lib.epochsend, 0.999, 0.2, stop, 35000, np.inf)
end = time.time()

print((end-start)/60)
