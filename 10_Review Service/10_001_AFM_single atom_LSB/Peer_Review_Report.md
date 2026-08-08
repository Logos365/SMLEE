# Peer Review Report

**Journal:** Advanced Functional Materials  
**Manuscript Title:** Single-Atom-Stabilized Defects: Breaking the Activity–Stability Trade-off in Li–S Battery Electrocatalysis  
**Submission ID:** dd403545-f6b0-4779-825e-fd2236265503  
**Authors:** Xiaohan Du, Chenxi Sun, Chengyang Zhang, Mengmeng Zhen\*  
**Affiliation:** Hebei University of Technology, Tianjin, P. R. China  
**Review Date:** 2026-06-15

---

## Decision: **Major Revision**

---

## General Assessment

This manuscript proposes a "catalyst-stabilized defects" strategy for Li–S battery electrocatalysts, in which atomically dispersed Nb single atoms (SAs) are anchored on vacancy-rich TiO₂(B) nanosheets grown on carbon cloth (Nb/V-T@CC). The central argument is that Nb SAs thermodynamically pin otherwise metastable vacancy clusters, simultaneously preventing structural degradation during cycling and enhancing the local electronic structure for polysulfide catalysis. The experimental evidence is broad, encompassing AC-HAADF-STEM, XAS/EXAFS, EPR, PALS, Raman, DFT calculations, and extensive galvanostatic cycling, and the reported electrochemical performance—an ultra-low capacity decay rate of 0.028% per cycle over 1000 cycles at 2.0 C—is notable.

However, the manuscript cannot be recommended for publication in its current form. Several critical issues must be resolved before the work can be properly evaluated. Most urgently, the synthesis description for the key control sample (HV-T@CC) is contradictory between the main text and the Supporting Information, calling the validity of the entire comparative study into question. Beyond this, the manuscript's novelty is substantially overstated: the core concept of using a guest atom to stabilize host vacancies and break the activity–stability trade-off in Li–S batteries has been reported concurrently and independently (Zhao et al., *Natl. Sci. Rev.* 2025, nwaf375—not cited), and the use of Nb SAs as electrocatalysts for Li–S batteries employing an identical d–p hybridization argument was already established by Zhang et al. (*JACS* 2023). The manuscript is also significantly overlength, with repetitive argumentation, pervasive figure legibility issues, and a headline pouch-cell capacity figure that is inconsistent between the Abstract and the main text. Detailed comments follow below.

---

## Major Comments

**Comment 1 — Critical | Synthesis Protocol Contradiction (HV-T@CC)**

The preparation of the control sample HV-T@CC is described differently in two parts of the manuscript, leading to an irreconcilable contradiction.

- *Main text (p. 3):* "The T@CC and HV-T@CC catalysts were synthesized via a solvothermal method followed by high-temperature calcination in **air** and **argon** atmospheres, respectively." This implies T@CC is calcined in air (→ stoichiometric TiO₂) and HV-T@CC is calcined in Ar (→ high-vacancy TiO₂), with no Nb involved in either.
- *Supporting Information (p. S3):* "The as-prepared T@CC was subsequently immersed in 15.0 mL of a NbCl₅ ethanol solution… annealed at 500 °C… under an **argon** atmosphere to obtain Nb/V-T@CC. The HV-T@CC sample was prepared using the **same procedure**, except that the annealing was carried out under an **air** atmosphere."

If "the same procedure" in the SI includes the NbCl₅ impregnation step, then HV-T@CC would contain Nb but with fewer vacancies—the opposite of what is claimed. In that case, the comparison between Nb/V-T@CC and HV-T@CC would not isolate the effect of Nb single atoms, invalidating the key mechanistic conclusion of the paper. The authors must provide:

1. An unambiguous step-by-step synthesis flowchart for all four samples (T@CC, HV-T@CC, Nb/V-T@CC, CC).
2. Explicit confirmation of whether HV-T@CC contains Nb, supported by ICP-MS or XPS data on HV-T@CC.
3. A corrected and self-consistent experimental section in both the main text and SI.

