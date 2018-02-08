import numpy as np
import lprogramming.model.lproblem as lp

class Solver:

    def __init__(self, engine=np):
        print("Solver instance successfully created with %s engine" % ("CPU" if engine is np else "GPU"))
        self.engine = engine



    # Try not to abuse this method. Could be very slow
    def __to_array(self, obj):
        return obj.asarray() if type(obj) is not np.ndarray else obj

    # Wrapper to have a generic dot operation for cpu or gpu.
    # In either case returns a np array, thus gpu impl will be slow.
    # It will make sense to use gpu only if the matrix are very huge
    def dot(self, a, b):

        # Fist, check which engine we are using
        if self.engine != np:
            # If we are un GPU we need to transfer the data from Host to Device
            # Don't worry about warnings: we will never call CUDAMatrix on np causing exceptions.
            if type(a) is np.ndarray:
                a = self.engine.CUDAMatrix(a)
            if type(b) is np.ndarray:
                b = self.engine.CUDAMatrix(b)

        # noinspection PyTypeChecker
        res = self.engine.dot(a, b)

        return self.__to_array(res)

    def __compute_active_constraints(self, A, x, b):

        print("Computing active constraints..")

        I = []
        # Compute A * x and then check which line is equal to b
        res = self.dot(A, x)

        a_components = self.__to_array(A)

        for i, const in enumerate(self.__to_array(b)):
            if const == res[i]:
                print("%d constraint is active" % (i+1))
                active = self.__to_array(a_components[i])
                I.append(active)
            else:
                print("%d constraint is NOT active" % (i + 1))

        return np.array(I)

    def solve(self, problem, start):

        optimal = False
        unlimited = False

        print("Solving problem:")
        print(problem)

        expected_shape = problem.c.transpose().shape

        if expected_shape != start.shape:
            raise Exception("Bad start point: vector size does not match."
                            "Expected => %ds, Got => %ds" % (expected_shape, start.shape))

        if (
                type(problem.A) is not np.ndarray or
                type(problem.b) is not np.ndarray or
                type(problem.c) is not np.ndarray or
                type(start) is not np.ndarray
        ) and self.engine is np:
            raise Exception("Warning: Solver was initialized with a CUDA dataset but is not using cudamat")

        print("Building restricted primal..")

        # Get active constraints

        # Todo...
        print(self.__compute_active_constraints(problem.A, start, problem.b))

        # TODO....
