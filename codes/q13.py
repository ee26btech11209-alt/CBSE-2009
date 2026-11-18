import numpy as np
import matplotlib.pyplot as plt

# Conic and line parameters from the matrix formulation
V = np.array([[0.0, 0.0], [0.0, 1.0]])
u = np.array([-1.5, 0.0])
f = 2.0

n = np.array([2.0, -1.0])   # Normal vector of 4x - 2y + 5 = 0
m = np.array([1.0, 2.0])    # Direction vector satisfying m^T n = 0

# Compute point of contact q = [x0, y0] from m^T(Vq + u) = 0 and the conic equation
y0 = -(m[0] * u[0]) / (m[1] * V[1, 1])
x0 = (V[1, 1] * y0**2 + f) / (-2.0 * u[0])
q = np.array([x0, y0])

# Coordinates for the curve y = sqrt(3x - 2) (domain: x >= 2/3)
x_curve = np.linspace(2 / 3, 2.5, 400)
y_curve = np.sqrt(3 * x_curve - 2)

# Coordinates for the given parallel line and the required tangent line
x_line = np.linspace(-0.5, 2.5, 400)
y_given = (4 * x_line + 5) / 2                   # 4x - 2y + 5 = 0
y_tangent = (n[0] * x_line - (n @ q)) / (-n[1])  # 48x - 24y - 23 = 0

plt.figure(figsize=(8, 6))

plt.plot(x_curve, y_curve, label=r'$y = \sqrt{3x - 2}$', color='blue', linewidth=2)
plt.plot(x_line, y_given, '--', label=r'Given line: $4x - 2y + 5 = 0$', color='green', linewidth=1.8)
plt.plot(x_line, y_tangent, label=r'Tangent: $48x - 24y - 23 = 0$', color='red', linewidth=2)

# Plot and annotate point of contact q
plt.scatter(q[0], q[1], color='black', zorder=5)
plt.annotate(r'$\mathbf{q}\left(\frac{41}{48}, \frac{3}{4}\right)$',
             xy=(q[0], q[1]),
             xytext=(q[0] + 0.15, q[1] - 0.35),
             arrowprops=dict(arrowstyle='->', color='black', lw=1),
             fontsize=11)

plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.xlim(-0.5, 2.5)
plt.ylim(-1.0, 4.5)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('../figs/tangent_plot.png', dpi=300)
plt.show()
