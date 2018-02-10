import numpy as np
import lprogramming.model.lproblem as lp
import lprogramming.utils.matrix as mx_util

class Solver:

    def __init__(self, engine=np):
        print("Solver instance successfully created with %s engine" % ("CPU" if engine is np else "GPU"))
        self.engine = engine
        self.build_method = self.engine.CUDAMatrix() if self.engine is not np else None

    def __compute_active_constraints(self, a, x, b):

        print("Computing active constraints..")

        active_set = []

        # Compute A * x and then check which line is equal to b
        # Lot of CPU <--> GPU Transfers if on GPU
        result_components = mx_util.to_array(self.engine.dot(a, x))
        a_components = mx_util.to_array(a)
        b_components = mx_util.to_array(b)

        for component, b_element in enumerate(b_components):
            if b_element == result_components[component]:
                print("%d constraint is active" % (component+1))
                active = a_components[component]
                active_set.append(active)
            else:
                print("%d constraint is NOT active" % (component + 1))

        return mx_util.build(method=self.build_method, a=active_set)

    def solve(self, problem, start=None):

        optimal = False
        unlimited = False

        print("Solving problem:")
        print(problem)

        expected_shape = problem.c.transpose().shape

        # Check that the given starting point has a correct shape
        if expected_shape != start.shape:
            raise Exception("Bad start point: vector size does not match."
                            "Expected => %ds, Got => %ds" % (expected_shape, start.shape))

        # Check consistency between matrix types and selected engine
        if (
                type(problem.a) is not np.ndarray or
                type(problem.b) is not np.ndarray or
                type(problem.c) is not np.ndarray or
                    (start is not None and type(start) is not np.ndarray)
        ) and self.engine is np:
            raise Exception("Warning: Solver was initialized with a CUDA dataset but is not using cudamat")

        # TODO: If a starting point was not given, compute one
        # TODO: Check that the constraints used to compute the starting point are not parallel

        print("Building restricted primal..")

        # Get active constraints
        active = self.__compute_active_constraints(problem.a, start, problem.b)
        print(active)

        # Build restricted primal


