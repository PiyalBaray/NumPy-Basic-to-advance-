# working with missing vale
import numpy as np

a=np.array([1,2,3,4,5,6,7,8,np.nan,6])
print(a)
print("Show missing vale :\n",np.isnan(a))