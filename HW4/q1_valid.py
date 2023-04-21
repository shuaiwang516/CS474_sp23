from z3 import *

r, s, r_prime, s_prime = Reals('r s r_prime s_prime')
P_R11, P_R12, P_R21, P_R22 = Reals('P_R11 P_R12 P_R21 P_R22')
P_S11, P_S12, P_S21, P_S22 = Reals('P_S11 P_S12 P_S21 P_S22')

EP_R = r * (s * P_R11 + (1 - s) * P_R12) + (1 - r) * (s * P_R21 + (1 - s) * P_R22)
EP_S = s * (r * P_S11 + (1 - r) * P_S21) + (1 - s) * (r * P_S12 + (1 - r) * P_S22)

EP_R_deviate = r_prime * (s * P_R11 + (1 - s) * P_R12) + (1 - r_prime) * (s * P_R21 + (1 - s) * P_R22)
EP_S_deviate = s_prime * (r * P_S11 + (1 - r) * P_S21) + (1 - s_prime) * (r * P_S12 + (1 - r) * P_S22)

nash_eq = ForAll([r_prime, s_prime, P_R11, P_R12, P_R21, P_R22, P_S11, P_S12, P_S21, P_S22],
            Implies(
                And(
                    0 <= r_prime, r_prime <= 1,
                    0 <= s_prime, s_prime <= 1,
                ),
            Exists([r, s],
                   Implies(
                          And(
                                0 <= r, r <= 1,
                                0 <= s, s <= 1,
                            ),
                            And(EP_R >= EP_R_deviate, EP_S >= EP_S_deviate)
                   )
            )))

negated_nash_eq = Not(nash_eq)

s = Solver()
s.add(negated_nash_eq)
result = s.check()

if result == unsat:
    print("Theorem is valid.")
else:
    print("Unable to prove the theorem valid.")

qe_nash_eq = Tactic('qe').apply(nash_eq).as_expr()

# print out the quantifier-free formula
print("Quantifier-free formula: ")
print(qe_nash_eq)