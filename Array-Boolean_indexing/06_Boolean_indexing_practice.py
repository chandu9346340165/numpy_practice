# Boolean indexing in 2D
import numpy as np

num = np.array([
    [2,3,4],
    [4,5,8],
    [5,6,8]
])
# elemnts greater than 5
print(num[num > 5])
