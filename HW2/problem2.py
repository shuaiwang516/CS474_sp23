from z3 import *;

(p, q, r) = Bools("p q r")

original_formula = And(Or(q, Not(r)), Or(Not(p), r), Or(Not(q), r, p), Or(p, q, Not(q)), Or(Not(r), q))
resolution_formula = And(Or(q, Not(r)), Or(Not(p), r), Or(Not(q), r, p), Or(q, Not(p)), Or(Not(q), r))

s = Solver()
s.add(original_formula)
print("=====================================")
print("Checking original, result is " + str(s.check()))
print("=====================================")
s.reset()
s.add(resolution_formula)
print("=====================================")
print("Checking resolution, result is " + str(s.check()))
print("=====================================")