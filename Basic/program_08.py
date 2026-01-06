# Dot product
import numpy as np

a=np.arange(12).reshape(3,4)
b=np.arange(12,24).reshape(4,3)

print("1st Numpy array is :","\n",a,"\n2nd Numpy array is :","\n",b)

#Dot product of this two array
print("result is :","\n",np.dot(a,b))