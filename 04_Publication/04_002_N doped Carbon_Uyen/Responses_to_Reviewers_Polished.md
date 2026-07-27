# Responses to the Comments of the Reviewers

**Journal:** Applied Surface Science  
**Manuscript title:** Role of Pyridinic Nitrogen in Redox Activity of Nitrogen-Doped Carbon Fabrics  
**Date:** 2026-06-22

---

> **Formatting note:** All newly added or modified text is indicated by **pink highlight** in the revised manuscript. Each response below follows the format: *Reviewer Comment → Author Response → Manuscript Changes*.

---

## Responses to the Comments of Reviewer 1

**General Response:**

We sincerely thank Reviewer 1 for the thorough and constructive evaluation of our manuscript. The comments have been highly valuable in strengthening the rigor and clarity of our work. We have carefully addressed each point, and the corresponding revisions are described below. All added or modified text is highlighted in pink in the revised manuscript.

---

*Reviewer 1 Summary:*

> This work reports a g-C₃N₄-assisted solid-state strategy for fabricating nitrogen-doped carbon fabrics with tunable nitrogen configurations. The topic aligns well with the journal's scope. The experimental design is generally sound, and the combination of experimental characterization with DFT calculations strengthens the mechanistic insight. However, several critical issues regarding nitrogen speciation accuracy, performance benchmarking, and practical applicability need to be addressed. The manuscript presents a valuable and timely study, but requires additional experiments and clarifications to fully support its conclusions before publication.

---

### C1. XPS Overlap between Residual g-C₃N₄ and Pyridinic-N

**Comment:**
> The overlap between residual g-C₃N₄ C=N–C (~398.1 eV) and pyridinic-N (~398.3–398.8 eV) in XPS makes it difficult to accurately quantify lattice-incorporated pyridinic nitrogen, especially in NCF-600 and NCF-700. Please explain.

**Response:**

We thank the reviewer for this important observation. We fully acknowledge that the close proximity of the N 1s binding energies of g-C₃N₄ C=N–C moieties (~398.1 eV) and lattice-incorporated pyridinic-N (~398.3–398.8 eV) presents an inherent limitation for unambiguous peak deconvolution by XPS alone.

To address this concern rigorously, we have explicitly discussed this limitation in the revised manuscript by cross-correlating the XPS results with thermogravimetric analysis (TGA). For the low-temperature samples (NCF-600 and NCF-700), TGA confirms incomplete decomposition of the g-C₃N₄ precursor. Consequently, the elevated pyridinic-N fractions apparent in these samples may partially reflect residual g-C₃N₄-derived C=N species rather than exclusively lattice-incorporated, electrochemically active pyridinic-N sites.

NCF-600 represents the most extreme case: although a significant XPS signal is observed in the pyridinic-N binding energy region, the simultaneous presence of multiple characteristic g-C₃N₄ nitrogen species strongly suggests that a substantial fraction of the nitrogen remains embedded in the polymeric g-C₃N₄ framework rather than being incorporated into the conductive carbon lattice. NCF-700 represents a transitional state in which g-C₃N₄ decomposition is nearly complete, yet the nitrogen species have not fully reorganized into electrochemically effective lattice configurations.

For samples carbonized at ≥800 °C, the contribution from residual g-C₃N₄-derived species is expected to decrease progressively, and the signal at 398.3–398.8 eV can be attributed with greater confidence to lattice-incorporated pyridinic-N.

**Manuscript Changes (pp. 9–10, Section 3.1):**

The following text has been added and revised:

> "...The presence of these multiple g-C₃N₄-related nitrogen configurations indicates incomplete thermal decomposition at 600 °C, consistent with the TGA results [25]. Under these conditions, a substantial fraction of the nitrogen species remains associated with the polymeric g-C₃N₄ framework rather than being incorporated into a conductive carbon lattice. Consequently, part of the ~398 eV signal in NCF-600 is likely associated with residual g-C₃N₄-derived C=N moieties. Therefore, the elevated pyridinic-N fraction observed in NCF-600 is attributed, at least in part, to residual g-C₃N₄-derived species rather than exclusively to lattice-incorporated pyridinic-N.
>
> Although NCF-700 exhibits a relatively high fraction of pyridinic-N according to XPS analysis...making it difficult to unambiguously distinguish lattice-incorporated pyridinic-N from residual g-C₃N₄-derived species by XPS alone. Therefore, the elevated pyridinic-N fraction observed in low-temperature samples does not directly reflect the density of structurally integrated pyridinic sites within the carbon framework. Instead, only pyridinic-N species effectively incorporated into the carbon lattice are expected to contribute significantly to the functional properties of the material. For samples pyrolyzed..."

