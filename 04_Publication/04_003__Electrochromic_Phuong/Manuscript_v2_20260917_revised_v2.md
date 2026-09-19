# [수정 메모 — v2] 반드시 먼저 읽어주세요

> 이 섹션은 투고용 원고에 포함되지 않는 편집자용 메모입니다. 다음 라운드 수정 시 삭제하세요.

## v2에서 반영한 사항 (사용자 요청 기준)
1. **본문(Main Text) Figure 1–5 캡션을 약 2/3 분량으로 축소.** SI Figure(S1–S8) 캡션은 그대로 유지했습니다 (요청이 "main figure"에 한정되었다고 판단).
2. **§1.3 NiO 박막 준비(스퍼터링 조건)는 그대로 두었습니다.** 추후 업데이트 예정이라고 하셔서 손대지 않았습니다.
3. **§1.4–1.6을 서술식(narrative prose)으로 재작성.** 기존 불릿 리스트 형식을 문단 형태로 바꾸었고, `[확인 필요]` 표시가 붙은 항목들은 그대로 유지했습니다 (실제 값이 없는 상태에서 임의로 채우지 않았습니다).
4. 파일명을 `Manuscript_v2_20260917_revised_v2.md`로 저장.

v1에서 정리했던 "4모드 최초 주장" 관련 확인 사항과 그림/본문 불일치 12가지(§ v1 메모 참조, 아래에 그대로 유지)는 이번 라운드에서 사용자가 별도 요청하지 않아 손대지 않았습니다.

---

## [v1에서 이월] 4모드 관련 중요 확인 사항

`References/References` 폴더의 12번, 14번 논문 제목에 이미 "Four-Mode Conversion"이 들어 있습니다.

- Ref. 12 — Huang, Zhao, Xu *et al.*, *Adv. Funct. Mater.* **36**, e25837 (2025) — Zn 음극 + phytic acid 도핑 PANI 단일 소재로 4모드 구현. 저장용량 4.0 μAh cm⁻², 왕복효율 23.7%, 10,000 사이클에서 63.2–70.9% 유지.
- Ref. 14 — Huang, Cao, Liu *et al.*, *Adv. Funct. Mater.* **35**, 2500064 (2025) — 역시 PANI 기반, Au 계면층으로 3모드→4모드 확장.
- Ref. 13 — Xiong *et al.*, *Adv. Opt. Mater.* **14**, e03866 (2026) — power-free 방식 4모드 관련 개념.

"세계 최초 4모드"는 위험한 주장이며, 본 원고는 다음 세 가지로 강조점을 옮겼습니다: **① 무기물 기반 4모드는 최초, ② MnWO₄를 EC+에너지저장 소재로 쓴 최초 보고, ③ 저장용량이 기존 4모드 소자 대비 약 500배(단, 사이클 수명은 PANI 소자가 10,000회로 훨씬 앞서므로 과장 금지).**

## [v1에서 이월] 그림/본문에서 발견된 모호하거나 상충되는 부분

1. NiO 스퍼터링 증착 조건 미기재 (§1.3, 추후 업데이트 예정 — 이번 라운드는 보류).
2. Zn 전극 형태 불일치 (foil vs. mesh).
3. MnWO₄ Mn 전구체 시약 불일치 (본문 MnCl₂·4H₂O vs. Fig. S1 캡션 Mn(CH₃COO)₂·4H₂O).
4. Figure S3의 x축 라벨 오류 ("Binding energy (eV)" → "2θ (°)").
5. Figure S4 캡션 오탈자 ("adsoption" → "adsorption").
6. Figure S3 캡션 오탈자 ("he PTFE liner" → "the PTFE liner").
7. Figure 5 캡션 오탈자 ("defferent" → "different").
8. 착색/탈색 사이클 테스트의 전압 유지시간(square-wave protocol) 미기재.
9. 태양광 모사 열화상 실험 조건(광량, 거리, 카메라 기종, 직물 재질) 미기재.
10. Cover letter 문장 오류/무관 문구 (별도 요청 시 재작성 가능).
11. 저자 목록 3, 4번 공란.
12. Acknowledgments 지원기관 문구가 끊김.

---

# Four-Mode Electrochromic Windows with Built-In Energy Storage Enabled by MnWO₄

Viet Phuong Nguyen,<sup>a,\*</sup> Seong-Jae Jeon,<sup>a</sup> […] Seung-Mo Lee<sup>a,b,†</sup>

<sup>a</sup> Korea Institute of Machinery & Materials (KIMM), Daejeon 34103, Republic of Korea
<sup>b</sup> University of Science and Technology (UST), Daejeon 34113, Republic of Korea

\*,† Corresponding authors: V.P.N. (nvphg9@gmail.com), S.M.L. (sm.lee@kimm.re.kr)

**One-sentence summary:** A single window that can independently let in or block visible light and invisible heat-carrying infrared light — in four combinations instead of the usual three — while also storing the electrical energy used to switch it.

---

## Abstract

A window that could let in daylight while keeping out summer heat — or the reverse in winter — would save a meaningful share of the energy buildings spend on heating, cooling, and lighting. Electrochromic windows, which change transmittance under a small applied voltage, can do this by separately controlling visible light (which we see) and near-infrared light (which we feel as heat). Most electrochromic windows reported so far only reach three of the four possible combinations of "light in/light out" and "heat in/heat out," and almost none also store electrical energy for reuse. Here we show that manganese tungstate (MnWO₄), a mineral-derived material never before used in electrochromic devices, can do both jobs in one electrode: it changes color to block near-infrared heat, and it stores charge like a small battery. Pairing a MnWO₄ electrode with a nickel oxide (NiO) electrode that independently controls visible light — sharing a single zinc metal counter-electrode — gives a three-terminal device that reaches all four optical states: bright-warm, bright-cool, dark-warm, and dark-cool. The same electrochemical reactions that switch the color also store charge, delivering a high areal capacity that is retained over 200 charge–discharge cycles. Under simulated sunlight, the surface beneath the window is more than 6 °C cooler in the dark-cool state than in the bright-warm state, showing that the effect is large enough to matter in practice. This work establishes MnWO₄ as a rare example of a single material that is both a color-changing "heat valve" and an energy-storage electrode, pointing toward simpler, self-powered smart windows.

