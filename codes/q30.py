import numpy as np

# 1. Simulation parameters
n_simulations = 10_000_000

# Bag parameters indexed as: 0 -> Bag I, 1 -> Bag II, 2 -> Bag III
red_balls = np.array([3, 1, 3])   # Number of Red balls in [Bag I, Bag II, Bag III]
black_balls = np.array([1, 2, 4]) # Number of Black balls in [Bag I, Bag II, Bag III]

# 2. Randomly select a bag for each trial (0, 1, or 2) with equal probability (1/3)
selected_bags = np.random.choice([0, 1, 2], size=n_simulations)

# 3. Vectorized ball drawing (sample 2 balls per trial without replacement)
red_drawn = np.random.hypergeometric(
    ngood=red_balls[selected_bags], 
    nbad=black_balls[selected_bags], 
    nsample=2
)

# 4. Identify event E (exactly 1 Red and 1 Black ball drawn)
event_E = (red_drawn == 1)

# 5. Compute P(Bag I | E) without any for loop
bag1_given_E = np.sum((selected_bags == 0) & event_E) / np.sum(event_E)

# 6. Output comparison
print(f"Simulated P(Bag I | E) : {bag1_given_E:.6f}")
print(f"Exact Analytical (21/73): {21/73:.6f}")
