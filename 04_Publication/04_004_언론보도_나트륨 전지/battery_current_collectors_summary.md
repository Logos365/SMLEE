# 배터리 종류별 집전체(Current Collector) 정리

## 1. 집전체 선정의 핵심 원리

집전체 재료 선정은 다음 3가지 기준으로 결정된다.

1. **전기화학적 안정성**: 해당 전극 전위 영역에서 부식(산화 용해)이나 활물질과의 합금화 반응이 없어야 함
2. **전기전도도**: 내부 저항 최소화
3. **비용·비중**: 에너지밀도 및 제조 단가에 영향

### Cathode / Anode 용어 정리

| 한국어 | 영어 | 극성 | 반응(방전 기준) |
|---|---|---|---|
| 양극 | Cathode (캐소드) | + (positive) | 환원(reduction) |
| 음극 | Anode (어노드) | − (negative) | 산화(oxidation) |

> 이차전지는 충전 시 반응이 뒤바뀌지만, 업계·논문 관행상 **방전 기준**으로 명칭을 고정한다 (흑연 전극은 항상 Anode, NCM/LFP는 항상 Cathode).

### 전기전도도 비교 (참고: Cu 5.96×10⁷ S/m vs Al 3.77×10⁷ S/m, Samsung SDI Tech Blog)

| 금속 | 전기전도도 (MS/m) | 비고 |
|---|---:|---|
| Cu | 59.6 | 가장 높음, 하지만 밀도(8.96 g/cm³) 높아 무거움 |
| Al | 37.7 | Cu 대비 저비중(2.7 g/cm³), 저비용 |
| Ti | 2.34 | 내식성 우수하나 전도도 낮음, 고가 |
| SUS304 | 1.39 | Ti보다 저렴, 유사한 내식성 |

---

## 2. 전지 종류별 집전체 정리

| 전지 종류                   | Cathode(양극,+) 집전체                            | Anode(음극,−) 집전체                       | 선정 이유                                                                                                                          |
| ----------------------- | -------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **리튬이온전지 (LIB)**        | **Al** foil                                  | **Cu** foil                           | Al: 표면 Al₂O₃ 부동태막 → 고전압 안정. Cu: 저전위에서 Li와 합금화하지 않음, 3.385V 이상에서만 산화                                                            |
| **리튬금속전지 / Anode-free** | **Al** foil                                  | **Cu** foil (3D 구조·리소필릭 코팅 등 표면개질 활발) | 기본 원리는 LIB와 동일. 다만 Li-Cu 간 큰 갈바닉 전위차(Li −3.0V vs Cu +0.8V)로 갈바닉 부식 문제 → Cu 표면 개질(3D 다공성 구조, artificial SEI, 친리튬성 코팅)이 핵심 연구 주제 |
| **나트륨이온전지 (SIB)**       | **Al** foil                                  | **Al** foil (Cu 대체 가능)                | Na은 저전위에서 Al과 합금 반응을 일으키지 않음 → 음극 집전체를 Cu에서 Al로 대체 가능 → 비용·중량 절감 (SIB 상업적 장점)                                                  |
| **아연이온전지 (수계 ZIB)**     | **Ti, 스테인리스강(SUS304/316)**, 탄소계(그래핀/CNT 페이퍼) | **Zn 금속 자체** (또는 Zn 도금 Ti/SUS/황동)     | 수계 ZnSO₄ 전해질에서 Ni, Al, Cu는 심각한 부식 발생. Ti·SUS는 수계 환경에서 우수한 내식성과 젖음성 보유 (SUS가 Ti 대비 저비용 대안으로 제안됨)                                |

### 케이스별 보충 설명

- **Li-metal/Anode-free**: Li(-3.0V)와 Cu(+0.8V)의 갈바닉 전위차로 계면 부식이 발생해 Li이 다공질화·박리되는 문제 → 3D 구조화, 인공 SEI, 친리튬성 표면처리 연구가 활발
- **Na-ion**: Na-Al 합금화 반응 자체가 존재하지 않는다는 점이 결정적. 다만 상용화 초기 단계에서는 Cu를 여전히 쓰는 경우도 많음
- **Zn-ion**: LIB/SIB와 달리 "합금화" 기준이 아니라 **수계 전해질 내 부식 저항성**이 지배적 선정 기준. Al의 부동태막(Al₂O₃)이 약산성 수계 환경에서 쉽게 파괴되어 오히려 가장 취약한 금속 중 하나가 됨