These revisions clarify the uncertainty associated with XPS-based quantification of pyridinic-N in NCF-600 and NCF-700 and provide a more rigorous interpretation of the nitrogen speciation in low-temperature samples.

---

### C2. Performance Benchmarking and pH Influence on Pyridinic-N Activity

**Comment:**
> The manuscript lacks direct performance comparison with recently reported nitrogen-doped carbon fabrics or graphene-based materials. The influence of electrolyte pH on pyridinic-N activity is not explored.

**Response:**

We thank the reviewer for this constructive suggestion. We have addressed both points as described below.

**Performance Benchmarking:**

To facilitate a direct comparison of the electrochemical performance of our material with the state of the art, we have compiled a new comparison table (Table S2) in the revised Supporting Information (pp. S-12–S-13), summarizing the capacitance and cycling stability of recently reported nitrogen-doped carbon-based electrodes for supercapacitor applications.

| Material | Nitrogen Source / Strategy | Electrolyte | Capacitance | Cycling | Ref. |
|----------|--------------------------|-------------|-------------|---------|------|
| N-doped carbon fabrics | Melamine, cotton fabric / Pyrolysis | 6 M KOH | 180 F g⁻¹ @ 0.5 A g⁻¹ | 95% (5,000 cycles) | [S1] |
| N-doped porous carbon | Juncus, ZnCl₂ / Pyrolysis | 6 M KOH | 290.5 F g⁻¹ @ 0.5 A g⁻¹ | 94.5% (10,000 cycles) | [S2] |
| N-doped carbon | PAN, melamine / Pyrolysis | 6 M KOH | 135.3 F g⁻¹ @ 0.5 A g⁻¹ | 96.6% (5,000 cycles) | [S3] |
| N-doped carbon | Citric acid, urea / Wet ball milling | 1 M Na₂SO₄ | 79.25 F g⁻¹ @ 1 A g⁻¹ | 96.1% (2,500 cycles) | [S4] |
| N-doped porous carbon | ZnCl₂, NH₄Cl, Ginger straw / Pyrolysis | EMIM-BF₄ | 122 F g⁻¹ @ 0.5 A g⁻¹ | 87% (10,000 cycles) | [S5] |
| N-doped porous carbon | Walnut shells, melamine / KOH activation | 6 M KOH | 329.2 F g⁻¹ @ 1 A g⁻¹ | 90.12% (5,000 cycles) | [S6] |
| **N-doped carbon fabrics (This work)** | g-C₃N₄, cotton fabric / Pyrolysis | 1 M H₂SO₄ | 789.4 mF cm⁻² @ 1 mA cm⁻² | 69.6% (5,000 cycles) | — |
| **N-doped carbon fabrics (This work)** | g-C₃N₄, cotton fabric / Pyrolysis | 6 M KOH | 139.6 F g⁻¹ @ 0.5 A g⁻¹ | 89% (10,000 cycles) | — |

The comparison demonstrates that NCF-900 delivers competitive gravimetric capacitance and cycling stability in alkaline electrolyte. We acknowledge that the cycling retention of 69.6% after 5,000 cycles in 1 M H₂SO₄ is lower than that of many literature systems measured under alkaline conditions. This difference is attributable to the harsher electrochemical environment of the acidic electrolyte, where reversible proton-coupled redox reactions involving nitrogen functional groups are intrinsically more active but also subject to greater structural perturbation over extended cycling. In contrast, the alkaline KOH measurement yields 89% retention after 10,000 cycles, placing NCF-900 favorably within the literature. This comparison highlights the importance of electrolyte selection when evaluating cycling durability, and we have added a corresponding discussion in the revised manuscript.

The following sentence has been added to **p. 15, Section 3.2**:

> "A benchmark comparison with representative nitrogen-doped carbon-based electrodes is summarized in Table S2. Although direct comparison is influenced by differences in testing conditions and electrolytes, NCF-900 exhibits competitive electrochemical performance and cycling stability among recently reported nitrogen-doped carbon materials."

**Influence of Electrolyte pH:**

We agree that the electrolyte environment can significantly modulate the electrochemical activity of nitrogen-containing functional groups. Although a systematic pH-dependent study was not the primary objective of the present work, we have evaluated the electrochemical response in both acidic (1 M H₂SO₄, pH ≈ 0) and alkaline (6 M KOH, pH ≈ 14) electrolytes and discuss the pH dependence in the context of the charge-storage mechanism.

