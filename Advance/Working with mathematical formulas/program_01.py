# sigmoid
import numpy as np


def sigmoid(b):
    return 1/(1+np.exp(-(b)))
a=np.arange(12)
print("sigmoid vale is :\n",sigmoid(a))