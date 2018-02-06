import time

import source.geneticalgorithm.geneticalgorithm as lib
from source.geneticalgorithm.MyChromosome import MyChromosome


def stop(pop):
    for i in range(0,pop.getDimension()):
        print(pop.chromosomes[i].positions, " ", pop.chromosomes[i].getfitness())
    print()
    print(pop.getbest().positions)
    print(pop.getbest().getfitness())

list = []
for i in range (0,50):
    c = MyChromosome()
    c.randomize()
    list.append(c)

start = time.time()

result=lib.execute(list,5,lib.roulettewheelselection,lib.epochsend,0.7,0.1,stop,1000)
end = time.time()

print((end-start)/60)