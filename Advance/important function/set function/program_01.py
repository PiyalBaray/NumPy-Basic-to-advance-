# How to use set function

import numpy as np


a = np.array([1,2,3,4,5])
b = np.array([3,4,5,6,7])

# How to use union1d() function
print("Union of arrays:", np.union1d(a, b))
print("Union of arrays:", np.union1d(b,a))

# How to use intersect1d() function
print(np.intersect1d(a,b))
print( np.intersect1d(b,a))

# How to use setdiff1d() function
print(np.setdiff1d(a,b))
print( np.setdiff1d(b,a))

# How to use setxor1d() function
print( np.setxor1d(a,b))
print( np.setxor1d(b,a))






