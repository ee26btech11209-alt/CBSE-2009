import numpy as np

# 1. Simulation parameters
n_questions = 5
p_correct = 1 / 3
n_simulations = 1_000_000

# 2. Monte Carlo Simulation using NumPy
np.random.seed(42)
simulations = np.random.binomial(n=n_questions, p=p_correct, size=n_simulations)

# Calculate simulated probability for X >= 4
successes = np.sum(simulations >= 4)
p_simulated = successes / n_simulations

# Analytical probability computation (11 / 243)
p_analytical = 11 / 243

print(f"Analytical Probability P(X >= 4): {p_analytical:.6f} (11/243)")
print(f"Simulated  Probability P(X >= 4): {p_simulated:.6f}")