This is the most critical issue in the manuscript and must be fully resolved before any other comments can be evaluated with confidence.

---

**Comment 2 — Critical | Pouch Cell Capacity Discrepancy**

The headline pouch cell capacity is reported inconsistently:

- *Abstract (and Conclusion, p. 15):* "a flexible pouch cell… achieves a **high total capacity of 1.3 Ah**"
- *Main text (p. 14):* "maintains a stable areal capacity of 7.7 mAh cm⁻², corresponding to a **total capacity of 1.03 Ah** after 30 cycles"

The discrepancy is greater than 26%. If 1.3 Ah refers to the initial discharge capacity before cycling, this must be stated explicitly in both the Abstract and Results sections, with the corresponding cycle number. The current presentation gives the misleading impression that 1.3 Ah is the stabilized capacity after repeated bending. Authors must:

1. Clarify which cycle number corresponds to each reported capacity value.
2. Correct all inconsistent statements in the Abstract, Results, and Conclusion.
3. Show the full pouch-cell capacity vs. cycle-number plot in the main figure (Figure 8g) with clearly labeled initial and post-bending values.

---

**Comment 3 — Critical | Uncited Directly Competing Work**

The authors claim their "catalyst-stabilized defects" strategy is "paradigm-shifting" and positions the work as the first to decouple activity from stability in defect-engineered Li–S electrocatalysts. However, the following recently published paper addresses the **identical scientific problem** through a closely related approach and must be cited and discussed:

> C. Zhao et al., "Intrinsic Stabilization of Vacancies in Catalysts via High-Entropy Approach for Lithium-Sulfur Batteries," *Natl. Sci. Rev.* **2025**, 12, nwaf375. DOI: 10.1093/nsr/nwaf375

This work uses five-metal high-entropy alloying to intrinsically pin oxygen vacancies in a 2D oxide, achieving 0.032% capacity fading per cycle over 2000 cycles at 1C. The conceptual parallel is direct: vacancy stabilization by a guest component → maintained activity + improved structural durability → breaking the activity–stability trade-off in Li–S batteries. The authors must:

1. Add this reference to the Introduction and Discussion.
2. Explicitly compare the "single-atom pinning" approach versus the "high-entropy alloying" approach in terms of mechanism, scalability, and performance.
3. Revise the abstract and conclusion to temper the "paradigm-shifting" language in view of this and other related works.

---

**Comment 4 — Critical | Duplicate and Erroneous References**

Two sets of duplicate/erroneous references were identified:

- **References [45] and [46]** are word-for-word identical: both cite S. Li et al., "Orbital-Tailoring Strategy via Dual-Defect Engineering in P-FeTe₂₋ₓ@NC Synergizes Polysulfide Adsorption-Conversion for Lithium-Sulfur Batteries," *Advanced Materials* 37, (2025): e11910. One of these must correspond to a different source. The in-text citations relying on [45] and [46] must be checked and corrected individually.
- **References [25] and [47]** appear to cite the same paper (J.Q. Liu et al., "Vacancy-Engineered Ceria Enables 4f-Orbital-Driven Redox Catalysis for Bidirectional Sulfur Conversion in Li-S Batteries," *Advanced Materials* 38) but list different publication years (2025 for [25] vs. 2026 for [47]). The correct year must be verified and the duplicate citation resolved.

Authors should conduct a full audit of all 48 references to ensure each citation is unique, correct, and matches the in-text claim.

---

**Comment 5 — Major | Novelty Overlap with Zhang et al., JACS 2023 (Ref. [20])**

The mechanistic narrative in the "Electrocatalytic Kinetics" section—specifically the d–p orbital hybridization between Nb and S 2p states as the origin of enhanced polysulfide binding and conversion—is reproduced almost verbatim from:

> Y. Zhang et al., "d-p Hybridization-Induced 'Trapping–Coupling–Conversion' Enables High-Efficiency Nb Single-Atom Catalysis for Li–S Batteries," *J. Am. Chem. Soc.* **2023**, 145, 1728–1739.

