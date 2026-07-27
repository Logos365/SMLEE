# BMW Corporate Web Design System Architecture & Guidelines
> **System Specifications & Slide Deck Layout**  
> **Format**: 16:9 Presentation Format | **Font**: Pretendard Only | **Density**: Maximum High Density Data

---

### CHAPTER 01 | DESIGN PHILOSOPHY · PAGE 01 / 08 (16:9 Slide)

# BMW 기업 웹사이트는 M의 레이싱 역동성과 차별화된 절제되고 안정된 'Corporate-Automotive' 가치를 정밀 구축한다
> **부제목**: 브랜드 정체성, 메인 컬러 스펙트럼, 서체 대조 구조 및 M 서브브랜드와의 포지셔닝 차별화 분석 [source: 1]

#### 1. BMW Corporate vs. BMW M Brand Axis Comparison
| 구분 항목 | BMW Corporate Site [source: 1] | BMW M Sub-Brand Site [source: 1] |
|---|---|---|
| **디자인 방향성** | 절제되고 정돈된 기업-자동차 (Measured Corporate) | 모터스포츠 폭발력 중심 (Motorsport-Bombastic) |
| **캔버스 배경** | 밝은 캔버스 (`#ffffff` / `#fafafa`) 위주의 높은 명도 | 다크 타이어 캔버스 위주의 높은 대비감 |
| **메인 액센트** | 단일 브랜드 블루 (`#1c69d4`) 100% 집중 사용 | M 트라이컬러 (`#0066b1` / `#1c69d4` / `#e22718`) |
| **버튼 모서리** | 완벽한 0px 직각 수직 구조 (`rounded.none`) | 스포츠 다이내믹 라디우스 및 공기역학 모서리 |
| **섹션 패딩 리듬** | `spacing.section` (80px) 고밀도 실용적 간격 | `96px` 여유로운 스포티 간격 |

#### 2. 핵심 디자인 시스템 구성 비중 (System Composition Ratio)
- **Light Canvas Base (`#ffffff` / `#fafafa`)** [source: 1]: `[████████████████████████████████████████] 85%`
- **Hero Navy Accent (`#1a2129`)** [source: 1]: `[███████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 15%`
- **Type Contrast Ratio (700 Bold vs 300 Light)** [source: 1]: `[████████████████████] 50% Bold : [░░░░░░░░░░░░░░░░░░░░] 50% Light`

#### 3. 핵심 수치 메트릭 (Key System Metrics)
- `0px` : Dominant Corner Radius (`rounded.none`) [source: 1]
- `80px` : Standard Section Rhythm (`spacing.section`) [source: 1]
- `#1c69d4` : Corporate Blue Primary CTA (`colors.primary`) [source: 1]

> **핵심 요약 [source: 1]**: BMW Corporate 사이트는 M 브랜드의 스포티함과 달리 라이트 캔버스 바탕 위에 어두운 네이비 히어로 밴드(`#1a2129`)와 단일 기업 블루(`#1c69d4`)를 교차 배치하여 신뢰감과 엔진 정밀 감성을 극대화함.

- **정보 출처**: BMW Corporate Web Design System Analysis (Version Alpha) [source: 1]

---

### CHAPTER 02 | COLOR SYSTEM · PAGE 02 / 08 (16:9 Slide)

# 브랜드 액센트는 단 하나의 전용 블루(#1c69d4)에 집중되며 명암 대비만으로 완벽한 시계성을 확보한다
> **부제목**: 컬러 팔레트 토큰 체계, 역할별 면적 점유율 및 M 트라이컬러 적용 예외 규정 [source: 1]

#### 1. UI 면적 점유율 스펙트럼 (Color Volume Distribution Chart)
`[ Canvas Base (#ffffff): 60% ████████████ ] [ Hero Navy (#1a2129): 20% ████ ] [ Card Plate (#fafafa): 12% ██ ] [ Blue CTA (#1c69d4): 8% █ ]`

