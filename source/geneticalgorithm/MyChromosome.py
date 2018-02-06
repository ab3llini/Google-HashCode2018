import random

import math

from source.geneticalgorithm.Chromosome import Chromosome


class MyChromosome(Chromosome):
    distances = [[58, 88, 65, 2, 95, 11, 12, 65, 90, 42, 55, 23, 41, 9, 1, 95, 33, 86, 4, 9, 47, 35, 27, 38, 96, 48, 46, 12, 4, 42, 55, 93, 32, 51, 65, 51, 33, 73, 58, 40, 72, 1, 75, 79, 76, 10, 47, 48, 24, 76], [89, 49, 77, 64, 93, 38, 9, 27, 48, 94, 88, 96, 94, 68, 6, 81, 65, 36, 45, 45, 75, 4, 80, 58, 71, 20, 38, 51, 16, 38, 37, 89, 60, 22, 56, 79, 14, 69, 50, 98, 91, 38, 11, 94, 98, 28, 15, 42, 35, 47], [37, 26, 79, 91, 66, 36, 85, 60, 57, 58, 77, 99, 1, 50, 3, 84, 8, 89, 28, 85, 10, 28, 13, 45, 27, 59, 46, 3, 51, 38, 68, 44, 77, 13, 78, 73, 90, 63, 1, 19, 11, 22, 58, 21, 38, 14, 26, 28, 34, 93], [73, 10, 74, 56, 77, 6, 29, 32, 98, 80, 31, 56, 8, 41, 57, 4, 41, 6, 74, 62, 43, 85, 82, 31, 70, 50, 31, 23, 34, 2, 21, 74, 3, 88, 91, 58, 9, 93, 90, 33, 83, 60, 77, 94, 11, 22, 80, 66, 94, 86], [87, 88, 55, 18, 26, 56, 48, 1, 30, 23, 5, 90, 35, 26, 20, 45, 8, 44, 73, 31, 85, 4, 32, 41, 33, 71, 16, 70, 55, 40, 76, 82, 89, 45, 40, 5, 6, 99, 10, 62, 33, 82, 16, 56, 99, 91, 12, 78, 21, 30], [98, 6, 56, 39, 11, 17, 6, 22, 87, 27, 37, 7, 37, 88, 61, 97, 71, 71, 34, 32, 70, 43, 11, 75, 71, 49, 48, 40, 46, 76, 47, 34, 36, 88, 44, 58, 16, 87, 62, 1, 56, 4, 37, 37, 78, 72, 34, 68, 79, 2], [87, 39, 41, 55, 19, 28, 41, 23, 84, 52, 52, 3, 37, 1, 2, 52, 97, 30, 96, 43, 71, 55, 1, 81, 87, 69, 53, 59, 35, 87, 29, 76, 30, 98, 42, 45, 64, 50, 96, 99, 61, 45, 3, 51, 71, 25, 77, 37, 35, 97], [96, 80, 82, 12, 77, 61, 28, 90, 39, 46, 3, 40, 25, 4, 40, 64, 69, 2, 13, 46, 12, 79, 64, 38, 28, 33, 11, 39, 14, 62, 21, 98, 91, 61, 65, 98, 65, 36, 70, 99, 38, 3, 20, 55, 93, 17, 21, 45, 95, 91], [95, 49, 89, 10, 48, 66, 84, 27, 32, 82, 27, 13, 34, 79, 1, 46, 70, 26, 69, 87, 6, 1, 94, 15, 50, 4, 2, 79, 37, 82, 28, 4, 55, 30, 53, 16, 98, 89, 41, 38, 29, 69, 37, 77, 15, 53, 92, 74, 34, 30], [91, 93, 20, 9, 48, 13, 15, 87, 71, 66, 99, 41, 37, 65, 55, 15, 23, 7, 23, 49, 91, 20, 98, 73, 69, 53, 40, 1, 75, 91, 10, 4, 42, 10, 88, 84, 80, 2, 51, 33, 50, 93, 28, 34, 71, 96, 13, 22, 64, 14], [76, 84, 87, 39, 94, 65, 45, 97, 75, 17, 92, 53, 42, 85, 62, 95, 45, 60, 55, 75, 46, 16, 92, 24, 53, 82, 4, 85, 34, 55, 63, 39, 97, 67, 51, 67, 76, 41, 13, 51, 81, 38, 45, 2, 18, 59, 73, 60, 66, 92], [28, 7, 51, 31, 96, 46, 6, 75, 17, 13, 35, 98, 46, 63, 66, 11, 76, 51, 81, 94, 11, 18, 33, 8, 3, 58, 83, 20, 15, 14, 90, 77, 23, 91, 13, 6, 20, 1, 33, 70, 72, 25, 57, 29, 73, 22, 48, 15, 68, 79], [69, 6, 97, 97, 76, 47, 54, 62, 96, 3, 41, 23, 31, 60, 27, 45, 33, 7, 20, 68, 81, 35, 30, 45, 29, 8, 1, 74, 9, 4, 4, 24, 12, 33, 45, 27, 56, 29, 49, 55, 54, 43, 48, 2, 84, 19, 97, 26, 53, 8], [76, 51, 95, 89, 67, 15, 41, 56, 71, 74, 7, 57, 13, 36, 24, 9, 12, 96, 27, 94, 97, 22, 94, 81, 18, 11, 24, 11, 62, 82, 65, 48, 14, 92, 70, 72, 76, 69, 4, 43, 86, 40, 78, 60, 32, 50, 60, 82, 54, 65], [83, 74, 91, 42, 74, 2, 2, 83, 13, 45, 15, 33, 3, 29, 49, 50, 93, 39, 31, 52, 44, 16, 98, 11, 29, 83, 33, 16, 95, 59, 79, 50, 45, 2, 49, 60, 91, 81, 85, 51, 73, 46, 93, 25, 55, 50, 30, 36, 3, 28], [3, 6, 92, 71, 55, 65, 58, 30, 84, 69, 50, 82, 56, 73, 22, 96, 4, 75, 51, 27, 22, 92, 40, 6, 79, 73, 60, 64, 62, 17, 90, 53, 9, 12, 32, 16, 70, 3, 20, 71, 57, 53, 46, 96, 68, 39, 1, 78, 85, 32], [27, 99, 23, 28, 60, 3, 10, 85, 60, 93, 12, 53, 29, 18, 31, 60, 66, 93, 15, 37, 35, 24, 90, 81, 80, 28, 50, 46, 91, 85, 81, 5, 28, 51, 77, 39, 4, 55, 27, 31, 92, 11, 92, 92, 25, 5, 52, 6, 5, 11], [47, 82, 57, 72, 85, 73, 13, 92, 62, 43, 45, 53, 89, 17, 26, 74, 58, 13, 67, 32, 97, 64, 86, 69, 93, 78, 92, 99, 87, 27, 50, 37, 43, 29, 3, 22, 29, 1, 9, 20, 34, 16, 94, 8, 11, 26, 69, 79, 23, 18], [73, 82, 37, 43, 14, 48, 24, 24, 19, 73, 87, 34, 68, 23, 52, 54, 3, 94, 33, 65, 99, 92, 91, 74, 77, 46, 8, 30, 90, 4, 23, 93, 81, 52, 69, 40, 38, 76, 51, 18, 99, 91, 9, 90, 13, 85, 73, 95, 35, 76], [25, 13, 51, 50, 94, 17, 86, 60, 64, 58, 82, 35, 49, 21, 65, 7, 75, 29, 42, 33, 76, 31, 26, 41, 6, 87, 7, 83, 9, 69, 24, 75, 4, 81, 11, 43, 5, 31, 1, 7, 15, 91, 51, 14, 37, 66, 92, 60, 69, 58], [18, 87, 83, 12, 29, 52, 85, 55, 56, 99, 98, 49, 72, 51, 24, 11, 27, 7, 43, 36, 61, 53, 43, 61, 38, 58, 72, 39, 6, 79, 10, 90, 54, 91, 30, 55, 68, 45, 58, 45, 65, 47, 70, 55, 6, 96, 67, 1, 16, 80], [47, 4, 43, 72, 97, 5, 43, 96, 96, 77, 89, 84, 26, 11, 81, 12, 82, 78, 26, 55, 9, 77, 54, 45, 6, 17, 98, 48, 50, 3, 42, 1, 43, 28, 71, 49, 17, 85, 40, 31, 7, 35, 78, 71, 79, 9, 86, 19, 7, 82], [92, 4, 41, 15, 29, 7, 44, 56, 98, 11, 88, 21, 19, 5, 82, 59, 35, 39, 59, 39, 69, 31, 81, 20, 21, 43, 7, 19, 38, 67, 65, 77, 29, 9, 2, 12, 98, 45, 25, 25, 29, 9, 73, 1, 66, 62, 72, 23, 3, 45], [45, 14, 22, 31, 94, 20, 64, 91, 5, 34, 69, 45, 75, 77, 82, 61, 38, 80, 94, 24, 88, 63, 25, 56, 81, 51, 3, 43, 72, 22, 1, 15, 64, 31, 78, 7, 43, 46, 63, 51, 48, 13, 27, 98, 9, 93, 84, 80, 1, 97], [81, 40, 99, 13, 93, 11, 3, 80, 30, 71, 94, 79, 12, 36, 52, 55, 44, 55, 64, 90, 90, 53, 99, 79, 56, 20, 75, 97, 42, 46, 32, 66, 31, 64, 40, 44, 86, 34, 22, 94, 44, 35, 16, 46, 49, 11, 25, 28, 5, 49], [90, 52, 56, 26, 96, 53, 22, 49, 76, 11, 36, 90, 41, 28, 27, 73, 3, 33, 3, 64, 80, 98, 85, 24, 69, 55, 58, 93, 23, 51, 88, 49, 98, 26, 80, 1, 56, 83, 17, 97, 67, 77, 70, 8, 4, 34, 87, 96, 79, 62], [5, 94, 6, 36, 18, 40, 72, 49, 94, 56, 56, 93, 2, 56, 48, 57, 90, 78, 91, 27, 39, 19, 28, 16, 38, 80, 74, 55, 22, 3, 82, 48, 93, 92, 11, 98, 23, 72, 8, 27, 8, 92, 49, 80, 23, 49, 3, 21, 26, 14], [82, 33, 89, 34, 12, 44, 81, 25, 33, 43, 88, 15, 8, 72, 10, 76, 92, 93, 92, 33, 1, 57, 34, 33, 60, 52, 53, 23, 44, 74, 51, 80, 98, 50, 84, 55, 19, 47, 25, 13, 96, 31, 52, 70, 37, 26, 28, 67, 26, 62], [89, 73, 85, 21, 59, 85, 69, 74, 11, 51, 27, 67, 37, 47, 8, 3, 27, 81, 3, 16, 75, 40, 49, 80, 88, 35, 63, 32, 75, 56, 77, 57, 58, 23, 9, 23, 18, 8, 78, 96, 91, 25, 30, 94, 12, 68, 58, 8, 12, 8], [22, 68, 23, 34, 11, 6, 10, 83, 35, 12, 93, 42, 45, 91, 58, 91, 47, 88, 61, 50, 15, 66, 44, 78, 3, 68, 70, 93, 66, 79, 68, 60, 3, 43, 56, 97, 70, 78, 17, 20, 20, 41, 18, 59, 49, 91, 2, 31, 78, 71], [52, 55, 85, 69, 45, 46, 56, 40, 51, 9, 5, 20, 41, 96, 91, 92, 22, 82, 5, 94, 47, 8, 96, 58, 58, 77, 16, 5, 11, 29, 11, 51, 36, 97, 44, 47, 36, 12, 63, 81, 13, 52, 46, 42, 67, 50, 7, 47, 45, 64], [72, 93, 28, 96, 98, 26, 38, 56, 83, 77, 97, 63, 85, 65, 1, 2, 69, 52, 99, 80, 44, 37, 23, 81, 58, 97, 15, 61, 37, 58, 58, 32, 71, 80, 5, 79, 15, 49, 89, 64, 85, 52, 15, 13, 71, 49, 44, 86, 17, 94], [89, 44, 29, 47, 50, 87, 9, 92, 76, 13, 59, 17, 61, 20, 91, 55, 50, 16, 13, 76, 49, 24, 24, 34, 45, 55, 19, 84, 36, 19, 72, 36, 27, 43, 81, 15, 25, 37, 16, 85, 83, 93, 95, 75, 82, 60, 58, 6, 85, 32], [41, 85, 20, 7, 19, 5, 49, 33, 84, 80, 86, 67, 50, 28, 3, 85, 7, 39, 27, 18, 50, 11, 46, 92, 70, 60, 30, 23, 74, 62, 69, 56, 78, 58, 99, 87, 48, 78, 96, 96, 51, 70, 41, 11, 20, 15, 70, 24, 39, 42], [96, 19, 32, 80, 13, 57, 25, 74, 90, 82, 58, 78, 47, 78, 57, 62, 17, 34, 17, 19, 91, 56, 15, 95, 59, 75, 97, 20, 70, 4, 87, 20, 42, 75, 28, 63, 86, 24, 81, 1, 80, 3, 40, 5, 32, 53, 59, 19, 15, 22], [28, 28, 31, 38, 28, 60, 47, 24, 61, 70, 94, 73, 38, 5, 13, 52, 6, 64, 44, 41, 24, 44, 97, 20, 83, 83, 76, 34, 39, 19, 7, 51, 83, 32, 72, 79, 98, 35, 77, 88, 41, 39, 73, 97, 89, 58, 82, 60, 51, 14], [76, 96, 2, 19, 15, 12, 19, 24, 79, 27, 66, 98, 78, 90, 66, 67, 54, 10, 96, 58, 97, 28, 17, 66, 30, 29, 45, 78, 94, 94, 98, 12, 9, 41, 53, 33, 98, 44, 61, 67, 90, 59, 15, 73, 39, 9, 32, 44, 95, 83], [89, 8, 97, 66, 77, 12, 35, 50, 45, 34, 97, 53, 49, 63, 15, 94, 29, 39, 96, 37, 47, 27, 37, 14, 44, 6, 19, 77, 56, 2, 75, 2, 12, 64, 40, 60, 90, 27, 86, 22, 71, 95, 52, 17, 74, 34, 32, 66, 7, 89], [19, 90, 60, 39, 90, 16, 14, 85, 46, 61, 92, 18, 1, 51, 78, 35, 53, 24, 32, 70, 85, 19, 90, 41, 7, 23, 90, 94, 54, 82, 43, 29, 25, 33, 6, 48, 20, 63, 58, 7, 54, 99, 63, 68, 86, 54, 28, 18, 55, 3], [69, 16, 1, 36, 59, 10, 92, 24, 61, 74, 4, 62, 38, 82, 74, 32, 21, 28, 19, 90, 31, 85, 28, 84, 2, 35, 73, 51, 13, 12, 65, 7, 67, 81, 16, 21, 72, 53, 31, 89, 53, 99, 3, 74, 82, 74, 94, 57, 36, 89], [74, 95, 78, 36, 37, 59, 29, 70, 80, 18, 88, 34, 60, 70, 68, 69, 27, 18, 88, 27, 25, 92, 54, 30, 82, 21, 68, 86, 48, 19, 32, 20, 29, 94, 18, 56, 67, 90, 25, 55, 49, 82, 51, 93, 59, 58, 71, 86, 85, 24], [36, 3, 99, 49, 21, 59, 6, 13, 1, 76, 59, 69, 89, 46, 93, 18, 67, 47, 77, 85, 39, 24, 1, 92, 28, 4, 14, 62, 84, 78, 84, 93, 98, 4, 22, 95, 10, 90, 95, 38, 75, 26, 31, 22, 94, 23, 76, 7, 61, 90], [17, 5, 47, 63, 64, 61, 30, 67, 20, 91, 8, 9, 43, 35, 65, 88, 56, 61, 22, 29, 32, 51, 17, 11, 90, 76, 20, 83, 79, 25, 32, 91, 93, 40, 81, 47, 38, 25, 71, 54, 10, 79, 2, 26, 52, 5, 44, 54, 65, 9], [69, 84, 14, 36, 17, 85, 62, 59, 80, 96, 53, 34, 57, 60, 71, 91, 28, 39, 79, 46, 68, 84, 43, 30, 57, 99, 61, 83, 33, 66, 8, 10, 94, 86, 67, 28, 13, 12, 38, 3, 54, 80, 52, 22, 21, 89, 81, 95, 32, 67], [86, 61, 16, 51, 12, 65, 29, 20, 15, 42, 84, 50, 80, 26, 2, 32, 4, 6, 27, 55, 65, 64, 87, 86, 77, 87, 88, 82, 70, 73, 4, 84, 62, 75, 2, 69, 4, 49, 78, 59, 91, 32, 16, 24, 53, 83, 35, 40, 43, 71], [66, 11, 33, 20, 49, 94, 25, 96, 33, 76, 94, 58, 75, 77, 47, 63, 36, 20, 78, 69, 48, 85, 12, 49, 13, 92, 62, 92, 41, 98, 99, 11, 58, 11, 61, 97, 39, 5, 63, 43, 13, 45, 17, 10, 49, 50, 9, 65, 45, 81], [69, 29, 32, 80, 34, 18, 45, 71, 99, 42, 92, 30, 61, 61, 49, 20, 98, 45, 81, 75, 75, 14, 90, 96, 72, 12, 33, 60, 63, 30, 60, 14, 28, 32, 66, 40, 47, 68, 50, 31, 77, 81, 46, 53, 62, 32, 47, 57, 59, 46], [7, 41, 66, 31, 47, 20, 81, 35, 43, 20, 15, 91, 1, 92, 1, 95, 71, 80, 87, 30, 70, 92, 2, 56, 99, 37, 6, 60, 5, 91, 88, 46, 72, 65, 47, 36, 23, 77, 80, 73, 39, 42, 33, 37, 30, 86, 51, 38, 36, 33], [6, 77, 91, 54, 22, 52, 41, 96, 68, 98, 54, 79, 55, 55, 53, 60, 99, 53, 27, 77, 73, 19, 27, 7, 19, 63, 98, 5, 75, 18, 25, 72, 22, 17, 57, 38, 41, 18, 97, 88, 45, 23, 41, 27, 29, 32, 96, 52, 95, 52], [8, 67, 29, 7, 40, 24, 24, 62, 2, 73, 85, 49, 23, 58, 81, 67, 56, 85, 24, 57, 27, 77, 19, 40, 17, 94, 92, 63, 76, 9, 82, 10, 33, 68, 20, 46, 54, 76, 37, 79, 24, 91, 59, 83, 36, 66, 90, 13, 49, 69]]


    def __init__(self):
        self.positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]


    """def setdistances(self):
        i=0
        while(i<20):
            list=[]
            j=0
            while(j<20):
                list.append(math.floor(random.uniform(1,100)))
                j+=1
            self.distances.append(list)
            i+=1
        print(self.distances)"""

    def calculatefitness(self):
        sum =0
        i = 0
        length=len(self.positions)
        while(i<length-1):
            sum += (self.distances[self.positions[i]-1])[self.positions[i+1]-1]
            i += 1
        self.fitness=4000-sum
        return 4000-sum

    def crossover(self, parent2):
        chromo=MyChromosome()
        crossoverpoint=math.floor(random.uniform(0, len(self.positions)))
        i=0
        while(i<=crossoverpoint):
            chromo.positions[i]=self.positions[i]
            i+=1
        j=0
        pos=crossoverpoint+1
        while(j<len(self.positions)):
            test=False
            i=0
            while(i<=crossoverpoint):
                if(chromo.positions[i]==parent2.positions[j]):
                    test=True
                i+=1
            if(test==False):
                chromo.positions[pos]=parent2.positions[j]
                pos+=1
            j+=1
        return chromo


    def mutation(self):
        pos1 = math.floor(random.uniform(0, len(self.positions)))
        pos2 = math.floor(random.uniform(0, len(self.positions)))
        i = self.positions[pos1]
        self.positions[pos1] = self.positions[pos2]
        self.positions[pos2] = i
        return self

    def feasible(self):
        return True

    def randomize(self):
        lista=[]
        length=len(self.positions)
        while(len(lista)<length):
            rand=math.ceil(random.uniform(0, len(self.positions)))
            while(rand==0 or lista.__contains__(rand)):
                rand = math.ceil(random.uniform(0, len(self.positions)))
            lista.append(rand)
        self.positions=lista