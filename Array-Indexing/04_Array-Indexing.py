import numpy as np

# indexing in 3d array
arr = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 9],
        [4, 9]
    ]

])
print(arr)
print(arr[0,1,1])
print(arr[1,0,1])