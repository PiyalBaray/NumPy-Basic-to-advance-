# How to use clip () function in numpy array

import numpy as np

a=np.array([110,350,28,50,37,94,92,5,30,8,9,78,2,21])
print("This is  numpy array :\n",a)
print("This is numpy array use clip function then:\n",np.clip(a,a_min=25,a_max=75))

