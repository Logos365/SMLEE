# Peer Review Report

**Journal:** Advanced Functional Materials  
**Title:** Single-Atom-Stabilized Defects: Breaking the Activity–Stability Trade-off in Li–S Battery Electrocatalysis  
**Authors:** X. Du, C. Sun, C. Zhang, M. Zhen\*  
**Review Date:** 2026-06-15  
**Decision:** **Major Revision**

---

## General Assessment

This manuscript introduces a "catalyst-stabilized defects" strategy in which Nb single atoms (SAs) anchored on vacancy-rich TiO₂(B)/carbon cloth (Nb/V-T@CC) thermodynamically pin metastable vacancy clusters, simultaneously suppressing structural degradation and enhancing polysulfide catalysis. The electrochemical performance—0.028% capacity decay per cycle over 1000 cycles at 2.0 C—is notable, and the use of PALS to quantify vacancy cluster evolution is a methodological strength. However, several critical problems preclude acceptance: a synthesis description contradiction that undermines the control experiment, an uncited competing paper that substantially overlaps the core concept, inconsistent headline performance numbers, and pervasive figure legibility failures. The manuscript also requires significant length reduction. Detailed comments are provided below.

---

## Critical Comments

**C1. Synthesis Protocol Contradiction (HV-T@CC)**

The preparation of HV-T@CC is described inconsistently. The main text (p. 3) states T@CC is calcined in *air* and HV-T@CC in *argon*, with no Nb involved. The SI (p. S3), however, states "The HV-T@CC sample was prepared using the **same procedure** [as Nb/V-T@CC], except that the annealing was carried out under an **air** atmosphere"—implying HV-T@CC includes the NbCl₅ impregnation step. If so, HV-T@CC would contain Nb with fewer vacancies, invalidating the entire comparative study. The authors must: (a) provide an unambiguous step-by-step synthesis flowchart for all samples, (b) clarify definitively whether HV-T@CC contains Nb, and (c) supply ICP-MS or XPS data on HV-T@CC confirming the absence of Nb.

**C2. Pouch Cell Capacity Discrepancy**

The Abstract and Conclusion claim a pouch cell capacity of **1.3 Ah**, while the main text (p. 14) reports **1.03 Ah after 30 cycles**—a >26% discrepancy. If 1.3 Ah is the initial discharge capacity, this must be stated explicitly with the corresponding cycle number in the Abstract, Results, and Conclusion. The full capacity vs. cycle-number profile (including the initial value) must be clearly labeled in Figure 8g.

**C3. Uncited Directly Competing Work**

The following paper—not cited—reports the **identical concept** of stabilizing oxygen vacancies in a 2D oxide to break the activity–stability trade-off in Li–S batteries:

> C. Zhao et al., "Intrinsic Stabilization of Vacancies in Catalysts via High-Entropy Approach for Lithium-Sulfur Batteries," *Natl. Sci. Rev.* **2025**, 12, nwaf375.

This work achieves 0.032%/cycle over 2000 cycles using a high-entropy alloying approach to pin vacancies. It must be cited, discussed, and explicitly compared with the single-atom approach presented here. Claims of being "paradigm-shifting" or "first" must be revised accordingly.

**C4. Duplicate and Erroneous References**

- **Refs. [45] and [46]** are word-for-word identical (S. Li et al., *Adv. Mater.* 37, 2025, e11910). One citation is erroneous and must be corrected.
- **Refs. [25] and [47]** appear to cite the same paper (J.Q. Liu et al., *Adv. Mater.* 38, on vacancy-engineered CeO₂) but list different years (2025 vs. 2026). Verify and correct. A full reference audit is required.

---

## Major Comments

**C5. Novelty Overlap — Zhang et al., JACS 2023 (Ref. [20])**

The d–p hybridization argument between Nb and S 2p states (Section "Electrocatalytic Kinetics") is taken almost verbatim from Zhang et al. (*J. Am. Chem. Soc.* **2023**, 145, 1728), which already established Nb SA catalysis for Li–S via d–p hybridization. The authors must clearly articulate what mechanistic insight is **new beyond** that paper. The TiO₂(B) support and vacancy stabilization are the genuine advances; these should be foregrounded.

