import numpy as np
import lprogramming.model.lproblem as lp
import lprogramming.utils.matrix as mx_util
import math


class UnlimitedSolutionException(Exception):
    def __init__(self, m): super(m)


class Solver:

    def __init__(self):
        self.engine = None
        self.build_method = None
        print("Solver instance successfully created")

    def compute_constraints(self, a, x, b):

        # Compute A * x and then check which line is equal to b
        # Lot of CPU <--> GPU Transfers if on GPU
        result_components = mx_util.to_array(self.engine.dot(a, x))
        a_components = mx_util.to_array(a)
        b_components = mx_util.to_array(b)

        active_idx = []
        inactive_idx = []
        out = {}

        for component, b_element in enumerate(b_components):
            if b_element == result_components[component]:
                print("%d constraint is active" % (component+1))
                active_idx.append(component)
            else:
                print("%d constraint is NOT active" % (component + 1))
                inactive_idx.append(component)

        # Please note that if we apply the build method to a matrix already built nothing will happen
        # It is just handy to do it anyway in order to get a dictionary containing all elements with 1 instruction
        # In this case if we are working with GPU we need to rebuild the ndarrays
        if len(active_idx) > 0:
            out["active"] = mx_util.build(
                method=self.build_method,
                a=a_components[active_idx, :],
                b=b_components[active_idx, :]
            )
        else:
            out["active"] = None

        if len(inactive_idx) > 0:
            out["inactive"] = mx_util.build(
                method=self.build_method,
                a=a_components[inactive_idx, :],
                b=b_components[inactive_idx, :]
            )
        else:
            out["inactive"] = None

        return out

    def grow_onto(self, start, direction, inactive_a, inactive_b):

        a_x = mx_util.to_array(self.engine.dot(inactive_a, start))
        a_csi = mx_util.to_array(self.engine.dot(inactive_a, direction))
        inactive_b = mx_util.to_array(inactive_b)

        growth = -1

        # lambda <= (b_i - a_x) / a_csi
        for component in range(0, inactive_b.size):
            if a_csi[component] > 0:
                qty = ((inactive_b[component] - a_x[component]) / a_csi[component])
                if growth == -1:
                    growth = qty
                else:
                    growth = min(growth, qty)

        if math.isinf(growth):
            raise UnlimitedSolutionException("Unlimited growth direction")

        else:
            if self.engine is np:
                return (direction * growth) + start
            else:
                return direction.mult(growth).add(start)

    def solve(self, problem, start=None):

        optimal = False
        current = None

        print("Matrix handling will be performed by: %s" % ("numpy" if problem.engine is np else "cudamat"))

        self.engine = problem.engine
        self.build_method = problem.build_method

        print("Solving problem:\n")
        print(problem)

        # Prepare the starting point, if exists
        if start is not None:

            # Build start point matrix
            start = mx_util.build(self.build_method, object=start)

            # Get expected start shape
            expected_shape = problem.c.transpose().shape

            # Check that the given starting point has a correct shape
            if expected_shape != start.shape:
                raise Exception("Bad start point: vector size does not match."
                                "Expected => %ds, Got => %ds" % (expected_shape, start.shape))

            # Check feasibility
            if not problem.is_feasible(start):
                raise Exception("Starting point is unfeasible :(")

        # TODO: If a starting point was not given, compute one
        # TODO: Check that the constraints used to compute the starting point are not parallel

        print("Computing active constraints..\n")
        # Get active constraints
        result = self.compute_constraints(problem.a, start, problem.b)

        # If there are no active constraints grow with respect to c
        if result["active"] is None:
            current = self.grow_onto(
                start=start,
                direction=problem.c.transpose(),
                inactive_a=result["inactive"]["a"],
                inactive_b=result["inactive"]["b"]
            )
            print(current)

        # Else compute next point
        else:
            print("Building restricted primal..\n")

            # Build the const matrix as a column vector of zeroes
            constants = mx_util.build(method=self.build_method, b=np.zeros(shape=(result["active"].shape[lp.kRowComponent], 1)))

            pr = lp.LPProblem(
                objective=lp.LPObjective.MAXIMIZE,
                c=problem.c,
                a=result["active"],
                b= constants,
                a_signs=lp.init_constraints_signs_to(lp.LPSign.LE, result["active"]),
                v_name="csi"
            )

            print(pr)

            print("Building restricted dual..\n")

            print(pr.get_dual(var_name="eta"))

            # Build restricted primal