That paper already established that Nb SAs enhance Li–S catalysis through d–p hybridization with S 2p orbitals, accelerating polysulfide trapping and conversion. The present manuscript uses TiO₂(B) as the support instead of N-doped carbon, and adds the vacancy stabilization argument, but the mechanistic interpretation is the same. The authors must:

1. Clearly state, in the Introduction and at the relevant mechanistic discussion point, what new mechanistic insight this work provides **beyond** Zhang et al. 2023.
2. Avoid reusing the same phrasing (e.g., "d-p hybridization," "trapping-coupling-conversion" logic) without explicit attribution.
3. Frame the novelty precisely: it is the synergy of Nb SA *plus* stabilized vacancy clusters in TiO₂(B), not Nb SA catalysis per se, that is new.

---

**Comment 6 — Major | Novelty Overlap with Mao et al., EES 2025 (Ref. [38])**

Reference [38] (Mao et al., *Energy Environ. Sci.* 2025, 18, 8631–8644) reports Nb single atoms on a lithiophilic support (Nb-C₃N₄₋ₓ) for high-efficiency sulfur catalysis in Li–S batteries, demonstrating similar strong Nb–S interactions and dual functionality for both cathode and anode stabilization. This work is cited but not discussed in relation to the novelty of the present manuscript. The authors should provide an explicit comparison of:

1. Why the TiO₂(B) support is superior to C₃N₄₋ₓ for the specific purpose of vacancy stabilization.
2. Whether the vacancy-pinning mechanism is possible on C₃N₄₋ₓ or unique to TiO₂(B).
3. The specific performance advantage of the present system over Mao et al.

---

**Comment 7 — Major | EXAFS Distance Reporting Ambiguity**

The EXAFS fitting (main text p. 4 and Table S1) reports the first-shell Nb–O distance at "~1.52 Å," described as "significantly shorter than the Nb–O distance in Nb₂O₅ (~1.77 Å)." In EXAFS analysis, distances extracted from the magnitude of the Fourier Transform without phase correction are systematically shorter than the true bond length by ~0.3–0.5 Å. It is therefore unclear whether:

- Both 1.52 Å and 1.77 Å are phase-uncorrected R-space values (valid comparison), or
- The 1.77 Å is the crystallographic Nb–O bond length in Nb₂O₅ (phase-corrected), while 1.52 Å is the R-space peak (uncorrected), making the comparison misleading.

The authors must explicitly state in the text and Table S1 whether the reported distances are phase-shift-corrected bond lengths (R + ΔR) or uncorrected R-space peak positions, and ensure all reported distances use the same convention.

---

**Comment 8 — Major | DFT+U Parameter Justification**

The DFT+U calculations employ Hubbard U values of 5.0 eV for Ti and 4.8 eV for Nb. These values are applied without any justification, reference to prior literature benchmarks, or validation against experimental observables (e.g., band gap, lattice parameters). For TiO₂, reported U values in the literature range from 3.5 eV to 7.0 eV, and the choice of U significantly affects computed vacancy formation energies, d-band center positions, and adsorption energies—all of which are central to this manuscript's claims. The authors must:

1. Provide a reference justifying the chosen U values.
2. Ideally, include a benchmark showing that the chosen U reproduces an experimental observable for TiO₂(B) (e.g., band gap, lattice constants, or known vacancy formation energy).
3. Alternatively, present a sensitivity analysis showing that the key conclusions (Eint vs. Esurf ordering, d-band center trend) are robust to ±1 eV variation in U.

---

**Comment 9 — Major | Missing Statistical Rigor in Key Performance Data**

The headline electrochemical performance claims lack adequate statistical support:

- Long-term cycling curves at 1.0 C (Figure 4e) and 2.0 C (Figure 4f) show no error bars, and the number of replicate cells is never stated anywhere in the manuscript.
- High-loading cycling data (Figures 4h, 4i) also lack error bars and replication information.
- The same issue applies to the Li nucleation overpotential values (Figure 5a), which appear to be single-point measurements.

