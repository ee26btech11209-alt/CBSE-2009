import numpy as np
import matplotlib.pyplot as plt

# 1. Define ODE right-hand side f(x, y) = y/x - tan(y/x)
def f(x, y):
    return (y / x) - np.tan(y / x)

# 2. Setup initial conditions & numerical domain
x0 = 1.0
y0 = np.pi / 6.0  # y(1) = pi/6 (~0.5236)
x_end = 2.0
h = 0.10
n_steps = int(round((x_end - x0) / h))

x_euler = np.zeros(n_steps + 1)
y_euler = np.zeros(n_steps + 1)

x_euler[0] = x0
y_euler[0] = y0

# 3. Euler's Method Iteration
for i in range(n_steps):
    x_euler[i+1] = x_euler[i] + h
    y_euler[i+1] = y_euler[i] + h * f(x_euler[i], y_euler[i])

# 4. Exact solution y(x) = x * arcsin(0.5 / x)
def exact_y(x):
    return x * np.arcsin(0.5 / x)

x_exact = np.linspace(x0, x_end, 500)
y_exact = exact_y(x_exact)

# 5. Plot setup
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

ax.plot(x_exact, y_exact, color='#1F77B4', linewidth=2.5, 
        label=r'Exact Solution: $y = x \sin^{-1}(0.5/x)$')
ax.plot(x_euler, y_euler, color='#D62728', linestyle='--', marker='o', 
        markersize=6, linewidth=2, label=r"Euler's Method ($h = 0.10$)")

# Point annotations
for xi, ye in zip(x_euler[::2], y_euler[::2]):
    ax.annotate(f'({xi:.1f}, {ye:.3f})', (xi, ye), textcoords="offset points", 
                xytext=(0, 10), ha='center', fontsize=9, fontweight='bold', color='#D62728')

ax.set_xlabel('$x$', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('$y$', fontsize=12, fontweight='bold', labelpad=10)
ax.set_title(r"Euler's Method vs. Exact Solution for $x \frac{dy}{dx} = y - x \tan(y/x)$", 
             fontsize=14, fontweight='bold', pad=15)
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='upper right', fontsize=11, frameon=True, facecolor='white', framealpha=0.95)

plt.tight_layout()
plt.show()
