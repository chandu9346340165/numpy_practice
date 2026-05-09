import numpy as np

# indexing on 2D array
arr = np.array([
    [1, 2, 4],
    [5, 3, 6],
    [9, 30, 6]
])
print(arr)
print(arr[0,1])
print(arr[1,2])
print(arr[2,2])

# Accessing full row
print(arr[0])

# Accessing full coloumn
print(arr[:,0])