For a manuscript in *Advanced Functional Materials*, a minimum of n = 3 independent cells per condition with mean ± SD is expected for all headline performance metrics. The authors must:

1. Report n (number of replicate cells) for every key electrochemical figure.
2. Add error bars (mean ± SD) to Figures 4e, 4f, 4h, 4i, 5a, and 5b at minimum.
3. Confirm that the claimed 0.028% capacity decay rate is reproducible across replicates.

---

**Comment 10 — Major | PALS Component Assignment Requires Justification**

The PALS analysis assigns τ₂ (~0.41–0.42 ns) to aggregated vacancy clusters and τ₁ (~0.28–0.35 ns) to isolated vacancies. While this assignment is qualitatively consistent with general trends for oxide defects, the manuscript provides no reference to established positron lifetime values for oxygen vacancies (VO) and titanium vacancies (VTi) in TiO₂ or similar oxides. This is critical because:

- The long component τ₃ (3.7–4.9 ns) is generally attributed to positronium formation in large voids or at surfaces. Its fractional intensity (I₃ ≈ 0.1–0.2%) is very small, but its inclusion in the τ_av calculation can still influence the result.
- Without reference lifetime values for TiO₂, the assignment of τ₁ and τ₂ to specific defect types is speculative.

The authors should provide at least two or three literature references reporting positron lifetime values for VO and VTi in TiO₂ or related systems (e.g., anatase, rutile), and confirm that their assigned τ values are consistent with those references.

---

**Comment 11 — Major | Overclaiming Universal Applicability**

The Abstract and Conclusion assert that the "catalyst-stabilized defects" principle provides "a universal thermodynamic blueprint for designing durable catalytic interfaces, which can be extended to oxygen electrocatalysis, CO₂ reduction, and ammonia synthesis across diverse defect-bearing materials." This claim is entirely speculative: no data, calculations, or even literature precedent is offered in the manuscript to support universality beyond the specific TiO₂/Nb/Li–S system studied. Either:

1. Provide at least one piece of preliminary evidence (e.g., one catalytic test in a different system), or
2. Remove the universality claim from the Abstract and Conclusion, and replace it with a more measured statement such as: "The thermodynamic principles demonstrated here may serve as a design guide for defect-engineered electrocatalysts in other electrochemical energy conversion reactions."

---

**Comment 12 — Major | Manuscript Length and Repetition**

The main text (~17 pages) is excessively long and the narrative is repetitive. The same performance advantages of Nb/V-T@CC—superior capacity, lower polarization, higher Li⁺ diffusivity, better structural stability—are re-stated in the Characterization, Electrochemical Evaluations, Electrocatalytic Kinetics, and Full Cell sections with only minor variation. This makes the paper difficult to follow and obscures the core message.

The authors are strongly encouraged to:

1. Reduce the main text to approximately 12–13 pages by consolidating redundant performance statements.
2. Move detailed kinetic analyses (CV contour maps, GITT details, DRT deconvolution) to the SI, retaining only the key results and figures in the main text.
3. Restructure the Results section so that each subsection delivers one new finding and does not recap previous findings.

---

## Minor Comments

**Comment 13 — Moderate | Randles–Ševčík Equation Applicability**

The Li⁺ diffusion coefficients (DLi⁺) are extracted from CV data using the Randles–Ševčík equation (SI p. S6), which assumes semi-infinite planar diffusion. This model is not strictly valid for a porous 3D carbon cloth electrode with complex tortuosity. The diffusion coefficients derived from GITT (Figure 7g) should be presented as the primary quantitative metric, with the CV-derived values treated as semi-quantitative trends. This limitation should be explicitly acknowledged in the text or SI.

---

**Comment 14 — Moderate | Vacancy Formation Energy Calculation and Reference State**

The DFT-calculated vacancy formation energies (Evac) shown in Figure S13 for different vacancy cluster configurations (VOVOVO, VOVOVO, VO-VO-VO, VOVOVTi) range from 10.69 to 15.63 eV. These are unusually high values even for multi-vacancy clusters. The authors should:

