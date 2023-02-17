from z3 import *
import sys

def check(file_name):
    print("=====================================")
    print("Checking file: {}".format(file_name))
    # Load the encoding file
    s = Solver()
    s.from_file(file_name)

    # Check satisfiability
    if s.check() == sat:
        print("file {} is SAT".format(file_name))
        m = s.model()
        print(m)
    
    else:
        print("file {} is UNSAT".format(file_name))
    
    print("=====================================")

if __name__ == '__main__':
    check('swang516_hw1_g.smt2')
    check('swang516_hw1_h.smt2')