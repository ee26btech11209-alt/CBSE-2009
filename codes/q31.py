import numpy as np
import matplotlib.pyplot as plt

# 1. Define x domain
x = np.linspace(0, 25, 500)

# 2. Constraint line equations defined in terms of x
# Line 1: x + y = 20  => y = 20 - x
y1 = 20 - x

# Line 2: 360x + 240y = 5760 => 3x + 2y = 48 => y = (48 - 3x) / 2
y2 = (48 - 3*x) / 2.0

# 3. Setup figure and axes
fig, ax = plt.subplots(figsize=(10, 7), dpi=150)

# Plot boundary lines
ax.plot(x, y1, color='#1F77B4', linewidth=2.5, label=r'$x + y = 20$ (Storage constraint)')
ax.plot(x, y2, color='#D9531E', linewidth=2.5, label=r'$3x + y = 24$ / $3x + 2y = 48$ (Investment constraint)')

# 4. Fill the feasible region bounded by non-negativity (x >= 0, y >= 0)
y_feasible = np.minimum(np.maximum(0, y1), np.maximum(0, y2))
ax.fill_between(x, 0, y_feasible, where=(x <= 16), color='#A6C8E0', alpha=0.5, label='Feasible Region')

# 5. Corner points of the feasible polygon
corner_points = [(0, 0), (16, 0), (8, 12), (0, 20)]

for point in corner_points:
    px, py = point
    ax.scatter(px, py, color='#D62728', s=90, zorder=5, edgecolor='black', linewidth=1.2)
    
    # Custom text placement for each vertex
    if point == (8, 12):
        label_text = f'B({px}, {py})\nOptimal Z = Rs. 392'
        offset = (12, 10)
    elif point == (16, 0):
        label_text = f'A({px}, {py})'
        offset = (-10, 12)
    elif point == (0, 20):
        label_text = f'C({px}, {py})'
        offset = (10, -5)
    else:
        label_text = f'O({px}, {py})'
        offset = (10, 10)
        
    ax.annotate(label_text, (px, py), textcoords="offset points", 
                xytext=offset, fontsize=11, fontweight='bold')

# 6. Axes formatting and grid setup
ax.axhline(0, color='black', linewidth=1.2)
ax.axvline(0, color='black', linewidth=1.2)

ax.set_xlim(-1, 22)
ax.set_ylim(-1, 26)

ax.grid(True, linestyle='--', alpha=0.6)

# Labels and title
ax.set_xlabel('Number of Fans ($x$)', fontsize=12, fontweight='bold', labelpad=10)
ax.set_ylabel('Number of Sewing Machines ($y$)', fontsize=12, fontweight='bold', labelpad=10)
ax.set_title('Linear Programming Feasible Region & Corner Points', fontsize=14, fontweight='bold', pad=15)

ax.legend(loc='upper right', fontsize=10.5)

plt.tight_layout()
plt.show()
