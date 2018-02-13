import lprogramming.model.lproblem as lp
import lprogramming.solver.simplex as simplex

# First things first: provide a consistent representation of the input
c = [
    [30, 50]
]

a = [
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
    [0],
    [0]
]

# Set signs, in this case all constraints have the same sign.
# Note: You could set signs manually if you want, just provide a consistent array of LPSigns
a_signs = lp.init_constraints_signs_to(lp.LPSign.LE, a)

# Set the 2 variable signs to less then or equal to 0
v_signs = [lp.LPSign.GE] * 2


# If you do not provide the signs for the variables, they are all set to FREE
# Create a new instance of a problem. See the class definition for the full list of parameters
# Shortly, we need the objective, the built input data, the A matrix signs,
# var signs (default to FREE) and var names (Default to x)
p = lp.LPProblem(lp.LPObjective.MAXIMIZE, c=c, a=a, b=b, a_signs=a_signs, v_signs=v_signs)

# We can build the dual representation like this
# An optional parameter can be specified and refers to the var names (default to y)
d = p.get_dual()

# Print the problem in an intuitive way
print(p)
print(d)

# simplex.solve(p, None)
solver = simplex.Solver()

solver.solve(p, start)