**C6. Novelty Overlap — Mao et al., EES 2025 (Ref. [38])**

Mao et al. (*Energy Environ. Sci.* **2025**, 18, 8631) reports Nb SAs on a TiO₂-related lithiophilic support for Li–S batteries with strong Nb–S interaction and dual cathode/anode functionality. This is cited but not discussed in relation to novelty. The authors must explicitly compare the two systems and justify why TiO₂(B) with vacancy clusters is superior.

**C7. EXAFS Distance Reporting**

The first-shell Nb–O distance is reported as "~1.52 Å… significantly shorter than Nb–O in Nb₂O₅ (~1.77 Å)." It is unclear whether these are uncorrected R-space peak positions or phase-shift-corrected bond lengths. If one is corrected and the other is not, the comparison is misleading. The reporting convention must be clearly stated and applied consistently throughout.

**C8. DFT+U Parameter Justification**

Hubbard U values of UTi = 5.0 eV and UNb = 4.8 eV are used without justification or reference. These parameters directly affect the computed vacancy formation energies and d-band center positions central to the manuscript's claims. A literature reference or benchmark against an experimental observable (e.g., TiO₂(B) band gap, lattice parameters) is required.

**C9. Missing Statistical Rigor**

The number of replicate cells is never stated. Error bars are absent in the key long-term cycling figures (Figs. 4e, 4f, 4h, 4i) and the Li nucleation overpotential plot (Fig. 5a). A minimum of n = 3 independent cells with mean ± SD is required for all headline performance claims.

**C10. PALS Component Assignment**

The assignment of τ₂ (~0.41–0.42 ns) to "vacancy clusters" and τ₁ (~0.28–0.35 ns) to "isolated vacancies" is made without reference to established positron lifetime values for VO and VTi in TiO₂. At least two literature references reporting TiO₂ positron lifetimes are needed to validate these assignments.

**C11. Universality Claim Is Unsupported**

The claim that the principle is "universal" and applicable to "oxygen electrocatalysis, CO₂ reduction, and ammonia synthesis" is entirely speculative and unsupported by any data in the manuscript. Remove this claim or provide preliminary supporting evidence.

**C12. Manuscript Length**

The main text (~17 pages) is too long and repetitive. The same performance advantages of Nb/V-T@CC are restated across the Characterization, Electrochemical, Kinetics, and Full Cell sections. A targeted reduction to ~12–13 pages, with detailed kinetic analyses (CV contour maps, DRT deconvolution) moved to SI, is required.

---

## Minor Comments

**C13.** The Randles–Ševčík equation (SI p. S6) assumes semi-infinite planar diffusion—not appropriate for porous 3D CC electrodes. Acknowledge this limitation; GITT-derived DLi⁺ values should be treated as primary.

**C14.** Vacancy formation energies in Figure S13 (10.69–15.63 eV) are unusually high. Specify the chemical potential reference state for the removed O/Ti atoms and clarify whether values are per-vacancy or per-cluster totals.

**C15.** The EPR signal at g ≈ 1.992 is attributed to VTi without a reference. This g-range commonly corresponds to Ti³⁺ centers, not cation vacancies. Provide a reference or revise the assignment.

**C16.** The ΔG profile (Fig. 6g) begins at Li₂S₆, omitting the Li₂S₈ → Li₂S₆ step and the liquid-to-solid phase transition. State explicitly why the pathway is truncated at Li₂S₆.

**C17.** Nb loading (0.615 wt%) is presented as a single measurement without optimization. Briefly justify the chosen loading or note that optimization was not performed.

**C18.** The manuscript overuses emphatic language ("Notably," "Remarkably," "Unambiguously," ≥ 6 times each; "paradigm-shifting" twice). Retain each term at most once per section; "paradigm-shifting" should be removed entirely.

**C19.** "a ultrahigh sulfur loading" (Abstract) is a grammatical error. Correct to "**an** ultrahigh sulfur loading."

**C20.** The pouch cell is demonstrated only at 0.05 C. Acknowledge this as a limitation, or add at least one measurement at 0.1 C.

---

## Figure-Specific Comments

**F1. All Figures — Font Size [Major]**  
All text in figures (axis labels, tick marks, legend, annotations) is illegible at journal column width (~5–6 pt at print size). All figures must be re-exported with ≥ 8 pt font at the intended final print dimensions (≥ 300 dpi). This is a non-negotiable requirement.

