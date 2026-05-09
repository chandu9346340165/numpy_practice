import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10])
# Even numbers
print(arr[arr % 2== 0])

#odd numbers
print(arr[arr % 2 != 0])