#### 2. 주요 색상 토큰 상세 사양 (Color Token Specification Table)
| 역할 (Role) | 토큰명 (Token) | Hex 코드 | 시각적 차트/표시 | 적용 가이드 [source: 1] |
|---|---|---|---|---|
| **Primary CTA** | `colors.primary` | `#1c69d4` | `[■■■■■■] Blue` | 모든 주 버튼, 활성 탭, 블루 링크 |
| **Primary Active** | `colors.primary-active` | `#0653b6` | `[■■■■■■] Dark Blue` | 버튼 눌림(Pressed/Active) 상태 |
| **Canvas Surface** | `colors.canvas` | `#ffffff` | `[□□□□□□] Pure White` | 기본 페이지 배경 면적 |
| **Card Surface** | `colors.surface-card` | `#fafafa` | `[░░░░░░] Soft Grey` | 모델 카드 차량 렌더링 플레이트 |
| **Hero Dark Navy** | `colors.surface-dark` | `#1a2129` | `[■■■■■■] Dark Navy` | 리드 모델 히어로 쇼케이스 밴드 |
| **Primary Ink** | `colors.ink` | `#262626` | `[■■■■■■] Ink Black` | 디스플레이 제목 및 강조 UI 텍스트 |

#### 3. M 트라이컬러 사용 예외 규정 (M Stripe Rules)
- **M Stripe Divider (`m-stripe-divider`) 구조 [source: 1]**:
  `M Blue Light (#0066b1) [███] + M Blue Dark (#1c69d4) [███] + M Red (#e22718) [███]`
- **적용 제한**: M 모델 전용 페이지, M Performance 배지 및 구분선에만 4px 높이로 제한 사용 [source: 1].
- **금지 사항**: 일반 기업 사이트 메인 CTA 버튼 배경이나 범용 UI 색상으로 절대 사용 금지 [source: 1].

> **원칙 [source: 1]**: BMW 기업 메인 사이트의 액센트 컬러는 오직 `#1c69d4` 블루 단 하나뿐이며, 다른 브랜드 컬러 확장을 엄격히 금지함.

- **정보 출처**: BMW Corporate Web Design System Analysis (Version Alpha) [source: 1]

---

### CHAPTER 03 | TYPOGRAPHY · PAGE 03 / 08 (16:9 Slide)

# 서체 체계는 700(Bold)과 300(Light)의 극명한 대비를 통해 독일 정밀 공학의 편집증적 세련미를 구현한다
> **부제목**: BMW Type Next Latin 타이포그래피 계층, Pretendard 매핑, 폰트 웨이트 비율 및 자간 규칙 [source: 1]

#### 1. 타이포그래피 계층 스펙 (Typography Hierarchy Table)
| 토큰명 (Token) | Size | Weight | Line Height | Letter Spacing | 적용 컨텍스트 [source: 1] |
|---|---|---|---|---|---|
| `typography.display-xl` | 64px | **700 (Bold)** | 1.05 | 0 | 히어로 메인 타이틀 ("iX3") |
| `typography.display-lg` | 48px | **700 (Bold)** | 1.10 | 0 | 주요 섹션 타이틀 |
| `typography.display-md` | 32px | **700 (Bold)** | 1.15 | 0 | 서브 섹션 타이틀, CTA 헤드 |
| `typography.display-sm` | 24px | **700 (Bold)** | 1.25 | 0 | 스펙 셀 핵심 숫자 데이터 |
| `typography.title-lg` | 20px | **700 (Bold)** | 1.30 | 0 | 카드 그룹 타이틀 |
| `typography.title-md` | 18px | **700 (Bold)** | 1.40 | 0 | 모델 카드 타이틀, 리드 단락 |
| `typography.body-md` | 16px | *300 (Light)* | 1.55 | 0 | 기본 본문 (BMW Light Signature) |
| `typography.body-sm` | 14px | *300 (Light)* | 1.55 | 0 | 푸터 본문, 약관 법적 고지 |
| `typography.label-uppercase` | 13px | **700 (Bold)** | 1.30 | 1.5px | "LEARN MORE ›" 링크 (Tracking) |
| `typography.button` | 14px | **700 (Bold)** | 1.00 | 0.5px | CTA 버튼 라벨 |

#### 2. 폰트 굵기(Weight) 사용 비중 차트
- **Weight 700 (Display / Headline / CTA)** [source: 1]: `[██████████████████████] 45%`
- **Weight 300 Light (Body / Paragraph Signature)** [source: 1]: `[░░░░░░░░░░░░░░░░░░░░░░] 45%`
- **Weight 400 (Utility Nav / Captions Only)** [source: 1]: `[▒▒▒▒▒] 10%`
- **Weight 500 (Medium)** [source: 1]: `[ ] 0% (STRICTLY ABSENT)`

