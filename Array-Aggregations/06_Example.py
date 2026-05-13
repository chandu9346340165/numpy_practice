import numpy as np

a = np.array([
    [2,3,4],
    [4,5,6]
])

# Aggregations on 2d 
print(np.sum(a))
print(np.mean(a))
print("highest element indices",np.argmax(a)) # highest element indices
print("lowest element indices",np.argmin(a)) # lowest element indices
print(" standard deviation",np.std(a))    # standard deviation
print("variance",np.var(a))    # variance
print(" cummulative sum",np.cumsum(a)) # cummulative sum
print("cummulative product",np.cumprod(a))# cummulative product
