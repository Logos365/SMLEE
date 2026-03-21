# PEER REVIEW REPORT

**Manuscript Title:** Atomic-Layer-Deposited ZnF₂ on Aluminum Enabling *in situ* NaZn₁₃/NaF Interphase for Robust Anode-Free Sodium Batteries

**Authors:** Viet Phuong Nguyen, Angelina Sarapulova, Michael Günthel, Markus Knäbbeler-Buß, Changin Kim, Young-Woon Byeon, Moonwon Lee, Kanghoon Yim, Eric Tröster, Sonia Dsoke, Seung-Mo Lee

**Version:** Ver_6_20260319

**Review Date:** 2026-03-20

**Reviewer:** Internal peer review (AI-assisted)

---

## MANUSCRIPT OVERVIEW

| Field | Details |
|-------|---------|
| **Title** | Atomic-Layer-Deposited ZnF₂ on Aluminum Enabling *in situ* NaZn₁₃/NaF Interphase for Robust Anode-Free Sodium Batteries |
| **Authors** | V. P. Nguyen et al. (11 authors) |
| **Affiliations** | KIMM (Korea), Fraunhofer ISE (Germany), FMF Freiburg (Germany), KIST (Korea), KIER (Korea), CNU (Korea), Albert-Ludwigs Universität Freiburg (Germany), UST (Korea) |
| **Keywords** | anode-free sodium battery, sodiophilic, NaF-rich SEI, cycling stability, dendrite |
| **Core Claim** | ALD-deposited ZnF₂ on Al is converted *in situ* to a NaZn₁₃/NaF interphase that enables ~99.7% CE, >1000 h symmetric cell life, and 323 Wh kg⁻¹ in anode-free Na‖NVP full cells |

---

## SECTION 1 — FATAL ERROR PRE-SCREENING

| # | Category | Fatal Error Description | Location |
|---|----------|------------------------|----------|
| **F-1** | **Data Inconsistency** | NVP cathode mass loading is stated as **11.5 mg cm⁻²** in the Abstract, **13.2 mg cm⁻²** in the lean-Na full-cell section (Para [70]), and **11.6–12.2 mg cm⁻²** in the anode-free section (Para [72]). Three different values appear without explanation. | Abstract vs. Para [70] vs. Para [72] |
| **F-2** | **Typographical / Scientific Term Error** | "**annual** dark field scanning transmission electron microscopy (ADF-STEM)" — "annual" must be "**annular**". ADF stands for Annular Dark Field, not Annual Dark Field. This is a fundamental microscopy terminology error. | Para [54] / Figure 3 caption |
| **F-3** | **Grammatical Fatal Error — Sentence Fragment** | "Although modifying Al with sodiophilic components (Au, Ag, Zn, Sn, etc.) can lower the nucleation barrier.**¹⁰⁻¹³** the resulting SEI often remains fragile..." — The subordinate clause introduced by "Although" is terminated with a period before its main clause, creating a sentence fragment. | Para [33], Introduction |
| **F-4** | **Affiliation Spelling Error** | "Emmy-**Nother**-Straße" should be "Emmy-**Noether**-Straße" (named after mathematician Emmy Noether). | Affiliation [g] |

---

## SECTION 2 — DETAILED PEER REVIEW

### 2.1 Originality

**Strengths:**
- The use of ALD to deposit ZnF₂ on Al with atomic-scale precision, followed by deliberate *in situ* conversion to a NaZn₁₃/NaF dual interphase, is a genuinely novel approach in the AFSB field.
- The work correctly positions itself against prior slurry-cast MFₓ@Al studies (Wang et al., Ref. 23), clearly articulating the gap filled by ALD precision and the specific NaZn₁₃ phase.
- The claim of being the "first example of an ALD-derived ZnF₂ coating on Al...deliberately converted into a NaZn₁₃/NaF interphase for AFSBs" appears well-supported by the literature survey.

**Areas Requiring Improvement:**
- The Introduction does not discuss existing ALD-based coating strategies for *lithium* batteries to contextualize why ALD has not previously been applied in this Na context. A brief paragraph on precedents from Li-metal batteries would strengthen the novelty argument.
- The N/P ratio of ~0.33 used in the lean-Na full-cell (Para [70]) is extremely low. The practical significance of operating at such lean conditions should be discussed more explicitly.

---

### 2.2 Creativity

**Strengths:**
- The selection of ZnF₂ is logically motivated: Zn provides sodiophilicity via NaZn₁₃ alloying, and F provides NaF-rich SEI formation. The dual-function design is creative and well-rationalized.
- DFT calculations of Na adsorption energy on NaZn₁₃ (100) and ZnF₂ (110) surfaces (Figure 1B, 1C) provide quantitative design guidance.
- The use of cryo-STEM/EELS for cross-sectional analysis of the interphase (Figure 3D, 3E) is methodologically sound and provides direct structural evidence.

