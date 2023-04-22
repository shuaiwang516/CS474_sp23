from z3 import *

# Declare functions and variables
f = Function("f", IntSort(), IntSort(), IntSort())
c, d, e = Ints("c d e")
g = Function("g", IntSort(), IntSort())

formula = And(
    f(f(c, c), c) == f(c, f(c, c)),
    f(f(d, c), c) == f(d, f(c, c)),
    f(f(c, d), c) == f(c, f(d, c)),
    f(f(c, c), d) == f(c, f(c, d)),
    f(f(d, d), c) == f(d, f(d, c)),
    f(f(c, d), d) == f(c, f(d, d)),
    f(f(d, c), d) == f(d, f(c, d)),
    f(f(d, d), d) == f(d, f(d, d)),
    And(f(c, e) == c, f(e, c) == c),
    And(f(d, e) == d, f(e, d) == d),
    And(f(c, g(c)) == e, f(g(c), c) == e),
    And(f(d, g(d)) == e, f(g(d), d) == e),
    And(f(c, d) == e, f(d, c) == e, Not(d == g(c))),
    And(f(d, c) == e, f(c, d) == e, Not(c == g(d)))
)

# Check the satisfiability
solver = Solver()
solver.add(formula)
result = solver.check()

print(result)
if result == sat:
    model = solver.model()
    print(model)
