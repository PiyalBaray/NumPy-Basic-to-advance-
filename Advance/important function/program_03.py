# Append use in 2D array
import numpy as np

a = np.random.randint(1, 100, 24).reshape(6, 4)
print("Original array:\n", a)

# New column (6 rows, 1 column)
new_col = np.ones((a.shape[0], 1), dtype=int)

# Append column
result = np.append(a, new_col, axis=1)
print("After appending column:\n", result)