**Keywords:** smart window, electrochromic device, energy storage, MnWO₄, four-mode, dual-band optical control

---

## Main Text

### Why windows need four settings, not three

Buildings use roughly 30–40% of the world's energy, and a large share of that goes into heating, cooling, and lighting rooms — much of it lost or gained through windows (*1*–*4*). Sunlight reaching a window carries two very different kinds of information. The visible part (roughly 380–780 nm) is what lets us see; the near-infrared part (roughly 780–2500 nm, invisible to the eye) is what we mostly feel as heat (*5*). An ordinary window cannot tell these apart — it either lets both through or blocks both. An "electrochromic" window can: applying a small voltage drives a reversible chemical reaction in a thin coating, switching it between a clear state and a colored, light-blocking state, without any moving parts.

The most capable electrochromic windows reported to date can separately dial visible and near-infrared transmittance up or down, but almost all of them stop at three usable combinations: *bright* (both let through), *cool* (heat blocked, light let through), and *dark* (both blocked) (*2*, *6*–*11*). A fourth, very useful combination is missing from most designs: *warm* — light blocked (for privacy or glare control) while heat is still let in (for passive winter heating). Reaching all four states requires switching the visible-light response and the near-infrared response completely independently, which is mechanically simple to describe but chemically hard to achieve in one material. A few recent devices have shown that four states are possible in principle, typically by finely tuning the voltage applied to a single organic dye layer (polyaniline) through several distinct oxidation levels (*12*–*14*). That approach works, but it asks one material to do a difficult balancing act, and none of those devices also stores a meaningful amount of energy.

A second, largely separate line of work has tried to make electrochromic coatings double as tiny batteries or supercapacitors, so that the energy spent switching the window can be partly recovered (*15*–*17*). Very few devices combine both ideas — independent four-state optical control *and* useful energy storage — in the same platform.

### MnWO₄: one material, two jobs

Most electrochromic research has focused on tungsten oxide (WO₃)–type materials, whose near-infrared coloring comes from free-electron absorption (a plasmon-like effect, similar to how metals reflect light) or from electrons hopping between tungsten sites (*18*). WO₃ is reliable for switching color, but its rigid, fully connected crystal framework leaves little room for ions to be stored — it is a poor "battery" material. We looked instead at manganese tungstate (MnWO₄), a mineral-like compound that pairs the same tungsten chemistry with manganese, an element well known in battery electrodes for its multiple, easily switched oxidation states (Mn²⁺/Mn³⁺) (*19*, *20*). We reasoned that combining the two inside one crystal structure might yield a material that both changes color in the near-infrared and stores charge — and that is what we found.

We built a device in which a MnWO₄ electrode (the "NIR module") and a NiO electrode (the "VIS module," NiO being a well-established material that darkens visibly when charged) share a single zinc metal counter-electrode, but can be switched on or off independently (Fig. 1). Because the two modules do not interfere with each other electrically, every combination of "MnWO₄ colored or not" and "NiO colored or not" is directly accessible — the full set of four optical modes (Fig. 1a–d): bright–warm (both bleached, for cold weather), bright–cool (only NiO colored, for daylighting without heat), dark–warm (only MnWO₄ colored, for privacy without losing winter heat gain), and dark–cool (both colored, for maximum summer heat rejection).

**Why "four modes" is worth emphasizing here.** A handful of recent devices have also reached four optical states, but by asking a single organic material (polyaniline) to pass through several finely tuned oxidation levels under one continuously varying voltage (*12*, *14*). That is an elegant chemistry trick, but it also means the four states are not fully independent — getting one state right depends on getting the voltage exactly right for that material's particular redox ladder. Our device instead uses two chemically distinct, inorganic electrodes that are each simply "on" or "off," addressed independently through a shared electrode. The two design philosophies are complementary, but ours is architecturally simpler to control and, because it stores roughly 500 times more charge per unit area than the best previously reported four-mode device (*12*) (about 2 mAh cm⁻² here versus about 4 μAh cm⁻² there), it is the first four-mode electrochromic window to combine independent inorganic dual-electrode switching with genuinely useful on-board energy storage. We are careful not to overstate this: those organic four-mode devices remain far ahead of ours in cycling lifetime (10,000 cycles versus the 200 cycles tested here), so long-term durability of the MnWO₄ electrode is a question for future work, not a claim we make in this Letter.

The structural reason MnWO₄ can store charge where WO₃ cannot is visible in its crystal structure (Fig. 1e,f). WO₃ is built from tungsten-oxygen octahedra (an octahedron is an eight-faced cage shape, here formed by six oxygen atoms around one metal atom) that all share corners in a dense, fully interlocked 3D lattice — good for letting the coloring reaction happen throughout the film, but leaving few open channels for extra ions to be parked and stored. MnWO₄ instead arranges manganese- and tungsten-oxygen octahedra in open, edge-sharing chains (edge-sharing means neighboring octahedra touch along a whole edge rather than just a corner, leaving more open space between chains). This looser packing exposes far more surface to the electrolyte and gives manganese's switchable oxidation states room to react quickly and reversibly, letting MnWO₄ combine reliable electrochromism with genuine, pseudocapacitive-like charge storage (pseudocapacitive storage means the charge is stored through fast, reversible surface chemical reactions rather than purely by physically packing ions onto a surface, giving it both battery-like capacity and capacitor-like speed).

### Confirming what MnWO₄ actually is

