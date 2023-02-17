from z3 import *

def is_three_colorable(graph):
    num_color = 3
    print("=====================================")
    print("Checking graph: {}".format(graph))
    solver = Solver()

    # Create a list of propositional variables
    props_vars = {}
    for node in graph:
        for color in range(num_color):
            props_vars[(node, color)] = Bool(f"p_{node}_{color}")

    # Add constraints to the solver
    for node in graph:
        # At least one color per node
        solver.add(Or([props_vars[(node, color)] for color in range(num_color)]))

        # At most one color per node
        for c1 in range(num_color):
            for c2 in range(c1 + 1, num_color):
                solver.add(Not(And(props_vars[(node, c1)], props_vars[(node, c2)])))

        # Nodes connected by an edge have different colors
        for neighbor in graph[node]:
            for color in range(num_color):
                solver.add(Implies(props_vars[(node, color)], Not(props_vars[(neighbor, color)])))

    # Check for satisfiability
    if solver.check() == sat:
        print("The graph is 3-colorable.")
        model = solver.model()
        # print the model with detailed color assignments
        for node in graph:
            for color in range(num_color):
                if is_true(model[props_vars[(node, color)]]):
                    print(f"Node {node} is colored {color}.")
        print("=====================================")
        return True
    else:
        print("The graph is not 3-colorable.")
        print("=====================================")
        return False
