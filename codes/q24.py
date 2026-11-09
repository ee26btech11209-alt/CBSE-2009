import numpy as np
import matplotlib.pyplot as plt

# 1. Setup coordinate grid
x_range = np.linspace(0, 6, 60)
y_range = np.linspace(0, 6, 60)
X, Y = np.meshgrid(x_range, y_range)

# 2. Define plane equations z = f(x, y)
Z1 = 6 - X - Y          # Plane 1: x + y + z = 6
Z2 = (7 - X) / 2.0      # Plane 2: x + 2z = 7
Z3 = 12 - 3*X - Y       # Plane 3: 3x + y + z = 12

# 3. Initialize figure and 3D axes
fig = plt.figure(figsize=(12, 8), dpi=150)
ax = fig.add_subplot(111, projection='3d')

# 4. Render plane surfaces with transparency
surf1 = ax.plot_surface(X, Y, Z1, color='#1F77B4', alpha=0.35, 
                        rstride=2, cstride=2, edgecolor='#103D5C', linewidth=0.2)
surf2 = ax.plot_surface(X, Y, Z2, color='#FF7F0E', alpha=0.35, 
                        rstride=2, cstride=2, edgecolor='#A64B00', linewidth=0.2)
surf3 = ax.plot_surface(X, Y, Z3, color='#2CA02C', alpha=0.35, 
                        rstride=2, cstride=2, edgecolor='#165216', linewidth=0.2)

# Dummy surface proxies for clean legend rendering
surf1_proxy = plt.Rectangle((0, 0), 1, 1, fc='#1F77B4', alpha=0.5)
surf2_proxy = plt.Rectangle((0, 0), 1, 1, fc='#FF7F0E', alpha=0.5)
surf3_proxy = plt.Rectangle((0, 0), 1, 1, fc='#2CA02C', alpha=0.5)

# 5. Plot exact plane-intersection lines parameterized by z
z_line = np.linspace(0, 4, 100)

# Intersection Line L12 (Plane 1 & Plane 2): (7 - 2z, z - 1, z)
ax.plot(7 - 2*z_line, z_line - 1, z_line, color='#0B2545', 
        linewidth=2.2, linestyle='--', label='Intersection Line: P1 ∩ P2')

# Intersection Line L13 (Plane 1 & Plane 3): (3, 3 - z, z)
ax.plot(np.full_like(z_line, 3), 3 - z_line, z_line, color='#8B0000', 
        linewidth=2.2, linestyle='--', label='Intersection Line: P1 ∩ P3')

# Intersection Line L23 (Plane 2 & Plane 3): (7 - 2z, 5z - 9, z)
ax.plot(7 - 2*z_line, 5*z_line - 9, z_line, color='#004B23', 
        linewidth=2.2, linestyle='--', label='Intersection Line: P2 ∩ P3')

# 6. Plot solution point and coordinate projection lines (3D depth guides)
px, py, pz = 3, 1, 2
ax.scatter([px], [py], [pz], color='#D62728', s=160, zorder=10, 
           edgecolor='black', linewidth=1.5, label='Solution Point (3, 1, 2)')

# Dashed projection drop-lines to axes planes
ax.plot([px, px], [py, py], [0, pz], color='black', linestyle=':', linewidth=1.5) # z-drop
ax.plot([px, px], [0, py], [pz, pz], color='black', linestyle=':', linewidth=1.5) # y-drop
ax.plot([0, px], [py, py], [pz, pz], color='black', linestyle=':', linewidth=1.5) # x-drop

# 7. Axes bounds, labels, and view elevation
ax.set_xlim(0, 6)
ax.set_ylim(0, 6)
ax.set_zlim(0, 6)

ax.set_xlabel('x-axis', fontsize=11, fontweight='bold', labelpad=10)
ax.set_ylabel('y-axis', fontsize=11, fontweight='bold', labelpad=10)
ax.set_zlabel('z-axis', fontsize=11, fontweight='bold', labelpad=10)
ax.set_title('Geometric Intersection of Three Planes at (3, 1, 2)', 
             fontsize=14, fontweight='bold', pad=20)

# Build unified legend
handles, labels = ax.get_legend_handles_labels()
handles.extend([surf1_proxy, surf2_proxy, surf3_proxy])
labels.extend([r'Plane 1: $x + y + z = 6$', r'Plane 2: $x + 2z = 7$', r'Plane 3: $3x + y + z = 12$'])
ax.legend(handles=handles, labels=labels, loc='upper left', bbox_to_anchor=(0.02, 0.98), fontsize=9.5)

# Camera angle for optimal depth visual
ax.view_init(elev=25, azim=-50)

plt.tight_layout()
plt.show()
