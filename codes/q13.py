import numpy as np
import matplotlib.pyplot as plt

# 1. Curve definition: y = sqrt(3x - 2)
# Domain condition: 3x - 2 >= 0 => x >= 2/3 ≈ 0.6667
x_curve = np.linspace(2/3, 2.5, 500)
y_curve = np.sqrt(3 * x_curve - 2)

# 2. Point of tangency
x0 = 41 / 48  # ≈ 0.85417
y0 = 3 / 4    # 0.75

# 3. Line domains
x_line = np.linspace(0.4, 2.5, 500)

# Given line: 4x - 2y + 5 = 0 => y = 2x + 2.5
y_given_line = 2 * x_line + 2.5

# Tangent line: 48x - 24y - 23 = 0 => y = 2x - 23/24
y_tangent = 2 * x_line - 23 / 24

# 4. Plot setup
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

# Plot trajectories
ax.plot(x_curve, y_curve, color='#1F77B4', linewidth=2.5, label=r'Curve: $y = \sqrt{3x - 2}$')
ax.plot(x_line, y_given_line, color='#2CA02C', linestyle='--', linewidth=2, label=r'Given Line: $4x - 2y + 5 = 0$')
ax.plot(x_line, y_tangent, color='#D62728', linewidth=2, label=r'Tangent Line: $48x - 24y - 23 = 0$')

# Highlight point of tangency
ax.scatter([x0], [y0], color='#D62728', s=80, zorder=5, edgecolor='black', linewidth=1.2)
ax.annotate(r'Tangency Point $\left(\frac{41}{48}, \frac{3}{4}\right)$', (x0, y0), textcoords="offset points", 
            xytext=(30, -20), fontsize=10, fontweight='bold', color='#D62728',
            arrowprops=dict(arrowstyle='->', color='#D62728', lw=1.2))

# Limits & Formatting
ax.set_xlim(0.4, 2.2)
ax.set_ylim(-0.5, 6.0)

ax.set_xlabel('$x$', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('$y$', fontsize=12, fontweight='bold', labelpad=10)
ax.set_title(r"Tangent to $y = \sqrt{3x - 2}$ Parallel to $4x - 2y + 5 = 0$", 
             fontsize=14, fontweight='bold', pad=15)

ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='upper left', fontsize=11, frameon=True, facecolor='white', framealpha=0.95)

plt.tight_layout()
plt.show()
