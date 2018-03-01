import time

from copy import deepcopy
import source.pizza.reader as r
import source.geneticalgorithm.geneticalgorithm as lib
from source.geneticalgorithm.pizza.PizzaChromo import  PizzaChromo
from scipy import io as scio

"""OPERATIONS TO BE DONE AT THE END OF EXECUTION WTH THE FINAL POPULATION"""
def stop(pop):
    print(pop.getbest().slices)
    print()
    print(pop.getbest().sliceslist)


"""READ FROM FILE"""
f = open("highbonus.in")
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

num = 1
pop = []
while num <= 36:
    lista = scio.loadmat("./../../pizza/solutions/highbonus"+ str(num)+".mat")['slices']
    lista = lista.tolist()
    c = PizzaChromo(lista, nrows, ncols, matr, miningr, maxcells)
    pop.append(c)
    num += 1
    if num == 23:
        num = 25

sol = r.read_problem_solution('highbonus', "673748")
sol = sol.tolist()
c = PizzaChromo(sol, nrows, ncols, matr, miningr, maxcells)
pop.append(c)
sol = r.read_problem_solution('highbonus', "712438")
sol = sol.tolist()
c = PizzaChromo(sol, nrows, ncols, matr, miningr, maxcells)
pop.append(c)
sol = r.read_problem_solution('highbonus', "726483")
sol = sol.tolist()
c = PizzaChromo(sol, nrows, ncols, matr, miningr, maxcells)
pop.append(c)



"""EXECUTION OF THE ALGORITHM"""
start = time.time()

result=lib.execute(pop,4,lib.roulettewheelselection,lib.fitepochsend,0.80,0.6,stop,10000, ncols*nrows)
end = time.time()

print((end-start)/60)