import numpy as np

a = np.array([3,4,5,7,5,6,7])
a.resize(2,2)
print(a)
# resize reduse the size of array also

b = a.reshape(2,2)
print(b)