1. Specify the chemical potential reference state used for the O (and Ti) atoms removed in the vacancy formation calculation (e.g., ½ O₂ molecule, bulk TiO₂, or a specific gas-phase reference).
2. Clarify whether the reported Evac values are the total formation energy of the entire cluster or a per-vacancy value.
3. Confirm that the VOVOVTi cluster is the most stable configuration under both oxidizing and reducing conditions (not just a single reference point).

---

**Comment 15 — Moderate | EPR Assignment of VTi Signal**

The EPR resonance at g ≈ 1.992 in HV-T@CC is "tentatively attributed to titanium vacancies (VTi)." This assignment is stated without a literature reference. EPR signals in this g-range in TiO₂ can arise from Ti³⁺ ions (reduced titanium centers), paramagnetic defect complexes, or surface-trapped electrons—not necessarily cation vacancies per se. The authors should:

1. Provide a specific literature reference supporting the g ≈ 1.992 assignment to VTi.
2. If the assignment is truly tentative, revise the language accordingly and avoid drawing mechanistic conclusions that depend specifically on the presence of VTi.

---

**Comment 16 — Moderate | Gibbs Free Energy Pathway Incompleteness**

The calculated ΔG profiles for the sulfur reduction reaction (SRR) in Figure 6g show the pathway Li₂S₆ → Li₂S₄ → Li₂S₂ → Li₂S. The well-established SRR mechanism in Li–S batteries includes higher-order polysulfides (S₈, Li₂S₈) and involves both liquid-phase and solid-phase intermediates with distinct dissolution/precipitation steps. By starting from Li₂S₆ and omitting the Li₂S₈ → Li₂S₆ step and the liquid-to-solid phase transition, the model may underestimate the actual kinetic barriers. The authors should either:

1. Extend the free energy diagram to include Li₂S₈ as the starting species and explicitly note any liquid–solid transitions, or
2. Clearly state in the text why the pathway is truncated at Li₂S₆ and what assumptions this entails.

---

**Comment 17 — Moderate | Nb Loading Not Optimized**

The Nb loading of 0.615 wt% (as determined by ICP-MS) is presented as a given without any loading optimization. It is unclear whether this loading is optimal, near-optimal, or simply the value obtained from the specific synthesis conditions used. Without an optimization curve (or at least a comparison with different loadings), the reader cannot determine whether the performance enhancement is maximized or whether higher/lower Nb loadings would perform comparably or better. A brief loading optimization or a comment justifying the chosen loading is needed.

---

**Comment 18 — Moderate | Li Anode Stabilization Mechanism Underdeveloped**

Section "Li Metal Anode Stabilization" (Figure 7a–c, Figure 5) presents DFT calculations of Li binding energies and diffusion barriers on Nb/V-T, alongside electrochemical lithium plating data. However, the mechanistic connection between the Nb/V-T catalyst (designed for polysulfide conversion on the cathode side) and its effect on Li metal deposition on the anode side is not clearly established. Specifically:

- The Nb/V-T@CC/Li anode is fabricated by electrochemical plating of Li into a Nb/V-T@CC substrate — the Nb/V-T surface is acting as a lithiophilic host, not as a polysulfide catalyst.
- The same DFT surfaces used to model polysulfide catalysis are used to model Li deposition, but these surfaces may not accurately represent the Li-plated interface.

The authors should more carefully distinguish these two functional roles and explain how the material's properties in the fully Li-plated state (Nb/V-T@CC/Li) relate to its catalytic properties in the sulfur-loaded state (Nb/V-T@CC/S).

---

**Comment 19 — Minor | Sentence Structure and Emphatic Language**

The manuscript overuses emphatic adverbs and adjectives, weakening their rhetorical impact and giving the text an exaggerated tone. The following terms appear an excessive number of times:

| Term | Approximate Count |
|---|---|
| "Notably" | ≥ 10 |
| "Remarkably" | ≥ 6 |
| "Unambiguously" | ≥ 6 |
| "Critically" | ≥ 4 |
| "Strikingly" | ≥ 3 |
| "Paradigm-shifting" | 2 |

