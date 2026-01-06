# Horizontal splitting
import numpy as np

a=np.arange(12,24).reshape(3,4)
print("Numpy array is :\n",a)

print(np.hsplit(a,2))