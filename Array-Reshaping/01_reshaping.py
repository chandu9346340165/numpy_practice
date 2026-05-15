import numpy as np

a = np.array([2,4,6,6,4,3,2,4,5])

# 1D to 2D
b = a.reshape(3,3)
print(b, "number of dimensions",b.ndim)