Each of these terms should be reserved for the single most impactful finding in the paper. All other instances should be deleted or replaced with neutral connective phrases ("In addition," "Furthermore," "Consistently,"). The term "paradigm-shifting" is particularly problematic given the substantial prior art (see Comments 3, 5, 6) and should be removed from the manuscript entirely.

---

**Comment 20 — Minor | Article Grammar in Abstract**

The Abstract contains the phrase "under **a** ultrahigh sulfur loading." Since "ultrahigh" begins with a vowel sound, the article should be "**an**." Please correct: "under **an** ultrahigh sulfur loading of 11.20 mg cm⁻²."

---

**Comment 21 — Minor | Pouch Cell Rate Description**

The pouch cell GCD measurement is described as performed "at 0.05 C" (Figure 8f). For a practical pouch cell demonstration intended to show commercial viability, 0.05 C is an extremely low current rate. The authors should acknowledge this limitation and, if possible, include at least one measurement at 0.1 C or 0.2 C to demonstrate that practical operation is feasible.

---

**Comment 22 — Minor | Self-Citation Context**

Reference [14] is a prior paper from the corresponding author's group (Zhen et al., *Adv. Sci.* 2024) using N-doped TiO₂(B)/MXene for Li–S batteries — essentially the same TiO₂(B) scaffold as in the current manuscript. This prior work is cited only once, briefly, without discussion of how the present work advances beyond it. The authors should explicitly state the incremental advance relative to their own prior publication.

---

## Figure-Specific Comments

**Figure Comment F1 — All Figures | Font Size [Major]**

Font sizes in axis labels, tick labels, legend text, and inset annotations are too small to be legible at journal column width. At the typical AFM double-column figure width of ~17.8 cm, all text elements in the current figures reduce to approximately 5–6 pt, which is below the minimum legible threshold (~8 pt). This is a pervasive problem affecting every main-text figure and must be corrected before resubmission. All figures must be re-exported with a minimum font size of 8 pt at the intended final print dimensions, at ≥ 300 dpi.

---

**Figure Comment F2 — Figure 1e, 1f | Single-Atom Verification [Major]**

The AC-HAADF-STEM images in Figures 1e and 1f show bright dots attributed to individual Nb atoms. However, no quantitative intensity analysis is provided to support this assignment. Given the very low Nb loading (0.615 wt%), a confusion of bright spots originating from surface contamination, local TiO₂ thickness variation, or crystallographic artifacts cannot be excluded. The following additions are required:

1. **Intensity line profiles** across at least 5 representative bright dots, demonstrating Z-contrast consistent with Nb (Z = 41) relative to the Ti (Z = 22) background.
2. **A statistical inter-dot spacing analysis** confirming that the bright dots are randomly distributed (as expected for SAC) rather than periodically arranged (which would indicate ordered nanostructures).
3. **A wider field-of-view image** (≥ 20 × 20 nm²) to show the overall distribution of Nb atoms across the TiO₂ surface.

---

**Figure Comment F3 — Figure 3a, 3b | DFT Visualization Thresholds [Moderate]**

The ELF (electron localization function) maps in Figure 3a and the charge density difference plots in Figure 3b are shown without specifying the isosurface threshold values. Small changes in the isosurface level can produce substantially different visual impressions of electron localization or charge transfer. The Bader charge threshold used to define "charge accumulation" (yellow) vs. "charge depletion" (blue) isosurfaces must be reported in the figure caption or SI.

---

**Figure Comment F4 — Figure 4f | Capacity Decay Rate Calculation [Moderate]**

The headline claim of 0.028% capacity decay per cycle is stated in the text but the calculation is never shown. From the Data Reporting Checklist (submitted with the manuscript), the initial capacity at 2.0 C appears to be ~1008 mAh g⁻¹, and the capacity after 1000 cycles is reported as 720 mAh g⁻¹. The implied decay rate is:

**(1008 − 720) / (1008 × 1000) × 100% = 0.0286% per cycle**

