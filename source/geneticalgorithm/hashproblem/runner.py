import time

import source.geneticalgorithm.geneticalgorithm as lib
import hash2018.reader as r
from text_parser import conventions
from source.geneticalgorithm.hashproblem.HashChromo import HashChromo

"""OPERATIONS TO BE DONE AT THE END OF EXECUTION WTH THE FINAL POPULATION"""
def stop(pop):
    print(pop.getbest().getfitness())

"""READ FROM FILE"""
id = conventions.HIGHBONUS
datas = r.read_in(id)

all_sols = r.read_all_solutions(id)



"""CREATE INITIAL STARTING LIST OF CHROMOSOMES"""

pop = []
i = 0
for sol in all_sols:
    c = HashChromo(sol, datas)
    pop.append(c)




"""EXECUTION OF THE ALGORITHM"""
start = time.time()

result=lib.execute(pop,8,lib.roulettewheelselection,lib.fitepochsend,0.80,0.5,stop,10000, 60000000)
end = time.time()

print((end-start)/60)