> **금지 수칙 [source: 1]**: Weight 500은 시스템 전체에서 의도적으로 완전히 배제됨. 본문 텍스트에 Bold(700)를 혼용하는 것을 금지하며, 본문은 오직 Light(300) 서체만 사용함.

- **정보 출처**: BMW Corporate Web Design System Analysis (Version Alpha) [source: 1]

---

### CHAPTER 04 | SHAPES & ELEVATION · PAGE 04 / 08 (16:9 Slide)

# 모든 버튼과 카드는 0px 직각 모서리로 설계되어 정밀 기계 공학적 단단함을 완성한다
> **부제목**: 모서리 곡률(Corner Radius) 스케일, 입체감(Elevation) 표현 방식 및 그림자 배제 원칙 [source: 1]

#### 1. 코너 라디우스(Border Radius) 적용 매트릭스
| 라디우스 토큰 | Pixel 값 | 적용 컴포넌트 | 점유율 차트 [source: 1] |
|---|---|---|---|
| `rounded.none` | **0px** | 모든 버튼, 카드, 인풋, 칩, 모달 섀시 | `[████████████████████] 95% (압도적 표준)` |
| `rounded.xs` | 2px | 극소형 모듈 내부 배지 (예외적) | `[░] <1%` |
| `rounded.sm` | 4px | 소형 인라인 버튼 (예외적) | `[░] <1%` |
| `rounded.lg` | 12px | 모바일 팝업 레이어 코너 (예외적) | `[░] <1%` |
| `rounded.full` | 9999px | 원형 아이콘 버튼, 프로필 아바타 | `[▒▒] <3%` |

#### 2. 입체감(Elevation & Depth) 및 레이어 구조
- **Level 1: Flat (0px Shadow)** [source: 1]: 상단 내비게이션, 푸터, 메인 본문, 히어로 밴드 (그림자 0px)
- **Level 2: Soft Hairline (1px Border `#e6e6e6`)** [source: 1]: 컨피규레이터 옵션 타일, 인풋박스, 테이블 구분선
- **Level 3: Surface Plate Block (`#fafafa`)** [source: 1]: 모델 카드 사진 백드롭 플레이트 (그림자 없이 색상면 분리)

#### 3. 디자인 양식 대조 (Dialect Comparison)
- **BMW 정밀 공학 스타일 (BMW Engineering Dialect)** [source: 1]: 0px 완전 직각 구조 (`rounded.none`)로 기계 장비의 정밀함 전달. Drop Shadow 그림자를 완전 제거하고, 색상 블록 대조만으로 입체감 형성.
- **일반 SaaS 소프트 UI (Apple / Cal.com Dialect)** [source: 1]: 8px ~ 16px 부드러운 둥근 모서리와 과도한 드롭 섀도우 사용. **BMW 기업 브랜드 가이드라인에서는 'Off-brand'로 엄격히 금지함 [source: 1].**

- **정보 출처**: BMW Corporate Web Design System Analysis (Version Alpha) [source: 1]

---

### CHAPTER 05 | GRID & SPACING · PAGE 05 / 08 (16:9 Slide)

# 80px 섹션 리듬과 1440px 최대 그리드로 딜러쉽 기능성과 미학적 고밀도를 동시 충족한다
> **부제목**: 8px 베이스 단위 간격 시스템, 카드 그리드 컬럼 구성 및 여백 밀도 관리 전략 [source: 1]

#### 1. 8px 베이스 간격 토큰 스케일 (Spacing Token Scale)
- `spacing.xxs` (4px): `[█]`
- `spacing.xs` (8px): `[██]`
- `spacing.sm` (12px): `[███]`
- `spacing.md` (16px): `[████]`
- `spacing.lg` (24px): `[██████]`
- `spacing.xl` (32px): `[████████]`
- `spacing.xxl` (48px): `[████████████]`
- `spacing.section` (80px): `[████████████████████] (Standard Section Rhythm)`

#### 2. 레이아웃 그리드 & 컨테이너 구조
| 구분 | 데스크톱 (>1024px) | 태블릿 (768-1024px) | 모바일 (<768px) |
|---|---|---|---|
| **최대 너비** | 1440px 중앙 정렬 | 100% Fluid (Gutters) | 100% Fluid (Gutters) |
| **모델 카드** | **4-Up / 5-Up 그리드** | 2-Up 그리드 | 1-Up 수직 스택 |
| **인벤토리** | 3-Up 필터 + 4-Up 카드 | 2-Up 그리드 | 1-Up 스크롤 |

