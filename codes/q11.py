import numpy as np


def arccot(y):
    """Computes arccot(y) in the principal range (0, pi)."""
    return np.arctan2(1.0, y)


# Sample 10 points in the open interval (0, pi/4)
x = np.linspace(0.05, (np.pi / 4.0) - 0.02, 10)

a = np.sqrt(1.0 + np.sin(x))
b = np.sqrt(1.0 - np.sin(x))
ratio = (a + b) / (a - b)

lhs = arccot(ratio)
rhs = x / 2.0
abs_error = np.abs(lhs - rhs)

print(f"{'x (rad)':<12} | {'LHS':<15} | {'RHS (x/2)':<15} | {'Abs Error':<15}")
print("-" * 66)
for xi, li, ri, ei in zip(x, lhs, rhs, abs_error):
    print(f"{xi:<12.6f} | {li:<15.10f} | {ri:<15.10f} | {ei:<15.2e}")

max_err = np.max(abs_error)
print("-" * 66)
print(f"Maximum absolute error: {max_err:.2e}")
print("Identity VERIFIED within machine precision." if max_err < 1e-12 else "Verification FAILED.")
