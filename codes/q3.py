import numpy as np
import matplotlib.pyplot as plt

# 1. ODE right-hand side f(x) = cos(x) / sqrt(1 + sin(x))
def f(x):
    return np.cos(x) / np.sqrt(1 + np.sin(x))

# 2. Setup numerical domain
x0, x_end = 0.0, np.pi
h = 0.25
n_steps = int(round((x_end - x0) / h))

x_euler = np.zeros(n_steps + 1)
y_euler = np.zeros(n_steps + 1)

# Initial condition y(0) = 2
x_euler[0] = x0
y_euler[0] = 2.0

# 3. Euler iteration
for i in range(n_steps):
    x_euler[i+1] = x_euler[i] + h
    y_euler[i+1] = y_euler[i] + h * f(x_euler[i])

# 4. Exact solution grid
x_exact = np.linspace(x0, x_end, 500)
y_exact = 2.0 * np.sqrt(1 + np.sin(x_exact))

# 5. Clean single-panel plot
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

# Trajectories
ax.plot(x_exact, y_exact, color='#1F77B4', linewidth=2.5, 
        label=r'Exact Solution: $y = 2\sqrt{1 + \sin(x)}$')
ax.plot(x_euler, y_euler, color='#D62728', linestyle='--', marker='o', 
        markersize=6, linewidth=2, label=r"Euler's Method ($h = 0.25$)")

# Point Annotations
for xi, ye in zip(x_euler[::2], y_euler[::2]):
    ax.annotate(f'({xi:.2f}, {ye:.2f})', (xi, ye), textcoords="offset points", 
                xytext=(0, 10), ha='center', fontsize=9, fontweight='bold', color='#D62728')

ax.set_xlabel('$x$', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('$y$', fontsize=12, fontweight='bold', labelpad=10)
ax.set_title(r"Euler's Method vs. Exact Solution for $\int \frac{\cos x}{\sqrt{1 + \sin x}} \, dx$", 
             fontsize=14, fontweight='bold', pad=15)
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='upper right', fontsize=11, frameon=True, facecolor='white', framealpha=0.95)

plt.tight_layout()
plt.show()
