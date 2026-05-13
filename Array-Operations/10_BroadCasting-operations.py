import numpy as np

a = np.array([
    [1,2,5],
    [4,8,9]
])
b = np.array([[10],
              [20]])
# coloumn wise braodcasting
print(a + b)
print((a+b).shape)
