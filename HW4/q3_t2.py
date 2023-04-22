from z3 import *

# Declare the function f, constants b and c, and variable e
f = Function('f', IntSort(), IntSort(), IntSort())
b, c, e = Ints('b c e')

# Set up the formula
formula1 = And(f(e, b) == e, f(b, e) == e)
formula2 = And(f(e, c) == e, f(c, e) == e)
formula3 = Not(b == c)
formula4 = And(formula1, formula2, formula3)

# Identity axioms
identity_b = And(f(b, e) == b, f(e, b) == b)
identity_c = And(f(c, e) == c, f(e, c) == c)

# Combine the formulas and axioms
complete_formula = And(formula4, identity_b, identity_c)

# Create a solver and add the formula
solver = Solver()
solver.add(complete_formula)

# Check satisfiability
result = solver.check()
print(result)
