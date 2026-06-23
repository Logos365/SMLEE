# 검토 보고서: 20260622_Responses to the comments of the reviewers_v3_revised.pdf

**검토 일자:** 2026-06-23  
**검토 대상:** Response letter to reviewers (R-1/16 ~ R-16/16)

---

## 1. 오타 (Typo)

### T-1 | R-6/16 — 마침표와 쉼표 중복
**위치:** Reviewer 1, C2 Response, pH discussion 단락

**원문:**
> "...in the context of the proposed mechanism., In 6 M KOH..."

**문제:** 마침표(`.`)와 쉼표(`,`)가 동시에 사용되고 `In`이 불필요하게 대문자로 시작됨.

**수정안:**
> "...in the context of the proposed mechanism. In 6 M KOH..."

---

## 2. 어색한 표현 (Awkward Expression)

### E-1 | R-6/16 — `likely`의 위치 오류
**위치:** Reviewer 1, C2 Response, pH discussion 단락

**원문:**
> "Under acidic conditions, likely the abundant proton supply (H⁺ activity ≈ 1 M) directly enables the reversible redox reaction..."

**문제:** `likely`가 주어 앞에 위치하여 문법적으로 어색함.

**수정안:**
> "Under acidic conditions, the abundant proton supply (H⁺ activity ≈ 1 M) likely directly enables the reversible redox reaction..."

---

### E-2 | R-8/16 — 비격식 표현
**위치:** Reviewer 1, C2 Response 마무리 문장

**원문:**
> "Except for the above revisions, we have revised and added some sentences and figures in the revised manuscript. So, we would be very pleased if you take a close look at the revised manuscript."

**문제:** `So,`로 시작하는 문장과 `take a close look`은 학술 서신에 어울리지 않는 구어체 표현.

**수정안:**
> "In addition to the above revisions, further modifications have been made throughout the manuscript. We kindly invite you to review the revised manuscript in its entirety."

---

### E-3 | Figure 6 caption (R-8/16, R-9/16) — 패널 레이블 표기 불일치
**위치:** Reviewer 1, C3 Response 및 원고 삽입 텍스트

**원문:**
> "**a)** CV curves and **(b)** GCD profiles of one, two, and three cells connected in series; **c)** Photographs..."

**문제:** `a)`, `c)`는 괄호 없이, `(b)`만 괄호가 있어 표기가 불일치함.

**수정안:** 아래 중 하나로 통일
- `a)`, `b)`, `c)` — 괄호 없는 형식
- `(a)`, `(b)`, `(c)` — 괄호 있는 형식

---

## 3. 과학적 오류 (Scientific Error)

### S-1 | R-5/16 — Na₂SO₄를 알칼리 전해질로 잘못 분류 ⚠️ **(중요)**
**위치:** Reviewer 1, C2 Response, cycling stability 설명 — Point i

**원문:**
> "All literature systems in Table S2 that report >87 % retention were measured in **alkaline (KOH or Na₂SO₄)** electrolytes, where nitrogen-related redox reactions are generally less pronounced and less structurally perturbative."

**문제:** Na₂SO₄ 수용액은 중성 염 용액으로 pH ≈ 7이며, 알칼리성이 아님. KOH(pH ≈ 14)와 동일한 범주인 "alkaline"으로 분류하는 것은 명백한 과학적 오류. 리뷰어가 지적할 가능성이 높음.

**수정안:**
> "All literature systems in Table S2 that report >87 % retention were measured in **neutral (Na₂SO₄) or alkaline (KOH)** electrolytes, where nitrogen-related redox reactions are generally less pronounced and less structurally perturbative."

---

## 4. 논리 문제 (Logic Issue)

### L-1 | R-5/16 — 스캔 속도 논거의 자기 모순 ⚠️ **(중요)**
**위치:** Reviewer 1, C2 Response, cycling stability 설명 — Points iii & iv

**Point iii 주장 (원문):**
> "The cycling test in H₂SO₄ was performed at 100 mV s⁻¹ (Figure S7d), a relatively fast scan rate that maximizes the contribution of pseudocapacitive processes and **can accelerate degradation**."