---

## 3. 표준환원전위와의 관계

### 3-1. 표준환원전위 (E°, vs SHE, 25°C 1M 수용액 기준)

| 산화환원쌍 | E° (V vs SHE) |
|---|---:|
| Li⁺/Li | −3.04 |
| Al³⁺/Al | −1.66 |
| Zn²⁺/Zn | −0.76 |
| Cu²⁺/Cu | +0.34 |

Li가 가장 반응성이 크고(전자를 잃기 쉬움), Cu가 가장 귀금속성(부식에 강함)을 가진다는 **정성적 서열**을 잘 설명한다.

### 3-2. Li/Li⁺ 기준으로 변환 (배터리 분야 표준 기준전극)

$$E_{X\, vs\, Li/Li^+} = E°_{X\, vs\, SHE} - E°_{Li^+/Li\, vs\, SHE} = E°_X + 3.04\text{ V}$$

| 금속 | 계산값 (V vs Li/Li⁺) | 실측 문헌값 | 일치 여부 |
|---|---:|---|---|
| Cu | 0.34 + 3.04 = **3.38 V** | 3.385 V (Cu 산화 개시 전위) | ✅ 거의 정확히 일치 |
| Al | −1.66 + 3.04 = **1.38 V** | 0.1~0.3 V (Al-Li 합금화 개시) | ❌ 크게 어긋남 |

### 3-3. 왜 Cu는 맞고 Al은 안 맞는가

| 구분 | Cu | Al |
|---|---|---|
| 반응 메커니즘 | 단순 금속→이온 용해 (Cu → Cu²⁺ + 2e⁻) | 고체상 Li 삽입에 의한 금속간화합물(LiAl) 형성 — 이원계 상평형도 자유에너지로 결정 |
| 부동태막 영향 | 미미 | Al₂O₃ 자연산화막이 반응을 kinetically 억제 → 열역학값과 실측 개시전위 괴리 |
| 전해질 기준 | SHE(수용액) → Li/Li⁺(유기전해질) 변환 시 오차 존재 | 상동 |

**결론**: 표준환원전위는 "어떤 금속이 더 반응성이 큰가"라는 **정성적 서열**(Li ≫ Al > Zn > Cu)을 설명하는 데는 유효하나,
- 단순 용해/석출 반응(Cu, Zn) → 정량적으로도 잘 맞음
- 합금화·삽입 반응(Al-Li 등) → 상평형도 기반 자유에너지, 부동태막 형성 여부를 별도로 고려해야 함

---

## 참고문헌 (검색 기반)

1. Samsung SDI Tech Blog, "[1-Minute Battery] Why Aluminum for the Cathode and Copper for the Anode?" (2025) — https://news.samsungsdi.com/global/articleView?seq=272
2. さぷり。, "Current Collectors in Lithium-Ion Batteries: Why Al for the Cathode and Cu for the Anode?" (2025) — https://note.com/vast_slug4459/n/n818e026f044e
3. Zhou et al., "Copper Current Collector: The Cornerstones of Practical Lithium Metal and Anode-Free Batteries," ChemPhysChem (2024) — https://pubmed.ncbi.nlm.nih.gov/38318964/
4. "Anode-free sodium metal batteries: optimisation of electrolytes and interphases," Energy & Environmental Science (2025) — https://pubs.rsc.org/en/content/articlehtml/2025/ee/d5ee00136f
5. "Stainless steel foil: A more appropriate current collector than titanium foil for the cathodes of aqueous zinc ion batteries," ScienceDirect (2022) — https://www.sciencedirect.com/science/article/abs/pii/S0013468622016760
6. "Influence of current collector materials on the electrochemical performance of aqueous zinc-ion batteries," J. Mater. Chem. A (2026) — https://pubs.rsc.org/en/content/articlehtml/2026/ta/d5ta07993d
7. "A review of current collectors for lithium-ion batteries," Journal of Power Sources, ScienceDirect (2020) — https://www.sciencedirect.com/science/article/abs/pii/S0378775320316098
8. "3D Porous Cu-Composites for Stable Li-Metal Battery Anodes" (Li/Li⁺ vs SHE = −3.04V) — https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10416568/
9. 표준환원전위(vs SHE) 값: CRC Handbook of Chemistry and Physics 등 표준 전기화학 교재 값 (일반 통용값)

*본 문서는 Claude와의 대화(2026-09-01)를 기반으로 정리되었습니다. 원문헌 확인을 권장합니다.*
