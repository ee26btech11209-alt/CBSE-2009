import numpy as np
import matplotlib.pyplot as plt

# Domain setup
x = np.linspace(0, 2 * np.pi, 500)
y = np.sin(x) + np.cos(x)

# Split domain into sub-intervals
x1 = np.linspace(0, np.pi/4, 100)
x2 = np.linspace(np.pi/4, 5*np.pi/4, 200)
x3 = np.linspace(5*np.pi/4, 2*np.pi, 200)

fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

# Plot increasing and decreasing sub-curves
ax.plot(x1, np.sin(x1) + np.cos(x1), color='#2CA02C', linewidth=2.5, label='Strictly Increasing')
ax.plot(x2, np.sin(x2) + np.cos(x2), color='#D62728', linewidth=2.5, label='Strictly Decreasing')
ax.plot(x3, np.sin(x3) + np.cos(x3), color='#2CA02C', linewidth=2.5)

# Critical points annotation
cp_x = [np.pi/4, 5*np.pi/4]
cp_y = [np.sqrt(2), -np.sqrt(2)]

ax.scatter(cp_x, cp_y, color='black', s=70, zorder=5)
ax.annotate(r'$\left(\frac{\pi}{4}, \sqrt{2}\right)$', (np.pi/4, np.sqrt(2)), textcoords="offset points", 
            xytext=(0, 10), ha='center', fontsize=10, fontweight='bold')
ax.annotate(r'$\left(\frac{5\pi}{4}, -\sqrt{2}\right)$', (5*np.pi/4, -np.sqrt(2)), textcoords="offset points", 
            xytext=(0, -18), ha='center', fontsize=10, fontweight='bold')

# Formatting x-axis with pi ticks
ticks = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4, 2*np.pi]
tick_labels = [r'$0$', r'$\frac{\pi}{4}$', r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$', r'$\pi$', r'$\frac{5\pi}{4}$', r'$\frac{3\pi}{2}$', r'$\frac{7\pi}{4}$', r'$2\pi$']
ax.set_xticks(ticks)
ax.set_xticklabels(tick_labels, fontsize=11)

ax.set_xlabel('$x$', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('$f(x)$', fontsize=12, fontweight='bold', labelpad=10)
ax.set_title(r"Intervals of Increase and Decrease for $f(x) = \sin x + \cos x$", fontsize=14, fontweight='bold', pad=15)

ax.grid(True, linestyle=':', alpha=0.7)
ax.legend(loc='upper right', fontsize=11, frameon=True, facecolor='white', framealpha=0.95)

plt.tight_layout()
plt.show()
