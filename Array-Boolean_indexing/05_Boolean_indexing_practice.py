import numpy as np

num = np.array([12,54,21,36,3,16,1,514,15,13,17])
# Elements between 10 - 20
print(num[(num >= 10) & (num <= 20)])

# elements less than 5 and greater than 15
print(num[(num < 5) | (num > 15)])