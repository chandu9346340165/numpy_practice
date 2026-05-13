import numpy as np

a = np.array([
    [3,4,7],
    [4,5,6]
])

print(np.sum(a,axis = 1))
# it sum row wise

print(np.sum(a,axis = 0))
# col wise sum