**Areas Requiring Improvement:**
- The layered structure described in Para [55] (NaZn₁₃ at top/electrolyte side, unreacted ZnF₂ at bottom/Al side) implies that NaZn₁₃ forms preferentially at the electrolyte interface. A mechanistic explanation of why NaZn₁₃ segregates to the outer layer while unreacted ZnF₂ persists near Al would strengthen the mechanistic narrative.
- The paper does not discuss the long-term fate of the NaZn₁₃ phase during repeated cycling. After the initial conversion, does the NaZn₁₃ alloy remain stable, or does it gradually dissolve/transform?

---

### 2.3 Data Objectivity

**Strengths:**
- Key metrics (CE, nucleation overpotential, symmetric cell lifetime) are supported by reproducible electrochemical data.
- Cryo-STEM, EELS, and XPS depth profiling provide multi-technique evidence for the proposed interphase composition.

**Areas Requiring Improvement:**
- The headline CE of ~99.7% (Abstract, Para [65]) is claimed at 0.5 mA cm⁻², 1 mAh cm⁻². No error bars or standard deviations are reported for CE values across multiple cells. At least n ≥ 3 cells should be tested and mean ± SD reported.
- The energy density of 323 Wh kg⁻¹ (Para [72]) is calculated "based on the total mass of active materials." It is unclear whether this refers only to the NVP cathode or to both electrodes. In a true anode-free cell, there is no anode active material initially; if the calculation is based on cathode mass only, this must be stated explicitly.
- The XPS interpretation in Para [57] — "one [Na 1s component] associated with metallic Na⁰ in the NaZn₁₃ alloy" — requires more careful justification. In NaZn₁₃, Na donates electron density to the Zn-Zn framework, so its binding energy would differ from purely metallic Na. Reference spectra or literature binding energy values for Na in NaZn₁₃ should be provided.
- The ADF-STEM image disclaimer in Para [54] ("the image contrast arises from a mixture of diffraction and mass-thickness scattering rather than Z-contrast") is important but is buried in the text. This caveat should appear in the figure caption as well, so readers examining the figure alone are not misled.

---

### 2.4 English Language Quality

| # | Location | Original Text | Issue | Suggested Correction |
|---|----------|--------------|-------|----------------------|
| E-1 | Abstract, Para [28] | "delivers a high Coulombic efficiency of ~99.7% **by a** depositing/stripping capacity of 1 mAh cm⁻²" | Wrong preposition; "by a capacity" is non-standard | "...at a depositing/stripping capacity of 1 mAh cm⁻²" |
| E-2 | Para [33], Intro | "Although modifying Al...can lower the nucleation barrier.**¹⁰⁻¹³** **t**he resulting SEI often remains fragile" | Sentence fragment: "Although" clause terminated with period before main clause | Change period after reference numbers to a comma: "...nucleation barrier,¹⁰⁻¹³ the resulting SEI often remains fragile." |
| E-3 | Para [35], Intro | "BiF₃-derived interphases **-** forming Na₃Bi and NaF in situ **-** as particularly effective" | Regular hyphens used as em-dashes | Replace with em-dashes: "BiF₃-derived interphases — forming Na₃Bi and NaF *in situ* — as particularly effective" |
| E-4 | Para [54], Results | "cross-sectional **annual** dark field scanning transmission electron microscopy (ADF-STEM)" | Critical typo: "annual" → "annular" | "cross-sectional **annular** dark field scanning transmission electron microscopy (ADF-STEM)" |
| E-5 | Para [61], Results | "amplified by '**the tip effect**'" | Unnecessary scare quotes around a standard technical term | Remove quotes: "amplified by the tip effect" |
| E-6 | Para [67], Results | "making ZnF₂/Al a robust current-collector platform for both **anode-less** and **anode-free** sodium battery systems" | Two terms used without definition to refer to subtly different configurations; may confuse readers | Define both terms at first use or consolidate: "...for both lean-Na (anode-lean) and truly anode-free sodium battery systems" |
| E-7 | Affiliation [g] | "Emmy-**Nother**-Straße" | Misspelling of Emmy Noether's name | "Emmy-**Noether**-Straße" |
| E-8 | Para [62], Results | "The finely dispersed NaZn₁₃ and **residual ZnF₂** likely acted as sodiophilic nucleation sites" | The role of residual (unreacted) ZnF₂ as a sodiophilic site is not well-justified; ZnF₂ itself may not be sodiophilic after only partial conversion | Revise to clarify: state whether residual ZnF₂ acts as sodiophilic or merely structural. The claim in Fig. 1C shows ZnF₂ has high negative adsorption energy, so it should be sodiophilic — but the sentence needs to clearly distinguish ZnF₂ from NaZn₁₃ in their respective roles. |
| E-9 | Para [28], Abstract | "The NaZn₁₃ alloy **is expected to** enhance sodiophilicity...while the NaF component **strengthens** the solid-electrolyte interphase, **ensuring** the Na⁺ flux" | Inconsistent modal hedging: hedged claim ("is expected to") followed by unhedged claims ("strengthens," "ensuring") for equivalent levels of evidence | Use consistent modal language throughout; if DFT + experimental data support the claims, use stronger declarative language uniformly |
| E-10 | Para [50], Results | "cells were first discharged to 0.01 V vs. Na⁺/Na and then **cycled five times between 0.01 and 1.0 V vs. Na⁺/Na** to stabilize the SEI" | The upper cutoff of 1.0 V for SEI stabilization is unusually wide. Typical Na-metal half-cell conditioning uses narrower windows. Should clarify the rationale. | Add a brief justification for the 1.0 V upper cutoff in the experimental section. |

