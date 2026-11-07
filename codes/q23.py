import numpy as np
import matplotlib.pyplot as plt

# 1. Line parameters
a1 = np.array([1, 2, 1])
b1 = np.array([1, -1, 1])

a2 = np.array([2, -1, -1])
b2 = np.array([2, 1, 2])

# 2. Compute points of closest approach on both lines
A = np.array([
    [np.dot(b1, b1), -np.dot(b1, b2)],
    [np.dot(b1, b2), -np.dot(b2, b2)]
])
B = np.array([
    np.dot(a2 - a1, b1),
    np.dot(a2 - a1, b2)
])
lam_val, mu_val = np.linalg.solve(A, B)

p1_closest = a1 + lam_val * b1
p2_closest = a2 + mu_val * b2

# 3. Parametric grids for lines
t1 = np.linspace(-1, 3, 200)
t2 = np.linspace(-1, 2.5, 200)

line1 = np.array([a1 + t * b1 for t in t1])
line2 = np.array([a2 + t * b2 for t in t2])

# 4. 3D Plot setup
fig = plt.figure(figsize=(10, 8), dpi=150)
ax = fig.add_subplot(111, projection='3d')

# Plot Lines
ax.plot(line1[:, 0], line1[:, 1], line1[:, 2], color='#1F77B4', linewidth=2.5, 
        label=r'Line 1: $\vec{r}_1 = (1,2,1) + \lambda(1,-1,1)$')
ax.plot(line2[:, 0], line2[:, 1], line2[:, 2], color='#2CA02C', linewidth=2.5, 
        label=r'Line 2: $\vec{r}_2 = (2,-1,-1) + \mu(2,1,2)$')

# Plot Shortest Distance Segment
ax.plot([p1_closest[0], p2_closest[0]], 
        [p1_closest[1], p2_closest[1]], 
        [p1_closest[2], p2_closest[2]], 
        color='#D62728', linestyle='--', linewidth=2.5, 
        label=r'Shortest Distance $d = \frac{3}{\sqrt{2}}$')

# Highlight closest points
ax.scatter([p1_closest[0]], [p1_closest[1]], [p1_closest[2]], color='#D62728', s=60, zorder=5)
ax.scatter([p2_closest[0]], [p2_closest[1]], [p2_closest[2]], color='#D62728', s=60, zorder=5)

# Formatting
ax.set_xlabel('$X$', fontsize=12, fontweight='bold')
ax.set_ylabel('$Y$', fontsize=12, fontweight='bold')
ax.set_zlabel('$Z$', fontsize=12, fontweight='bold')
ax.set_title(r"3D Shortest Distance Between Two Skew Lines", fontsize=14, fontweight='bold', pad=15)

ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left', fontsize=10.5, frameon=True, facecolor='white', framealpha=0.95)

plt.tight_layout()
plt.show()
