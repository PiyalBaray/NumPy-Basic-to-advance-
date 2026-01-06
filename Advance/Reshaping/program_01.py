# 2D,3D,.....nD numpy array convert to 1D numpy array. use nditer()

import numpy as np


a=np.arange(27).reshape(3,3,3)
a1=np.arange(12).reshape(4,3)

a=np.arange(12).reshape(4,3)
print("3D numpy array to convert 1D numpy array :")
for i in np.nditer(a):
    print(i)
print("2D numpy array to convert 1D numpy array :")
for i in np.nditer(a1):
    print(i)



