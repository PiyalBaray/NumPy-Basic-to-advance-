# ndim=checking numpy array which dimension.

import numpy as np



a=np.arange(10)
b=np.arange(12,dtype=float).reshape(3,4)
c=np.arange(8).reshape(2,2,2)
print(a,'\n',a.ndim, "D Numpy array")
print(b,'\n',b.ndim,'D Numpy array')
print( c,'\n',c.ndim,'D Numpy array')
