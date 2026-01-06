#sort
import numpy as np

a=np.random.randint(1,100,15)
b=np.random.randint(1,100,24).reshape(6,4)
print("This is numpy array:",a)
print("This numpy array sort vale :\n",np.sort(a))
print("This numpy array largest vale :\n",np.sort(a)[::-1])
print("This is numpy array:\n",b)
print("This numpy array sort vale of rows :\n",np.sort(b,axis=1))
print("This numpy array largest vale of rows :\n",np.sort(b,axis=1)[::-1])
print("This numpy array sort vale of columns :\n",np.sort(b,axis=0))
print("This numpy array largest vale of columns :\n",np.sort(b,axis=0)[::-1])
