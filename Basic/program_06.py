# A numpy array max,min,mean,median

import numpy as np

a=np.arange(12).reshape(3,4)

# max value of numpy array's row and column
print(a,'\n',"This nampy array row's max is :",np.max(a,axis=0),"\n","This nampy array column's max is :",np.max(a,axis=1))

# min value of numpy array's row and column
print("This nampy array row's min is :",np.min(a,axis=0),"\n","This nampy array column's min is :",np.min(a,axis=1))

# mean value of numpy array's row and column
print("This nampy array row's mean is :",np.mean(a,axis=0),"\n","This nampy array column's mean is :",np.mean(a,axis=1))

# median value of numpy array's row and column
print("This nampy array row's median is :",np.median(a,axis=0),"\n","This nampy array column's median is :",np.median(a,axis=1))

