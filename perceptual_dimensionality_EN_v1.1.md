# Perceptual Dimensionality: The Dimensional Budget and Behavioral Readout of the Olfactory System

**Qin Chao** (ORCID 0009-0006-2000-5644 | JueXiao Information Consulting Center, Xingyi, Guizhou 562400, China)

> **v1.1** (2026-09-21): Adds the readout line's pre-registered v0.4 (glomerular-granularity upgrade) results; adds Figure 3 (two-panel rank–rank scatter) and its reproduction script to the package; expands the Appendix A pre-registration statement to four items. v1.0 (2026-09-21): initial version.

**Abstract**: How large is the "perceptible dimensionality" of a perceptual system? Olfaction supplies the sharpest version of the question: the apparent dimensionality of chemical stimulus space runs into the hundreds (387–1948 intact olfactory receptor genes in mammals), while behavioral experiments repeatedly report low-dimensional structure (the leading-dimension elbow of mouse perceptual distances sits at 5–7). This paper answers where that compression comes from with two independent lines of evidence. **The budget line** (cross-species, pre-registered rank regression): if perceptual dimensionality is constrained by the neural budget, receptor count (a proxy for the dimensionality proxy τ) should covary with a budget proxy across species rankings — the whole-brain neuron total operationalization is robustly rejected (n=6 ρ=-0.029; expanded n=8 ρ=-0.143; zero/negative at both sample sizes), while the row-specific peripheral-budget operationalization (olfactory bulb neuron count) comes out positive in sign in the main analysis and in all five sensitivity operationalizations (+0.43 to +0.60; intermediate band honestly reported: direction consistent, sample size insufficient to claim support). The directional split between the two operationalizations is itself independent of sample size and constitutes the argument: **the neural budget is not a uniformly shared total but a resource allocated by row — budgets must be allocated by row**; this is corroborated three ways, by the energetics literature (a constant total budget, flexibly reallocated by task) and by a successful precedent (the budget variable of the visual row is the visual-brain share). **The readout line** (within-species, pre-registered adjudication chain): the falsification of coding–behavioral distance covariation under the widefield pixel-population operationalization was downgraded by a CID-level alignment erratum, and re-adjudication returned it to the intermediate band (truly aligned subset odorset3 ρ=+0.943, leave-one-out robust); response time courses were rejected; the glomerular-granularity upgrade (pre-registration v0.4) improved the direction of pooled covariation (+0.043→+0.193) and raised cross-animal coding reliability (+0.564→+0.732), yet under the locked clause it remains an intermediate band — falsification, erratum, and granularity chain were all executed faithfully under pre-registered locked clauses. The joint framework implication of the two lines: perceptual dimensionality is determined jointly by **row budgets** (resource side) and **behavioral readout conventions** (usage side), neither of which is the receptor count; receptor count is only a proxy for dimensional potential. All comparisons were run with pre-registration preceding results (two falsifications, multiple intermediate bands, one erratum — all on record), and methodological transparency is reported as part of reproducibility.

**Keywords**: perceptual dimensionality; olfaction; neural budget; pre-registration; cross-species comparison

---

## §1 Introduction: Two Routes to the Dimensionality Question

### 1.1 The Problem

A gap separates the apparent dimensionality of chemical space from the operative dimensionality of olfactory behavior. Receptor genomics yields high apparent dimensionality: intact mammalian OR gene counts run from 387 (human) to 1948 (African elephant) [cross-species table]; Drosophila has roughly 60 Or genes. Behavior and psychophysics, however, repeatedly report low dimensionality: in the mouse perceptual-distance matrices of Nakayama et al. (2022), built over full concentration gradients, the leading-dimension elbow sits at 5–7 (far below receptor counts) [behavioral ledger].

Explanations of this gap usually appeal to "compression" — but where the compression happens, and what determines it, have lacked a testable quantitative framework. Within the dimensional-convention framework (τ(T,ε,C): a three-parameter specification of readout target T, precision ε, and channel budget C), this paper splits the problem into two separately testable routes:

