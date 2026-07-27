# ALD 산화물 코팅을 통한 나트륨 이온 전지 양극재 성능 개선
## 연구 검토 보고서

> **작성 목적**: High-nickel 계열 SIB 양극재에 ALD 산화물 코팅을 적용하여 에너지 밀도 160 Wh/kg 및 수명 특성 개선 가능성 검토
> **작성일**: 2026-06-09

---

## 목차

1. [ALD 코팅의 문헌적 근거 및 기본 효과](#1-ald-코팅의-문헌적-근거-및-기본-효과)
2. [코팅 소재별 성능 비교](#2-코팅-소재별-성능-비교)
3. [160 Wh/kg 에너지 밀도 달성 경로](#3-160-whkg-에너지-밀도-달성-경로)
4. [V₂O₅ ALD 코팅의 가능성](#4-v₂o₅-ald-코팅의-가능성)
5. [High-nickel 양극재에서 V₂O₅ vs Al₂O₃/TiO₂ 비교](#5-high-nickel-양극재에서-v₂o₅-vs-al₂o₃tio₂-비교)
6. [V₂O₅/TiO₂ 이중층 ALD 설계](#6-v₂o₅tio₂-이중층-ald-설계)
7. [최종 연구 전략 제안](#7-최종-연구-전략-제안)
8. [참고 문헌](#8-참고-문헌)

---

## 1. ALD 코팅의 문헌적 근거 및 기본 효과

### 1.1 결론 요약

ALD(원자층 증착) 산화물 코팅은 나트륨 이온 전지(SIB) 양극재의 **수명 특성 개선에 이미 검증된 방법**이다. 단, 160 Wh/kg은 소재 수준이 아닌 **셀 시스템 수준의 목표**임을 먼저 구분해야 한다.

### 1.2 ALD의 기술적 우위

| 항목     | ALD              | 습식코팅   | 건식코팅  |
| ------ | ---------------- | ------ | ----- |
| 두께 제어  | **Å 수준**         | 수십 nm  | nm~μm |
| 균일성    | **완전 conformal** | 불균일    | 부분 접촉 |
| 기재 손상  | **없음**           | 열처리 필요 | 낮음    |
| 양산 확장성 | 낮음 (고비용)         | 중간     | 높음    |
| 성능 재현성 | **매우 높음**        | 중간     | 중간    |

### 1.3 핵심 문헌 데이터

- **Al₂O₃ ALD on O3-NNCm**: 반쪽 전지 151 mAh/g, 파우치 전지 300사이클 후 75% 용량 유지, 130 Wh/kg (Ji et al.)
- **Al₂O₃ ALD 메커니즘**: HF 공격으로부터 양극 표면 보호 → AlF₃ 보호층 in-situ 형성
- **ZrO₂ ALD**: 전해질 부식 완화, Na₂CO₃ 형성 억제
- **TiO₂/Al₂O₃ 이중층 ALD on LLO**: 100사이클 후 ~90.4% 용량 유지율, 146 mAh/g (Chen et al., ACS AMI, 2024)

### 1.4 ALD 코팅 메커니즘 정리

```
HF 공격 차단
  → 전해질 분해 생성물 HF로부터 양극 보호
  → Al₂O₃ → AlF₃ 변환으로 보호층 재생

Na₂CO₃ 형성 억제 (ZrO₂)
  → 표면 탄산화 방지
  → 계면 임피던스 증가 억제

상전이 억제 (TiO₂, SnO₂)
  → P2→O2, O3→P3 비가역 상전이 완화
  → 전압 안정성 향상

전이금속 용출 억제 (공통)
  → Mn, Ni 용출 차단
  → 애노드 오염 방지, 용량 유지
```

---

## 2. 코팅 소재별 성능 비교

### 2.1 주요 ALD 코팅 소재 가이드

| 산화물                | 주요 기능              | 최적 두께    | 적합 양극 구조           |
| ------------------ | ------------------ | -------- | ------------------ |
| **Al₂O₃**          | HF 차단, AlF₃ 보호층 형성 | 1–3 nm   | O3형 (Ni-rich)      |
| **ZrO₂**           | Na₂CO₃ 억제, 구조 안정화  | 2–4 nm   | P2형, O3형           |
| **TiO₂**           | 이온 전도성, 상전이 억제     | 1–3 nm   | P2형                |
| **TiO₂/Al₂O₃ 이중층** | 복합 보호, 이중 메커니즘     | 총 3–5 nm | Li-rich, SIB 적용 가능 |

### 2.2 문헌 기반 전기화학 성능 비교

| 코팅                 | 비용량 (mAh/g) | 용량유지율 (%) | 사이클 수 | 전지 구성           |
| ------------------ | ----------- | --------- | ----- | --------------- |
| Al₂O₃ ALD          | 151         | 75        | 300   | Full cell (파우치) |
| TiO₂ ALD           | ~145        | 78        | 100   | Half cell       |
| Al₂O₃/TiO₂ ALD     | 146         | 90.4      | 100   | Half cell       |
| V₂O₅ 습식 (NCA)      | 163         | 83        | 200   | Half cell       |
| **V₂O₅ ALD (SIB)** | **미확인**     | **미확인**   | —     | **연구 공백**       |

---

## 3. 160 Wh/kg 에너지 밀도 달성 경로

### 3.1 상용 현황

- **CATL Naxtra (2024)**: EV용 SIB, ~175 Wh/kg
- **CATL BESS용 SIB (2026 ESIE)**: 300 Ah 이상 대형 포맷, **160 Wh/kg**, 시스템 에너지 변환 효율 97%, 15,000사이클 이상 (80% 유지)
- **HiNa**: 140–150 Wh/kg 수준

### 3.2 소재 수준 요구 조건

160 Wh/kg 셀 목표를 위해 **소재 수준**에서 필요한 것:

```
양극 비용량   ≥ 150–160 mAh/g
작동 전압     ≥ 3.2–3.5 V (vs. Na/Na⁺, 평균)
N/P 비율      최적화 (1.05–1.15)
전극 로딩량   ≥ 3.0 mAh/cm²
전해질        Na⁺ 전도성 최적화
```

> ⚠️ **주의**: ALD 코팅만으로 160 Wh/kg이 달성되는 것이 아님. 코팅은 주로 **수명 특성(cycle life)** 및 **율속 특성** 개선에 기여하며, 에너지 밀도는 셀 설계 전체의 결과임.

### 3.3 ALD 코팅의 역할

```
ALD 코팅의 기여 영역
├── 수명 특성 (Cycle Life)     ★★★★★ 주요 기여
├── 율속 특성 (Rate Capability) ★★★★☆
├── 초기 용량                   ★★☆☆☆ (두꺼우면 오히려 감소)
└── 에너지 밀도 (직접 기여)      ★★☆☆☆ (간접적, 용량 유지로 기여)
```

---

## 4. V₂O₅ ALD 코팅의 가능성

### 4.1 V₂O₅의 두 가지 역할 구분

| 역할 | 내용 | ALD 적용 현황 |
|------|------|--------------|
| **① 양극 활물질** | V₂O₅ 자체가 Na⁺ 저장층 | ALD 합성 사례 있음 (LIB 중심) |
| **② 코팅층** | 레이어드 옥사이드 표면 보호막 | **습식/건식 위주, ALD는 미확인** |

### 4.2 V₂O₅ ALD 합성 현황

- **전구체**: VO(thd)₂ + O₃, 공정 온도 215°C
- **성장률**: ~0.2 Å/cycle (Al₂O₃의 TMA 대비 복잡)
- **박막 성능**: 비정질 30 nm V₂O₅, 1C 100사이클 후 330 mAh/g (Chen et al.)
- **상 제어**: 공정 조건에 따라 결정성/비정질 VOₓ 선택 가능

### 4.3 V₂O₅ 코팅층으로서의 고유 장점 (High-nickel 기준)

#### Li/Na 잔류물 제거 — Al₂O₃·TiO₂에 없는 고유 기능
V₂O₅는 high-nickel 양극재 표면의 리튬 잔류물(LiOH, Li₂CO₃)과 직접 반응:

```
V₂O₅ + 2LiOH → 2LiVO₃ + H₂O
V₂O₅ + Li₂CO₃ → 2LiVO₃ + CO₂
```

→ **생성된 LiVO₃/Li₃VO₄는 Li⁺ 전도성 물질** (Nb₂O₅→LiNbO₃ 유사 메커니즘)

- V₂O₅/rGO 코팅 LiNi₀.₈₄Co₀.₁₁Mn₀.₀₅O₂: 1C 100사이클 후 90.43% 유지, 10C에서 145.7 mAh/g
- V₂O₅ 코팅 NCA: 200사이클 후 88.39% (미코팅 대비 +22%)

#### 혼합 이온-전자 전도성 (MIEC)
V⁵⁺/V⁴⁺/V³⁺ 다중 산화 환원 쌍 → 계면 임피던스 증가 최소화

> Al₂O₃ 코팅 NMC의 경우 코팅 전 RCT = 74.7 Ω → 코팅 후 323.0 Ω로 증가 (Herzog et al., 2021)

#### 산소 방출 억제
표면 V⁵⁺이 비가역 산소 방출 및 레이어드→스피넬 상전이를 동시 억제 (Li-rich 계 기준 74% → 92% 용량 유지)

### 4.4 V₂O₅ ALD의 치명적 위험 요인

```
⚠️ 코팅층 자체의 전기화학적 활성
   V₂O₅ 운전 전압: 2.0–3.5 V (vs. Li⁺/Li)
   SIB 양극 운전 전압: 2.0–4.2 V
   → 전압 범위 상당 부분 겹침

결과:
  두꺼운 V₂O₅ 코팅 → 독립 전극으로 반응
  → 전압 프로파일 교란
  → 전해질과 추가 부반응
  → 오히려 성능 저하

해결책:
  ALD의 Å 수준 두께 제어 활용
  → 1–2 nm (약 5–10 ALD 사이클) 이하로 제한
  → 비정질(amorphous) VOₓ 상태 선호
```

### 4.5 SIB 환경의 추가 고려사항

Na⁺ 이온 반경(1.02 Å) vs Li⁺(0.76 Å):
- V₂O₅ 코팅층 내 Na⁺ 확산 경로 불리 → 임피던스 증가 위험
- NaₓV₂O₅ 구조가 LiₓV₂O₅보다 불안정
- **비정질 VOₓ 코팅이 결정성 V₂O₅보다 SIB에서 유리**

---

## 5. High-nickel 양극재에서 V₂O₅ vs Al₂O₃/TiO₂ 비교

### 5.1 메커니즘별 상세 비교

| 메커니즘 | Al₂O₃ ALD | TiO₂ ALD | Al₂O₃/TiO₂ 이중층 | V₂O₅ ALD (예측) |
|---------|-----------|----------|------------------|----------------|
| HF 차단 | ★★★★★ 우수 | ★★★☆☆ 양호 | ★★★★★ 우수 | ★★★☆☆ 양호 |
| Li 잔류물 제거 | ★☆☆☆☆ 미흡 | ★☆☆☆☆ 미흡 | ★☆☆☆☆ 미흡 | **★★★★★ 우수** |
| 이온 전도성 | ★☆☆☆☆ 낮음 | ★★★☆☆ 양호 | ★★★☆☆ 양호 | **★★★★★ 우수** |
| 전자 전도성 | ★☆☆☆☆ 낮음 | ★★☆☆☆ 보통 | ★★☆☆☆ 보통 | **★★★★☆ 우수** |
| 상전이 억제 | ★★★☆☆ 양호 | ★★★☆☆ 양호 | ★★★★☆ 우수 | ★★★☆☆ 양호 |
| 산소 방출 억제 | ★★★☆☆ 양호 | ★★★☆☆ 양호 | ★★★☆☆ 양호 | **★★★★★ 우수** |
| 코팅층 안정성 | ★★★★★ 불활성 | ★★★★☆ 거의 불활성 | ★★★★★ 불활성 | ★★☆☆☆ 활성 위험 |

### 5.2 총평

V₂O₅ ALD는 Al₂O₃/TiO₂와 **동일한** 효과를 내는 것이 아니라 **더 광범위한 효과**가 기대되나, 코팅층 자체의 전기화학 활성이라는 치명적 위험이 존재한다.

- **V₂O₅가 Al₂O₃를 완전히 대체할 수 없는 이유**: HF 차단 능력 열세, 코팅층 불안정성
- **V₂O₅가 Al₂O₃보다 우수한 이유**: Li/Na 잔류물 제거, 이온·전자 전도성, 산소 방출 억제

---

## 6. V₂O₅/TiO₂ 이중층 ALD 설계

### 6.1 V₂O₅/TiO₂ 이종접합의 시너지

V₂O₅/TiO₂ 이종접합은 독립 소재보다 우수한 전기화학 특성을 보인다:

- **Rct 감소**: V₂O₅/TiO₂ 이종접합 202.4 Ω vs V₂O₅ 단독 687.6 Ω (약 1/3 수준)
- **메커니즘**: TiO₂ 밴드 구조가 V₂O₅의 polaron-격자 상호작용을 약화 → polaron 호핑 속도 향상 → 이온 확산 제한 거동으로 전환
- **시너지 효과**: V₂O₅의 다중 레독스 + TiO₂의 구조적 안정성 결합

### 6.2 V₂O₅/Al₂O₃ vs V₂O₅/TiO₂ 비교

| 항목 | V₂O₅/Al₂O₃ | V₂O₅/TiO₂ |
|------|------------|-----------|
| HF 차단 | ★★★★★ 매우 우수 | ★★★☆☆ 보통 |
| 계면 저항 (Rct) | 증가 위험 | **최소화 가능** |
| 이종접합 시너지 | 약함 | **강함** |
| V₂O₅ 활성 억제 | 우수 (Al₂O₃ 절연) | 보통 |
| Na⁺ 확산 (SIB) | 제한 | **양호** |
| ALD 공정 온도 호환 | 가능 | **가능 (더 용이)** |
| SIB 분야 선례 | 없음 | **없음 (연구 공백)** |

### 6.3 층서(Layer Order)의 결정적 중요성

#### ✅ 권장 구조: V₂O₅(내층) / TiO₂(외층)

```
[High-Ni SIB 양극재]
        ↕  화학 반응 계면
[V₂O₅ ALD, ~1 nm]
  역할: Li/Na 잔류물 제거
        산소 방출 억제
        이온/전자 전도성 확보
        ↕  이종접합 형성
[TiO₂ ALD, ~1–2 nm]
  역할: 전해질 직접 접촉 차단
        Rct 최소화
        구조적 기계적 지지
        V₂O₅ 전기화학 활성 외부 차단
        ↕  전해질 접촉면
[전해질]
```

#### ❌ 비권장 구조: TiO₂(내층) / V₂O₅(외층)

```
[High-Ni SIB 양극재] / [TiO₂] / [V₂O₅]
  → V₂O₅가 전해질과 직접 접촉
  → 전기화학 활성화 및 용해 위험 극대화
  → 성능 저하 가능성 높음
```

### 6.4 TiO₂ 코팅 단독 문헌 성능

- **TiO₂–LiF 복합 코팅 NCM622**: 200사이클 후 79.7% (미코팅 68.9%) (Huang et al., RSC, 2023)
- **Ti³⁺ 도핑 TiO₂ 코팅 NCM622**: 150사이클 후 95.1% (미코팅 79.9%, TiO₂ 코팅 92.8%) (Xi et al.)
- **SIB TiO₂ 코팅**: TiO₂가 NLNMO 양극의 격자 산소 함량 유지 효과 확인 (Sun et al., 2024)

---

## 7. 최종 연구 전략 제안

### 7.1 단계별 연구 로드맵

#### Phase 1: 단층 ALD 코팅 기준선 확보
```
대상 양극재: O3형 High-Ni SIB (예: Na[Ni₀.₆Co₀.₂Mn₀.₂]O₂)

실험군:
  A) Al₂O₃ ALD (2–4 nm) — 기준 시료
  B) TiO₂ ALD (2–4 nm)
  C) V₂O₅ ALD (1–2 nm) — 비정질 VOₓ 타겟

평가 항목:
  - 전기화학: 비용량, 용량 유지율, 율속 특성
  - 계면 분석: EIS, XPS, TEM-EELS
  - 구조 분석: GIXRD, Raman
```

#### Phase 2: 이중층 ALD 구조 탐색
```
실험군:
  D) V₂O₅(1 nm) / Al₂O₃(1 nm)
  E) V₂O₅(1 nm) / TiO₂(1–2 nm)   ← 핵심 독창적 구조
  F) TiO₂(1 nm) / Al₂O₃(1 nm)    — 비교 기준 (문헌 검증됨)

층서 비교:
  E-1) [양극재] / V₂O₅ / TiO₂
  E-2) [양극재] / TiO₂ / V₂O₅    — 비권장, 대조군
```

#### Phase 3: 최적화 및 메커니즘 규명
```
최적 조건에서:
  - ALD 사이클 수 최적화 (두께 의존성)
  - 공정 온도 영향 (비정질 vs 결정성 VOₓ)
  - In-situ/operando 분석 (V 산화 상태 변화 추적)
  - Full cell (hard carbon 음극) 성능 검증
```

#### Phase 4: 스케일업 방향 도출
```
ALD 최적 조건 → 습식/건식 코팅 가이드라인 제시
산업화 feasibility study
```

### 7.2 기대 성과 및 독창성

| 항목 | 내용 |
|------|------|
| **연구 공백** | V₂O₅ ALD 코팅을 SIB 양극재에 적용한 사례 전무 |
| **독창성** | V₂O₅/TiO₂ ALD 이중층의 SIB 양극재 적용 최초 |
| **차별성** | KIMM ALD 역량 + SIB 소재 연구의 결합 |
| **기대 효과** | Li/Na 잔류물 제거 + Rct 최소화 + 수명 개선 동시 달성 |

### 7.3 핵심 연구 질문

1. V₂O₅ ALD 코팅이 SIB high-nickel 양극재 표면의 Na 잔류물과 반응하여 NaVO₃/Na₃VO₄를 형성하는가?
2. 생성된 바나데이트 상은 Na⁺ 전도성을 가지는가? (LiNbO₃ 유사)
3. V₂O₅/TiO₂ 이중층에서 이종접합 밴드 정렬이 SIB 환경에서도 Rct 감소를 유도하는가?
4. 비정질 VOₓ와 결정성 V₂O₅ ALD 코팅의 SIB 성능 차이는?

---

## 8. 참고 문헌

### ALD 코팅 SIB 양극재

1. Ji, G. et al. "ALD oxide coatings on P3/P2 layered Na₂/₃Ni₁/₃Mn₂/₃O₂ cathode." *J. Electrochem. Soc.* (2021)
2. Sun, R. et al. "Recent progress of interface modification of layered oxide cathode material for sodium-ion batteries." *Electron* 2024, Wiley.
3. Zhou, Y. et al. "Al₂O₃ ALD coating on P2-type Na₂/₃[Ni₁/₃Mn₂/₃]O₂: 73.2% retention after 300 cycles." Interface Issues review, *PMC* (2024)

### V₂O₅ 코팅 High-nickel 양극재 (습식)

4. Mao, G. et al. "V₂O₅ coating NCA by spray drying: 88.39% retention after 200 cycles (+22% vs bare)." *J. Alloys Compd.* 892, 162161 (2022)
5. Wang, L. et al. "V₂O₅/rGO dual coating on LiNi₀.₈₄Co₀.₁₁Mn₀.₀₅O₂: 90.43% retention at 1C/100cy, 145.7 mAh/g at 10C." *Appl. Surf. Sci.* (2022)
6. Wang, H. et al. "V₂O₅ coating on NMC 111." *Electrochim. Acta* (2024)

### V₂O₅ ALD 박막 합성

7. Chen, X. et al. "ALD V₂O₅ thin films from VO(thd)₂/O₃ at 215°C: 330 mAh/g at 1C/100cy." *Chem. Mater.* (2012)
8. O'Donoghue, A. et al. "Nanoengineering of V₂O₅ cathode interfaces via ALD." *Batteries & Supercaps* (2023). DOI: 10.1002/batt.202300447

### TiO₂/Al₂O₃ 이중층 ALD

9. Chen, W.-M. et al. "Advanced TiO₂/Al₂O₃ Bilayer ALD Coatings for Improved Li-Rich Layered Oxide Electrodes." *ACS Appl. Mater. Interfaces* 2024. DOI: 10.1021/acsami.3c16948

### V₂O₅/TiO₂ 이종접합

10. Kim, D. et al. "V₂O₅/TiO₂@Ti₃C₂ MXene: Rct = 202.4 Ω vs V₂O₅ 687.6 Ω." *ACS Appl. Mater. Interfaces* (2024). DOI: 10.1021/acsami.4c10656
11. Park, S. et al. "V₂O₅/TiO₂/SnO₂ ternary nanocomposites for supercapacitor." *J. Mol. Struct.* (2025)
12. Liu, J. et al. "Enhancing V₂O₅ cathode performance through heterostructure: polaron hopping kinetics." *J. Phys. Chem. C* 128, 10774 (2024)

### TiO₂ 코팅 NCM 계열

13. Xi, X. et al. "Ti³⁺ doped TiO₂ coating NCM622: 95.1% retention after 150 cycles." *J. Alloys Compd.* (2021)
14. Huang, K. et al. "TiO₂–LiF composite coating NCM622: 79.7% retention after 200 cycles." *RSC Advances* (2023)
15. Zhang, Y. et al. "TiO₂-coated NCM622 at high cutoff voltage: 163.9 mAh/g after 150 cycles." *MDPI Inorganics* (2024)

### 상용 SIB 현황

16. CATL Naxtra 기술 발표 자료 (2024); CATL BESS SIB, ESIE 2026 발표

---

*본 문서는 연구 검토 목적으로 작성되었으며, 수록된 성능 데이터는 각 문헌의 실험 조건에 종속됩니다.*
*ALD 코팅 조건(전구체, 온도, 사이클 수)에 따라 실제 성능은 달라질 수 있습니다.*
