"""READ FROM FILE"""
from copy import deepcopy
import numpy as np
from scipy import io as scio


file = "big"
number = "8"
f = open(file + ".in")
lines=f.readlines()
nrows = int(lines[0])
ncols = int(lines[1])
miningr = int(lines[2])
maxcells = int(lines[3])
matr=[]


for i in range(0,nrows):
    row=[]
    for j in range(0,ncols):
        if lines[i+4][j] == "T":
            row.append(1)
        else:
            row.append(0)
    matr.append(deepcopy(row))

matr = np.array(matr)
def singleslicefeasible(slice):
    sum1 = 0
    sum2 = 0
    if slice.shape[0]*slice.shape[1] > maxcells:
        return False
    for i in range(slice.shape[0]):
        for j in range(slice.shape[1]):
            sum1 += slice[i][j]
            sum2 += 1 - slice[i][j]
    if sum1 < miningr or sum2 < miningr:
        return False
    return True


kernel_height = 3
kernel_width = 4

kernel_shape = [kernel_height, kernel_width]

slices = []
number_slices = 0
i = 0
while i < nrows - kernel_height:
    j = 0
    while j < ncols - kernel_width:
        slice = np.array(matr[i:i+kernel_height, j:j+kernel_width])
        if singleslicefeasible(slice):
            slices.append([[i, j], [i+kernel_height, j+kernel_width]])
            number_slices += 1
        j += kernel_width
    i += kernel_height
    print(number_slices)


slices = np.array(slices)
a = {}
a['slices'] = slices
print(slices)

scio.savemat(file+number+".mat", a)
