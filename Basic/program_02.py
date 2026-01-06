# checking type of numpy array use dtype.

import numpy as np

a=np.arange(10)
b=np.arange(12,dtype=float).reshape(3,4)
c=np.arange(8).reshape(2,2,2)
d = np.array(["apple", "banana", "cherry"])
print('This Numpy array is :',a.dtype,'\n',a)
print('This Numpy array is :',b.dtype,'\n',b)
print('This Numpy array is :',c.dtype,'\n',c)
print('This Numpy array is :',d.dtype,'\n',d)