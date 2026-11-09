import numpy as np
import matplotlib.pyplot as plt

# Integrand definition
def f(x):
    return (x * np.sin(x)) / (1 + np.cos(x)**2)

# Domain setup
x_fine = np.linspace(0, np.pi, 500)
y_fine = f(x_fine)

# Number of trapezoids for visualization
n = 6
x_nodes = np.linspace(0, np.pi, n + 1)
y_nodes = f(x_nodes)

# Figure setup (Single Plot)
fig, ax = plt.subplots(figsize=(9, 6), dpi=150)

# Function Curve & Exact Area Under Curve
ax.plot(x_fine, y_fine, color='#1F77B4', linewidth=2.5, label=r'$f(x) = \frac{x \sin x}{1 + \cos^2 x}$')
ax.fill_between(x_fine, y_fine, color='#1F77B4', alpha=0.15, label=r'Exact Area ($I = \frac{\pi^2}{4} \approx 2.4674$)')

# Draw trapezoidal regions
for i in range(n):
    xs = [x_nodes[i], x_nodes[i], x_nodes[i+1], x_nodes[i+1]]
    ys = [0, y_nodes[i], y_nodes[i+1], 0]
    ax.fill(xs, ys, edgecolor='#D62728', facecolor='#D62728', alpha=0.2, linewidth=1.2)
    ax.plot([x_nodes[i], x_nodes[i+1]], [y_nodes[i], y_nodes[i+1]], color='#D62728', linestyle='--', linewidth=1.8)

ax.scatter(x_nodes, y_nodes, color='#D62728', s=40, zorder=5, label=f'Trapezoid Nodes ($n = {n}$)')

# Axis formatting with exact pi ticks
ticks = [0, np.pi/6, 2*np.pi/6, 3*np.pi/6, 4*np.pi/6, 5*np.pi/6, np.pi]
tick_labels = [r'$0$', r'$\frac{\pi}{6}$', r'$\frac{\pi}{3}$', r'$\frac{\pi}{2}$', r'$\frac{2\pi}{3}$', r'$\frac{5\pi}{6}$', r'$\pi$']
ax.set_xticks(ticks)
ax.set_xticklabels(tick_labels, fontsize=11)

ax.set_xlabel('$x$', fontsize=12, fontweight='bold', labelpad=8)
ax.set_ylabel('$f(x)$', fontsize=12, fontweight='bold', labelpad=8)
ax.set_title(r"Trapezoidal Integration Area ($n = 6$)", fontsize=14, fontweight='bold', pad=12)
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='upper left', fontsize=10.5, frameon=True, facecolor='white', framealpha=0.95)

plt.tight_layout()
plt.show()
