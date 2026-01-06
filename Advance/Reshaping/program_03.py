# Vertical stacking
import numpy as np


a=np.arange(12,24).reshape(4,3)
b=np.arange(12).reshape(4,3)

print("1st numpy array :\n",a)
print("2nd numpy array :\n",b)

print("Vertical is :\n",np.vstack((a,b)))