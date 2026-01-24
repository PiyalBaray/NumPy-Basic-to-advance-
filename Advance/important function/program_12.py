# how to use isin() function

import numpy as np

a=np.array([2000,40000,35000,60000])
b=np.array([20000,8848,40000,35000,60000,9444,8595,9494,9,4484])
print(np.isin(a,b))

print(np.isin(b,a))

