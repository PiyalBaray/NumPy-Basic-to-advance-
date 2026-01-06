# indexing for 2D

import numpy as np

a=np.arange(12).reshape(3,4)
print(a)

# print value :6
print('\t',a[1,2])
# print value : 11
print('\t',a[-1,-1])
#print value :3
print("\t",a[0,3])
#print value :8
print("\t",a[-1,0])
#print value :5
print("\t",a[1,1])