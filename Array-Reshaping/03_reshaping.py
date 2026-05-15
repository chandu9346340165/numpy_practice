import numpy as np

a = np.array([1,2,3,4,5,6,7,8])
b = a.reshape(2,2,2)
print(b)
print("dimensions of an array is : ",b.ndim)