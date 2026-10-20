# Discrete Scale Invariance in Particle Mass-Ratio Comparisons: An Operator-Based Analysis

**Author:** Benjamin Edward Gray  
**Affiliation:** Independent Researcher, Central Missouri, USA  
**Contact:** graybenjamin217@gmail.com  
https://doi.org/10.5281/zenodo.23455272

---

## Overview

This repository hosts the formal mathematical derivations, analytical frameworks, and computational documentation accompanying the preprint **"Discrete Scale Invariance in Particle Mass-Ratio Comparisons: An Operator-Based Analysis"**. 

The framework transitions away from traditional continuous Renormalization Group (RG) curve-fitting. Instead, it evaluates fundamental baryonic and leptonic mass observables using a **dual-dilation operator framework** defined on a 16-dimensional GNS Hilbert state space ($\mathcal{H}_{M} \cong \mathbb{C}^{16}$), driven by Discrete Scale Invariance (DSI) and non-scalar operator mechanics.

---

## Key Theoretical Architecture

1. **Hybrid Inductive Limit & Local Projection ($\mathcal{H}_M$)**  
   Defined on an inductive limit $C^*$-algebraic Hilbert space $\mathcal{H}_{\infty} = \varinjlim \mathcal{H}_k$, mapped to $\mathcal{H}_{M} \cong \mathbb{C}^{16}$ via mutually orthogonal rank-1 projection operators. Primorial indexing is governed by $N_k = \prod_{j=1}^k p_j$ over a torus of length $L_k = \ln N_k$.

2. **Dual Dilation Operator ($\hat{D}_k$) & Spectra**  
   Scale transformations are driven by the self-adjoint operator $\hat{D}_k = D_{0,k} \otimes \mathbb{I}_4 + \epsilon \mathbb{I}_4 \otimes T_{k,Herm}$, whose point spectrum yields quantized discrete scale steps ($\Delta E = \frac{1}{8}E_0$).

3. **Four-Sector Partitioning ($S_1 \oplus S_2 \oplus S_3 \oplus S_4$)**  
   * **Sector 1 ($S_1$):** Leptonic Ground States (anchored to baseline $E_0$).  
   * **Sector 2 ($S_2$):** Chiral Neutral Flux.  
   * **Sector 3 ($S_3$):** Electroweak Boundary Junction.  
   * **Sector 4 ($S_4$):** Baryonic Confinement Core.  

4. **Universal Feedback & Stability Bounds**  
   Incorporates the non-linear feedback operator $\hat{\Omega}_G(\hat{A}) = \hat{A}^{-(I-\hat{A}^{-1})}$ anchored by the metric drag factor $\eta_{drag,scaled} \approx 0.0136071168$. Evaluated under Kato-Rellich spectral stability with a localized projection bound of $\delta_{crit,local} \approx 0.27417$.

---

## Summary of Derived Observables vs. CODATA (2022)

| Observable | Evaluated DSI Output | CODATA Reference (2022) | Physical Residual ($\Delta$) | Structural Step Position |
| :--- | :--- | :--- | :--- | :--- |
| **$m_p / m_e$** | 1836.152672 | 1836.15267343 | -0.00000143 | Plateau Baseline |
| **$m_\mu / m_e$** | 206.780523 | 206.7682827 | +0.0122403 | Upper Edge of DSI Step |
| **$m_n / m_p$** | 1.001379227 | 1.001378419 | +0.000000808 | Upper Edge of DSI Step |
| **$m_n - m_p$** | 1.294090 MeV | 1.293332 MeV | +0.000758 MeV | Upper Edge of DSI Step |

*Note: Physical residuals quantify the structural delta between unshielded DSI holonomy plateaus and continuous, environmentally screened experimental readings.*

---

## Repository Structure

```text
├── docs/                 # Formal derivation papers and preprints
├── scripts/              # Python calculation modules & operator engines
├── data/                 # Comparative CODATA benchmark datasets
└── README.md             # Project documentation
```

--- 

## Citation

Gray, B. E. (2026). Discrete Scale Invariance in Particle Mass-Ratio Comparisons: An Operator-Based Analysis. Zenodo. https://doi.org/10.5281/zenodo.23455272
