import time

from copy import deepcopy

import source.geneticalgorithm.geneticalgorithm as lib
from source.geneticalgorithm.pizza.PizzaChromo import PizzaChromo

"""OPERATIONS TO BE DONE AT THE END OF EXECUTION WTH THE FINAL POPULATION"""
def stop(pop):
    print(pop.getbest().slices)
    print()
    for i in range(0, len(pop.getbest().sliceslist)):
        print(pop.getbest().sliceslist[i][0]," ",pop.getbest().sliceslist[i][2]," ",pop.getbest().sliceslist[i][1]," ",pop.getbest().sliceslist[i][3])

"""READ FROM FILE"""
f = open("big.in")
lines=f.readlines()
nrows = int(lines[0])
ncols = int(lines[1])
miningr = int(lines[2])
maxcells = int(lines[3])
print(nrows, " ", ncols, " ", miningr, " ", maxcells)

matr=[]
for i in range(0,nrows):
    row=[]
    for j in range(0,ncols):
        if lines[i+4][j] == "T":
            row.append(1)
        else:
            row.append(0)
    matr.append(deepcopy(row))

"""CREATE INITIAL STARTING LIST OF CHROMOSOMES"""
list = []
for i in range(0, 20):
    c = PizzaChromo([],nrows,ncols,matr, miningr, maxcells)
    c.randomize()
    list.append(c)
for i in range(0,len(list)):
    print(list[i].slices, " ", list[i].sliceslist)



"""EXECUTION OF THE ALGORITHM"""
start = time.time()

result=lib.execute(list,10,lib.roulettewheelselection,lib.fitepochsend,0.80,0.6,stop,10000, ncols*nrows)
end = time.time()

print((end-start)/60)