NCF-900 exhibits more pronounced pseudocapacitive behavior in the acidic electrolyte, which is consistent with the proposed proton-coupled charge-storage mechanism. This observation is further supported by the DFT calculations, which reveal a highly favorable proton adsorption energy (E_ads = −2.58 eV) at pyridinic-N sites, indicating that these edge-associated nitrogen configurations can effectively participate in reversible proton adsorption/desorption processes under acidic conditions.

The following text has been added to **p. 12, Section 3.2**:

> "The capacitive behavior of the NCF-T materials was examined using both a three-electrode configuration in 1 M H₂SO₄ electrolyte and a symmetric two-electrode configuration in 6 M KOH electrolyte. In the symmetric two-electrode configuration using 6 M KOH electrolyte, the CV curves maintained nearly rectangular profiles at 5 mV s⁻¹, indicative of efficient ion transport and reversible adsorption processes (Figure 4a). In contrast, the CV curves obtained in 1 M H₂SO₄ exhibited broader redox features (Figure 4c), suggesting an additional pseudocapacitive contribution associated with nitrogen-containing functional groups. Among the series, NCF-900 consistently exhibited the highest capacitance in both systems, suggesting that its favorable nitrogen configuration and porous structure are beneficial for charge storage. Corresponding charge–discharge profiles (Figure S6a) revealed longer discharge times for NCF-900 under identical current densities, whereas NCF-600, NCF-700, and NCF-1000 showed lower capacitance, likely due to incomplete nitrogen incorporation into electrochemically active lattice configurations (NCF-600 and NCF-700) or excessive graphitization (NCF-1000)."

---

### C3. Real-Device Demonstration

**Comment:**
> Real-device demonstration is missing. Demonstrate a flexible pouch cell or a simple application (e.g., powering an LED).

**Response:**

We thank the reviewer for this valuable suggestion. To demonstrate the practical applicability of the fabricated electrodes, we have performed an additional device-level demonstration using symmetric NCF-900 supercapacitors connected in series to power a commercial red LED.

As shown in the newly added Figure 6, one, two, and three symmetric NCF-900 cells were connected in series to progressively increase the operating voltage. The CV and GCD results from the series-connected devices confirm the expected proportional voltage expansion while maintaining stable capacitive behavior. Three cells connected in series were then used to power a red LED; the LED remained illuminated for more than 3 minutes after charging, directly demonstrating the ability of the assembled devices to store and deliver electrical energy for practical applications.

These results provide unambiguous evidence of the feasibility of NCF-900 electrodes for real-world energy-storage applications beyond laboratory-scale electrochemical characterization.

**Manuscript Changes:**

*Section 2.6 (p. 7) – revised as follows:*

> "**2.6. Fabrication and demonstration of symmetric supercapacitor device**
> The symmetric supercapacitor device was assembled using two circular NCF-900 electrodes (14 mm diameter) directly punched from the carbon fabric and used without any conductive additives or polymer binders. A separator soaked in 6 M KOH electrolyte was placed between the two electrodes, and the assembly was packaged in a coin-cell configuration."

A new **Figure 6** and **Movie S1** have been added to the revised manuscript, together with the following discussion on **pp. 15–16, Section 3.2**:

> "To demonstrate the practical applicability of the NCF-900 electrodes, symmetric supercapacitor devices were connected in series and evaluated at the device level. As shown in Figure 6a, 6b, the operating voltage increased proportionally with the number of connected cells while maintaining capacitive behavior. Furthermore, three NCF-900 devices connected in series were able to power a commercial red LED for over 3 min after charging (Figure 6c and Movie S1), demonstrating the feasibility of the fabricated electrodes for practical energy-storage applications."

---

## Responses to the Comments of Reviewer 2

**General Response:**

We sincerely thank Reviewer 2 for the careful and insightful review of our manuscript. The comments have helped us strengthen the scientific rigor and completeness of the work. We have addressed all points thoroughly, and the corresponding revisions are described below. All added or modified text is highlighted in pink in the revised manuscript.

---

*Reviewer 2 Summary:*

> This work provided a solid-state strategy that employs exfoliated g-C₃N₄ nanosheets as both a nitrogen source and porogen to synthesize nitrogen-doped carbon fabrics. The relative proportions of pyridinic, pyrrolic, and graphitic nitrogen species were systematically tuned. An optimal balance of pyridinic-N content, abundant defect sites, and a well-developed mesoporous network can achieve high specific capacitance, excellent rate capability, and capacitance retention after 10,000 cycles. According to the experimental and theoretical results, the authors concluded that pyridinic nitrogen acts as a major contributor to redox activity by facilitating reversible proton-coupled electron transfer and enhanced ion adsorption. However, there are some issues that should be considered.