#### 3. 밀도 철학 비교 (BMW Corporate vs BMW M)
- **BMW Corporate Density (기능적 고밀도)** [source: 1]:
  - 섹션 패딩: **80px (`spacing.section`)**
  - 카드 내부 패딩: **24px (`spacing.lg`)**
  - 딜러쉽 쇼룸 및 재고 검색 등 실용적 데이터 밀도 극대화.
- **BMW M Motorsport Density (여유로운 공간감)** [source: 1]:
  - 섹션 패딩: **96px** (Corporate 대비 16px 넓음)
  - 카드 내부 패딩: **32px**

- **정보 출처**: BMW Corporate Web Design System Analysis (Version Alpha) [source: 1]

---

### CHAPTER 06 | COMPONENTS · PAGE 06 / 08 (16:9 Slide)

# 핵심 UI 컴포넌트는 직관적인 카드 그리드와 명확한 계층구조로 일관된 상호작용을 보장한다
> **부제목**: 상단 내비게이션, 버튼 4종 스펙, 히어로 밴드, 모델 카드 및 필터 칩 상세 사양 [source: 1]

#### 1. 주요 컴포넌트 명세표 (Component Specifications)
| 컴포넌트 토큰 | 높이 / 패딩 | 배경색 (Background) | 타이포그래피 및 서체 | 형태 및 모서리 [source: 1] |
|---|---|---|---|---|
| `top-nav` | 64px Height | `colors.canvas` (`#ffffff`) | 14px / 400 (Nav-link) | 상단 고정, 하단 1px Hairline border |
| `button-primary` | 48px / 14x32px | `colors.primary` (`#1c69d4`) | 14px / 700 White (`#ffffff`) | 0px 직각 수직 구조 (`rounded.none`) |
| `button-secondary` | 48px / 13x31px | `colors.canvas` (`#ffffff`) | 14px / 700 Ink (`#262626`) | 1px Strong Hairline (`#cccccc`), 0px |
| `hero-band-dark` | 80px Pad | `colors.surface-dark` (`#1a2129`) | 64px / 700 Display-XL White | 전폭 다크 네이비 히어로 밴드 |
| `model-card` | 24px Pad | `colors.canvas` (`#ffffff`) | 18px / 700 Title-MD | `#fafafa` 사진 플레이트 + "LEARN MORE ›" |
| `filter-chip` | 8x14px Pad | `#ffffff` (Active: `#262626`) | 12px / 400 Caption | 1px Border (Active 시 solid ink 배경) |
| `text-input` | 48px Height | `colors.canvas` (`#ffffff`) | 16px / 300 Body-MD | 1px Hairline, Focus 시 Ink 색상 두꺼워짐 |

#### 2. 모델 카드 레이아웃 와이어프레임 구조 (`model-card`)
```
+-------------------------------------------------------------+
| [Vehicle Render Photo Plate] (`surface-card` #fafafa | 16:10)|
+-------------------------------------------------------------+
| BMW iX3 xDrive50                                            |
| Electrified Precision Engineering                           |
| LEARN MORE ›                                                |
+-------------------------------------------------------------+
```

#### 3. 버튼 유형별 상태 변화 가이드 (Button States)
- **Primary Default**: Background `#1c69d4`, Text `#ffffff` [source: 1]
- **Primary Active**: Background `#0653b6`, Text `#ffffff` [source: 1]
- **Primary Disabled**: Background `#d6d6d6`, Text `#6b6b6b` [source: 1]

- **정보 출처**: BMW Corporate Web Design System Analysis (Version Alpha) [source: 1]

---

### CHAPTER 07 | RESPONSIVE · PAGE 07 / 08 (16:9 Slide)

# 반응형 그리드는 디바이스별 완벽한 유동적 재배치로 모든 화면에서 최적의 밀도를 유지한다
> **부제목**: 4단계 브레이크포인트 스펙, 모바일 내비게이션 전환 및 터치 타깃 최소 기준 [source: 1]