The initial capacity at 2.0 C and the calculation formula should be explicitly labeled on Figure 4f and stated in the text. Additionally, the initial capacity at 2.0 C should be labeled on the y-axis of Figure 4f, as it is currently unlabeled.

---

**Figure Comment F5 — Figure 4g | Radar Chart Transparency [Major]**

The radar chart compares the Nb/V-T@CC/S cathode against "previously reported cathodes" across multiple performance metrics, but none of the comparison data points are identified by reference number, author, or testing conditions. Radar charts without traceable data are scientifically uninformative and may mislead readers. The authors should:

1. Replace Figure 4g with a comparison **scatter plot** or **bar chart** where each data point is labeled with its reference number and tested under explicitly noted conditions (current rate, sulfur loading, E/S ratio, cycle number).
2. Alternatively, if the radar chart format is retained, add a companion table (which may go in the SI) listing each comparison reference with its DOI, specific testing conditions, and values for each metric on the radar chart.

---

**Figure Comment F6 — Figure 6g | SRR Free Energy Pathway [Moderate]**

The Gibbs free energy profile in Figure 6g covers the reaction Li₂S₆ → Li₂S₄ → Li₂S₂ → Li₂S, but does not include the first step from dissolved S₈ or Li₂S₈ to Li₂S₆, which involves a liquid-to-liquid phase transition. Omitting this step may make the calculated barriers appear more favorable than they are in reality. The caption should explicitly state that the pathway is calculated starting from Li₂S₆ (rather than S₈ or Li₂S₈) and justify this choice (e.g., Li₂S₆ is taken as the dominant soluble polysulfide species under the experimental electrolyte conditions). The RDS identification (Li₂S₂ → Li₂S) should also include a statement about whether the solid-phase nucleation energy is included in the barrier.

---

**Figure Comment F7 — Figure 8 | Sub-panel Label Order [Minor]**

The Figure 8 caption lists "(a) Rate capability at various current rates, and (b) GCD profiles of Nb/V-T@CC/S||Nb/V-T@CC/Li coin cells," but in most Li–S battery papers and as is standard practice, GCD profiles are presented before rate capability plots. Please verify whether the sub-panel order in the figure itself matches the caption description, and correct if necessary.

---

**Figure Comment F8 — Figure S1 | EPR VTi Assignment [Minor]**

The EPR signal at g ≈ 1.992 in HV-T@CC is "tentatively attributed to titanium vacancies (VTi)." No reference is provided for this assignment. EPR signals at g < 2.000 in TiO₂ are commonly assigned to Ti³⁺ centers (reduced Ti) rather than to VTi per se. A reference supporting the specific VTi assignment at this g-value should be added, or the assignment should be revised to the more commonly accepted Ti³⁺ interpretation.

---

## Summary of Required Actions

