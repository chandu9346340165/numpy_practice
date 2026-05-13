import numpy as np

a = np.array([
    [3,4,7],
    [4,5,6]
])

print(np.mean(a,axis = 0))
# mean col wise

print(np.mean(a,axis=1))
# mean row wise