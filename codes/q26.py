import os
import numpy as np
import matplotlib.pyplot as plt

# Bag configurations: [Black balls, Red balls]
bags = {
    1: np.array([1, 3]),  # Bag I: 1 Black, 3 Red (Total = 4)
    2: np.array([2, 1]),  # Bag II: 2 Black, 1 Red (Total = 3)
    3: np.array([4, 3]),  # Bag III: 4 Black, 3 Red (Total = 7)
}

N_sim = 100000  # Large number of simulated trials
np.random.seed(42)

# Theoretical PMFs
k_vals = np.array([1, 2, 3])
prior_theory = np.array([1 / 3, 1 / 3, 1 / 3])
cond_theory = np.array([
    (1 * 3) / 6,    # C(1,1)*C(3,1)/C(4,2) = 1/2
    (2 * 1) / 3,    # C(2,1)*C(1,1)/C(3,2) = 2/3
    (4 * 3) / 21,   # C(4,1)*C(3,1)/C(7,2) = 4/7
])
joint_theory = prior_theory * cond_theory
marginal_theory = np.sum(joint_theory)
post_theory = joint_theory / marginal_theory  # [21/73, 28/73, 24/73]

# Monte Carlo Simulation using NumPy
# Step 1: Randomly select bag X in {1, 2, 3}
selected_bags = np.random.randint(1, 4, size=N_sim)

# Step 2: Draw 2 balls without replacement from the selected bag
# Represent Black = 1, Red = 0
black_counts = np.zeros(N_sim, dtype=int)
for k in k_vals:
    idx = np.where(selected_bags == k)[0]
    m = len(idx)
    b_cnt, r_cnt = bags[k]
    total = b_cnt + r_cnt
    rand_vals = np.random.rand(m, total)
    drawn_indices = np.argpartition(rand_vals, 2, axis=1)[:, :2]
    black_counts[idx] = np.sum(drawn_indices < b_cnt, axis=1)

# Filter trials where event A = {B = 1} (1 Black and 1 Red ball) occurred
event_A_mask = (black_counts == 1)
bags_given_A = selected_bags[event_A_mask]

# Simulated Posterior PMF p_{X|B}(k|1)
post_sim = np.array([
    np.mean(bags_given_A == k) for k in k_vals
])

# Print numerical comparison
print("Bag (k) | Theoretical PMF | Simulated PMF | Abs Error")
print("-" * 55)
for i, k in enumerate(k_vals):
    print(f"   {k}    |    {post_theory[i]:.6f}     |   {post_sim[i]:.6f}    |  {abs(post_theory[i] - post_sim[i]):.6f}")

# Stem plot comparing Theoretical vs. Simulated Posterior PMF
os.makedirs("figs", exist_ok=True)
plt.figure(figsize=(8, 5), dpi=150)

offset = 0.06
marker_t, stem_t, _ = plt.stem(
    k_vals - offset,
    post_theory,
    linefmt="b-",
    markerfmt="bo",
    basefmt="k-",
    label=r"Theoretical Posterior PMF $p_{X \mid B}(k \mid 1)$",
)
plt.setp(stem_t, linewidth=2.0)
plt.setp(marker_t, markersize=8)

marker_s, stem_s, _ = plt.stem(
    k_vals + offset,
    post_sim,
    linefmt="r--",
    markerfmt="rs",
    basefmt="k-",
    label=rf"Simulated Posterior PMF ($N = {N_sim:,}$)",
)
plt.setp(stem_s, linewidth=2.0)
plt.setp(marker_s, markersize=7)

# Annotate values above markers
for i, k in enumerate(k_vals):
    plt.text(k - offset - 0.03, post_theory[i] + 0.015, f"{post_theory[i]:.4f}", ha="right", fontsize=9, color="blue")
    plt.text(k + offset + 0.03, post_sim[i] + 0.015, f"{post_sim[i]:.4f}", ha="left", fontsize=9, color="red")

plt.title(r"PMF $p_{X \mid B}(k \mid 1)$: Theoretical vs. Simulated", fontsize=12, fontweight="bold")
plt.xlabel(r"Selected Bag ($k$)", fontsize=11)
plt.ylabel(r" Probability $p_{X \mid B}(k \mid 1)$", fontsize=11)
plt.xticks(k_vals, ["Bag I ($k=1$)", "Bag II ($k=2$)", "Bag III ($k=3$)"])
plt.xlim(0.5, 3.5)
plt.ylim(0, 0.48)
plt.grid(True, linestyle=":", alpha=0.6)
plt.legend(frameon=True, fontsize=10, loc="upper right")
plt.tight_layout()
plt.savefig("figs/bags_pmf_stem.png", dpi=150)
plt.show()
