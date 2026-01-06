# slicing for 2D numpy array

import numpy as np

a=np.arange(12).reshape(3,4)
print(a)
# print [0],1,2,3](row index:0)
print("row index:0:\n",a[0,: ])
#print [0,4,8](column:index:0)
print("column:index:0\n",a[:,0])
#print [0 4 8],[5 6],[9 10]
print(a[1: ,1:3])