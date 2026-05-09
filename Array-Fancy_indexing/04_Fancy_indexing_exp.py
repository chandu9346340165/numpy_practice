import numpy as np

arr = np.array([
    [3,4,6],
    [4,6,7],
    [7,8,9]
])

# entire rows and coloumns
print(arr[[0,2]][:,[0,2]])