---

### C1. Surface Sensitivity of XPS and Need for Complementary Characterization

**Comment:**
> There has always been argument over the relationship between nitrogen configurations doped in carbon structures and the charge storage performance. This study analyzes the relative contents of various nitrogen configurations using XPS results. Other characterization techniques are required to supplement the experiments, as the limited detection depth of XPS means that the analyzed nitrogen configurations only represent the surface phase.

**Response:**

We thank the reviewer for raising this important methodological point. We fully acknowledge that XPS is inherently a surface-sensitive technique with a typical sampling depth of only a few nanometers, and therefore does not directly represent the bulk composition of the material.

However, we emphasize that the objective of the present study is not to quantify the bulk nitrogen distribution throughout the carbon fibers, but rather to investigate the electrochemical role of nitrogen species that are accessible at or near the electrode surface — precisely where electrochemical reactions occur. In our synthesis route, exfoliated g-C₃N₄ nanosheets were intentionally coated onto the cotton fabric surface prior to pyrolysis. Therefore, nitrogen functionalities are by design expected to be concentrated near the outer region of the carbon fibers, where they are most electrochemically relevant.

To directly address the reviewer's concern and provide complementary spatial evidence, we have added cross-sectional EDS characterization of NCF-900 in the revised manuscript (Figure S1c). The cross-sectional analysis reveals a clear nitrogen signal in the outer region of the carbon fiber, while the nitrogen signal decreases markedly toward the interior and is nearly absent in the fiber core. This finding confirms that the nitrogen species are predominantly enriched in the surface and near-surface regions, which is exactly the domain probed by XPS.

Since charge storage in supercapacitors is governed primarily by surface-accessible active sites, the nitrogen configurations identified by XPS are directly and quantitatively relevant to the observed electrochemical behavior. We have revised the manuscript to clarify explicitly that the conclusions of this work pertain to electrochemically accessible nitrogen species rather than the bulk nitrogen composition.

**Manuscript Changes (p. 4, Introduction):**

> "...Nitrogen introduced via this route typically enables better control over the formation of different nitrogen configurations, including pyridinic and graphitic configurations [15]. [...] The sample prepared at 900 °C (NCF-900) exhibited the most favorable combination of a high density of electrochemically accessible pyridinic-N sites, defect-rich structure, and mesoporosity, resulting in superior capacitive performance and durability."

**Manuscript Changes (p. 8, Section 3.1):**

> "...using exfoliated g-C₃N₄ nanosheets as both the nitrogen source and sacrificial template. The physical appearance of the samples is shown in Figure S1a, while EDS mapping confirms the successful incorporation of nitrogen species within the carbon fabric (Figure S1b). To further examine the spatial distribution of nitrogen species within the carbon fibers, cross-sectional EDS analysis was performed on NCF-900 (Figure S1c). A distinct nitrogen signal was detected near the outer region of the fiber, while the nitrogen intensity decreased markedly toward the interior and became negligible in the fiber core. This result indicates that the nitrogen functionalities introduced by the g-C₃N₄-assisted treatment are predominantly concentrated in the surface and near-surface regions of the carbon fibers. Thermogravimetric analysis..."

---

### C2. Total Nitrogen Content and Its Relationship to Electrochemical Performance

**Comment:**
> Furthermore, the research did not provide data on the overall nitrogen content in the carbon. If the total nitrogen content is low, the effect of nitrogen configurations on performance may not be the primary factor, as the BET data indicate that the specific surface areas of the materials differ as well.

**Response:**

We thank the reviewer for this insightful comment. We fully agree that both the total nitrogen content and the specific surface area contribute to the electrochemical performance of nitrogen-doped carbon materials, and that the charge-storage behavior cannot be attributed to a single parameter in isolation.

In response to this comment, we have added Table 3 to the revised manuscript, which presents the total nitrogen contents determined from XPS survey spectra alongside the calculated absolute atomic contents of each nitrogen configuration (derived by combining the total N content with the relative fractions from N 1s peak deconvolution). These data are presented alongside Table 2, which reports the relative fractions of nitrogen configurations.

Key observations from these data:

