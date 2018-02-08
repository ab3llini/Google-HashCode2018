import numpy as np
import cudamat as cm
import lprogramming.model.lproblem as lp
import lprogramming.utils.matrix as mx_util
import lprogramming.solver.simplex as simplex

# First things first: provide a consistent representation of the input
c = [
    [30, 50]
]

A = [
    [1, 0],
    [0, 2],
    [3, 2]
]
b = [
    [4],
    [12],
    [18]
]

start = [
    [2],
    [6]
]

# In order for our model to work, we need another representation of our input matrices
# Valid formats are numpy's multidimensional arrays or cudamat one's.
# You decide which format to use an implicitly select the host (CPU or GPU)
dataset = mx_util.build(raw_c=c, raw_A=A, raw_b=b, raw_start=start)

# Set signs, in this case all constraints have the same sign.
# Note: You could set signs manually if you want, just provide a consistent array of LPSigns
A_sign = lp.init_constraints_signs_to(lp.LPSign.LE, dataset[lp.kConstraintsRef])

# Set the 2 variable signs to less then or equal to 0
var_signs = [lp.LPSign.GE] * 2

# If you do not provide the signs for the variables, they are all set to FREE
# Create a new instance of a problem. See the class definition for the full list of parameters
# Shortly, we need the objective, the built input data, the A matrix signs,
# var signs (default to FREE) and var names (Default to x)
p = lp.LPProblem(lp.LPObjective.MAXIMIZE, dataset, A_sign, var_signs)

# We can build the dual representation like this
# Note that if the data set was build with cudamat the transpose op. will be performed on GPU
# An optional parameter can be specified and refers to the var names (default to y)
d = p.get_dual()

# Print the problem in an intuitive way
print(p)
print(d)

# simplex.solve(p, None, engine=cm)
solver = simplex.Solver()

solver.solve(p, dataset[lp.kStartRef])
