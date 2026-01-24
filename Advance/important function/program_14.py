# how to use flip() function in 2D numpy array
import numpy as np

b = np.arange(12, 24).reshape(3, 4)

print("This is real numpy array:\n", b)

print("Flip full array:\n", np.flip(b))
print("Flip row-wise:\n", np.flip(b, axis=0))
print("Flip column-wise:\n", np.flip(b, axis=1))
