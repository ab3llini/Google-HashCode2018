from enum import Enum
import numpy as np


# Global constant definitions
kRowComponent = 0
kColComponent = 1
kCostRef = "c"
kConstraintsRef = "A"
kConstantRef = "b"


# Auxiliary functions
def init_signs_to(sign, matrix):
    return [sign] * matrix.shape[kRowComponent]


# Objects declaration
class LPObjective(Enum):
    MINIMIZE = "min"
    MAXIMIZE = "max"


class LPSign(Enum):
    GE = ">="
    LE = "<="
    EQ = "="
    FREE = "<>"


class LPProblem:

    """Input needs to be a tuple (literally) of elements of type: c, b, A"""
    def __init__(self, objective, input_v, constraints_signs, var_signs=None, var_names="x"):

        self.obj = objective
        self.c = input_v["c"]
        self.A = input_v["A"]
        self.b = input_v["b"]

        if var_signs is None:
            var_signs = [LPSign.FREE] * self.A.shape[kColComponent]

        if self.c.shape[kRowComponent] > 1:
            raise Exception("Incompatible cost vector: cost vector has %s rows instead of 1" % (self.c.shape[kRowComponent]))

        if self.c.shape[kColComponent] != self.A.shape[kColComponent]:
            raise Exception("Incompatible constraint matrix: the cost vector has %s cols while the constraint matrix "
                            "has %s cols" % (self.c.shape[kColComponent], self.A.shape[kColComponent]))

        if self.A.shape[kRowComponent] != self.b.shape[kRowComponent] or self.b.shape[kColComponent] > 1:
            raise Exception("Incompatible constant vector: the constant vector has %s rows while the constraint matrix "
                            "has %s rows" % (self.b.shape[kRowComponent], self.A.shape[kRowComponent]))

        if len(constraints_signs) != self.A.shape[kRowComponent]:
            raise Exception("Wrong sign number for constraints:"
                            "have %s, expected %s" % (len(constraints_signs), self.A.shape[kRowComponent]))

        if len(var_signs) != self.A.shape[kColComponent]:
            raise Exception("Wrong sign number for variables:"
                            "have %s, expected %s" % (len(constraints_signs), self.A.shape[kColComponent]))

        for sign in constraints_signs:
            if sign == LPSign.FREE:
                raise Exception("A constraint sign cannot be free")

        for sign in var_signs:
            if sign == LPSign.EQ:
                raise Exception("A variable sign cannot be equal")

        self.A_sign = constraints_signs
        self.var_signs = var_signs
        self.var_names = var_names


    def get_dual(self, var_name="y"):

        dual_signs = self.get_dual_signs()

        return LPProblem(
            LPObjective.MINIMIZE if self.obj == LPObjective.MAXIMIZE else LPObjective.MAXIMIZE,
            {
                kCostRef: self.b.transpose(),
                kConstraintsRef: self.A.transpose(),
                kConstantRef: self.c.transpose()
            },
            dual_signs["A"],
            dual_signs["VAR"],
            var_name
        )

    def get_dual_signs(self):
        dual_a_signs = []
        dual_var_signs = []
        if self.obj == LPObjective.MAXIMIZE:
            for sign in self.A_sign:
                dual_var_signs.append(LPSign.GE if sign == LPSign.LE else LPSign.LE if sign == LPSign.GE else LPSign.FREE)
            for sign in self.var_signs:
                dual_a_signs.append(sign if sign != LPSign.FREE else LPSign.EQ)
        else:
            for sign in self.var_signs:
                dual_a_signs.append(LPSign.GE if sign == LPSign.LE else LPSign.LE if sign == LPSign.GE else LPSign.EQ)
            for sign in self.A_sign:
                dual_var_signs.append(sign if sign != LPSign.EQ else LPSign.FREE)
        return {"A" : dual_a_signs, "VAR" : dual_var_signs}

    def __str__(self):
        x = "%s {" % self.obj.value
        for i, e in enumerate((self.c.asarray() if type(self.c) is not np.ndarray else self.c)[0]):
            x += " %s%.2f * %s%d" % (
                ("+ " if e >= 0 and i != 0 else ""),
                e,
                self.var_names, i + 1
            )
        x += " }\n"

        for i, row in enumerate(self.A.asarray() if type(self.A) is not np.ndarray else self.A):
            for j, col_e in enumerate(row):
                x += "%s%.2f * %s%d " % (
                    ("+ " if col_e >= 0 and j != 0 else ""),
                    col_e,
                    self.var_names,
                    j + 1
                )
            x += "%s %d\n" % (
                self.A_sign[i].value,
                (self.b.asarray() if type(self.b) is not np.ndarray else self.b)[i]
            )

        for i, sign in enumerate(self.var_signs):
            x += "%s%d %s%s" % (
                self.var_names,
                i + 1,
                "free" if sign == LPSign.FREE else ("%s 0" % sign.value),
                ", " if (len(self.var_signs) - 1) != i else "\n"
            )
        return x


