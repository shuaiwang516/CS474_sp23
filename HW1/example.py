from solver_any_graph import *

# define your graph here
my_graph = {
    0: [1, 2],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [1, 2],
    4: [1, 2]
}

my_graph2 = {
    0: [1, 2, 3, 4],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [0, 1, 2, 4],
    4: [0, 1, 2, 3]
}

# call checker function
is_three_colorable(my_graph)
is_three_colorable(my_graph2)