---

### 2.5 Figure and Data Issues

| # | Figure | Severity | Issue Description |
|---|--------|----------|-------------------|
| FIG-1 | **Abstract / Para [70] / Para [72]** | **Critical** | NVP mass loading discrepancy: Abstract = 11.5 mg cm⁻², lean-Na = 13.2 mg cm⁻², AFSB = 11.6–12.2 mg cm⁻². These must be reconciled. If different batches were used, state so explicitly. |
| FIG-2 | **Figure 3D / Para [54]** | **Critical** | "annual dark field" → "annular dark field." Fundamental microscopy terminology error affecting the scientific credibility of characterization description. |
| FIG-3 | **Figure 3D, caption** | **Major** | The ADF-STEM contrast disclaimer (diffraction + mass-thickness, not Z-contrast) appears only in the main text (Para [54]) but not in the figure caption. Readers viewing the figure independently will misinterpret the image contrast as compositional (Z-contrast). |
| FIG-4 | **Figure 5A / Para [65]** | **Major** | CE of ~99.7% is reported as a single representative value with no error bars or statistical information across multiple cells (n = ?). Battery CE measurements are notoriously variable between cells. At least n ≥ 3 should be tested and mean ± SD reported. |
| FIG-5 | **Figure 6E / Para [72]** | **Major** | Energy density of 323 Wh kg⁻¹ — calculation basis ("total mass of active materials") is ambiguous. For anode-free cells, clarify whether cathode mass only or cathode + anticipated plated Na mass was used. Inconsistency with NVP mass loading values (FIG-1) further complicates verification. |
| FIG-6 | **Figure 3H, 3I / Para [57]** | **Moderate** | Na 1s XPS peak assigned to "metallic Na⁰ in NaZn₁₃ alloy" without reference binding energy values for Na in NaZn₁₃ from the literature. Na in an intermetallic compound would have a shifted binding energy that needs to be quantified and compared to standards. |
| FIG-7 | **Figure 4A / Para [60]** | **Moderate** | "Na‖ZnF₂/Al cell shows smooth stripping profiles" — present tense ("shows") used inconsistently within a predominantly past-tense narrative. Standardize tense throughout Results. |
| FIG-8 | **Figure S9 / Para [61–62]** | **Minor** | Na layer thickness on bare Al "exceeded ~26 µm" vs. ZnF₂/Al "only ~23.6 µm." The difference of ~10% in thickness may not be statistically significant. SEM cross-section measurements typically have ≥5–10% uncertainty. Consider reporting mean ± SD from multiple cross-sections. |

---

### 2.6 Figures Requiring Revision

#### Figure 3D — Cross-Sectional ADF-STEM Image

**Current State:** The figure caption (and main text, Para [54]) describes the image as "cross-sectional annual [sic] dark field scanning transmission electron microscopy (ADF-STEM)." The main text notes that the image was acquired under low-angle collection conditions, resulting in mixed diffraction + mass-thickness contrast rather than pure Z-contrast. This disclaimer is absent from the figure caption.

**Required Actions:**
1. Correct "annual" to "annular" in both the caption and all text references.
2. Add the following statement directly to the figure caption: "Note: image acquired under low-angle ADF collection conditions; contrast reflects diffraction and mass-thickness contributions rather than Z-contrast alone."
3. Consider acquiring a conventional HAADF-STEM image at the same location for direct comparison to unambiguously show Z-contrast-based compositional distribution.

---

#### Figure 6 (Full-Cell Performance) — Mass Loading and Energy Density Inconsistency

**Current State:** Three different NVP mass loading values appear across the manuscript (11.5, 13.2, 11.6–12.2 mg cm⁻²). The energy density of 323 Wh kg⁻¹ (Figure 6E) is claimed to be based on "total mass of active materials," but this is not clearly defined. The literature comparison in Figure 6E may therefore be misleading if other works use different calculation bases.

