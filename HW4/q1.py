from z3 import *

# Create real variables for r, s, r', s'
r, s = Reals('r s')
r_prime, s_prime = Reals("r' s'")

# Define the expected payoffs for player R and player S
EP_R = r * (s * 90 + (1 - s) * 20) + (1 - r) * (s * 30 + (1 - s) * 60)
EP_S = s * (r * 10 + (1 - r) * 70) + (1 - s) * (r * 80 + (1 - r) * 40)

# Define the expected payoffs for player R and player S when deviating
EP_R_deviate = r_prime * (s * 90 + (1 - s) * 20) + (1 - r_prime) * (s * 30 + (1 - s) * 60)
EP_S_deviate = s_prime * (r * 10 + (1 - r) * 70) + (1 - s_prime) * (r * 80 + (1 - r) * 40)

# Create a solver
solver = Solver()

# Add constraints on r, s, r', and s' to be within the interval [0, 1]
solver.add(0 <= r, r <= 1, 0 <= s, s <= 1, 0 <= r_prime, r_prime <= 1, 0 <= s_prime, s_prime <= 1)

# Add the conditions for Nash equilibrium
solver.add(ForAll(r_prime, EP_R <= EP_R_deviate))
solver.add(ForAll(s_prime, EP_S <= EP_S_deviate))

# Check the satisfiability and print the result
if solver.check() == sat:
    model = solver.model()
    print("Nash equilibrium found:")
    print("r =", model[r].as_decimal(5))
    print("s =", model[s].as_decimal(5))
else:
    print("No Nash equilibrium found or unable to solve.")
