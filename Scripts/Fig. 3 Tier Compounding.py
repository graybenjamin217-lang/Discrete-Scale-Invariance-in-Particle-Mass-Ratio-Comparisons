import matplotlib.pyplot as plt
import numpy as np

tiers = np.array([0, 1, 2, 3])
delta_dsi = 0.00390
baseline_vals = np.array([1836.152672, 206.780523, 1.001379, 1.294090]) # representative scale baselines

# Compounding calculation: I_baseline * (1 + delta_dsi)^N
compounded_values = []
for n, base in zip(tiers, baseline_vals):
    if n == 0:
        compounded_values.append(base)
    else:
        compounded_values.append(base * ((1 + delta_dsi)**n))

plt.figure(figsize=(9, 6), dpi=300)
plt.plot(tiers, compounded_values, marker='o', markersize=8, color='#2CA02C', linewidth=2, label="Multiplicative Compounding Curve: $(1 + \\Delta_{{DSI}})^N$")

for i, txt in enumerate(compounded_values):
    plt.annotate(f"Tier {tiers[i]}\\nVal: {txt:.4f}", (tiers[i], compounded_values[i]), 
                 textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, fontweight='bold')

plt.title("Hierarchical Tier Compounding Across Generational Intervals ($N$)", fontsize=12, fontweight="bold", pad=15)
plt.xlabel("Generational Tier Index ($N$)", fontsize=11)
plt.ylabel("Compounded Invariant Output", fontsize=11)
plt.xticks(tiers)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(frameon=True, facecolor="#F9F9F9")
plt.tight_layout()

plt.savefig("fig3_tier_compounding.png", dpi=300)
plt.show()