**F2. Figures 1e, 1f — HAADF-STEM Single-Atom Verification [Major]**  
No intensity line profiles or statistical analysis are provided to support the identification of bright dots as individual Nb atoms. Add: (a) intensity line profiles across ≥ 5 bright dots showing Z-contrast consistent with Nb (Z = 41) vs. Ti (Z = 22); (b) a wider-field image (≥ 20 × 20 nm²) confirming random rather than periodic distribution.

**F3. Figure 4f — Capacity Decay Calculation [Moderate]**  
The initial capacity at 2.0 C is not labeled on Figure 4f. Show the initial capacity value and explicitly state the 0.028%/cycle calculation in the figure or caption: (1008 − 720) / (1008 × 1000) × 100 = 0.0286%/cycle.

**F4. Figure 4g — Radar Chart [Major]**  
The radar chart compares Nb/V-T@CC against unidentified literature references with no traceable testing conditions. Replace with a scatter plot where each reference is labeled, or add a companion table in SI listing all benchmark sources with current rate, sulfur loading, E/S ratio, and cycle number.

**F5. Figure 3a, 3b — DFT Isosurface Thresholds [Moderate]**  
ELF maps and charge density difference plots do not report isosurface threshold values. Report these values in the figure caption or SI.

**F6. Figure 6g — ΔG Pathway [Moderate]**  
The SRR pathway omits Li₂S₈ → Li₂S₆ and the liquid-to-solid phase transition. State in the caption that the pathway begins at Li₂S₆ and justify this choice.

**F7. Figure S1 — EPR Assignment [Minor]**  
Add a literature reference for the VTi assignment at g ≈ 1.992; alternatively revise to Ti³⁺ assignment.

---

## Summary Checklist

| # | Priority | Action |
|---|---|---|
| C1 | **Critical** | Resolve HV-T@CC synthesis contradiction + ICP-MS/XPS proof of Nb absence |
| C2 | **Critical** | Fix pouch cell capacity inconsistency (1.3 Ah vs. 1.03 Ah) |
| C3 | **Critical** | Cite Zhao et al., *NSR* 2025; revise novelty claims |
| C4 | **Critical** | Fix duplicate references [45]=[46] and [25]/[47]; full reference audit |
| C5–C6 | Major | Differentiate from Zhang *JACS* 2023 and Mao *EES* 2025 |
| C7 | Major | Clarify EXAFS distance convention |
| C8 | Major | Justify DFT+U values |
| C9 | Major | Add n ≥ 3 replication and error bars to all key figures |
| C10 | Major | Add PALS literature reference values for TiO₂ defects |
| C11 | Major | Remove unsupported "universal applicability" claim |
| C12 | Major | Shorten manuscript by ~20–25% |
| C13–C20 | Minor/Moderate | See individual comments above |
| F1 | **Major** | Fix all figure font sizes to ≥ 8 pt at print size |
| F2 | **Major** | Add HAADF-STEM intensity line profiles for Nb atom verification |
| F4 | **Major** | Replace radar chart with traceable benchmark comparison |
| F3, F5, F6, F7 | Moderate/Minor | See individual figure comments |

---

## Closing Remarks

The core thermodynamic argument—Nb SAs inverting the vacancy migration driving force to pin surface vacancies—is intellectually compelling and the PALS evidence is genuinely novel for this field. These strengths can support publication after the above revisions are addressed. The authors are encouraged to build a more focused narrative centered on the PALS-based mechanistic proof and the DFT vacancy-pinning argument, rather than a broad claim of universal paradigm shift.

---

*Key references for author consideration:*  
[A] Y. Zhang et al., *JACS* **2023**, 145, 1728. DOI: 10.1021/jacs.2c10345  
[B] X. Zhou et al., *Nano-Micro Lett.* **2025**. DOI: 10.1007/s40820-025-01806-0  
[C] C. Zhao et al., *Natl. Sci. Rev.* **2025**, nwaf375. DOI: 10.1093/nsr/nwaf375  
[D] Y. Mao et al., *Energy Environ. Sci.* **2025**, 18, 8631. DOI: 10.1039/d5ee02048d
