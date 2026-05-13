import numpy as np

a = np.array([
    [3,4,7],
    [4,5,6]
])

print(sum(a[a % 2 == 0]))
# sum of all even numbers

print(np.sum(a,axis = 1,keepdims = True))
# keepdims = True it keeps dimensions[[14][15]]

print(np.median(a))
# meadian 
                                        