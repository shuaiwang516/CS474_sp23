from z3 import *

# Declare function symbols
f = Function('f', IntSort(), IntSort(), IntSort())
g = Function('g', IntSort(), IntSort())

# Declare constants
e, c = Ints('e c')

# Declare variables
x = Int('x')

# Identity formula
identity_formula = And(f(x, e) == x, f(e, x) == x)

# Instantiate with depth 0 ground terms
instance_c = substitute(identity_formula, (x, c))
instance_e = substitute(identity_formula, (x, e))

# Negated formula with substituted constant symbol c
negated_formula = And(f(x, c) == x, f(c, x) == x, Not(e == c))

# Instantiate with depth 0 ground terms
instance_neg_c = substitute(negated_formula, (x, c))
instance_neg_e = substitute(negated_formula, (x, e))

# Create solver and add constraints
solver = Solver()
solver.add(instance_c)
solver.add(instance_e)
solver.add(instance_neg_c)
solver.add(instance_neg_e)

# Check for satisfiability
result = solver.check()
print("Result:", result)
