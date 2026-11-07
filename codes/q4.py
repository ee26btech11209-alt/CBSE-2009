import matplotlib.pyplot as plt
import numpy as np

# Generate x values from -4π to 4π
x = np.linspace(-4 * np.pi, 4 * np.pi, 1000)

# Compute y = arccos(cos(x))
y = np.arccos(np.cos(x))

# Coordinates for x = 7π/6
x_point = 7 * np.pi / 6
y_point = np.arccos(np.cos(x_point))  # Evaluates to 5π/6

# Configure the plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, label=r'$y = \cos^{-1}(\cos(x))$', color='#1f77b4', linewidth=2)

# Highlight point and guide lines
plt.scatter([x_point], [y_point], color='red', zorder=5, s=60)
plt.plot([x_point, x_point], [0, y_point], color='red', linestyle=':', linewidth=1.2)
plt.plot([0, x_point], [y_point, y_point], color='red', linestyle=':', linewidth=1.2)

# Annotate the specific point
plt.annotate(
    r'$\left(\frac{7\pi}{6}, \frac{5\pi}{6}\right)$',
    xy=(x_point, y_point),
    xytext=(x_point + 0.3, y_point - 0.4),
    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6),
    fontsize=11
)

# Graph styling
plt.title(r'Graph of $y = \cos^{-1}(\cos(x))$ with $\cos^{-1}\left(\cos\left(\frac{7\pi}{6}\right)\right)$ Labeled', fontsize=13, pad=12)
plt.xlabel('$x$', fontsize=12)
plt.ylabel('$y$', fontsize=12)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')
plt.grid(True, linestyle=':', alpha=0.7)

# Set ticks in multiples of π
x_ticks = np.arange(-4, 5) * np.pi
x_labels = [r'$-4\pi$', r'$-3\pi$', r'$-2\pi$', r'$-\pi$', '$0$', r'$\pi$', r'$2\pi$', r'$3\pi$', r'$4\pi$']
plt.xticks(x_ticks, x_labels)

y_ticks = [0, np.pi / 2, np.pi]
y_labels = ['$0$', r'$\frac{\pi}{2}$', r'$\pi$']
plt.yticks(y_ticks, y_labels)

plt.ylim(-0.5, np.pi + 0.5)
plt.legend(loc='upper right')
plt.tight_layout()

# Render plot
plt.show()
