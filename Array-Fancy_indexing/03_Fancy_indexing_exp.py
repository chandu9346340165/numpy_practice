import numpy as np

arr = np.array([
    [3,4,6],
    [4,6,7],
    [7,8,9]
])
print(arr[[0,2]])
# 1st and 3rd row

print(arr[[0,2],[1,2]])
# out put is 3 9

print(arr[:, [0,2]])