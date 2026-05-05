import numpy as np

#conver 1-6 into 2x3 
a = np.arange(1,7).reshape(2,3)
print(a)

# conver 2d into 1d

a = np.array([[1,3],[3,5]]).flatten()
print(a)