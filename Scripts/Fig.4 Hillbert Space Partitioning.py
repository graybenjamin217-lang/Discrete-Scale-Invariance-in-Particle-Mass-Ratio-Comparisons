import matplotlib.pyplot as plt
import numpy as np

sectors = ['Sector 1 ($S_1$)\nLeptonic Ground', 'Sector 2 ($S_2$)\nChiral Neutral Flux', 'Sector 3 ($S_3$)\nEW Boundary', 'Sector 4 ($S_4$)\nBaryonic Core']
dimensions = [4, 4, 4, 4] # 4x4 sub-blocks summing to 16-dim GNS Hilbert space
colors = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728']

fig, ax = plt.subplots(figsize=(9, 6), subplot_kw=dict(aspect="equal"))

wedges, texts, autotexts = ax.pie(dimensions, labels=sectors, autopct='%1.1f%%',
                                  startangle=90, colors=colors, 
                                  textprops=dict(color="black", fontweight='bold'),
                                  wedgeprops=dict(width=0.4, edgecolor='white', linewidth=2))

plt.setp(autotexts, size=10, weight="bold", color="white")
plt.title("16-Dimensional GNS Hilbert Space Partitioning ($\mathcal{H}_M \cong \mathbb{C}^{16}$)", fontsize=12, fontweight="bold", pad=20)

plt.tight_layout()
plt.savefig("fig4_sector_partition.png", dpi=300)
plt.show()
