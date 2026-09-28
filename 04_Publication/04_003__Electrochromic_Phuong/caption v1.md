# [수정 메모] 반드시 먼저 읽어주세요

> 이 섹션은 투고용 원고에 포함되지 않는 편집자용 메모입니다. 확인 후 삭제하세요.

## 확인해주셔야 할 사항

1. **Figure 3a의 "IV. Reverse Intercalation" 반응식 오타로 추정됩니다.** 그림에는 "III. Reverse Conversion"과 "IV. Reverse Intercalation" 두 라벨 모두 동일하게 `ZnₓMnO → MnO + xZn²⁺ + 2e⁻`로 표기되어 있습니다. 화학적으로 IV번(①의 역반응, 삽입 역반응)은 `ZnₓWO₃ → WO₃ + xZn²⁺ + 2e⁻`이어야 본문 및 Fig. 1f의 텅스텐 골격 설명과 일치합니다. 아래 캡션은 **올바른 반응식(ZnₓWO₃ 기준)으로 작성**했으니, 그림 파일(IV번 라벨)을 이에 맞춰 수정해 주세요.

2. **Figure S5의 새 CV 모양 그래프는 y축이 "Current density (a.u.)"로, 실측 데이터가 아니라 개념도(schematic)입니다.** (Figure 3a는 y축이 실측 단위 mA cm⁻²를 유지하고 있어 실제 데이터에 주석만 추가하신 것으로 보이지만, Figure S5의 새 그래프는 임의단위입니다.) SI에 개념도를 넣는 것 자체는 문제없지만, **리뷰어가 실측 CV로 오해하지 않도록 캡션에 "schematic"임을 명시**했습니다. 만약 실제로는 NiO의 정량적 CV 데이터를 측정해서 실측 곡선으로 바꾸실 계획이라면 캡션의 해당 문구(및 축 라벨의 "a.u.")를 그때 함께 수정해야 합니다.

3. Figure 5a에 새로 추가된 4가지 모드 개략도(회로도)는 사진 위에 잘 통합되어 있어 그대로 캡션에 반영했습니다.

---

## Figure 3

**Figure 3. Energy-storage performance of MnWO₄, tested as a battery-type electrode against a Zn counter-electrode, with the full four-step reaction pathway now annotated directly on the CV curve.**
**(a)** Cyclic voltammogram of the Zn‖MnWO₄ cell (0.1 mV s⁻¹). The plot is shaded and labeled to separate the two half-cycles: the lower, shaded branch is the discharge (reduction) half-cycle that colors the electrode ("Discharging (Reduction) → Colored"), and the upper, unshaded branch is the charge (oxidation) half-cycle that bleaches it ("Charging (Oxidation) → Bleached"). Four reactions are numbered directly on the curve. On discharge: **(I) Intercalation** — WO₃ + xZn²⁺ + 2e⁻ → ZnₓWO₃, in which Zn²⁺ ions insert into the tungsten-oxygen framework; **(II) Conversion** — MnO + xZn²⁺ + 2e⁻ → ZnₓMnO, in which the manganese-oxygen framework is reduced and structurally reorganized. On charging, both steps reverse in the opposite order: **(III) Reverse conversion** — ZnₓMnO → MnO + xZn²⁺ + 2e⁻; and **(IV) Reverse intercalation** — ZnₓWO₃ → WO₃ + xZn²⁺ + 2e⁻, which restores the bleached state. **(b)** Galvanostatic charge–discharge curves at 0.01–0.1 mA cm⁻², with plateaus matching the reactions in (a); the slowest rate delivers the largest areal capacity, ≈2 mAh cm⁻². **(c)** Rate capability over 25 cycles as the current density is stepped up and back down, showing capacity is largely recovered after fast cycling. **(d,e)** Cycling stability over 200 cycles at **(d)** 0.02 and **(e)** 0.1 mA cm⁻², showing stable areal capacity (left axis) and coulombic efficiency near 100% (right axis) throughout.

