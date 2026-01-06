#concatenate()
import numpy as np

a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)

print('This is 1st numpy array :\n', a)
print('This is 2nd numpy array :\n', b)

print("New numpy array:\n",np.concatenate((a, b), axis=1))
