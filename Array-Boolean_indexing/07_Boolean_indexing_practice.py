import numpy as np

num = np.array([2,3,5,6,7,7,2])
# Replace elements 7 is 0
num[num == 7] = 0
print(num)

# count elements greater than 5
print(len(num[num > 5]))

# multiples of 2

print(num[num % 2 == 0])