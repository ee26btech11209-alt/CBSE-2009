import numpy as np
import matplotlib.pyplot as plt

# 1. ODE right-hand side f(x) = x * arcsin(x)
def f(x):
    return x * np.arcsin(x)

# 2. Exact solution y(x) = ((2*x^2 - 1)/4)*arcsin(x) + (x*sqrt(1-x^2))/4
def exact_y(x):
    return ((2*x**2 - 1) / 4.0) * np.arcsin(x) + (x * np.sqrt(1 - x**2)) / 4.0

# 3. Setup numerical domain
x0, x_end = 0.0, 0.90
h = 0.10
n_steps = int(round((x_end - x0) / h))

x_euler = np.zeros(n_steps + 1)
y_euler = np.zeros(n_steps + 1)

x_euler[0] = x0
y_euler[0] = 0.0  # Initial condition y(0) = 0

# 4. Euler's Method Iteration
for i in range(n_steps):
    x_euler[i+1] = x_euler[i] + h
    y_euler[i+1] = y_euler[i] + h * f(x_euler[i])

# 5. Exact solution grid
x_exact = np.linspace(x0, x_end, 500)
y_exact = exact_y(x_exact)

# 6. Single-panel plot using stem plot for numerical approximation
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

# Continuous exact solution curve
ax.plot(x_exact, y_exact, color='#1F77B4', linewidth=2.5, 
        label=r'Exact Solution: $y = \frac{2x^2-1}{4}\sin^{-1}(x) + \frac{x\sqrt{1-x^2}}{4}$')

# Stem plot for discrete Euler points
markerline, stemlines, baseline = ax.stem(
    x_euler, y_euler, 
    linefmt='#D62728', 
    markerfmt='o', 
    basefmt=' ', 
    label=r"Euler's Method Stem Plot ($h = 0.10$)"
)
plt.setp(markerline, color='#D62728', markersize=6)
plt.setp(stemlines, linestyle='--', linewidth=1.5, color='#D62728')

# Point Annotations
for xi, ye in zip(x_euler[::2], y_euler[::2]):
    ax.annotate(f'({xi:.1f}, {ye:.3f})', (xi, ye), textcoords="offset points", 
                xytext=(0, 10), ha='center', fontsize=9, fontweight='bold', color='#D62728')

ax.set_xlabel('$x$', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('$y$', fontsize=12, fontweight='bold', labelpad=10)
ax.set_title(r"Euler's Method Stem Plot vs. Exact Solution for $\int x \sin^{-1}(x) \, dx$", 
             fontsize=14, fontweight='bold', pad=15)
ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='upper left', fontsize=11, frameon=True, facecolor='white', framealpha=0.95)

plt.tight_layout()
plt.show()  
