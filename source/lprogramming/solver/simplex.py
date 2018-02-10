import numpy as np
import lprogramming.model.lproblem as lp
import lprogramming.utils.matrix as mx_util

class Solver:

    def __init__(self, engine=np):
        print("Solver instance successfully created with %s engine" % ("CPU" if engine is np else "GPU"))
        self.engine = engine
        self.build_method = self.engine.CUDAMatrix if self.engine is not np else None

    def __compute_active_constraints(self, a, x, b):

        # Compute A * x and then check which line is equal to b
        # Lot of CPU <--> GPU Transfers if on GPU
        result_components = mx_util.to_array(self.engine.dot(a, x))
        a_components = mx_util.to_array(a)
        b_components = mx_util.to_array(b)

        selected_idx = []

        for component, b_element in enumerate(b_components):
            if b_element == result_components[component]:
                print("%d constraint is active" % (component+1))
                selected_idx.append(component)
            else:
                print("%d constraint is NOT active" % (component + 1))

        # Please note that if we apply the build method to a matrix already built nothing will happen
        # It is just handy to do it anyway in order to get a dictionary containing all elements with 1 instruction
        # In this case if we are working with GPU we need to rebuild the ndarrays
        return mx_util.build(method=self.build_method, a=a_components[selected_idx, :])

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

        print("Computing active constraints..")
        # Get active constraints
        active_constraints = self.__compute_active_constraints(problem.a, start, problem.b)

        print("Building restricted primal..")

        # Build the const matrix as a column vector of zeroes
        constants = mx_util.build(method=self.build_method, b=np.zeros(shape=(active_constraints.shape[lp.kRowComponent], 1)))

        pr = lp.LPProblem(
            objective=lp.LPObjective.MAXIMIZE,
            c=problem.c,
            a=active_constraints,
            b= constants,
            a_signs=lp.init_constraints_signs_to(lp.LPSign.LE, active_constraints),
            v_name="csi"
        )

        print(pr)

        print("Building restricted dual..")

        print(pr.get_dual(var_name="eta"))

        # Build restricted primal


