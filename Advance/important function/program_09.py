# calculate a cumulative sum in 2d use cumsum() function

import numpy as np
a=np.array([2,1,1,2,1,5,56,9,1,8,5,7,5,2,4,5,6,8]).reshape(3,6)
print(np.cumsum(a,axis=0))

print(np.cumsum(a,axis=1))
