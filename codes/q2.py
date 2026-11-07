import numpy as np
import matplotlib.pyplot as plt

# Define ODE right-hand side f(x, y)
def f(x, y):
    return (1 / np.cos(np.sqrt(x)))**2 / np.sqrt(x)

# Parameters
x0, x_end = 0.10, 1.70
h = 0.20
steps = int((x_end - x0) / h)

# Euler's Method Iteration
x_euler = [x0]
y_euler = [2 * np.tan(np.sqrt(x0))]

x, y = x0, y_euler[0]
for _ in range(steps):
    y = y + h * f(x, y)
    x = x + h
    x_euler.append(x)
    y_euler.append(y)

# Continuous Exact Solution
x_exact = np.linspace(0.10, 1.70, 400)
y_exact = 2 * np.tan(np.sqrt(x_exact))

# Plot setup
fig, ax = plt.subplots(figsize=(9, 6), dpi=150)

ax.plot(x_exact, y_exact, color='#1F77B4', linewidth=2.5, label=r'Exact Solution: $y = 2\tan(\sqrt{x})$')
ax.plot(x_euler, y_euler, color='#D62728', linestyle='--', marker='o', markersize=6, 
        linewidth=1.8, label=r"Euler's Method ($h = 0.20$)")

ax.set_xlabel('$x$', fontsize=12, fontweight='bold')
ax.set_ylabel('$y$', fontsize=12, fontweight='bold')
ax.set_title(r"Euler's Method vs Exact Solution for $\int \frac{\sec^2(\sqrt{x})}{\sqrt{x}} dx$", 
             fontsize=13, fontweight='bold', pad=12)

ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper left', fontsize=11)

plt.tight_layout()
plt.show()