**Required Actions:**
1. Reconcile all NVP mass loading values. If different cathode batches were used in different experiments, clearly state the mass loading for each specific experiment in both the figure caption and the main text.
2. Provide the explicit formula used to calculate energy density (numerator = integrated discharge energy in Wh, denominator = mass in kg of what materials?).
3. In Figure 6E, add a footnote specifying the calculation basis for all compared works, or restrict comparison to works using the same basis.

---

#### Figure 5A — Coulombic Efficiency Statistics

**Current State:** CE of ~99.7% at 0.5 mA cm⁻² is reported for ZnF₂/Al, averaged over 150 cycles. No information is given about the number of cells tested (n), variability between cells, or mean ± SD.

**Required Actions:**
1. Perform CE measurement on n ≥ 3 independent cells.
2. Report mean CE ± SD in the figure, the main text, and the abstract.
3. If only one cell was tested, add a clear statement acknowledging this limitation.

---

## SECTION 3 — OVERALL ASSESSMENT

| Criterion | Rating | Key Comment |
|-----------|--------|-------------|
| **Originality** | ★★★★☆ Moderate-High | First ALD-ZnF₂/NaZn₁₃/NaF interphase for AFSBs; well-differentiated from prior slurry-cast approaches |
| **Creativity** | ★★★★☆ Moderate-High | Clever dual-function design (sodiophilic + SEI); cryo-STEM/EELS mechanistic evidence is strong |
| **Data Objectivity** | ★★★☆☆ Moderate | Mass loading inconsistency (critical), missing CE statistics, ambiguous energy density calculation basis weaken otherwise solid dataset |
| **English Language** | ★★★☆☆ Moderate | Several grammatical errors and one critical typo ("annual" → "annular"); overall readable but needs careful proofreading |
| **Figure Quality** | ★★★☆☆ Moderate | ADF-STEM contrast caveat missing from caption; mass loading/energy density inconsistencies in Fig. 6 |
| **Scientific Rigor** | ★★★★☆ Moderate-High | Mechanistic claims are generally well-supported by multi-technique evidence; Na 1s XPS assignment needs additional justification |

---

## SECTION 4 — RECOMMENDATION

> **MAJOR REVISION REQUIRED**

### Mandatory Revisions (must be addressed before re-submission):

- [ ] **[Critical]** Reconcile NVP mass loading values across Abstract, lean-Na section, and AFSB section (three different values given: 11.5, 13.2, 11.6–12.2 mg cm⁻²).
- [ ] **[Critical]** Correct "annual dark field" → "annular dark field" in all occurrences (Para [54] and Figure 3 caption).
- [ ] **[Critical]** Fix the sentence fragment in Para [33]: change the period after the citation superscript "¹⁰⁻¹³" to a comma so "Although...can lower the nucleation barrier, the resulting SEI often remains fragile."
- [ ] **[Major]** Report CE data as mean ± SD from n ≥ 3 independent cells; add error bars to Figure 5A.
- [ ] **[Major]** Add ADF-STEM contrast disclaimer to Figure 3D caption.
- [ ] **[Major]** Clarify the energy density calculation basis for the 323 Wh kg⁻¹ claim and ensure consistent comparison with literature in Figure 6E.
- [ ] **[Moderate]** Provide Na 1s XPS reference binding energy for Na in NaZn₁₃ (literature or standard) to justify the metallic Na⁰ assignment.
- [ ] **[Moderate]** Correct affiliation spelling: "Emmy-Nother-Straße" → "Emmy-Noether-Straße".
- [ ] **[Minor]** Replace hyphens with em-dashes in Para [35]: "BiF₃-derived interphases — forming Na₃Bi and NaF *in situ* —".
- [ ] **[Minor]** Change "by a depositing/stripping capacity" → "at a depositing/stripping capacity" in the Abstract.
- [ ] **[Minor]** Remove scare quotes around "the tip effect" in Para [61].
- [ ] **[Minor]** Define "anode-less" vs. "anode-free" at first use in Para [67] or unify terminology.

---

## CLOSING NOTE

This manuscript reports scientifically interesting and timely work on ALD-engineered interphases for anode-free sodium batteries. The core concept — using ALD-ZnF₂ to generate a dual NaZn₁₃/NaF interphase — is creative and well-motivated, and the multi-technique characterization (cryo-STEM/EELS, XPS depth profiling, DFT) provides compelling mechanistic evidence. However, several issues must be resolved before publication: the mass loading inconsistency undermines the reproducibility of the full-cell data, the critical "annual/annular" typo damages scientific credibility, and the CE statistics are insufficient for a headline claim. Addressing the mandatory revisions listed above will substantially strengthen the manuscript and bring it to publication readiness.

---

*Report prepared: 2026-03-20 | Reviewer: AI-assisted internal peer review*
