from z3 import *
import sys

def check(file_name):
    # Load the encoding file
    s = Solver()
    s.from_file(file_name)

    # Check satisfiability
    if s.check() == sat:
        print("SAT")
        m = s.model()
        print(m)
    
    else:
        print("UNSAT")
    

if __name__ == '__main__':
    if (len(sys.argv) != 2):
        print("Usage: python solver.py <input_file>")
        exit(1)
    
    check(sys.argv[1])