**Point iv 주장 (원문):**
> "In contrast, the two-electrode KOH measurement at **200 mV s⁻¹** yields 89.2 % retention after 10,000 cycles — twice as many cycles as the H₂SO₄ test..."

**문제:** Point iii에서 "빠른 스캔 속도(100 mV s⁻¹)가 열화를 가속한다"고 주장하면서, Point iv에서는 더 빠른 스캔 속도(200 mV s⁻¹)의 KOH 테스트가 더 우수한 용량 유지율(89.2%)을 보인다고 제시함. 스캔 속도 논거가 자기 모순됨. KOH에서의 우수한 결과는 스캔 속도가 아닌 **전해질 특성(EDLC-dominated vs. proton-coupled redox)의 차이**가 주 원인임.

**권장 수정 방향:**  
Point iii에서 스캔 속도는 부가적 요인으로만 언급하고, H₂SO₄에서의 낮은 용량 유지율의 **주 원인은 산성 조건에서의 proton-coupled redox 반응 강화**임을 명확히 기술. Point iv에서 스캔 속도 비교를 전면에 내세우지 않도록 수정.

**수정 예시 (Point iii 마지막 문장 추가):**
> "However, it is important to note that the primary factor governing cycling stability differences between H₂SO₄ and KOH electrolytes is the distinct charge-storage mechanism rather than the difference in scan rate alone."

---

### L-2 | R-6/16 & R-7/16 — 그림 번호 불일치
**위치:** Reviewer 1, C2 Response

**Response body (파란 글씨, R-6/16):**
> "In 1 M H₂SO₄ (three-electrode, **Figure 4c**), the CV curves of NCF-900 exhibit pronounced broad redox humps..."

**원고 삽입 텍스트 (분홍 글씨, R-7/16, "On page 12"):**
> "In contrast, the CV curves obtained in 1 M H₂SO₄ exhibited broader redox features **(Figure 4b)**..."

**문제:** 동일한 H₂SO₄ CV 데이터를 Response letter에서는 Figure 4c로, 원고 본문(p.12 삽입문)에서는 Figure 4b로 다르게 인용함. 원고의 실제 그림 번호를 확인하여 통일 필요.

---

## 5. 표기 통일 (Formatting Consistency) — Table S2

| 항목 | 문제 | 위치 |
|------|------|------|
| Cycle 수 쉼표 | `5000 cycles` vs `10000 cycles` — 천 단위 쉼표 통일 필요 (이미 저자 메모 [SML1] 인지) | R-4/16, Table S2 |
| 용량 단위 | [S3] 항목만 `135.3 F/g` (슬래시 표기), 나머지는 모두 `F g⁻¹` (위첨자 표기) — 통일 필요 | R-4/16, Table S2 |

---

## 요약 테이블

| 번호 | 구분 | 위치 | 내용 | 중요도 |
|------|------|------|------|--------|
| T-1 | 오타 | R-6/16 | `mechanism., In` → `mechanism. In` | 낮음 |
| E-1 | 어색한 표현 | R-6/16 | `likely`의 위치 수정 | 낮음 |
| E-2 | 어색한 표현 | R-8/16 | `So, we would be very pleased...` 비격식체 | 낮음 |
| E-3 | 어색한 표현 | Fig.6 caption | 패널 레이블 `a)` vs `(b)` 불일치 | 낮음 |
| **S-1** | **과학적 오류** | **R-5/16, Point i** | **Na₂SO₄를 "alkaline"으로 잘못 분류** | **높음** |
| **L-1** | **논리 오류** | **R-5/16, Points iii & iv** | **스캔 속도 논거와 KOH 결과의 자기 모순** | **높음** |
| L-2 | 논리 오류 | R-6/16 & R-7/16 | Figure 4b vs 4c 불일치 — 확인 필요 | 중간 |
| — | 표기 통일 | R-4/16, Table S2 | Cycle 수 쉼표, 용량 단위 표기 | 낮음 |

---

> **최우선 수정 항목:** S-1 (Na₂SO₄ 분류 오류)와 L-1 (스캔 속도 논거 모순)은 리뷰어가 재지적할 가능성이 높으므로 반드시 수정할 것.
