import numpy as np
import matplotlib.pyplot as plt

# Parameters for Binomial Distribution B(n, p)
n = 5
p = 1 / 3
N_sim = 100000

# Reproducibility
np.random.seed(42)

# Support k in {0, 1, 2, 3, 4, 5}
k_vals = np.arange(0, n + 1)

# Theoretical PMF using NumPy: p_X(k) = C(n, k) * p^k * (1 - p)^(n - k)
nCr = np.array([np.prod(np.arange(n - k + 1, n + 1)) / np.prod(np.arange(1, k + 1)) for k in k_vals])
pmf_theory = nCr * (p ** k_vals) * ((1 - p) ** (n - k_vals))

# Simulated (empirical) PMF
simulated_scores = np.random.binomial(n=n, p=p, size=N_sim)
pmf_sim = np.bincount(simulated_scores, minlength=n + 1) / N_sim

# Print comparison table
print("k | Theoretical PMF | Simulated PMF | Abs Error")
print("-" * 48)
for k, pt, ps in zip(k_vals, pmf_theory, pmf_sim):
    print(f"{k} | {pt:15.6f} | {ps:13.6f} | {abs(pt - ps):9.6f}")

print(f"\nP(X >= 4) Theoretical = {np.sum(pmf_theory[k_vals >= 4]):.6f}")
print(f"P(X >= 4) Simulated   = {np.sum(pmf_sim[k_vals >= 4]):.6f}")

# Stem plot comparing Theoretical PMF and Simulated PMF
plt.figure(figsize=(8, 5), dpi=150)

offset = 0.08
marker_t, stem_t, _ = plt.stem(
    k_vals - offset,
    pmf_theory,
    linefmt="b-",
    markerfmt="bo",
    basefmt="k-",
    label=r"Theoretical PMF $p_X(k)$",
)
plt.setp(stem_t, linewidth=1.8)
plt.setp(marker_t, markersize=7)

marker_s, stem_s, _ = plt.stem(
    k_vals + offset,
    pmf_sim,
    linefmt="r--",
    markerfmt="rs",
    basefmt="k-",
    label=rf"Simulated PMF ($N = {N_sim:,}$)",
)
plt.setp(stem_s, linewidth=1.8)
plt.setp(marker_s, markersize=6)

plt.title(r"Comparison of Theoretical and Simulated PMF ($n = 5, p = 1/3$)", fontsize=12, fontweight="bold")
plt.xlabel(r"Number of Correct Answers ($k$)", fontsize=11)
plt.ylabel(r"Probability Mass Function $p_X(k)$", fontsize=11)
plt.xticks(k_vals)
plt.ylim(0, 0.42)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(frameon=True, fontsize=10)
plt.tight_layout()
plt.savefig("stem_plot_q19.png", dpi=150)
plt.show()
