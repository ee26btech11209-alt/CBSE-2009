import numpy as np
import matplotlib.pyplot as plt

# 1. Vector definitions
a = np.array([1, 1, 1])
b = np.array([1, 2, 3])

# Sum and Difference vectors
u = a + b  # (2, 3, 4)
v = a - b  # (0, -1, -2)

# 2. Cross product and unit normal vector
w = np.cross(u, v)  # (-2, 4, -2)
w_norm = np.linalg.norm(w)
n_hat = w / w_norm  # Unit normal vector

# 3. 3D Plotting
fig = plt.figure(figsize=(10, 8), dpi=150)
ax = fig.add_subplot(111, projection='3d')
origin = np.array([0, 0, 0])

# Plotting vectors
ax.quiver(*origin, *u, color='#1F77B4', linewidth=2.5, 
          label=r'$\vec{a}+\vec{b} = (2, 3, 4)$', arrow_length_ratio=0.08)
ax.quiver(*origin, *v, color='#2CA02C', linewidth=2.5, 
          label=r'$\vec{a}-\vec{b} = (0, -1, -2)$', arrow_length_ratio=0.1)
ax.quiver(*origin, *n_hat, color='#D62728', linewidth=3.0, 
          label=r'$\hat{n} = \frac{1}{\sqrt{6}}(-1, 2, -1)$', arrow_length_ratio=0.2)
ax.quiver(*origin, *-n_hat, color='#E377C2', linestyle='--', linewidth=2.0, 
          label=r'$-\hat{n} = \frac{1}{\sqrt{6}}(1, -2, 1)$', arrow_length_ratio=0.2)

# Axis limits & labels
ax.set_xlim([-2, 3])
ax.set_ylim([-2, 4])
ax.set_zlim([-2, 5])

ax.set_xlabel('$X$', fontsize=12, fontweight='bold')
ax.set_ylabel('$Y$', fontsize=12, fontweight='bold')
ax.set_zlabel('$Z$', fontsize=12, fontweight='bold')
ax.set_title(r"3D Vectors: $(\vec{a}+\vec{b})$, $(\vec{a}-\vec{b})$ & Unit Normal $\hat{n}$", 
             fontsize=14, fontweight='bold', pad=15)

ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left', fontsize=10, frameon=True, facecolor='white', framealpha=0.95)

plt.tight_layout()
plt.show()