| # | Priority | Action Required |
|---|---|---|
| C1 | **Critical** | Resolve HV-T@CC synthesis contradiction; provide ICP-MS/XPS to confirm Nb absence |
| C2 | **Critical** | Correct pouch cell capacity inconsistency (Abstract 1.3 Ah vs. text 1.03 Ah) |
| C3 | **Critical** | Cite and discuss Zhao et al., *Natl. Sci. Rev.* 2025 (nwaf375); revise novelty framing |
| C4 | **Critical** | Fix duplicate references [45]=[46] and [25] vs. [47]; full reference audit |
| C5 | **Major** | Differentiate d-p hybridization narrative from Zhang et al., *JACS* 2023 |
| C6 | **Major** | Explicitly compare performance and mechanism with Mao et al., *EES* 2025 |
| C7 | **Major** | Clarify EXAFS R-space vs. corrected bond distance reporting |
| C8 | **Major** | Justify DFT+U values (UTi = 5.0 eV, UNb = 4.8 eV) with benchmark or reference |
| C9 | **Major** | Add n ≥ 3 replication and error bars to all key performance figures |
| C10 | **Major** | Provide literature-referenced PALS lifetime values for VO and VTi in TiO₂ |
| C11 | **Major** | Remove or support with data the "universal applicability" claim |
| C12 | **Major** | Shorten manuscript by ~20–25%; eliminate repetitive performance restatements |
| C13 | Moderate | Acknowledge Randles–Ševčík limitation for porous 3D electrodes |
| C14 | Moderate | Specify vacancy formation energy reference state and per-defect vs. total energy |
| C15 | Moderate | Provide reference for VTi EPR assignment at g ≈ 1.992 |
| C16 | Moderate | Extend ΔG pathway to include Li₂S₈ or explicitly justify truncation at Li₂S₆ |
| C17 | Moderate | Provide Nb loading optimization or justify the 0.615 wt% choice |
| C18 | Moderate | Clarify distinction between cathode-side catalytic role and anode-side lithiophilic role |
| C19 | Minor | Remove/reduce "Notably," "Remarkably," "Unambiguously," "paradigm-shifting" |
| C20 | Minor | Correct "a ultrahigh" → "an ultrahigh" in Abstract |
| C21 | Minor | Comment on the limitation of demonstrating the pouch cell only at 0.05 C |
| C22 | Minor | Discuss incremental advance relative to the same group's prior work (Ref. [14]) |
| F1 | **Major** | Increase all figure font sizes to ≥ 8 pt at final print dimensions |
| F2 | **Major** | Add HAADF-STEM intensity line profiles and spatial statistics for Nb atom assignment |
| F3 | Moderate | Report isosurface thresholds for ELF and charge density difference plots |
| F4 | Moderate | Label initial capacity on Figure 4f and show the 0.028% calculation explicitly |
| F5 | **Major** | Replace or fully annotate radar chart (Figure 4g) with traceable benchmark data |
| F6 | Moderate | Clarify SRR ΔG starting species and solid-phase nucleation assumptions |
| F7 | Minor | Verify and correct sub-panel label order in Figure 8 caption |
| F8 | Minor | Add reference for VTi EPR assignment in Figure S1 caption |

---

## Overall Ratings

| Criterion | Rating |
|---|---|
| Originality | Moderate |
| Creativity | Moderate–High |
| Data Quality | Moderate (pending resolution of C1–C4) |
| Writing Quality | Moderate (verbose; revision required) |
| Figure Quality | Needs Revision (font size; F2, F5 critical) |
| Reproducibility | Needs Revision (C1, C8, C9) |

---

## Closing Remarks

The reviewer recognizes the considerable experimental effort invested in this study and acknowledges that the thermodynamic "vacancy-pinning" argument, supported by DFT and PALS, is the manuscript's most intellectually distinctive contribution. The practical demonstration using a binder-free, CC-based freestanding cathode architecture also adds engineering value.

Nevertheless, the manuscript requires substantial revision before it merits publication in *Advanced Functional Materials*. The synthesis ambiguity (Comment 1) is the most pressing issue and must be fully resolved, as it determines whether the experimental comparisons are internally valid. The omission of a closely related paper (Zhao et al., *Natl. Sci. Rev.* 2025) and the overstated novelty relative to Zhang et al. (*JACS* 2023) and Mao et al. (*EES* 2025) must also be addressed with intellectual honesty. A focused, shorter manuscript that clearly articulates what is genuinely new—particularly the PALS-based quantification of vacancy cluster evolution and the thermodynamic inversion of the migration driving force—would represent a much stronger submission.

---

## Key References for Author Consideration

1. Y. Zhang et al., *J. Am. Chem. Soc.* **2023**, 145, 1728–1739. DOI: 10.1021/jacs.2c10345
2. X. Zhou et al., *Nano-Micro Lett.* **2025**. DOI: 10.1007/s40820-025-01806-0
3. C. Zhao et al., *Natl. Sci. Rev.* **2025**, 12, nwaf375. DOI: 10.1093/nsr/nwaf375
4. Y. Mao et al., *Energy Environ. Sci.* **2025**, 18, 8631–8644. DOI: 10.1039/d5ee02048d
5. M.M. Zhen et al. (same group), *Adv. Sci.* **2024**, 11, 2406475.
