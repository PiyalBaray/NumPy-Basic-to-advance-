import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# data
a = np.linspace(-10, 9, 20)
b = np.linspace(-10, 9, 20)

xx, yy = np.meshgrid(a, b)

# 2D scatter (matplotlib)
plt.scatter(xx.ravel(), yy.ravel())
#plt.show()

# function
def func(x, y):
    return x**2 + y**2

zz = func(xx, yy)

# 3D surface plot (plotly)
fig = go.Figure(data=[
    go.Surface(x=xx, y=yy, z=zz)
])

fig.show()






