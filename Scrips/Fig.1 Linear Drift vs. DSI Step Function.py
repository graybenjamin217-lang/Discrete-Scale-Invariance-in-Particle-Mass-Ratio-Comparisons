import numpy as np
import matplotlib.pyplot as plt

# Data generation for continuous drift vs DSI step function
delta_crit = 0.27417
x = np.linspace(0, 0.5, 500)

# Continuous linear/smooth contraction mapping below threshold
y_continuous = np.where(x <= delta_crit, x * 1.5, delta_crit * 1.5 + (x - delta_crit) * 0.1)

# DSI Step function holonomy lock
y_dsi = np.zeros_like(x)
for i, val in enumerate(x):
    if val < delta_crit:
        y_dsi[i] = val * 1.2
    else:
        # Quantized holonomy step transition
        y_dsi[i] = (delta_crit * 1.2) + 0.35 + (val - delta_crit) * 0.05

plt.figure(figsize=(9, 6), dpi=300)
plt.plot(x, y_continuous, label="Continuous Screening Drift", color="#4682B4", linestyle="--", linewidth=2)
plt.plot(x, y_dsi, label="DSI Step-Function Holonomy Lock", color="#D9534F", linewidth=2.5)

plt.axvline(x=delta_crit, color="black", linestyle=":", alpha=0.7, label=f"Critical Threshold ($\\delta_{{crit}} \\approx {delta_crit}$)")

plt.title("Continuous Linear Drift vs. DSI Step-Function Mechanics", fontsize=12, fontweight="bold", pad=15)
plt.xlabel("Accumulated Phase Perturbation ($\\delta$)", fontsize=11)
plt.ylabel("Effective State Response / Scaling Offset", fontsize=11)
plt.legend(frameon=True, facecolor="#F9F9F9", edgecolor="none")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()

plt.savefig("fig1_dsi_drift.png", dpi=300)
plt.show()
