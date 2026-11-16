import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt

# 1. Define Problem Parameters in Matrix-Vector Form
# x[0] = number of fans, x[1] = number of sewing machines
c = np.array([22, 18])
A = np.array([
    [360, 240],  # Investment constraint: 360*x1 + 240*x2 <= 5760
    [1, 1]       # Space constraint:      x1 + x2 <= 20
])
b = np.array([5760, 20])

# 2. Formulate and Solve LPP using CVXPY
x = cp.Variable(2, nonneg=True)
objective = cp.Maximize(c @ x)
constraints = [A @ x <= b]

problem = cp.Problem(objective, constraints)
problem.solve()

# Extract optimal values
x_opt = np.round(x.value, 4)
max_profit = round(problem.value, 4)

print("Status:", problem.status)
print(f"Optimal number of fans (x1)            = {int(round(x_opt[0]))}")
print(f"Optimal number of sewing machines (x2) = {int(round(x_opt[1]))}")
print(f"Maximum Profit (Z)                     = Rs. {max_profit:.2f}")

# 3. Graphical Solution Plot
x1 = np.linspace(0, 22, 400)
x2_inv = (5760 - 360 * x1) / 240  # 360*x1 + 240*x2 = 5760
x2_spc = 20 - x1                  # x1 + x2 = 20

plt.figure(figsize=(8, 6), dpi=150)

# Plot constraint boundary lines
plt.plot(x1, x2_inv, "b-", linewidth=2, label=r"$360x_1 + 240x_2 \leq 5760$ (Investment)")
plt.plot(x1, x2_spc, "g-", linewidth=2, label=r"$x_1 + x_2 \leq 20$ (Space)")

# Shade feasible region
x2_feasible = np.maximum(0, np.minimum(x2_inv, x2_spc))
plt.fill_between(x1, 0, x2_feasible, where=(x1 <= 16), color="skyblue", alpha=0.4, label="Feasible Region")

# Corner points and objective values
corners = np.array([
    [0, 0],
    [16, 0],
    [8, 12],
    [0, 20]
])
corner_labels = [
    r"$O(0, 0),\ Z = 0$",
    r"$A(16, 0),\ Z = 352$",
    r"$B(8, 12),\ Z_{\max} = 392$",
    r"$C(0, 20),\ Z = 360$"
]
offsets = [(0.4, 0.5), (0.4, 0.5), (0.5, 0.5), (0.5, -1.2)]

plt.scatter(corners[:, 0], corners[:, 1], color="black", zorder=5, s=45)
plt.scatter([x_opt[0]], [x_opt[1]], color="red", zorder=6, s=90, label=r"Optimal Point $B(8, 12)$")

for (cx, cy), lbl, (dx, dy) in zip(corners, corner_labels, offsets):
    is_opt = (cx == 8 and cy == 12)
    plt.text(
        cx + dx,
        cy + dy,
        lbl,
        fontsize=10,
        color="red" if is_opt else "black",
        fontweight="bold" if is_opt else "normal"
    )

plt.xlim(-1, 22)
plt.ylim(-1, 25)
plt.xlabel(r"Number of Fans ($x_1$)", fontsize=11)
plt.ylabel(r"Number of Sewing Machines ($x_2$)", fontsize=11)
plt.title("Graphical Solution of the Linear Programming Problem", fontsize=12, fontweight="bold")
plt.axhline(0, color="black", linewidth=1)
plt.axvline(0, color="black", linewidth=1)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(loc="upper right", fontsize=9.5)
plt.tight_layout()
plt.savefig("lpp_graphical_solution.png", dpi=150)
plt.show()
