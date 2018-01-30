import cudamat as cm
from lp_solver.lp_problem import *


def matrix_builder(matrix, cuda_func=None):
    m = np.array(matrix)
    if cuda_func is not None:
        m = cuda_func(m)
    return m


c = [[2, 3]]
A = [[4, 5], [6, 8], [3, 5]]
b = [[5], [7], [4]]


c = matrix_builder(c, cm.CUDAMatrix)
A = matrix_builder(A, cm.CUDAMatrix)
b = matrix_builder(b, cm.CUDAMatrix)

# Set signs, in this case all constraints have the same sign
A_sign = [LPSign.LE] * A.shape[ROW]

#try:
p = LPProblem(LPObjective.MAXIMIZE, c, A, b, A_sign)
d = p.get_dual()
print(p)
print(d)


#except Exception as e:
#print("Oops, there is a problem: %s" % e)
