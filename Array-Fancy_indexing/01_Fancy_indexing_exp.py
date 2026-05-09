import numpy as np

arr = np.array([2,3,4,6,6,7,3])
#print elements at indexes 0 2 3
print(arr[[0,2,3]])

# Repeated elements
print(arr[[0, 0, 0]])
#output : 2 2 2

# Access elements in different order
print(arr[[3,1,4]])