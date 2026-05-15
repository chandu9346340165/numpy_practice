import numpy as np

a = np.array([3,4,6,3,5,6,3,5])
# -1 indicates automatic takes coloumn
b = a.reshape(2,-1)
print(b)

# automatically required rows are selected
c = a.reshape(-1,4)
print(c)