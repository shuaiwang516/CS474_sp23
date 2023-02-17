# Check 3-colorable for any arbitrary graph

An simple python code to use this checker:
```python
from solver_any_graph import *

# define your graph here
my_graph = {
    0: [1, 2],
    1: [0, 2, 3, 4],
    2: [0, 1, 3, 4],
    3: [1, 2],
    4: [1, 2]
}

# call checker function
is_three_colorable(my_graph)
```

To run the example:
```
$ python3 example.py
```

The expected output is:
```
=====================================
Checking graph: {0: [1, 2], 1: [0, 2, 3, 4], 2: [0, 1, 3, 4], 3: [1, 2], 4: [1, 2]}
The graph is 3-colorable.
Node 0 is colored 0.
Node 1 is colored 2.
Node 2 is colored 1.
Node 3 is colored 0.
Node 4 is colored 0.
=====================================
=====================================
Checking graph: {0: [1, 2, 3, 4], 1: [0, 2, 3, 4], 2: [0, 1, 3, 4], 3: [0, 1, 2, 4], 4: [0, 1, 2, 3]}
The graph is not 3-colorable.
=====================================
```