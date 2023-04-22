from z3 import *

# Declare functions and variables
f = Function("f", IntSort(), IntSort(), IntSort())
c, e = Ints("c e")
g = Function("g", IntSort(), IntSort())

# Create the formula
formula = And(
    f(f(c, c), c) == f(c, f(c, c)),
    f(f(e, c), c) == f(e, f(c, c)),
    f(f(c, e), c) == f(c, f(e, c)),
    f(f(c, c), e) == f(c, f(c, e)),
    f(f(e, e), c) == f(e, f(e, c)),
    f(f(c, e), e) == f(c, f(e, e)),
    f(f(e, c), e) == f(e, f(c, e)),
    f(f(e, e), e) == f(e, f(e, e)),
    And(f(c, e) == c, f(e, c) == c),
    And(f(e, e) == e, f(e, e) == e),
    And(f(c, g(c)) == e, f(g(c), c) == e),
    And(f(e, g(e)) == e, f(g(e), e) == e),
    And(f(c, c) == c, f(c, c) == c, Not(e == c)),
    And(f(e, c) == e, f(c, e) == e, Not(e == c))
)

# Check the satisfiability
solver = Solver()
solver.add(formula)
result = solver.check()

print(result)
if result == sat:
    model = solver.model()
    print(model)
