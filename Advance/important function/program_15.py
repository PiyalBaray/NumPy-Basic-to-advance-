# how to use put () in numpy array

import numpy as np

a=np.arange(12,24)
print("This is my numpy array:\n",a)
np.put(a,[0,1],[50,52])
print("This my new numpy array:\n",a)