#### 1. 브레이크포인트 스케일 & 반응형 레이아웃 변환표
| 구분 (Breakpoint) | 화면 너비 (Width) | 내비게이션 UI | 그리드 스택 구조 | 핵심 레이아웃 재배치 규칙 [source: 1] |
|---|---|---|---|---|
| **Mobile** | `< 768px` | 햄버거 풀스크린 시트 | **1-Up 수직 스택** | 히어로 h1 (64px → 40px 축소), 필터 칩 가로 스크롤 |
| **Tablet** | `768px ~ 1024px` | 축약형 상단 내비 | **2-Up 그리드** | 인벤토리 2-up 스택, 히어로 2컬럼 레이아웃 유지 |
| **Desktop** | `1024px ~ 1440px` | 풀 수평 메뉴 바 | **4-Up / 5-Up 그리드** | 1440px 최대 너비 안에서 풀 컨피규레이터 그리드 작동 |
| **Wide Desktop** | `> 1440px` | 풀 수평 메뉴 바 | **1440px 고정 중앙** | 1440px 초과 여백은 좌우 여백(Gutter)으로 흡수 |

#### 2. 터치 타깃 최소 규격 (Touch Target Minimums)
- **Primary CTA Button Height** [source: 1]: `48px` (WCAG AAA 충족)
- **Text Input Field Height** [source: 1]: `48px` (접근성 표준)
- **Category Sub-Tab Tap Area** [source: 1]: `> 44px` (수직 12px 패딩 적용)

#### 3. 반응형 이미지 비율 가이드라인
- **데스크톱 히어로 밴드**: 21:9 시네마틱 및 16:9 와이드 비율 적용 [source: 1]
- **모델 카드 렌더링**: 16:10 비율 스튜디오 백드롭 유지 [source: 1]
- **모바일 인벤토리**: 4:3 컴팩트 비율로 아트 다이렉션 재잘라내기(Crop) 허용 [source: 1]

- **정보 출처**: BMW Corporate Web Design System Analysis (Version Alpha) [source: 1]

---

### CHAPTER 08 | GOVERNANCE · PAGE 08 / 08 (16:9 Slide)

# 엄격한 Do's & Don'ts 수칙 준수를 통해 브랜드 아이덴티티의 일관성과 품질을 유지한다
> **부제목**: 디자인 시스템 필수 수칙, 엄격한 금지 사항, 제약 사항 및 시스템 품질 관리 모니터링 [source: 1]

#### 1. 디자인 시스템 핵심 준수 수칙 (Do's & Don'ts Checklist)
| 구분 영역 | 권장 준수 사항 (DO) [source: 1] | 엄격 금지 사항 (DON'T) [source: 1] |
|---|---|---|
| **Color Role** | Primary CTA에는 오직 BMW Blue (`#1c69d4`)만 적용 | 블루 외의 다른 액센트 컬러를 주 버튼에 사용 금지 |
| **Geometry** | 모든 버튼과 카드는 0px 직각 모서리 (`rounded.none`) 적용 | Rounded 또는 Pill 형태의 둥근 모서리 버튼 사용 금지 |
| **Typography** | Display 700 Bold vs Body 300 Light 계층 대조 엄수 | Body 서체에 Bold 적용 금지 / Weight 500 사용 금지 |
| **Surface Depth** | 히어로 밴드는 `#1a2129` 어두운 네이비 전용 적용 | 어두운 배경을 일반 본문 섹션에 연속 배치 금지 |
| **Card Elevation** | 카드 경계는 색상 블록 대조와 1px Hairline으로 처리 | 카드 요소에 Drop Shadow 그림자 효과 부여 금지 |
| **M Tricolor** | M 트라이컬러는 M 모델 및 모터스포츠 배지에만 한정 | M 트라이컬러 스트라이프를 CTA 버튼 배경으로 사용 금지 |

#### 2. 서체 대체 예외 규정 (Font Fallback Rule)
- BMW Type Next Latin 라이선스 미보유 환경에서는 오픈소스 **Inter Variable (700 Bold / 300 Light)** 서체로 대체 적용 [source: 1].
- 한글 환경에서는 본 슬라이드 가이드에 명시된 바와 같이 **Pretendard (700 Bold / 300 Light)** 서체로 통일 적용 [source: 1].
- 자간(Letter Spacing)은 0.0em 고정을 유지함 [source: 1].

#### 3. 시스템 출처 표기 고지 (References & Citation)
- 본 시스템 가이드라인의 모든 수치, 토큰, 컴포넌트 명세는 **BMW Corporate Web Design System Analysis Document (Version Alpha) [source: 1]** 원본 분석 데이터에 기반하여 작성되었습니다.

- **정보 출처**: BMW Corporate Web Design System Analysis (Version Alpha) [source: 1]
