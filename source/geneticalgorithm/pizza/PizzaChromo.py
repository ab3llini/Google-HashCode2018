import math

from copy import deepcopy

from source.geneticalgorithm.Chromosome import Chromosome
import random

class PizzaChromo(Chromosome):

    def __init__(self, lista,nrows,ncols,matr,miningr,maxcells):
        self.slices = len(lista)
        self.sliceslist = lista
        self.ncols = ncols
        self.nrows = nrows
        self.matr = matr
        self.miningr = miningr
        self.maxcells = maxcells

    def calculatefitness(self):
        fit=0
        for i in range(0, len(self.sliceslist)):
            fit += (self.sliceslist[i][1]-self.sliceslist[i][0]+1)*(1+self.sliceslist[i][3]-self.sliceslist[i][2])
        return fit


    def crossover(self, parent2):
        slicesoff = []
        for i in range(0, len(self.sliceslist)):
            slicesoff.append(deepcopy(self.sliceslist[i]))
        for i in range(0, len(parent2.sliceslist)):
            slicesoff.append(deepcopy(parent2.sliceslist[i]))
            if(not self.slicesfeasible(slicesoff)):
                slicesoff.remove(slicesoff[len(slicesoff)-1])
        return PizzaChromo(slicesoff,self.nrows,self.ncols,self.matr,self.miningr,self.maxcells)


    def slicesfeasible(self, slices):
        for i in range(0,len(slices)):
            if slices[i][0]>slices[i][1] or slices[i][2]> slices[i][3]:
                return False
            if slices[i][0]>=self.nrows or slices[i][1]>=self.nrows or slices[i][2]>=self.ncols or slices[i][3]>=self.ncols:
                return False
            if slices[i][0]<0 or slices[i][1]<0 or slices[i][2]<0 or slices[i][3]<0:
                return False
            if (slices[i][3]-slices[i][2]+1)*(1+slices[i][1]-slices[i][0])>self.maxcells:
                return False
            sum =0
            sum2=0
            for k in range(slices[i][0],slices[i][1]+1):
                for z in range(slices[i][2],slices[i][3]+1):
                    sum += self.matr[k][z]
                    sum2 += 1-self.matr[k][z]
            if(sum<self.miningr or sum2<self.miningr):
                return False
            for j in range(i+1, len(slices)):
                if slices[j][0]>=slices[i][0] and slices[j][0]<=slices[i][1] and slices[j][2]>=slices[i][2] and slices[j][2]<=slices[i][3]:
                    return False
                if slices[j][1]>=slices[i][0] and slices[j][1]<=slices[i][1] and slices[j][3]>=slices[i][2] and slices[j][3]<=slices[i][3]:
                    return False
                if slices[j][0]>=slices[i][0] and slices[j][0]<=slices[i][1] and slices[j][3]>=slices[i][2] and slices[j][3]<=slices[i][3]:
                    return False
                if slices[j][1]>=slices[i][0] and slices[j][1]<=slices[i][1] and slices[j][2]>=slices[i][2] and slices[j][2]<=slices[i][3]:
                    return False
                if slices[j][0]<slices[i][0] and slices[j][0]<slices[i][1] and slices[j][2]<slices[i][2] and slices[j][2]<slices[i][3] and slices[j][1]>slices[i][0] and slices[j][1]>slices[i][1] and slices[j][3]>slices[i][2] and slices[j][3]>slices[i][3]:
                    return False
                if slices[j][0]<slices[i][0] and slices[j][1]>slices[i][1] and (slices[j][3]>=slices[i][2] and slices[j][3]<=slices[i][3] or slices[j][2]>=slices[i][2] and slices[j][2]<=slices[i][3]):
                    return False
                if slices[j][2]<slices[i][2] and slices[j][3]>slices[i][3] and (slices[j][0]>=slices[i][0] and slices[j][0]<=slices[i][1] or slices[j][1]>=slices[i][0] and slices[j][1]<=slices[i][1]):
                    return False

        return True

    def mutation(self):
        which=random.uniform(0,1)
        if which < 0.8:
            return self.addslice()
        if which < 0.9:
            return self.modifyslice()
        return self.removeslice()

    def addslice(self):
        lista= deepcopy(self.sliceslist)
        n1 = math.floor(random.uniform(0, self.nrows - 1))
        n2 = math.floor(random.uniform(n1, n1 + self.maxcells))
        c1 = math.floor(random.uniform(0, self.nrows - 1))
        c2 = math.floor(random.uniform(c1, c1 + self.maxcells))
        lista.append([n1, n2, c1, c2])
        return PizzaChromo(lista, self.nrows, self.ncols, self.matr, self.miningr, self.maxcells)

    def removeslice(self):
        lista = deepcopy(self.sliceslist)
        elim = math.floor(random.uniform(0,len(lista)))
        lista.remove(lista[elim])
        return PizzaChromo(lista,self.nrows,self.ncols,self.matr,self.miningr,self.maxcells)

    def modifyslice(self):
        lista = deepcopy(self.sliceslist)
        mod = math.floor(random.uniform(0, len(lista)))
        which = math.floor(random.uniform(0, 4))
        what = math.floor(random.uniform(-1, 2))
        lista[mod][which] += what
        return PizzaChromo(lista,self.nrows,self.ncols,self.matr,self.miningr,self.maxcells)

    def feasible(self):
        return self.slicesfeasible(self.sliceslist)

    def randomize(self):
        done = False
        while( not done):
            n1 = math.floor(random.uniform(0, self.nrows - 1))
            n2 = math.floor(random.uniform(n1, self.nrows))
            c1 = math.floor(random.uniform(0, self.nrows - 1))
            c2 = math.floor(random.uniform(c1, self.nrows))
            lista = [[n1, n2, c1, c2]]
            if(self.slicesfeasible(lista)):
                done=True
                self.sliceslist=lista
                self.slices = len(lista)

