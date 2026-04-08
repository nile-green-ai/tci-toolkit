"""
TCI Demo — 10‑Second Quickstart
Run with:  python run_demo.py

This simulates a persistent agent over 20 timesteps,
showing TCI rising, falling, and recovering.
"""

import random
from tci_calculator import TCICalculator
from k_estimator import KEstimator

# Initialize components
k_est = KEstimator(window_size=50)
tci   = TCICalculator(f_survival=0.35)

print("\n=== TCI Demo: Surplus Dynamics in a Persistent Agent ===\n")

for t in range(20):

    # Simulate model loss (F_total) drifting over time
    f_total = 0.35 + random.uniform(-0.15, 0.45)

    # Simulate complexity / novelty score
    complexity = random.uniform(0.2, 0.9)

    # Update k(s)
    k = k_est.update(f_total - 0.35, complexity)

    # Compute TCI
    result = tci.compute(f_total, k)

    # Pretty print
    stage = result.stage
    grade = result.grade
    tci_v = round(result.tci, 3)

    alert = ""
    if grade == "D":
        alert = " ⚠️  Collapse Warning"
    elif grade == "F":
        alert = " ❌ Collapse Imminent"

    print(f"t={t:02d} | TCI={tci_v} | Grade={grade} | Stage={stage}{alert}")

print("\nDemo complete.\n")
