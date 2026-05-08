import numpy as np

# shape of 1d array
#shape tells dimensions of array
arr1d = np.shape([2,5,4,6])
print(arr1d)
# here one row 4 elemnts

# shape of 2d array
arr2d = np.array([[1,2,3,4]
                ,[5,6,7,8]])
print(arr2d.shape)
# here two rows and 4 coloumns

#shape of 3d array
arr3d = np.array([
    [[4,6,8,],
    [4,9,6],
    [9,7,6]]
                ])
print(arr3d.shape)

