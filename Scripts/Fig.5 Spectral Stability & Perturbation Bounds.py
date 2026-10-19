import matplotlib.pyplot as plt
import numpy as np

coupling_strength = np.linspace(0, 1.2, 300)
delta_min = 0.125 # Minimum spectral gap (0.125 E_0)
delta_crit_local = 0.27417

# Eigenvalue behavior under perturbation
ev_branch_1 = delta_min + 0.5 * coupling_strength
ev_branch_2 = np.maximum(0.0, delta_min - 0.5 * coupling_strength) # Spectral floor approaching zero at failure limit

plt.figure(figsize=(9, 6), dpi=300)
plt.plot(coupling_strength, ev_branch_1, label="Upper Spectral Branch", color="#1F77B4", linewidth=2)
plt.plot(coupling_strength, ev_branch_2, label="Lower Spectral Branch (Floor)", color="#D62728", linewidth=2)

plt.axvline(x=delta_crit_local, color="orange", linestyle="--", linewidth=2, label=f"Localized Stability Bound ($\\delta_{{crit}} \\approx {delta_crit_local}$)")
plt.axvline(x=1.0, color="black", linestyle=":", linewidth=1.5, label="Kato-Rellich Absolute Limit ($\\delta_{{crit}} = 1.0$")

plt.fill_between(coupling_strength, 0, ev_branch_2, color='#D62728', alpha=0.1, label="Active Stability Domain")

plt.title("Kato–Rellich Spectral Stability & Perturbation Bounds", fontsize=12, fontweight="bold", pad=15)
plt.xlabel("Perturbation Strength Norm ($\\Vert \\eta_{\\text{drag}} M_{\\text{coupling}} \\Vert$)", fontsize=11)
plt.ylabel("Normalized Eigenvalue Spectrum", fontsize=11)
plt.xlim(0, 1.2)
plt.ylim(-0.05, 1.0)
plt.legend(loc="upper right", frameon=True, facecolor="#F9F9F9")
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("fig5_kato_rellich.png", dpi=300)
plt.show()
