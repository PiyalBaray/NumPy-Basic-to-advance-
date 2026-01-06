import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create data
x = np.linspace(-np.pi/2 + 0.1, np.pi/2 - 0.1, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

Z = np.tan(X)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z)

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('tan(X)')
ax.set_title('3D Tan Graph')

plt.show()