---

## Figure 5

**Figure 5. Performance of the complete four-mode MnWO₄‖Zn‖NiO device, including a solar heat-blocking demonstration.**
**(a)** Each of the four operating modes is shown as a paired schematic-and-photograph panel. The small circuit schematic above each photograph indicates the bleached/colored state of the MnWO₄ (NIR) module and the NiO (VIS) module, with arrows showing whether VIS and NIR light are transmitted through that module; the photograph directly below (same "NVP" logo transparency reference as Fig. 4a) shows the resulting visual appearance of the assembled device. **Bright–Warm** (MnWO₄ bleached, NiO bleached) is lightest/most transparent, with both VIS and NIR transmitted. **Bright–Cool** (MnWO₄ bleached, NiO colored) blocks VIS while still transmitting NIR. **Dark–Warm** (MnWO₄ colored, NiO bleached) blocks NIR while still transmitting VIS — the mirror-image state relative to Bright–Cool. **Dark–Cool** (MnWO₄ colored, NiO colored) is darkest, blocking both VIS and NIR. **(b)** Transmittance spectra (300–1500 nm) confirming this quantitatively: bright–warm gives the highest transmittance in both bands; bright–cool suppresses VIS while preserving NIR; dark–warm shows the mirror-image selectivity; dark–cool suppresses both. **(c)** Test setup: a solar simulator illuminates the device, a black heat-absorbing textile behind it mimics an interior surface, and an infrared camera tracks its temperature. **(d)** Infrared thermal images of the textile in bright–warm (top) and dark–cool (bottom) modes at 0, 10, 60, and 600 s. Bright–warm heats steadily (24.5→37.2 °C); dark–cool suppresses warming (24.5→31.1 °C) — after 600 s, dark–cool is ~6 °C cooler than bright–warm and ~11 °C cooler than ordinary glass (Fig. S8), showing the modes make a practically meaningful difference in transmitted heat.

---

## Figure S5

**Figure S5. Reversible electrochromic switching of the NiO half-cell, with the underlying reaction pathway summarized in a schematic cyclic voltammogram.**
**(Top)** Digital photographs of the Zn‖NiO cell (same "NVP" logo transparency reference as Fig. 4a) at 1.0 V (bleached, light tan/grey, logo clearly legible, labeled **1**), after switching to 2.3 V (colored, dark brownish-grey, logo much harder to read, labeled **2**), and after returning to 1.0 V (bleached state restored, labeled **1** again), confirming that, like MnWO₄, the NiO electrode's coloration is optically reversible. **(Bottom)** A schematic cyclic voltammogram (current density in arbitrary units, not a digitized experimental trace) links these same two states, numbered **1** and **2** to match the photographs above, and separates the cycle into its two half-reactions. The upper, orange branch is the charge (oxidation) half-cycle that colors the electrode ("Charging (Oxidation) → Coloring"): **(I) Oxidation**, Ni(OH)₂ → NiOOH + H⁺ + e⁻ (Ni²⁺ → Ni³⁺), proceeding as the voltage is raised toward 2.3 V. The lower, blue branch is the discharge (reduction) half-cycle that bleaches the electrode ("Discharging (Reduction) → Bleaching"): **(II) Reduction**, NiOOH + H⁺ + e⁻ → Ni(OH)₂ (Ni³⁺ → Ni²⁺), the reverse reaction that proceeds as the voltage is lowered back toward 1.0 V. Unlike MnWO₄, which is a cathodic material that colors at low voltage, NiO is an anodic material that colors at high voltage — this opposite voltage dependence is what allows the two electrodes to be combined for fully independent four-mode control (see also Fig. 1a–d and Fig. 3a). The reaction directions and single-redox-couple shape shown here follow the previously reported CV/XPS behavior of NiO thin-film electrodes (ref. 15), plotted here schematically over this device's own tested voltage window (1.0–2.4 V vs Zn/Zn²⁺).
