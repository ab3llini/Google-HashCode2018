from enum import Enum
import numpy as np
import cudamat as cm

ROW = 0
COL = 1


class LPException(Exception):
    """TODO"""


class LPHost(Enum):
    CPU = 1
    GPU = 2


class LPObjective(Enum):
    MINIMIZE = "min"
    MAXIMIZE = "max"


# Utility to dynamically create representation of matrix for cpu using numpy or gpu using cudamat
class LPMatrixBuilder:

    def __init__(self, host=LPHost.CPU):
        self.host = host;

    def build(self, matrix):
        m = np.array(matrix)
        return m if self.host == LPHost.CPU else cm.CUDAMatrix(m)


class LPProblem:

    def __init__(self, objective, cost_v, constraints_v, constant_v, var_names="x"):

        if cost_v.shape[ROW] > 1:
            raise Exception("Incompatible cost vector: cost vector has %s rows instead of 1" % (cost_v.shape[ROW]))

        if cost_v.shape[COL] != constraints_v.shape[COL]:
            raise Exception("Incompatible constraint matrix: the cost vector has %s cols while the constraint matrix "
                            "has %s cols" % (cost_v.shape[COL], constraints_v.shape[COL]))

        if constraints_v.shape[ROW] != constant_v.shape[ROW] or constant_v.shape[COL] > 1:
            raise Exception("Incompatible constant vector: the constant vector has %s rows while the constraint matrix "
                            "has %s rows" % (constant_v.shape[ROW], constraints_v.shape[ROW]))

        self.obj = objective
        self.c = cost_v
        self.A = constraints_v
        self.b = constant_v
        self.var_names = var_names

    def get_dual(self, var_name="y"):

        return LPProblem(
            LPObjective.MINIMIZE if self.obj == LPObjective.MAXIMIZE else LPObjective.MAXIMIZE,
            self.b.transpose(),
            self.A.transpose(),
            self.c.transpose(),
            var_name
        )

    def __str__(self):
        x = "%s {" % self.obj.value
        for i, e in enumerate((self.c.asarray() if type(self.c) is not np.ndarray else self.c)[0]):
            x += " %s%.2f * %s%d" % (("+ " if e >= 0 and i != 0 else ""), e, self.var_names, i + 1)
        x += " }\n"

        for i, row in enumerate(self.A.asarray() if type(self.A) is not np.ndarray else self.A):
            for j, col_e in enumerate(row):
                x += "%s%.2f * %s%d " % (("+ " if col_e >= 0 and j != 0 else ""), col_e, self.var_names, j + 1)
            x += "= %d\n" % (self.b.asarray() if type(self.b) is not np.ndarray else self.b)[i]
        return x


c = [[2, 3]]
A = [[4, 5], [6, 8], [3, 5]]
b = [[5], [7], [4]]

builder = LPMatrixBuilder(LPHost.CPU)

c = builder.build(c)
A = builder.build(A)
b = builder.build(b)

try:
    p = LPProblem(LPObjective.MAXIMIZE, c, A, b)
    d = p.get_dual()
    print(p)
    print(d)


except Exception as e:
    print("Oops, there is a problem: %s" % e)
