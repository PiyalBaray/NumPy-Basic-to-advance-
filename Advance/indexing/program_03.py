# indexing for 3D

import numpy as np

a=np.arange(8).reshape(2,2,2)
print(a)

# print vale: 3
print(a[0,1,1])
#print value :7
print(a[1,-1,-1])
#print vale :6
print(a[-1,-1,-2])