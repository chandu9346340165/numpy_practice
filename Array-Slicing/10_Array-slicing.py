import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# slice last two coloumns
print(arr[:,1:])

# sllicing using step
print(arr[: , ::2])

# reverse row order
print(arr[::-1])

#reverse  coloumns
print(arr[: , ::-1])