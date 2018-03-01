import numpy as np
import lprogramming.model.lproblem as lp
import lprogramming.utils.matrix as mx_util
import math
import lprogramming.utils.plotter as plt


class UnlimitedSolutionException(Exception):
    def __init__(self, m): super(m)


class Solver:

    def __init__(self):
        print("Solver instance successfully created")

    def compute_constraints(self, a, x, b):

        print("Computing active constraints..\n")

        # Compute A * x and then check which line is equal to b
        result_components = np.dot(a, x)

        active_idx = []
        inactive_idx = []
        out = {}

        for component, b_element in enumerate(b):
            if b_element == result_components[component]:
                print("%d constraint is active" % (component+1))
                active_idx.append(component)
            else:
                print("%d constraint is NOT active" % (component + 1))
                inactive_idx.append(component)

        if len(active_idx) > 0:
            out["active"] = {
                "a": a[active_idx, :],
                "b": b[active_idx, :]
            }
        else:
            out["active"] = None

        if len(inactive_idx) > 0:
            out["inactive"] = {
                "a": a[inactive_idx, :],
                "b": b[inactive_idx, :]
            }
        else:
            out["inactive"] = None

        print("")

        return out

    def grow_onto(self, start, direction, inactive_a, inactive_b):

        a_x = np.dot(inactive_a, start)
        a_csi = np.dot(inactive_a, direction)

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

        new = (direction * growth) + start

        print("Start : %s\nDirection : \n%s\nStep: %s\nDestination : \n%s\n" % (start, direction, growth, new))

        return new

    def solve(self, problem, start=None):

        optimal = False
        history = []

        print("Solving problem:\n")
        print(problem)

        # Prepare the starting point, if exists
        if start is not None:

            # Build start point matrix
            start = mx_util.build(object=start)

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

        history.append(start)

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

            # Recompute active constraints
            result = self.compute_constraints(problem.a, current, problem.b)
            history.append(current)
        else:
            current = start

        # Find the optimal solution, if exists
        while not optimal:

            print("Building restricted primal..\n")

            # Build the const matrix as a column vector of zeroes
            zeroes = mx_util.build(
                b=np.zeros(shape=result["active"]["b"].shape)
            )

            # Build the restricted primal
            restricted_p = lp.LPProblem(
                objective=lp.LPObjective.MAXIMIZE,
                c=problem.c,
                a=result["active"]["a"],
                b=zeroes,
                a_signs=lp.init_constraints_signs_to(lp.LPSign.LE, result["active"]["a"]),
                v_name="csi"
            )

            print(restricted_p)

            # If the restricted dual has no solution, than grow like c * csi = 1
            # The problem has no solution when there are more columns than rows in a.
            # Thus we cant compute the inverse of a
            if restricted_p.a.shape[lp.kColComponent] > restricted_p.a.shape[lp.kRowComponent]:

                print("The restricted dual has no solution, computing growing direction")

                # Add cost row to csi matrix
                i = np.vstack([result["active"]["a"], problem.c])
                b = np.vstack([np.zeros(shape=result["active"]["b"].shape), [1]])

                # a * csi = 0 & c * csi = 1
                csi = np.linalg.inv(i).dot(b)

                # After computing csi, grow
                current = self.grow_onto(
                    start=current,
                    direction=csi,
                    inactive_a=result["inactive"]["a"],
                    inactive_b=result["inactive"]["b"]
                )

                # Recompute active constraints
                result = self.compute_constraints(problem.a, current, problem.b)

                history.append(current)

            # Otherwise compute growing direction
            else:

                # We now may have the same amount rows = cols or rows > cols.
                # If rows > cols, we must remove some linear dependent constraint
                if restricted_p.a.shape[lp.kColComponent] < restricted_p.a.shape[lp.kRowComponent]:
                    # Remove the constraint whose gradient is in the cone produced by the others
                    # while restricted_p.a.shape[lp.kColComponent] == restricted_p.a.shape[lp.kRowComponent]:
                    print("Not able to eliminate linear dependent constraints. YET.")



                    return

                print("Building restricted dual..\n")

                # Build the restricted dual
                restricted_d = restricted_p.get_dual(var_name="eta")

                print(restricted_d)

                # Compute the solution
                eta = np.linalg.inv(restricted_d.a).dot(restricted_d.b)

                # Check that is feasible
                if restricted_d.respects_var_signs(eta):
                    # We found the optimal solution
                    optimal = True

                    print("Optimal solution found: %s" % current)

                # Otherwise compute a growing direction
                else:

                    print("The restricted dual has an inconsistent solution, computing growing direction..")

                    idx = -1
                    base = []

                    # Find a base
                    for component, value in enumerate(eta):
                        if idx == -1 and not restricted_d.var_signs[component](value, 0):
                            idx = component
                            base.append([-1])
                        else:
                            base.append([0])

                    base = np.array(base)

                    csi = np.linalg.inv(restricted_p.a).dot(base)

                    # After computing csi, grow
                    current = self.grow_onto(
                        start=current,
                        direction=csi,
                        inactive_a=result["inactive"]["a"],
                        inactive_b=result["inactive"]["b"]
                    )

                    # Recompute active constraints
                    result = self.compute_constraints(problem.a, current, problem.b)

                    history.append(current)

        plt.plot(problem, history=history)