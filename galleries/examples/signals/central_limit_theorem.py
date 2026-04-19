"""Central Limit Theorem demonstration using sums of uniform random variables.

This example shows how adding together multiple independent uniform random
variables produces a distribution that approaches a normal distribution.
It demonstrates a core concept in probability and statistics used in
engineering, signal processing, and data analysis.
"""

import matplotlib.pyplot as plt
import numpy as np

# --- Your plotting code here (15-30 lines) ---
# Use plt.subplots(), ax.plot(), ax.set(), etc.
# Generate data with numpy (linspace, random, exp, sin, etc.)

rng = np.random.default_rng(42)
N_values = [1, 2, 5, 20]

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.ravel()

for i, N in enumerate(N_values):
    samples = rng.uniform(size=(10000, N)).sum(axis=1)
    
    axes[i].hist(samples, bins=40, color='tab:blue', alpha=0.7)
    axes[i].set_title(f'N = {N}')
    axes[i].set_xlabel('Sum of random variables')
    axes[i].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

References
----------
- matplotlib.pyplot.subplots
- matplotlib.pyplot.hist
- matplotlib.pyplot.set_xlabel
- matplotlib.pyplot.set_ylabel
- numpy.random.default_rng
- numpy.ndarray.sum

tags:
- plot-type: histogram
- level: beginner