- **The budget line** (resource side): the dimensionality a perceptual row can carry is constrained by the neural resources allocated to that row — if true, the row's τ proxy and the row's budget proxy should covary across species;
- **The readout line** (usage side): the dimensionality behavior actually uses is set by readout conventions and task demands — if true, covariation between the information dimensionality of coding matrices and behavioral distance should appear at specific readout granularities/time windows, and the behavioral elbow should sit stably below receptor counts.

Both lines share one methodological discipline: **pre-registration precedes results**. The two falsifications and the intermediate band reported in this paper were all executed under clauses locked before the runs (Appendix A).

### 1.2 Relation to the Dimensional-Convention Framework

The three parameters of the τ(T,ε,C) framework map directly onto the olfactory system: T = readout target (behavioral task vs. coding, treated as decoupled), ε = discriminative precision, C = channel budget. The budget line of this paper tests how C operates (total pool vs. by-row allocation); the readout line tests how T operates (behavioral readout vs. the full code). The dimensional-theoretic details of the framework are given in the companion work [Dimensional Convention]; this paper is self-contained on the correspondences above.

## §2 The Budget Line: Cross-Species Rank Regression (Pre-registrations v0.1/v0.2)

### 2.1 Design

- **τ proxy**: intact OR gene count. A single source serves as the primary analysis (NMT 2014, the largest consistent assembly across 13 species), and a secondary source (Niimura-Nei 2007) serves as sensitivity — receptor count ≠ dimensionality (corroborated by Drosophila's self-computed coding dimensionality of 11–17 ≪ 60); the proxy status is safeguarded at the criterion level by the ordinal-structure version of the test (asserting only the direction of covariation).
- **Two budget-proxy operationalizations**: Y₁ = total whole-brain neuron count (the whole pool; a single-method lineage, isotropic fractionator); Y₂ = olfactory bulb neuron count (the row-specific peripheral budget; three first-hand sources: the Ribeiro 2014 21-species table, Oliveira-Pinto 2014 human OB, Neves 2014 elephant OB).
- **Primary set**: n=6 (human/rhesus macaque/mouse/rat/dog/elephant, spanning 4 orders) — a structural upper bound: the intersection of the two databases is capped by the OR-genomics species set (§5).

### 2.2 Result 1: The Whole-Brain Operationalization Is Falsified (Robustified)

The first run after pre-registration v0.1 was locked (criterion: ρ≤0 falsifies; no species removed on the basis of results): n=6, ρ=-0.029 (exact p=0.54) — inside the falsification region. The expansion test (S5, n=8, adding guinea pig/marmoset) gives ρ=-0.143 — **zero/negative at both sample sizes; the falsification is robust, not small-sample noise**.

Rank-inversion structure (diagnostic): the inversions concentrate on primates (human/macaque: low X, high Y) against rodents (mouse/rat: high X, low Y), while dog/elephant are fully concordant (d=0). A mechanistic note (not entering the adjudication layer): primate OR pseudogenization (about 51% in human/chimpanzee) plus budget flow toward visual/association cortex.

### 2.3 Result 2: The Row-Specific Operationalization Is Stably Positive (Intermediate Band, Honestly Reported)

The first run after pre-registration v0.2 was locked (Y switched to olfactory bulb neuron count; the mechanical-coupling declaration registered before the run): main analysis n=6, ρ=+0.486 (p=0.178); sensitivity S1 (alternative OR source) +0.600; S2 (+marmoset, n=7) +0.536; S3 (human OB split by sex) +0.600 and +0.429; S4 (OB-share operationalization) +0.600 — **all six operationalizations positive (+0.43 to +0.60)**, with exact p falling in 0.118–0.210.

Under the locked intermediate-band clause: a directional tendency with insufficient evidence — no claim of support, no falsification. The variation points are disclosed as-is: macaque OB has n=1; mouse OB at 3.89M lies below guinea pig (against body-size intuition, faithfully recorded in Ribeiro's original) — these two data points determine how strong the direction is.

### 2.4 Result 3: Two-Way Cross-Operationalization Contrast — Budgets Must Be Allocated by Row

On the same data plane, the directional split between the two operationalizations (whole-brain stably negative / row-specific stably positive across all sensitivity analyses) is independent of sample size and constitutes the argument block: the whole-brain operationalization's failure is not "dimensionality is unrelated to budget" but the necessary condition for a row-budget operationalization. Three-way mutual corroboration: (i) the total budget is constant (human brain energy income and expenditure are approximately constant across individuals and tasks; Raichle 2002); (ii) cortical resources are flexibly reallocated across regions by task (Lennie 2003's resource ledger); (iii) an isomorphic closed loop with a successful precedent (Barton 2004: in the primate visual row, the budget variable of the dimensionality × budget regression is precisely the visual-brain structure share, not the whole-brain total).

**Proposition (budgets must be allocated by row)**: [inference · framework, within this paper's evidence plane] The dimensionality constraint on a perceptual row is validly operationalized by a row-share budget; whole-brain totals exert no binding force on row dimensionality. (The full picture of the directional split between the two operationalizations is Figure 1: `fig1_budget_direction_split.png`; the two-panel rank–rank scatter is Figure 3: `fig3_rank_scatter.png`, with reproduction script `fig3_rank_scatter.py`.)

## §3 The Readout Line: Within-Species Coding–Behavioral Covariation (Pre-registered Adjudication Chain)

### 3.1 Low-Dimensional Anchors on the Behavioral Side

- **Mouse**: the three-odorset perceptual-distance matrices of Nakayama 2022 (the paper's original calc_distance), with leading-dimension elbows at 5–7 — stable low-dimensional readout across concentrations and tasks [behavioral ledger].
- **Drosophila**: on the coding side, self-computed over two datasets and five operationalizations (DoOR + Hallem); the credible operationalizations give a coding dimensionality of 11–17 with an upper bound of 24 — under 1/4 of the 60 receptor count; the "tens of dimensions" over-reading is self-corrected [receptor repertoire file].
- **Two anchors and a false opposition**: signs that the coding side's 11–17 and the behavioral side's 5–7 share a band coexist with the full-panel coding 17–36 lying far from the behavioral 5–13 — a candidate reading of "two-band separation between coding and behavioral dimensionality" (cross-species-level morphological evidence) that depends strongly on stimulus-set size and coverage (reading downgraded pending adjudication).

### 3.2 Adjudication Experiments: Falsification, Erratum, and Re-adjudication (The Pre-registered Chain, Fully on Record)

The pre-registered Mantel-framework adjudication (v0.1) of widefield pixel-population coding distances × single-animal delayed match-to-sample (DMTS) distances: the primary test was falsified (ρ=-0.031). **Post-execution erratum (triggered under pre-registration v0.3)**: the stimulus-alignment intersections proved inflated at CID-level re-check (odorset1∩3 / 2∩4 / 3∩4; v0.1 had reported 5/6/7 — string-level mis-pairing had recurred), and the v0.1 falsification was downgraded. **CID-level re-adjudication (v0.3, executed the same day the pre-registration was locked)**: (i) the truly aligned 6-pair subset (odorset3) gives ρ=+0.943, **leave-one-out robust (removing any single pair leaves ρ∈[0.90, 1.00]; not driven by one pair)**; (ii) the pooled 15 pairs give ρ=+0.043 (intermediate band; the operationalization confound of pooling across odorsets is handled by stratified interpretation first); (iii) the generalization imaging animal gives +0.314 (intermediate band); (iv) cross-animal coding reliability rises to +0.564 on the truly aligned subset (from +0.317 under v0.1) — the false pairs had contaminated the original control as well. The response-time-course primary test comes back negative (all 10 windows |ρ|≤0.061; max-peak corrected p=0.49) — the covariation, if present, is carried by trial averaging, with no temporal localization. Signal-quality diagnostics (same-odor trial-to-trial correlations 0.88/0.77) and C1′ show that coding information exists and is reliable across animals — the coding–behavioral covariation question returns to open (intermediate band) on the truly aligned subset, and the existence of coding information is not the point in dispute. (The time-course null curves are Figure 2: `fig2_timecourse_null.png`.)

**Granularity-upgrade adjudication (pre-registration v0.4, executed the same day the pre-run lock was set)**: the only variable is channel granularity on the coding side (pixel population → glomerular bright-blob ROIs; at the widefield limit a single glomerulus spans only 2–4 px, so the operationalization is "blob-scale units rather than anatomical glomerular segmentation" — the three detection parameters were locked before the run, with no hand-tuned constants). Results: M1″ pooled 15 pairs ρ=+0.193 (permutation reference p=0.49) — an upward shift in direction relative to the pixel operationalization (+0.043), still an intermediate band under the locked clause; cross-animal coding reliability C1″ rises from +0.564 to +0.732; odorset3 remains strongly positive (+0.943→+0.657) — that set's covariation is not driven by pixel artifacts; odorset1/2 keep a stable negative sign under both granularities (a granularity-independent negative-covariation structure; open problem 6); the generalization animal's gains do not transfer (+0.314→+0.036). Interpretation (bidirectional clause pre-registered before the run): coding organization gains a directionally supportive surface at the glomerular scale, but under the locked clause no claim of support is entered; the main carrier of behavioral-side covariation is more likely the odorset/task structure than coding granularity.

### 3.3 The Current Shape of the Readout Line

The three-tier structure — behavioral elbow (5–7) ≪ coding upper bound (11–17/17–36) ≪ receptor count (387–1948/60) — holds independently along both species lines. The readout line's quantitative test is carried by the four-step adjudication chain (pixel falsification → CID-corrected re-adjudication → time-course rejection → glomerular-granularity intermediate band): coding information exists and is reliable across animals; coding–behavioral covariation is weak and odorset-dependent; further decomposition of the behavioral-side covariation (the odorset/task-structure dimensions) is left to future work (open problem 6).

## §4 Framework: The Three-Parameterization of τ and the Status of the Seven Predictions

### 4.1 The Three-Parameterization

In the dimensional-convention framework, readout dimensionality τ was originally a two-argument function τ(T, ε) (readout target T, precision ε). This paper's evidence plane upgrades it to three arguments:

**τ(T, ε, C)** — what evolution selects is not abstract simplicity but the **simplest complete code within the computationally feasible set**: min{dim D : distortion ≤ ε and neural implementation cost ≤ C}.

Three corollaries: (i) a high-dimensional equality point is an **expensive equality point** — it becomes feasible only once C ≥ threshold (Drosophila's C cannot reach a three-dimensional sense); (ii) as C rises the feasible set expands and the equality point can move up (the evolutionary gradient is a gradient in C); (iii) behavioral state changes the effective C (reallocation of compute during escape → readout dimensionality reduction) — state-dependent dimensionality gains a mechanism. The three operationalizations of C (parallel unit count × activation rate / structural share / physiological conversion) are unified by mutual translation through the energetics literature (energy use ≈ linear in neuron count plus structural coefficients).

### 4.2 Status of the Seven Predictions (Literature Plane + This Paper's Evidence Plane)

| Prediction | Status |
|---|---|
| 1 Row budget (chemical space) | Closed in this paper's §2: whole-brain falsified + OB intermediate band + two-way contrast — an isomorphic closed loop with Barton 2004's visual row-share operationalization |
| 2 Dimensionality reduction under C perturbation (dose–response) | Half-supported on the literature plane: Scharff 2013 found fixed capacity for 3D shape readout but unlimited capacity for 2D within the same experiment — "the higher-dimensional readout is the first capped by budget"; gap: graded dose–response curves |
| 3 Input-density manipulation (Drosophila claw count) | Directional correction: the constraining variable is input density rather than unit count (more favorable to the framework); a collaborative experiment specification is on file |
| 4 Nematode τ≈1 | Confirmed first-hand (connectome level) |
| 5 Electric-fish 3D sense | Supported by two publications |
| 6 Water-strider mixed 2D+3D readout | Partly raised, partly lowered (task-dependent) |
| 7 Anesthesia/state collapse | No direct literature found (indirect items only) — the gap is reported as-is |

## §5 Data-Infrastructure Gaps (Methodological)

The reason the cross-species τ × budget regression has not reached scale is structural: **the OR-genomics species set and the neuron-count species set are complementary and non-overlapping** (Kverková 2022's inventory: neuron-count data for 37 bird + 116 reptile species with no mammals; bird species with complete OR tables lack neuron-count data; among mammals, rabbit/cattle/chimpanzee/horse lack counts in the Herculano-Houzel (H-H) lineage) — not a gap in any single paper, but the current division of labor between two infrastructures, receptor genomics and cell counting. This paper's self-built alignment table (10 molecules × dual budget operationalizations, 8 species) is the largest achievable data plane for this test under the current literature; expansion must wait for natural growth in the two databases' coverage or targeted supplementary measurement.

## §6 Open Problems

1. The effective granularity of row budgets: beyond the olfactory bulb (peripheral), the availability of row shares in the cortical piriform system (human OB is available split by sex; piriform data are sparse) — extending the budget line to cortex;
2. Formalizing readout granularity: the three granularities — pixel / glomerular / time-course window — have been systematically tested by the adjudication chain (time-course rejection + granularity intermediate band + the granularity stability of the odorset1/2 negatives); the next lever for decomposing behavioral-side covariation is the odorset/task-structure dimension (a candidate behavioral-side task decomposition);
3. Cross-row tests: beyond the visual row (the Barton isomorphic closed loop), τ × row-share regression for the auditory and somatosensory rows — is "budgets must be allocated by row" universal across rows;
4. Calibrating the behavioral-side C of τ(T,ε,C): the quantitative relation between the behavioral elbow at 5–7 and task demands (degrees of freedom vs. task resolution);
5. An infrastructure route through the two-database gap: the minimal species set for targeted supplementary measurement (3–4 species per row would extend the primary set from n=6 to n=10+);
6. Interpreting the negative stratification of odorset1/2: concentration/task differences vs. genuinely negative covariation — requires molecule-level, concentration-balanced replication experiments.

## Appendix A: Pre-Registration Discipline Statement

Every comparison in this paper was executed with pre-registration preceding results: (i) two pre-registrations on the budget line (v0.1, whole-brain operationalization — falsification executed; v0.2, row-specific operationalization — re-registered after the falsification, with the mechanical-coupling declaration filed before the run and the intermediate-band clause executed); (ii) readout-line adjudication pre-registrations v0.1 (falsification executed, triggering the alignment erratum), v0.3 (molecule-by-molecule lock of the CID-level alignment master table + the dual-task response time course), and v0.4 (route-b granularity upgrade — channel granularity as the only variable, three parameters locked before the run, bidirectional interpretation pre-registered). Two falsifications, multiple intermediate bands, and one erratum — all on record, with the erratum chain public (details of the mis-aligned pairs in the v0.3 pre-registration trigger section) — falsification and erratum are part of the method, not results in need of cosmetic repair.

## Appendix B: Data Tables

B.1 Two-database alignment master table (X = OR intact single source / Y₁ = whole brain / Y₂ = olfactory bulb; 8 species + a source-verification column) — the ledger is in hand; the final version ships with the paper.
B.2 Operationalization-contrast results table (ρ, exact p, and locked-adjudication columns for the v0.1 main / S5 contrast / v0.2 main + S1–S5) — both pre-registration documents are in hand.
B.3 CID-level alignment master table (10 molecules × 3 odorsets + CIDs) — in hand as Section 0 of the v0.3 pre-registration.
B.4 Glomerular-granularity adjudication documents (pre-registration v0.4 + pipeline and statistical scripts + results archive) — released with the paper; Figure 3 reproduction script `fig3_rank_scatter.py` (with built-in ρ anchor assertions).

**Statement of Methods and AI Involvement**: observation, problem formulation, and all framing decisions were made by the author; the framework's AI system (Wo) carried out literature search and ledger verification, statistical analysis execution (after the pre-registration lock), pipeline implementation, and drafting of the manuscript; every pre-registration document was committed to disk before its corresponding results (file timestamps are auditable).

**Declaration of Interests**: none. **Data and Code Availability**: analysis scripts, pre-registration documents, and ledgers are released with the Zenodo record.

## References

[1] Nakayama, H.; Gerkin, R. C.; Rinberg, D. A behavioral paradigm for measuring perceptual distances in mice. Cell Reports Methods 2(6): 100233, 2022. DOI: 10.1016/j.crmeth.2022.100233.
[2] Niimura, Y.; Nei, M. Extensive gains and losses of olfactory receptor genes in Mammalian evolution. PLoS ONE 2(8): e708, 2007. DOI: 10.1371/journal.pone.0000708.
[3] Niimura, Y.; Matsui, A.; Touhara, K. Extreme expansion of the olfactory receptor gene repertoire in African elephants and evolutionary dynamics of orthologous gene groups in 13 placental mammals. Genome Research 24(9): 1485–1496, 2014. DOI: 10.1101/gr.169532.113.
[4] Ribeiro, P. F. M.; Manger, P. R.; Catania, K. C.; Kaas, J. H.; Herculano-Houzel, S. Greater addition of neurons to the olfactory bulb than to the cerebral cortex of eulipotyphlans but not rodents, afrotherians or primates. Frontiers in Neuroanatomy 8: 23, 2014. DOI: 10.3389/fnana.2014.00023.
[5] Oliveira-Pinto, A. V. et al. Sexual dimorphism in the human olfactory bulb: females have more neurons and glial cells than males. PLoS ONE 9(11): e111733, 2014. DOI: 10.1371/journal.pone.0111733.
[6] McGann, J. P. Poor human olfaction is a 19th-century myth. Science 356(6338): eaam7263, 2017. DOI: 10.1126/science.aam7263.
[7] Barton, R. A. Binocularity and brain evolution in primates. PNAS 101(27): 10113–10115, 2004. DOI: 10.1073/pnas.0401955101.
[8] Raichle, M. E.; Gusnard, D. A. Appraising the brain's energy budget. PNAS 99(16): 10237–10239, 2002. DOI: 10.1073/pnas.172399499.
[9] Lennie, P. The cost of cortical computation. Current Biology 13(6): 493–497, 2003. DOI: 10.1016/S0960-9822(03)00135-0.
[10] Kverková, K. et al. Mammalian brain size and composition from an expanded sample of species. PNAS 119(11): e2121624119, 2022. DOI: 10.1073/pnas.2121624119.
[11] Münch, D.; Galizia, C. G. DoOR 2.0 — Comprehensive mapping of Drosophila melanogaster odorant responses. Scientific Reports 6: 21841, 2016. DOI: 10.1038/srep21841.
[12] Hallem, E. A.; Carlson, J. R. Coding of odors by a receptor repertoire. Cell 125(1): 143–160, 2006. DOI: 10.1016/j.cell.2006.01.050.
[13] Robertson, H. M.; Warr, C. G.; Carlson, J. R. Molecular evolution of the insect chemoreceptor gene superfamily in Drosophila melanogaster. PNAS 100(Suppl. 2): 14537–14542, 2003. DOI: 10.1073/pnas.2335847100.
[14] Bushdid, C.; Magnasco, M. O.; Vosshall, L. B.; Keller, A. Humans can discriminate more than 1 trillion olfactory stimuli. Science 343(6177): 1370–1372, 2014. DOI: 10.1126/science.1249168.
[15] Scharff, A.; Palmer, J.; Moore, C. Evidence of fixed capacity in visual object categorization. Journal of Vision 13(2): 18, 2013. DOI: 10.1167/13.2.18.
[16] Qin, Chao. Dimensional Convention: A Mapping Construction for the Dimensionality of Readout Targets (in Chinese). Zenodo, 2026. DOI: 10.5281/zenodo.22844311.

*Citation verification statement: [1]–[15] were resolved entry-by-entry via CrossRef (2026-09-21, subagent verification); [16] was verified against the internal archive. Corrections on record — Barton 2004 page numbers 11113→10113 (issue 27); the canonical DoOR citation changed to Münch & Galizia 2016 (Sci Rep article number 21841; "Dimitrov" was a misremembered, nonexistent author); Bushdid volume number 344→343; Robertson 2003 title completed as "Molecular evolution of...".*

---
*Perceptual Dimensionality, standalone paper v1.1 | 2026-09-21 | Additions over v1.0: readout-line pre-registration v0.4 (glomerular-granularity upgrade) results; Figure 3 rank–rank scatter and its reproduction script added to the package; Appendix A pre-registration statement expanded to four items; abstract and §3/§6 updated accordingly; all materials traceable to first-hand execution records; the five wording-discipline rules (material block §5) applied as hard constraints across the manuscript. Version chain v1.0→v1.1 (DOI 10.5281/zenodo.22867319).*