Before testing what MnWO₄ can do, we confirmed what it *is*. We grew it directly on transparent conducting glass (ITO) using a one-pot hydrothermal synthesis — mixing water-soluble manganese and tungsten salts, adjusting the acidity, and heating the sealed mixture at 180 °C (Fig. S1; full recipe in the Supporting Information). Electron microscope images showed a dense mat of interconnected nanowires spread evenly over the glass (Fig. 2a), a shape expected to help the electrolyte penetrate the film and reach reaction sites quickly, both during color switching and during charge storage. Closer imaging confirmed individual nanowires (Fig. 2b) with well-ordered atomic planes spaced 3.75 Å apart (Fig. 2c), matching the (110) crystal plane expected for MnWO₄ (*22*) and consistent with the electron-diffraction pattern in Fig. S2. X-ray diffraction confirmed that the film was single-phase, monoclinic "wolframite"-structure MnWO₄ with no leftover starting materials or side products (Fig. 2d, Fig. S3). Finally, X-ray photoelectron spectroscopy — a technique that reads the electronic "fingerprint" of each element at the surface — showed tungsten sitting entirely in its fully oxidized +6 state (Fig. 2e) and manganese in its +2 state with the satellite peak pattern expected for high-spin Mn²⁺ sitting in an octahedral oxygen cage (Fig. 2f) (*23*). Together, these checks confirm we made clean, stoichiometric MnWO₄ with the expected chemistry — the correct starting point for testing its electrochromic and energy-storage behavior.

### MnWO₄ as an energy-storage electrode

We first tested MnWO₄ purely as a charge-storage electrode, paired against a zinc metal counter-electrode in a simple two-electrode cell (a "Zn‖MnWO₄" cell). Cyclic voltammetry — a technique that sweeps the voltage back and forth while recording current, producing a fingerprint of which reactions happen at which voltage — showed multiple distinct reaction steps rather than one broad feature (Fig. 3a), a sign of rich, multi-step redox chemistry. On discharge, two separate reactions occur in sequence: at moderate voltage, Zn²⁺ ions slot into the tungsten-oxygen framework (an "intercalation" reaction, like a key sliding into a lock, forming ZnₓWO₃); at lower voltage, a more drastic "conversion" reaction takes over, in which Zn²⁺ chemically breaks down the manganese-oxygen framework to form a new Zn–Mn–O phase. On charging, this conversion reaction runs in reverse. Having *two* different storage mechanisms working together in one electrode — a gentle intercalation step plus a deeper conversion step — lets MnWO₄ store substantially more charge than a material relying on just one mechanism. For comparison, commercial WO₃ tested the same way showed only a single, broad, weak feature (Fig. S4), confirming it has much more limited redox chemistry to draw on.

Charge–discharge tests across a range of currents (0.01–0.1 mA cm⁻²) showed clear voltage plateaus matching the reactions identified above (Fig. 3b). At the slowest, most complete rate of charge/discharge (0.01 mA cm⁻²), the electrode delivered an areal capacity — the amount of charge stored per unit of electrode area, the standard way to compare thin-film storage electrodes — of about 2 mAh cm⁻². As expected, capacity dropped at faster rates (Fig. 3c), but a usable amount remained even at 0.1 mA cm⁻², ten times faster than the base-case test, indicating reasonably fast ion transport through the nanowire film. Cycling the electrode 200 times in a row at both 0.02 and 0.1 mA cm⁻² showed stable capacity throughout, with coulombic efficiency — the fraction of the charge put in during charging that is recovered during discharging, ideally 100% — staying close to 100% the whole time (Fig. 3d,e). This tells us the reactions inside MnWO₄ are highly reversible over the timescales we tested, without the material breaking down.

### MnWO₄ as a color-switching electrode

We then tested the same Zn‖MnWO₄ cell purely for its color-changing behavior. Photographs taken at different voltages showed a clean, reversible switch: at 1.2 V the electrode was a light, near-transparent "bleached" state; dropping the voltage to 0.0 V turned it a deep blue-grey; raising the voltage back to 1.2 V fully restored the original clear appearance (Fig. 4a). Measuring transmittance across the full 300–1500 nm range — spanning ultraviolet through visible to near-infrared — showed that this color change is strongly concentrated in the near-infrared: the difference in transmittance between colored and bleached states is much larger beyond 780 nm than it is in the visible range (Fig. 4b). This selectivity fits a "localized surface plasmon resonance" mechanism (LSPR — a collective, wave-like sloshing of free electrons that absorbs light only in a specific band, here the near-infrared, somewhat like how a swimming pool sloshes at a particular frequency when pushed), which switches on first at low voltage, before deeper, more visible-light-absorbing chemistry sets in. The intermediate voltage (0.5 V) produced an intermediate transmittance curve, showing that the near-infrared blocking can be dialed continuously, not just switched fully on or off. Cycling the electrode through 500 full coloring/bleaching cycles left the transmittance spectra of both the colored and bleached states essentially unchanged from the first cycle (Fig. 4c) — combined with the charge-storage cycling stability above, this shows MnWO₄ can reliably do both jobs at once over hundreds of cycles.

### Putting it together: the four-mode window

