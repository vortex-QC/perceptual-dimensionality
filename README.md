# perceptual-dimensionality

Replication and data package for **"Perceptual Dimensionality: Dimensional Budgets and Behavioral Readout in Olfaction"**.

**Zenodo (CN bilingual + figures + preregistration chain): DOI [10.5281/zenodo.22867319](https://doi.org/10.5281/zenodo.22867319)**
Author: Chao Qin (ORCID [0009-0006-2000-5644](https://orcid.org/0009-0006-2000-5644))

## Contents

| File | Content |
|---|---|
| `perceptual_dimensionality_CN_v1.0.md` | Main document (Chinese): budget line (cross-species rank regressions) + readout line (pre-registered adjudication chain) + τ(T,ε,C) framework |
| `fig1_budget_direction_split.png` | Direction split across all pre-registered budget panels (whole-brain vs OB row-specific) |
| `fig2_timecourse_null.png` | Response-timecourse null (10 windows, max-peak corrected)
| `fig3_rank_scatter.png` | Rank-scatter, dual budget panels (OB row-specific n=6 / whole-brain n=8) |
| `preregistration_v0.1_mantel.md` | Adjudication preregistration v0.1 (locked before results) |
| `preregistration_v0.2_crossspecies.md` | Cross-species preregistration v0.2 (row-specific budget proxy) |
| `preregistration_v0.3_CID_alignment.md` | v0.3 correction + response-timecourse preregistration (CID-level alignment table locked) |
| `stimulus_alignment_v0.2.md` | Stimulus alignment ledger (CID-verified) |
| `B3_CID_alignment.csv` | CID-level alignment table (10 molecules × 3 odorsets) |

## Two falsification chains, fully pre-registered

1. **Budget line**: whole-brain neuron count as budget proxy refuted (n=6 ρ=-0.029; n=8 ρ=-0.143, robust); row-specific (olfactory bulb) proxy positive in all six panels (+0.43~+0.60, intermediate band honestly reported) — *budgets must be allocated by row*.
2. **Readout line**: v0.1 adjudication falsified (ρ=-0.031) then corrected — alignment table inflated by string-level mismatches (CID recheck: true overlaps 3/4/4, not 5/6/7); v0.3 re-adjudication: true-aligned odorset3 pairs ρ=+0.943 (leave-one-out robust 0.90–1.00), merged 15 pairs intermediate (+0.043); response-timecourse null (no temporal localization).

Falsifications and corrections are part of the method, not results to be polished.

## Related

- Dimensional-convention framework: [DOI 10.5281/zenodo.22844311](https://doi.org/10.5281/zenodo.22844311)