- The total nitrogen content decreases progressively from 15.34 at.% (NCF-600) to 2.01 at.% (NCF-1000) with increasing pyrolysis temperature, reflecting thermally driven nitrogen loss.
- Despite possessing the highest total nitrogen content, NCF-600 exhibits lower capacitance than NCF-900. This clearly demonstrates that total nitrogen content alone does not determine electrochemical activity; the chemical state (configuration and lattice incorporation) of the nitrogen species is a decisive factor.
- NCF-900 and NCF-800 have comparable total nitrogen contents (~8.3–8.4 at.%), yet NCF-900 outperforms NCF-800 electrochemically. This further underscores the importance of nitrogen configuration and structural accessibility rather than nitrogen quantity per se.
- The decrease in capacitance from NCF-900 to NCF-1000 is accompanied not only by changes in pore structure but also by a marked reduction in the absolute content of electrochemically active pyridinic-N (from 3.03 to 0.41 at.%), indicating that the decline in pyridinic-N density at elevated temperatures is a key contributing factor.

Regarding the role of specific surface area, we acknowledge that NCF-900 also benefits from the highest BET surface area (~646 m² g⁻¹) and the most developed mesoporous structure among all samples. These structural features facilitate electrolyte accessibility and ion transport. The superior electrochemical performance of NCF-900 is therefore interpreted as arising from the synergistic combination of favorable nitrogen configurations (particularly a high density of electrochemically accessible pyridinic-N sites), abundant structural defects, and well-developed mesoporosity — rather than from any single parameter acting alone.

The manuscript has been revised throughout (Abstract, Introduction, Sections 3.1, 3.2, 3.3, and Conclusions) to clarify this synergistic interpretation and to distinguish explicitly between pyridinic-N as a major electrochemically active nitrogen configuration and the overall structural contributions to device performance.

**Manuscript Changes (p. 4, Introduction):**

> "The sample prepared at 900 °C (NCF-900) exhibited the most favorable combination of a high density of electrochemically accessible pyridinic-N sites, defect-rich structure, and mesoporosity, resulting in superior capacitive performance and durability."

**Manuscript Changes (p. 8, Section 3.1 — new Table 3 discussion):**

> "The relative percentages of nitrogen configurations in the NCF-T series are summarized in Table 2, while the corresponding total nitrogen contents and calculated atomic contents of each nitrogen configuration are presented in Table 3. As the pyrolysis temperature increases from 600 to 1000 °C, the total nitrogen content gradually decreases, accompanied by temperature-dependent evolution of nitrogen configurations, reflecting thermally induced transformation among nitrogen species. [...] Notably, the calculated pyridinic-N content alone does not fully explain the electrochemical performance, indicating that the accessibility and chemical environment of nitrogen species are also important factors governing charge storage. At the same time, a gradual rise in graphitic nitrogen could contribute to enhanced electronic conductivity [21]."

**Manuscript Changes (p. 13, Section 3.2):**

> "NCF-900 displayed a smaller semicircle in the high-frequency region, implying lower charge-transfer resistance, and a steeper slope in the low-frequency region, characteristic of efficient ion diffusion [34]. The superior performance of NCF-900 is attributed to the synergistic combination of favorable nitrogen configurations, defect-rich carbon domains, and well-developed mesoporosity, which collectively enhance ion accessibility and charge-storage capability. After 10,000 charge–discharge..."

**Manuscript Changes (pp. 14–15, Section 3.2):**

> "Although NCF-600 exhibits a higher pyridinic-N fraction by XPS, TGA and XPS analyses suggest that a significant portion of these species originate from incompletely decomposed g-C₃N₄ rather than from electrochemically active lattice-incorporated configurations. Consequently, the apparent high pyridinic-N fraction does not directly translate into enhanced charge-storage performance. This observation further indicates that the electrochemical behavior does not simply follow the trend of total nitrogen content or the relative abundance of a specific nitrogen species alone. Instead, the electrochemical activity is governed by the combined effects of nitrogen configuration, nitrogen accessibility, and the structural characteristics of the carbon framework. For NCF-1000..."

**Manuscript Changes (p. 15, Section 3.2):**

> "In addition, excessive graphitization at 1000 °C suppresses defect-rich edge sites and reduces ion-accessible active regions. The partial loss of mesoporosity further restricts electrolyte access to electrochemically active sites, resulting in lower pseudocapacitive charge-storage capability despite improved graphitic ordering."

The discussion in the Abstract, Introduction, Sections 3.1, 3.2, 3.3, and Conclusions has been comprehensively revised to reflect this more nuanced and balanced interpretation.

---

*End of Responses to Reviewers*
