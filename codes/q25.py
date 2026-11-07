import numpy as np
import matplotlib.pyplot as plt

# 1. Point definitions
A = np.array([3, -1, 2])
B = np.array([5, 2, 4])
C = np.array([-1, -1, 6])
P = np.array([6, 5, 9])

# 2. Plane equation: 3x - 4y + 3z = 19
a, b, c, d_val = 3, -4, 3, -19

# Foot of perpendicular from P onto the plane
foot = P - ((a * P[0] + b * P[1] + c * P[2] + d_val) / (a**2 + b**2 + c**2)) * np.array([a, b, c])

# 3. Meshgrid for plane surface
x_grid = np.linspace(-2, 8, 30)
y_grid = np.linspace(-2, 8, 30)
X, Y = np.meshgrid(x_grid, y_grid)
Z = (19 - 3 * X + 4 * Y) / 3.0

# 4. Figure & 3D Axes setup
fig = plt.figure(figsize=(11, 8), dpi=150)
ax = fig.add_subplot(111, projection='3d')

# Camera view angle optimized to separate P and F clearly
ax.view_init(elev=18, azim=-125)

# Translucent plane surface with wireframe grid for spatial depth
ax.plot_surface(X, Y, Z, alpha=0.20, color='#3182BD', edgecolor='#2B5C8F', linewidth=0.3)

# Scatter points lying in the plane
ax.scatter(*A, color='#1F77B4', s=90, depthshade=False, label='A (3, -1, 2)', zorder=5)
ax.scatter(*B, color='#1F77B4', s=90, depthshade=False, label='B (5, 2, 4)', zorder=5)
ax.scatter(*C, color='#1F77B4', s=90, depthshade=False, label='C (-1, -1, 6)', zorder=5)

# Scatter external point P and foot of perpendicular F
ax.scatter(*P, color='#D62728', s=110, depthshade=False, label='P (6, 5, 9)', zorder=6)
ax.scatter(*foot, color='#2CA02C', s=100, depthshade=False, 
           label=r'Foot $F\left(\frac{93}{17}, \frac{97}{17}, \frac{144}{17}\right)$', zorder=6)

# Perpendicular distance segment between P and F
ax.plot([P[0], foot[0]], [P[1], foot[1]], [P[2], foot[2]], 
        color='#D62728', linestyle='--', linewidth=3, 
        label=r'Perpendicular Distance $d = \frac{6}{\sqrt{34}}$', zorder=7)

# Direct point annotations in 3D space
ax.text(A[0], A[1]-1.2, A[2], '  A(3, -1, 2)', fontsize=9.5, fontweight='bold', color='#1F77B4')
ax.text(B[0], B[1]+0.5, B[2], '  B(5, 2, 4)', fontsize=9.5, fontweight='bold', color='#1F77B4')
ax.text(C[0]-1.5, C[1], C[2], 'C(-1, -1, 6)  ', fontsize=9.5, fontweight='bold', color='#1F77B4')
ax.text(P[0]+0.3, P[1]+0.3, P[2]+0.3, '  P(6, 5, 9)', fontsize=10, fontweight='bold', color='#D62728')
ax.text(foot[0]-1.2, foot[1]-1.2, foot[2]-0.5, 'F (Foot)', fontsize=9.5, fontweight='bold', color='#2CA02C')

# Labels & legend formatting
ax.set_xlabel('$X$', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('$Y$', fontsize=12, fontweight='bold', labelpad=10)
ax.set_zlabel('$Z$', fontsize=12, fontweight='bold', labelpad=10)
ax.set_title(r"Plane $3x - 4y + 3z = 19$ & Distance from $P(6,5,9)$", 
             fontsize=14, fontweight='bold', pad=15)

ax.legend(loc='upper left', fontsize=10.5, frameon=True, facecolor='white', framealpha=0.95)

plt.tight_layout()
plt.show()
