import matplotlib.pyplot as plt
import numpy as np

observables = ['$m_p / m_e$', '$m_\\mu / m_e$', '$m_n / m_p$', '$m_n - m_e$ (Scaled)']
residuals_sigma = [-44.7, 2660.9, 67.3, 1516.0]
colors = ['#4682B4', '#D9534F', '#4682B4', '#D9534F']

plt.figure(figsize=(10, 6), dpi=300)
bars = plt.barh(observables, residuals_sigma, color=colors, alpha=0.85, edgecolor='black', height=0.5)

plt.axvline(0, color='black', linewidth=1)
plt.title("Standardized Physical Residuals ($\\Delta / \\sigma_{{exp}}$) Relative to CODATA (2022)", fontsize=12, fontweight="bold", pad=15)
plt.xlabel("Residual Magnitude in Experimental Uncertainty Units ($\\sigma$)", fontsize=11)
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Value annotations on bars
for bar in bars:
    width = bar.get_width()
    ha_pos = 'left' if width >= 0 else 'right'
    offset = 30 if width >= 0 else -30
    plt.annotate(f'{width:+.1f} $\\sigma$',
                 xy=(width, bar.get_y() + bar.get_height() / 2),
                 xytext=(offset, 0),
                 textcoords="offset points",
                 ha=ha_pos, va='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig("fig2_residuals_bar.png", dpi=300)
plt.show()
