import numpy as np

# 1. Verify the general solution x = n*pi + pi/4 for n in {-2, -1, 0, 1, 2}
n_vals = np.arange(-2, 3)
x_sols = n_vals * np.pi + np.pi / 4.0

lhs = 2.0 * np.arctan(np.cos(x_sols))
rhs = np.arctan(2.0 / np.sin(x_sols))  # 2 * csc(x) = 2 / sin(x)
abs_err = np.abs(lhs - rhs)

print("Verification at x = n*pi + pi/4:")
print(f"{'n':<4} | {'x (rad)':<12} | {'LHS':<15} | {'RHS':<15} | {'Abs Error':<12}")
print("-" * 66)
for n, x, l_val, r_val, err in zip(n_vals, x_sols, lhs, rhs, abs_err):
    print(f"{n:<4} | {x:<12.6f} | {l_val:<15.10f} | {r_val:<15.10f} | {err:<12.2e}")

# 2. Numerical root scan on (0, 2*pi) excluding singularities where sin(x) = 0
x_grid = np.linspace(1e-4, 2 * np.pi - 1e-4, 100000)
valid = np.abs(np.sin(x_grid)) > 1e-3
x_valid = x_grid[valid]

diff = np.abs(2.0 * np.arctan(np.cos(x_valid)) - np.arctan(2.0 / np.sin(x_valid)))
roots = [
    x_valid[i]
    for i in range(1, len(diff) - 1)
    if diff[i] < 1e-4 and diff[i] < diff[i - 1] and diff[i] < diff[i + 1]
]

print("\nNumerically detected roots in (0, 2*pi):")
for r in roots:
    print(f"x = {r:.6f} rad  (x / pi = {r / np.pi:.6f})")
