import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the function
def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2)) / np.sqrt(x**2 + y**2)

# Create grid
x = np.linspace(-10, 10, 200)
y = np.linspace(-10, 10, 200)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k', alpha=0.9)

ax.set_title("3D Visualization: sinc(r) function", fontsize=14, fontweight='bold')
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

fig.colorbar(surf, shrink=0.5, aspect=10)
plt.show()
