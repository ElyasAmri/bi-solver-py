import matplotlib.pyplot as plt
import numpy as np

xr = range(1, 5)
yr = range(1, 2)

loss = 10


def clamp(v):
    v -= loss
    return 0 if v < 0 else v


def generate(r, c):
    return sum(clamp(x ^ y) for x in range(1, r) for y in range(1, c))


xdata = [i for i in xr for _ in yr]
ydata = [i for i in yr for _ in xr]
zdata = [generate(i, j) for i in yr for j in xr]

fig = plt.figure(figsize=(18, 12))
# Create 3D container
ax = plt.axes(projection='3d')
# Visualize 3D scatter plot
ax.scatter3D(xdata, ydata, zdata)
# Give labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
# Save figure
# plt.savefig('6d_scatter.png', dpi=300)
plt.show()
if __name__ == '__main__':
    pass
