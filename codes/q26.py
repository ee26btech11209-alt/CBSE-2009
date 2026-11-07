import numpy as np
import matplotlib.pyplot as plt

# 1. Generate y values for plotting curves continuously along the y-axis
y = np.linspace(-3.2, 3.2, 500)

# Equations defined in terms of y:
# Parabola: x = y^2
x_parabola = y**2

# Line: x = 2 - y
x_line = 2 - y

# 2. Setup figure canvas
fig, ax = plt.subplots(figsize=(10, 6), dpi=150)

# Plot the line and parabola
ax.plot(x_line, y, color='#D9531E', linewidth=2.5, label=r'$x + y = 2$')
ax.plot(x_parabola, y, color='#1A4D7C', linewidth=2.5, label=r'$y^2 = x$')

# 3. Fill the bounded area between y = -2 and y = 1
y_fill = np.linspace(-2, 1, 500)
x_fill_parabola = y_fill**2
x_fill_line = 2 - y_fill

ax.fill_betweenx(y_fill, x_fill_parabola, x_fill_line, color='#A6C8E0', alpha=0.55)

# 4. Highlight and label intersection points (1, 1) and (4, -2)
intersections = [(1, 1), (4, -2)]
for xi, yi in intersections:
    ax.scatter(xi, yi, color='#87CEFA', edgecolors='#1A4D7C', s=80, zorder=5, linewidth=1.5)
    
    # Position text labels clearly around points
    offset = (-20, 12) if yi > 0 else (12, 10)
    ax.annotate(f'({xi}, {yi})', (xi, yi), textcoords="offset points", 
                xytext=offset, fontsize=13, fontweight='bold')

# Inline curve labels
ax.text(3.1, 1.25, r'$y^2 = x$', fontsize=14, fontweight='bold', color='#111111')
ax.text(2.6, -0.9, r'$x + y = 2$', fontsize=14, fontweight='bold', color='#111111')

# 5. Axes formatting and grid lines
ax.axhline(0, color='black', linewidth=1.2)
ax.axvline(0, color='black', linewidth=1.2)

ax.set_xlim(-1, 5.2)
ax.set_ylim(-3.2, 3.2)

ax.grid(True, which='both', linestyle='-', linewidth=0.8, color='#D0D0D0')
ax.set_title(r'Graph of the Region Bounded by $y^2 = x$ and $x + y = 2$', fontsize=15, fontweight='bold', pad=15)

# Axis labels with arrows styling
ax.set_xlabel('x-axis', fontsize=12, fontweight='bold', loc='right')
ax.set_ylabel('y-axis', fontsize=12, fontweight='bold', loc='top')

plt.tight_layout()
plt.show()
