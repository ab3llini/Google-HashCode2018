import cudamat as cm
import lprogramming.model.lproblem as lp
import lprogramming.utils.matrix as mx_util

# First things first: provide a consistent representation of the input
c = [[2, 2, 4, 3]]
A = [[4, 5, 4, 6], [6, 8, 8, 3], [1, 3, 3, 5]]
b = [[5], [7], [4]]

# In order for our model to work, we need another representation of our input matrices
# Valid formats are numpy's multidimensional arrays or cudamat one's.
# You decide which format to use an implicitly select the host (CPU or GPU)
input_v = mx_util.build(raw_c=c, raw_A=A, raw_b=b, cudamat=cm.CUDAMatrix)

# Set signs, in this case all constraints have the same sign.
# Note: You could set signs manually if you want, just provide a consistent array of LPSigns
A_sign = lp.init_signs_to(lp.LPSign.LE, input_v[lp.kConstraintsRef])

# If you do not provide the signs for the variables, as in this case, they are all set to FREE
# Create a new instance of a problem. See the class definition for the full list of parameters
# Shortly, we need the objective, the built input data, the A matrix signs,
# var signs (default to FREE) and var names (Default to x)
p = lp.LPProblem(lp.LPObjective.MAXIMIZE, input_v, A_sign)

# We can build the dual representation like this
# Note that if the data set was build with cudamat the transpose op. will be performed on GPU
# An optional parameter can be specified and refers to the var names (default to y)
d = p.get_dual()

# Print the problem in an intuitive way
print(p)
print(d)