We then assembled the complete three-electrode device — MnWO₄ (NIR module) and NiO (VIS module) sharing one Zn electrode — and tested all four optical modes (device details and NiO's own coloring behavior are in Fig. S5–S7; note that unlike MnWO₄, the NiO electrode showed more limited cycling stability in our tests, an issue we flag as a target for future improvement rather than something already solved). Photographs of the four modes look visibly distinct from one another (Fig. 5a): bright–warm is the lightest and most see-through; dark–cool is the darkest; bright–cool and dark–warm sit in between, each showing the "signature" of whichever single electrode is colored. Transmittance spectra confirm this is not just a visual impression but a real, quantifiable spectral shift (Fig. 5b): bright–warm transmits the most light across both bands; bright–cool keeps visible transmittance high while cutting near-infrared; dark–warm shows the mirror-image pattern, near-infrared preserved while visible light is cut; and dark–cool cuts both. Switching cleanly between all four of these spectrally distinct states in one device is the central practical result of this work.

To check whether this actually matters for keeping a room comfortable, we placed a black, heat-absorbing cloth behind the device, lit it with a solar simulator, and tracked its temperature with an infrared camera (Fig. 5c). Under ordinary window glass (no electrochromic coating), the cloth reached 42.1 °C after 10 minutes of illumination (Fig. S8) — a useful "worst case" reference. Behind the device in bright–warm mode, the cloth still warmed substantially, reaching 32.1 °C after 10 s, 34.4 °C after 60 s, and 37.2 °C after 10 minutes (Fig. 5d) — letting heat through, as intended for a cold-weather setting. Behind the device in dark–cool mode, warming was strongly suppressed: only 29.2 °C after 10 s, 30.7 °C after 60 s, and 31.1 °C after 10 minutes. After 10 minutes, the dark–cool state ran about 11 °C cooler than plain glass, and about 6 °C cooler than the device's own bright–warm state — a difference large enough to be felt, and a direct demonstration that switching modes genuinely changes how much solar heat gets through.

### Outlook

We have shown a four-mode electrochromic window built from two independently switchable inorganic electrodes sharing one zinc counter-electrode, in which the near-infrared-active electrode — MnWO₄, used here for the first time in any electrochromic device — also works as a genuine charge-storage electrode. The device reaches all four optical states, including the "dark–warm" combination that is missing from most three-state designs, and does so using two simple on/off electrodes rather than one finely tuned material, while storing roughly 500 times more charge per unit area than the best previously reported four-mode device. A greater-than-6-°C surface temperature gap between the warmest and coolest settings, measured under simulated sunlight, shows the effect is large enough to be practically useful, not just a laboratory curiosity.

The most important limitation is durability: our cycling tests cover 200 cycles for MnWO₄ and only 30 cycles for NiO, both far short of the 10,000-cycle results already reported for organic four-mode devices (*12*). Closing that gap — particularly stabilizing the NiO electrode — is the clear next step before this platform could be considered for real windows. With that caveat, combining season-adaptive, fully independent four-mode optical control with meaningful on-board energy storage in one simple architecture is a step toward smart windows that manage both light and heat, and help pay for the energy they use to do it.

---

## Methods (summary)

Full experimental details, reagent quantities, instrument settings, and calculation formulas are provided in the Supporting Information. Briefly: MnWO₄ nanowire films were grown directly on ITO glass by a one-step hydrothermal reaction; NiO films were deposited by sputtering (parameters to be added in a future revision); half-cells and the full three-electrode device were assembled in a sandwich configuration with a Zn-foil/mesh frame and 0.5 M aqueous ZnSO₄ electrolyte; electrochemical and optical measurements used a potentiostat/galvanostat and a UV–Vis–NIR spectrophotometer (300–1500 nm); thermal performance was assessed by infrared imaging of a black textile under solar-simulator illumination behind the device.

## Acknowledgments

We would like to acknowledge the financial support from the internal research program of the Korea Institute of Machinery and Materials (NK255F) and *[확인 필요: 추가 지원기관/과제번호가 있다면 기재]*.

## Conflict of Interest

The authors declare no conflicts of interest.

## Data Availability

*[확인 필요: 본 저널의 데이터 가용성 정책에 맞춰 문구 확정 — 예: "The data supporting the findings of this study are available from the corresponding authors upon reasonable request."]*

---

## References

1. F. Zhao, B. Wang, B. Huang, W. Zhang, J. Chen, L. Liu, H. Wang, A. Y. Elezzabi, P. S. Lee, D. J. Milliron, W. W. Yu, H. Li, Inorganic electrochromic smart windows for advancing building energy efficiency. *Nat. Rev. Clean Technol.* **1**, 396–412 (2025).
2. Z. Shao, A. Huang, C. Cao, X. Ji, W. Hu, H. Luo, J. Bell, P. Jin, R. Yang, X. Cao, Tri-band electrochromic smart window for energy savings in buildings. *Nat. Sustain.* **7**, 796–803 (2024).
3. N. C. Davy, M. Sezen-Edmonds, J. Gao, X. Lin, A. Liu, N. Yao, A. Kahn, Y. L. Loo, Pairing of near-ultraviolet solar cells with electrochromic windows for smart management of the solar spectrum. *Nat. Energy* **2**, 17104 (2017).
4. H. Li, J. Zhang, Y. Liu, Z. Bai, H. Liang, C. Hou, Q. Zhang, Y. Li, K. Li, H. Wang, Scalable all-in-one electrochromic glazing for full-spectrum solar radiation management. *Nat. Sustain.* **9**, 910–920 (2026).
5. S. Cao, S. Zhang, T. Zhang, Q. Yao, J. Y. Lee, A visible light-near-infrared dual-band smart window with internal energy storage. *Joule* **3**, 1152–1162 (2019).
6. J. Wang, Z. Wang, L. Cui, M. Zhang, X. Huo, M. Guo, Visible-near infrared independent modulation of hexagonal WO₃ induced by ionic insertion sequence and cavity characteristics. *Adv. Mater.* **36**, 2406939 (2024).
7. P. Dutta, K. V. Palliyal, R. Prabhu, A. K. Singh, Oxygen-deficient bimetallic oxide M₀.₁₁W₀.₈₉O₃₋ₓ for flexible energy storage and electrochromic applications. *J. Mater. Chem. A* **14**, 13504–13519 (2026).
8. H. Bi, X. Wang, L. Xu, H. Zhao, L. Fan, J. Xuan, X. Zhao, Q. Liao, Y. Zhang, Structure-dependent trap passivation in WO₃ enables ultra-stable electrochromic devices. *Adv. Funct. Mater.* **36**, e76298 (2026).
9. W. Shi, Y. Huang, X. Zheng, J. Ma, J. He, R. Zhang, Y. Mei, P. Lyu, R. Zhang, X. Liu, Vacancy engineering in tungsten oxide for enhanced temperature-modulated electrochromic smart windows. *Nano Lett.* **26**, 4507–4512 (2026).
10. P. Li, Y. Lv, X. You, H. Ma, T. Wang, Y. Shen, X. Li, X. Guo, G. Cai, X. Liu, Bio-inspired ordered WO₃ nano-helixes enable multi-band electrochromic smart windows with ultrafast switching and robust cyclability. *Energy Environ. Mater.* **9**, e70185 (2025).
11. W. Zhang, R. Tafoya, I. Ouarag, C. H. Hsu, Z. Zhang, D. J. Milliron, Composite anodes with dual-stage charging for efficient dual-band electrochromic devices. *ACS Energy Lett.* **11**, 3818–3825 (2026).
12. B. Huang, F. Zhao, Y. Xu, J. Y. Yang, L. Kang, J. Chen, H. Li, W. W. Yu, Multicolored dual-band zinc anode-based electrochromic device with four-mode conversion based on phytic acid-doped polyaniline. *Adv. Funct. Mater.* **36**, e25837 (2025).
13. L. Xiong, Y. Zhou, P. Wang, Z. Wu, J. Wang, D. Ma, Potential gradient-driven power-free films fabrication strategy for electrochromic window achieving on-demand indoor photothermal regulation. *Adv. Opt. Mater.* **14**, e03866 (2026).
14. L. Huang, S. Cao, Y. Liu, J. Chen, H. Li, Y. Liang, T. Yang, B. Zou, Built-in electric field-assisted polyaniline for boosting dual-band electrochromic smart windows with multicolor displays and four-mode conversion. *Adv. Funct. Mater.* **35**, 2500064 (2025).
15. B. Sahu, L. Bansal, N. Ahlawat, D. K. Rath, A. S. S. S. Shekhawat, K. S. Chondath, S. K. Saxena, R. Kumar, Developing solid state electrochromic-supercapacitor prototype through dft-guided charge transfer engineering in 2d-carbon doped NiO. *J. Mater. Chem. C* **14**, 5284–5297 (2026).
16. N. Cao, Y. Lang, G. Gu, X. Jia, D. Chao, Mixed ionic-electronic conducting polymer enables efficient electrochromic supercapacitor. *Adv. Funct. Mater.* **36**, e17668 (2025).
17. M. Y. Tan, G. S. H. Thien, K. B. Tan, A. R. Marlinda, M. S. Mastuli, H. C. A. Murthy, B. S. Surendra, Y. I. Go, K. Y. Chan, Enhancing electrochromic energy storage devices with water-in-bisalt (Zn²⁺/Al³⁺) electrolytes for energy saving smart glass applications. *Sci. Rep.* **16**, 16121 (2026).
18. B. Tandon, H. C. Lu, D. J. Milliron, Dual-band electrochromism: plasmonic and polaronic mechanisms. *J. Phys. Chem. C* **126**, 9228–9238 (2022).
19. T. K. Shivasharma, A. S. Jhala, P. Singh, B. R. Sankapal, Hybridization of manganese 3d orbitals with tungsten 5d orbitals in hydroxylated mixed phase manganese tungsten oxide: nano surface architecture to design high-performance mechanically bendable solid-state supercapacitor. *Adv. Sustain. Syst.* **10**, e01045 (2026).
20. A. Rajput, P. K. Nayak, D. Ghosh, B. Chakraborty, Structural and electronic factors behind the electrochemical stability of 3d-metal tungstates under oxygen evolution reaction conditions. *ACS Appl. Mater. Interfaces* **16**, 28756–28770 (2024).
21. P. J. Morankar, R. U. Amate, M. K. Bhosale, C. W. Jeon, Harnessing 4f-orbital rare-earth ion chemistry in WO₃ for next-generation electrochromic windows with tunable modulation kinetics and enhanced ion-optical dynamics. *Nanoscale* **17**, 23032–23048 (2025).
22. W. Tong, L. Li, W. Hu, T. Yan, X. Guan, G. Li, Kinetic control of MnWO₄ nanoparticles for tailored structural properties. *J. Phys. Chem. C* **114**, 15298–15305 (2010).
23. A. Tiwari, V. Singh, T. C. Nagaiah, Tuning the MnWO₄ morphology and its electrocatalytic activity towards oxygen reduction reaction. *J. Mater. Chem. A* **6**, 2681–2692 (2018).

---

## Figure Legends

**Figure 1. Operating principle of the four-mode electrochromic window, and why MnWO₄ can store charge while WO₃ cannot.**
**(a–d)** Schematic of the three-electrode device: an NIR-active MnWO₄ electrode and a VIS-active NiO electrode share one Zn electrode via independent switches, so each can be switched on (colored) or off (bleached) separately. Arrows trace the VIS and NIR components of transmitted sunlight; the room scenes illustrate the resulting comfort effect. **(a) Bright–warm** — both electrodes bleached; VIS and NIR both transmitted, for cold or low-light conditions. **(b) Bright–cool** — NiO colored, MnWO₄ bleached; VIS blocked, NIR (heat) still admitted. **(c) Dark–warm** — MnWO₄ colored, NiO bleached; NIR (heat) blocked, VIS preserved, for hot sunny days without darkening the room. **(d) Dark–cool** — both colored; VIS and NIR both blocked, for maximum solar rejection. **(e,f)** Crystal structures of **(e)** WO₃, built from corner-sharing WO₆ octahedra in a dense, fully connected framework, and **(f)** MnWO₄, built from more open, edge-sharing MnO₆/WO₆ chains. WO₃'s framework supports electrochromism but leaves little room for ion storage; MnWO₄'s exposed Mn sites support both electrochromism and genuine charge storage, as summarized by the checkmarks.

**Figure 2. Structural and chemical confirmation of the as-synthesized MnWO₄ nanowire film.**
**(a)** SEM image (scale bar 1 μm) showing a dense, uniform mat of MnWO₄ nanowires on ITO — a porous morphology expected to aid electrolyte penetration and ion transport. **(b)** Low-magnification TEM image (scale bar 20 nm) confirming the nanowire morphology at the single-particle level. **(c)** High-resolution TEM image (scale bar 2 nm) showing continuous lattice fringes spaced 3.75 Å apart, matching the (110) plane of monoclinic MnWO₄ (*22*) and confirming the nanowires are single-crystalline. **(d)** XRD pattern (red) matched against the reference pattern for monoclinic wolframite MnWO₄ (grey bars); every peak is accounted for with no impurity phases. **(e)** High-resolution XPS of the W 4f region: the spin-orbit-split 4f₅/₂/4f₇/₂ doublet confirms tungsten is entirely in the W⁶⁺ state before any coloring reaction. **(f)** High-resolution XPS of the Mn 2p region; the Mn²⁺ 2p₃/₂/2p₁/₂ peaks and their satellite features confirm high-spin Mn²⁺ in an octahedral oxygen site, consistent with the structure in Fig. 1f (*23*).

**Figure 3. Energy-storage performance of MnWO₄, tested as a battery-type electrode against a Zn counter-electrode.**
**(a)** Cyclic voltammogram of the Zn‖MnWO₄ cell (0.1 mV s⁻¹). On discharge, Zn²⁺ first intercalates into the WO₆ framework to form ZnₓWO₃, then at lower potential converts the MnO₆ framework to ZnₓMnO; both reactions reverse on charging, as labeled directly on the curve. **(b)** Galvanostatic charge–discharge curves at 0.01–0.1 mA cm⁻², with plateaus matching the reactions in (a); the slowest rate delivers the largest areal capacity, ≈2 mAh cm⁻². **(c)** Rate capability over 25 cycles as the current density is stepped up and back down, showing capacity is largely recovered after fast cycling. **(d,e)** Cycling stability over 200 cycles at **(d)** 0.02 and **(e)** 0.1 mA cm⁻², showing stable areal capacity (left axis) and coulombic efficiency near 100% (right axis) throughout.

**Figure 4. Electrochromic (color-switching) performance of the MnWO₄ electrode, in the same Zn‖MnWO₄ cell.**
**(a)** Photographs (green "NVP" logo as a transparency reference) at 1.2 V (bleached, logo legible), 0.0 V (colored, deep blue-grey, logo obscured), and back at 1.2 V (bleached state fully restored), demonstrating reversible switching. **(b)** Transmittance spectra (300–1500 nm) at 1.2, 0.5, and 0.0 V: the colored–bleached contrast is far larger in the near-infrared (>780 nm) than in the visible range, showing MnWO₄ selectively blocks heat-carrying NIR light, consistent with a plasmon-like (LSPR) mechanism; the 0.5 V curve shows the modulation is continuously voltage-tunable. **(c)** Transmittance spectra at the colored and bleached states, compared between cycle 1 and cycle 500 — the curves overlap closely, showing negligible loss of optical contrast after 500 cycles.

**Figure 5. Performance of the complete four-mode MnWO₄‖Zn‖NiO device, including a solar heat-blocking demonstration.**
**(a)** Photographs of the assembled device in each of the four modes (same logo reference as Fig. 4a): bright–warm is lightest/most transparent, dark–cool is darkest, and bright–cool/dark–warm show visually distinct intermediate colorations from NiO and MnWO₄, respectively. **(b)** Transmittance spectra (300–1500 nm) confirming this quantitatively: bright–warm gives the highest transmittance in both bands; bright–cool suppresses VIS while preserving NIR; dark–warm shows the mirror-image selectivity; dark–cool suppresses both. **(c)** Test setup: a solar simulator illuminates the device, a black heat-absorbing textile behind it mimics an interior surface, and an infrared camera tracks its temperature. **(d)** Infrared thermal images of the textile in bright–warm (top) and dark–cool (bottom) modes at 0, 10, 60, and 600 s. Bright–warm heats steadily (24.5→37.2 °C); dark–cool suppresses warming (24.5→31.1 °C) — after 600 s, dark–cool is ~6 °C cooler than bright–warm and ~11 °C cooler than ordinary glass (Fig. S8), showing the modes make a practically meaningful difference in transmitted heat.

---

# Supporting Information

## Four-Mode Electrochromic Windows with Built-In Energy Storage Enabled by MnWO₄

Viet Phuong Nguyen,<sup>a,\*</sup> Seong-Jae Jeon,<sup>a</sup> […] Seung-Mo Lee<sup>a,b,†</sup>

<sup>a</sup> Korea Institute of Machinery & Materials (KIMM), Daejeon 34103, Republic of Korea
<sup>b</sup> University of Science and Technology (UST), Daejeon 34113, Republic of Korea

---

## 1. Experimental Section

### 1.1 Materials

All chemicals were used as received without further purification unless noted otherwise. Sodium tungstate dihydrate (Na₂WO₄·2H₂O), manganese(II) chloride tetrahydrate (MnCl₂·4H₂O) *[확인 필요: Figure S1 캡션에는 초산망간(Mn(CH₃COO)₂·4H₂O)으로 표기되어 있어 실제 사용 시약 확인 필요]*, sodium sulfate (Na₂SO₄), hydrochloric acid (HCl), and zinc sulfate (ZnSO₄) were used for MnWO₄ synthesis and electrolyte preparation. ITO-coated glass substrates (sheet resistance *[확인 필요]*, supplier *[확인 필요]*) served as the transparent conducting substrate for both electrodes. Zinc foil/mesh (thickness *[확인 필요]*, purity *[확인 필요]*, supplier *[확인 필요]*) was used as the shared counter-electrode. Deionized water and absolute ethanol were used for all rinsing steps.

### 1.2 Synthesis of MnWO₄ nanowire films on ITO glass

MnWO₄ was synthesized directly onto ITO glass by a one-step hydrothermal method. Briefly, 0.3 mmol Na₂WO₄·2H₂O, 0.3 mmol MnCl₂·4H₂O, and 0.1 mmol Na₂SO₄ (a 1:1 Mn:W molar ratio, with Na₂SO₄ added as a mineralizing/morphology-directing additive) were dissolved in 40 mL deionized water under magnetic stirring. The solution pH was adjusted to ≈2 by the dropwise addition of HCl, and the mixture was stirred for 1 h at room temperature to ensure complete homogenization. The precursor solution was then transferred into a 50 mL Teflon (PTFE)-lined stainless-steel autoclave. ITO glass substrates, pre-cleaned by sequential ultrasonication in ethanol and deionized water *[확인 필요: 세척 시간]* and dried under a nitrogen/air stream, were immersed vertically in the precursor solution inside the autoclave (substrate holder/orientation: *[확인 필요]*). The sealed autoclave was heated at 180 °C for 1.5 h in a temperature-controlled convection oven, then allowed to cool naturally to room temperature. The MnWO₄-coated ITO substrates were removed, rinsed thoroughly with deionized water and ethanol to remove residual salts, and dried under ambient conditions *[확인 필요: 실온 자연건조 vs. 오븐건조]*. A portion of MnWO₄ powder also nucleates on the PTFE liner wall during synthesis; this byproduct powder was collected separately and used for the bulk XRD measurement in Fig. S3, since the thin film's diffraction signal on ITO is weak relative to the substrate background.

### 1.3 Preparation of NiO thin films on ITO glass

*[본 항목은 추후 업데이트 예정입니다.]*

NiO films were deposited on ITO glass by magnetron sputtering. *[확인 필요 — 아래 항목의 실제 수치를 채워주시면 재현 가능한 절차가 완성됩니다]*
- Target: *[확인 필요: 예 — NiO ceramic target, or Ni metal target with reactive O₂ sputtering]*, purity *[확인 필요]*
- Sputtering mode/power: *[확인 필요: DC or RF, power in W]*
- Base pressure / working pressure: *[확인 필요]*
- Process gas and flow ratio: *[확인 필요: Ar only, or Ar/O₂ ratio]*
- Substrate temperature during deposition: *[확인 필요: room temperature or heated]*
- Deposition time and resulting film thickness: *[확인 필요; internal notes indicate a target thickness in the 50–100 nm range — please confirm the exact value used for the electrodes reported in Fig. S5–S7]*
- Post-deposition treatment: *[확인 필요: as-deposited, or annealed — temperature/time/atmosphere if applicable]*

Prior to arriving at the sputtering process above, NiO films were also attempted by a hydrothermal route; those films showed poor electrochromic switching behavior and were not used for the data reported in this manuscript. All NiO data reported here are from sputter-deposited films.

### 1.4 Device assembly (half-cells and full three-electrode device)

Both the single-electrode ("half-cell") test cells and the complete three-electrode MnWO₄‖Zn‖NiO device were assembled in a sandwich configuration inside ambient laboratory air, without the use of a glovebox. For the half-cells (Zn‖MnWO₄ or Zn‖NiO), a 1-mm-thick double-sided adhesive tape (3M) with a rectangular window (1.5 × 1.5 cm² active area) cut into its center was laminated onto the MnWO₄- or NiO-coated ITO substrate, so that the tape simultaneously defined the active-area spacer and provided an edge seal. A zinc electrode (foil or mesh — see note below) pre-mounted on a plain glass cover slide was then aligned over the tape to close the cell, and the resulting cavity was filled with 0.5 M aqueous ZnSO₄ electrolyte, injected through a small unsealed gap with a syringe, after which the fill point was sealed *[확인 필요: 실제 봉지(sealing) 방법 — 예: epoxy resin, additional tape]*. The complete three-electrode device was assembled using the same lamination procedure, but with a zinc frame electrode sandwiched between one MnWO₄-coated ITO substrate and one NiO-coated ITO substrate, each contacted independently so that the two electrodes could be addressed separately against the shared Zn electrode, giving the three-terminal wiring shown schematically in Fig. 1a–d.

It should be noted that the main-text device fabrication description refers to a "zinc foil frame," while the electrochemical measurement description refers to a "transparent Zn mesh" counter/reference electrode; these are not necessarily the same component, and it remains to be confirmed which form was actually used for the half-cells versus the full device (see Revision Notes). Both descriptions are retained here until this is clarified.

### 1.5 Material characterization

Scanning electron microscopy (SEM) images were collected on a field-emission SEM (JSM-7800F, JEOL) equipped with energy-dispersive X-ray spectroscopy (EDS, AZtec®, Oxford Instruments), at an accelerating voltage of *[확인 필요, 예: 5–15 kV]*; samples were imaged directly on the ITO growth substrate without a conductive coating *[확인 필요]*. Transmission electron microscopy (TEM) was carried out on a Talos G2 (Thermo Fisher Scientific) operated at 200 kV, on samples prepared by gently scraping the MnWO₄ film from the ITO substrate, dispersing the resulting powder in ethanol by brief sonication, and drop-casting the suspension onto a carbon-coated copper grid *[확인 필요: 정확한 시편 준비 절차]*. X-ray diffraction (XRD) patterns were collected on an Empyrean diffractometer (PANalytical) using Cu Kα radiation (λ = 1.5418 Å), over a scan range, step size, and scan rate of *[확인 필요, 예: 2θ = 10–60°, 0.02° step, 2° min⁻¹]*; the pattern in Fig. S3 was collected on powder scraped from the autoclave's PTFE liner wall (§1.2), while the pattern in Fig. 2d was collected directly on the thin film on ITO. X-ray photoelectron spectroscopy (XPS) was performed on a MultiLab 2000 (Thermo Fisher Scientific) with an Al Kα source, using a pass energy of *[확인 필요]* and binding energies calibrated to *[확인 필요, 예: adventitious C 1s = 284.8 eV]*. UV–Vis–NIR transmittance spectra (300–1500 nm) were collected on a Shimadzu spectrophotometer in transmission mode, using air as the 100% transmittance reference, so that the reported values include reflection/absorption losses from the glass/ITO substrate, electrolyte, and both electrodes of the assembled cell rather than the active layer alone; whether an integrating sphere was used, and the beam spot size/measurement geometry, remain to be confirmed *[확인 필요]*.

### 1.6 Electrochemical and electrochromic testing protocols

All electrochemical measurements were performed on a VSP potentiostat/galvanostat (Bio-Logic Science Instruments) at room temperature in ambient air, using a two-electrode configuration in which the MnWO₄- or NiO-coated ITO substrate served as the working electrode and the Zn foil/mesh served as the combined counter and reference electrode, so that all reported potentials are versus Zn/Zn²⁺. Cyclic voltammetry was recorded at a scan rate of 0.1 mV s⁻¹ (Fig. 3a, Fig. S4), over a voltage window of *[확인 필요, 본문상 대략 0–1.2 V로 추정 — 정확한 상·하한 확인 필요]*. Galvanostatic charge–discharge and rate-capability tests were carried out at current densities of 0.01, 0.02, 0.05, and 0.1 mA cm⁻² (Fig. 3b,c), with voltage cutoffs of *[확인 필요]*. Long-term cycling of the energy-storage performance was carried out for 200 consecutive charge–discharge cycles at 0.02 mA cm⁻² (Fig. 3d) and, separately, at 0.1 mA cm⁻² (Fig. 3e), with a rest time between cycles of *[확인 필요]*. Electrochromic (coloration/bleaching) cycling durability was assessed by switching the MnWO₄ half-cell between its bleached (1.2 V) and colored (0.0 V) states for 500 cycles (Fig. 4c), and the NiO half-cell between its bleached (1.0 V) and colored (2.3 V) states for 30 cycles (Fig. S7); the exact switching waveform used for both tests — specifically, the hold time at each voltage per cycle — is not yet specified in the draft and should be confirmed for reproducibility *[확인 필요]*. Areal capacity was calculated as *Q* (mAh cm⁻²) = *I* × *t* / *A*, where *I* is the applied current (mA), *t* is the discharge time (h), and *A* is the geometric active-device area (1.5 × 1.5 cm², §1.4); coulombic efficiency was calculated as the discharge areal capacity divided by the charge areal capacity, expressed as a percentage. Each of the four optical modes of the complete device (Fig. 5a,b) was set by independently biasing the MnWO₄ electrode to its bleached (1.2 V) or colored (0.0 V) state and the NiO electrode to its bleached (1.0 V) or colored (2.3 V) state, using the shared Zn electrode as the common reference for both.

### 1.7 Solar-simulator thermal imaging

A solar simulator was used to illuminate the assembled device from above, with a black heat-absorbing textile placed directly behind the device to mimic an interior surface (Fig. 5c). Surface temperature of the textile was recorded with an infrared (thermal) camera at 0, 10, 60, and 600 s after the start of illumination. *[확인 필요: solar simulator 기종 및 광량(예: AM 1.5G, 1-sun = 100 mW cm⁻²), 램프–시료 거리, IR 카메라 기종·모델, 검은 직물의 재질/흡수율, 측정 시 주변 온도/환기 조건]*. The same protocol, without the electrochromic device present (bare glass only), was used to obtain the reference curve in Fig. S8.

---

## 2. Supporting Figures

**Figure S1. Hydrothermal synthesis route for MnWO₄ films on ITO glass.**
Schematic flow diagram of the one-step synthesis described in §1.2: the precursor reagents (Na₂WO₄·2H₂O, Na₂SO₄, and the manganese precursor *[확인 필요: 본문에는 MnCl₂·4H₂O, 이 그림에는 Mn(CH₃COO)₂·4H₂O로 표기됨]*, together with HCl for pH adjustment) are combined with an ITO glass substrate inside a sealed autoclave and heated at 180 °C; after the hydrothermal step, the substrate emerges coated with a uniform MnWO₄ nanowire film (pale, translucent coating), ready for rinsing and drying.

**Figure S2. Selected-area electron diffraction (SAED) pattern of a MnWO₄ nanowire.**
Electron diffraction pattern collected on an individual nanowire (dark triangular shadow at image center is the sample holder/beam stop). The bright diffraction spots form a regular pattern consistent with a single-crystalline (rather than amorphous or randomly polycrystalline) nanowire; the spot circled and labeled "(110)" corresponds to the same lattice plane measured directly by lattice-fringe spacing in Fig. 2c (3.75 Å), cross-confirming that assignment by an independent method.

**Figure S3. X-ray diffraction pattern of bulk MnWO₄ powder collected from the autoclave liner wall.**
XRD pattern (blue trace) of MnWO₄ powder that nucleated on the inner wall of the PTFE autoclave liner during the same hydrothermal synthesis batch used for the ITO thin films (collected here rather than on the thin film itself because the bulk powder gives a stronger, background-free signal for phase confirmation; see §1.2). Vertical reference bars mark the standard peak positions for monoclinic MnWO₄. All measured peaks align with the reference pattern, and no unassigned peaks are present, corroborating the thin-film phase assignment in Fig. 2d. **Note:** the x-axis of this panel is currently mislabeled "Binding energy (eV)"; it should read "2θ (°)" — corrected in the next figure-artwork pass.

**Figure S4. Cyclic voltammogram of commercial WO₃, tested for comparison against MnWO₄.**
CV curve of a commercial WO₃ electrode (Zn‖WO₃ cell, 0.1 mV s⁻¹, same conditions as Fig. 3a) showing a single, broad redox feature associated with Zn²⁺ adsorption/insertion, in clear contrast to the multiple distinct, sharper redox features seen for MnWO₄ in Fig. 3a. This comparison supports the claim in the main text that MnWO₄ has substantially richer, more multi-step redox chemistry than conventional WO₃, underlying its higher energy-storage capacity.

**Figure S5. Reversible electrochromic switching of the NiO half-cell.**
Digital photographs of the Zn‖NiO cell (same "NVP" logo transparency reference as Fig. 4a) at 1.0 V (bleached, light tan/grey, logo clearly legible), after switching to 2.3 V (colored, dark brownish-grey, logo much harder to read), and after returning to 1.0 V (bleached state restored) — confirming that, like MnWO₄, the NiO electrode's coloration is optically reversible.

**Figure S6. Voltage-dependent transmittance of the NiO half-cell.**
Transmittance spectra (300–1500 nm) of the Zn‖NiO cell at four voltages (1.0, 2.0, 2.3, and 2.4 V, color-coded). Transmittance decreases progressively across the visible-light-dominated portion of the spectrum as voltage increases from 1.0 to 2.4 V, confirming that NiO coloration is primarily a visible-light-modulating (rather than near-infrared-selective) effect — the complementary spectral behavior to MnWO₄ (Fig. 4b), which is what allows the two electrodes to be combined for independent VIS/NIR control in the full four-mode device.

**Figure S7. Cycling stability of the NiO half-cell.**
Digital photographs comparing the colored-state appearance of the Zn‖NiO cell at the 1st and 30th coloration/bleaching cycle. The visibly similar appearance between the two indicates reasonable short-term reversibility, but cycling was only carried through 30 cycles in this study (compared with 500 cycles for MnWO₄, Fig. 4c) — consistent with the main-text observation that NiO cycling stability is more limited than MnWO₄'s, and flagged there as a target for future improvement rather than a solved problem.

**Figure S8. Reference thermal-imaging test with ordinary window glass (no electrochromic device).**
Infrared thermal images of the black heat-absorbing textile (same setup as Fig. 5c,d) placed behind a sheet of ordinary, uncoated window glass instead of the electrochromic device, at 0, 10, 60, and 600 s of solar-simulator illumination (same false-color temperature scale, 20–50 °C). The textile heats steadily and reaches the highest temperature of any condition tested in this study (24.5 → 38.1 → 40.3 → 42.1 °C), serving as the "no control" baseline against which the bright–warm and dark–cool performance of the actual device (Fig. 5d) is compared.
