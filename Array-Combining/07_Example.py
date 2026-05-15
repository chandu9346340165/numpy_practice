import numpy as np

a = np.array([1,2,3,4,5,6])

print(np.split(a,3))

# horizontal split
print(np.hsplit(a,2))

# vertical split
print(a.vsplit(a,3))