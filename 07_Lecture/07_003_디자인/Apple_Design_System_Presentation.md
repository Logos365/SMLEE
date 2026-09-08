# Apple Design Analysis & UI/UX System Benchmark
> Executive Presentation Deck & Quantitative Architectural Blueprint

---

<!-- SLIDE 1 -->
<div class="slide-container">
  <div class="slide-header">
    <span class="chapter-name">CHAPTER 01 : SYSTEM OVERVIEW & ARCHITECTURE</span>
    <span class="slide-title">애플 디자인 시스템은 미니멀리즘 표면 뒤에 철저하게 계산된 정량적 표준 규격을 강제한다</span>
    <span class="slide-subtitle">Design Token Breakdown & Structural Surface Analysis</span>
  </div>

  <div class="slide-body">
    <div class="grid-2col">
      <div class="card">
        <h3>디자인 시스템 핵심 수치 및 정량적 표준</h3>
        <p>애플 UI/UX 시스템은 8px 베이스 Grid와 엄격한 Typography 계층 구조를 바탕으로 구축되어 있습니다 [출처: DESIGN-apple.md Overview].</p>
        <table class="data-table">
          <thead>
            <tr>
              <th>토큰 항목</th>
              <th>설정 값 / 규격</th>
              <th>적용 가이드라인</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Primary Accent</td>
              <td>#0066cc (Action Blue)</td>
              <td>모든 상호작용 요소 및 CTA 버튼 유일 적용</td>
            </tr>
            <tr>
              <td>Body Base Font</td>
              <td>17px (SF Pro Text / Pretendard)</td>
              <td>SaaS 표준 16px 탈피, 가독성 및 가로줄 호흡 확보</td>
            </tr>
            <tr>
              <td>Base Spacing Unit</td>
              <td>8px Grid (4/8/12/17/24/32/48/80px)</td>
              <td>모든 레이아웃, 마진, 패딩의 정렬 기준으로 활용</td>
            </tr>
            <tr>
              <td>Drop Shadow</td>
              <td>rgba(0,0,0,0.22) 3px 5px 30px</td>
              <td>바닥면에 놓인 제품 실물 이미지 단 1곳에만 국한 적용</td>
            </tr>
          </tbody>
        </table>
        <div class="citation">출처: DESIGN-apple.md - Colors & Typography Analysis</div>
      </div>

      <div class="card">
        <h3>색상 팔레트 점유율 및 사용 분포 (Color Distribution)</h3>
        <p>기능적 컬러 1종(Action Blue)을 제외하면 모두 무채색의 캔버스 및 잉크 톤으로 구성됩니다 [출처: DESIGN-apple.md Colors].</p>
        <!-- Horizontal Bar Chart SVG -->
        <svg viewBox="0 0 500 180" class="chart-svg">
          <!-- Canvas Pure White -->
          <rect x="100" y="20" width="320" height="22" fill="#fafafa" stroke="#ccc" rx="3"/>
          <text x="10" y="36" class="chart-label">Canvas White</text>
          <text x="430" y="36" class="chart-val">40%</text>

          <!-- Parchment Canvas -->
          <rect x="100" y="55" width="240" height="22" fill="#f5f5f7" stroke="#ccc" rx="3"/>
          <text x="10" y="71" class="chart-label">Parchment</text>
          <text x="350" y="71" class="chart-val">30%</text>

          <!-- Tile Dark Surfaces -->
          <rect x="100" y="90" width="160" height="22" fill="#272729" rx="3"/>
          <text x="10" y="106" class="chart-label">Dark Tile</text>
          <text x="270" y="106" class="chart-val">20%</text>

          <!-- Ink Text Black -->
          <rect x="100" y="125" width="64" height="22" fill="#1d1d1f" rx="3"/>
          <text x="10" y="141" class="chart-label">Ink (#1d1d1f)</text>
          <text x="172" y="141" class="chart-val">8%</text>

          <!-- Action Blue -->
          <rect x="100" y="160" width="16" height="22" fill="#0066cc" rx="3"/>
          <text x="10" y="176" class="chart-label">Action Blue</text>
          <text x="124" y="176" class="chart-val">2%</text>
        </svg>
        <div class="citation">출처: DESIGN-apple.md - Brand & Accent Color System</div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="footer-left">Apple UI/UX Architecture Analysis Report</span>
    <span class="page-number">PAGE 01</span>
  </div>
</div>

---

<!-- SLIDE 2 -->
<div class="slide-container">
  <div class="slide-header">
    <span class="chapter-name">CHAPTER 02 : TYPOGRAPHY & METRICS</span>
    <span class="slide-title">디스플레이 자간 축소와 17px 본문 설정이 애플 특유의 정교한 타이포그래피 밀도를 완성한다</span>
    <span class="slide-subtitle">Font Hierarchy, Letter Spacing & Line Height Specifications</span>
  </div>

  <div class="slide-body">
    <div class="grid-3col">
      <div class="card span-2">
        <h3>타이포그래피 위계별 스펙 비교 (Typography Hierarchy)</h3>
        <table class="data-table">
          <thead>
            <tr>
              <th>토큰명</th>
              <th>폰트 크기</th>
              <th>Font Weight</th>
              <th>Line Height</th>
              <th>Letter Spacing</th>
              <th>주요 용도</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>hero-display</code></td>
              <td>56px</td>
              <td>600 (SemiBold)</td>
              <td>1.07</td>
              <td>-0.28px</td>
              <td>메인 히어로 타이틀 (Apple Tight)</td>
            </tr>
            <tr>
              <td><code>display-lg</code></td>
              <td>40px</td>
              <td>600 (SemiBold)</td>
              <td>1.10</td>
              <td>0.00px</td>
              <td>제품 타일 헤드라인</td>
            </tr>
            <tr>
              <td><code>lead</code></td>
              <td>28px</td>
              <td>400 (Regular)</td>
              <td>1.14</td>
              <td>+0.196px</td>
              <td>제품 서브 카피 및 강조 설명</td>
            </tr>
            <tr>
              <td><code>body</code></td>
              <td>17px</td>
              <td>400 (Regular)</td>
              <td>1.47</td>
              <td>-0.374px</td>
              <td>기본 본문 텍스트 (16px 대치)</td>
            </tr>
            <tr>
              <td><code>dense-link</code></td>
              <td>17px</td>
              <td>400 (Regular)</td>
              <td>2.41</td>
              <td>0.00px</td>
              <td>푸터 및 고밀도 링크 리스트</td>
            </tr>
          </tbody>
        </table>
        <div class="citation">출처: DESIGN-apple.md - Typography Hierarchy Breakdown</div>
      </div>

      <div class="card">
        <h3>글자 크기 vs 자간 관계 (Letter Spacing Ratio)</h3>
        <p>크기가 커질수록 음수 자간(- tracking)을 적용하여 조형적 단단함을 유지합니다 [출처: DESIGN-apple.md Principles].</p>
        <!-- Visual Comparison Chart -->
        <div class="metric-box">
          <div class="metric-title">56px Hero Display</div>
          <div class="metric-value">-0.28px</div>
          <div class="metric-desc">타이트한 시각적 묶음 효과 (Apple Tight)</div>
        </div>
        <div class="metric-box">
          <div class="metric-title">17px Body Text</div>
          <div class="metric-value">-0.374px</div>
          <div class="metric-desc">화면 가독성 최적화 마이크로 자간</div>
        </div>
        <div class="citation">출처: DESIGN-apple.md - Typography Principles</div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="footer-left">Apple UI/UX Architecture Analysis Report</span>
    <span class="page-number">PAGE 02</span>
  </div>
</div>

---

<!-- SLIDE 3 -->
<div class="slide-container">
  <div class="slide-header">
    <span class="chapter-name">CHAPTER 03 : COMPONENT & SHAPE SYSTEM</span>
    <span class="slide-title">버튼과 카드의 곡률은 기능별로 격자화되어 일관된 상호작용 신호를 제공한다</span>
    <span class="slide-subtitle">Border Radius Scaling & Interactive Element Hierarchy</span>
  </div>

  <div class="slide-body">
    <div class="grid-2col">
      <div class="card">
        <h3>곡률 규격별 컴포넌트 매핑 (Border Radius Distribution)</h3>
        <!-- Horizontal Bar Chart SVG -->
        <svg viewBox="0 0 480 200" class="chart-svg">
          <!-- None (0px) -->
          <rect x="120" y="15" width="40" height="22" fill="#272729" rx="0"/>
          <text x="10" y="31" class="chart-label">None (0px)</text>
          <text x="170" y="31" class="chart-val">전면 풀블리드 타일 (Tile)</text>

          <!-- SM (8px) -->
          <rect x="120" y="50" width="80" height="22" fill="#1d1d1f" rx="3"/>
          <text x="10" y="66" class="chart-label">SM (8px)</text>
          <text x="210" y="66" class="chart-val">다크 유틸리티 버튼 (Sign In)</text>

          <!-- MD (11px) -->
          <rect x="120" y="85" width="110" height="22" fill="#fafafc" stroke="#ccc" rx="4"/>
          <text x="10" y="101" class="chart-label">MD (11px)</text>
          <text x="240" y="101" class="chart-val">펄 캡슐 버튼 (Pearl Capsule)</text>

          <!-- LG (18px) -->
          <rect x="120" y="120" width="180" height="22" fill="#ffffff" stroke="#0066cc" rx="6"/>
          <text x="10" y="136" class="chart-label">LG (18px)</text>
          <text x="310" y="136" class="chart-val">스토어 유틸리티 카드</text>

          <!-- Pill (9999px) -->
          <rect x="120" y="155" width="320" height="22" fill="#0066cc" rx="11"/>
          <text x="10" y="171" class="chart-label">Pill (9999px)</text>
          <text x="450" y="171" class="chart-val">시그니처 CTA</text>
        </svg>
        <div class="citation">출처: DESIGN-apple.md - Border Radius Scale</div>
      </div>

      <div class="card">
        <h3>인터랙티브 컴포넌트 규격 및 피드백 구조</h3>
        <p>모든 클릭 가능한 요소는 <code>transform: scale(0.95)</code> 마이크로 인터랙션을 공유합니다 [출처: DESIGN-apple.md Components].</p>
        <table class="data-table">
          <thead>
            <tr>
              <th>컴포넌트명</th>
              <th>배경색 / 테두리</th>
              <th>패딩 / 높이</th>
              <th>인터랙션 특성</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>button-primary</code></td>
              <td>#0066cc (Solid)</td>
              <td>11px × 22px</td>
              <td>Full Pill, Press: scale(0.95)</td>
            </tr>
            <tr>
              <td><code>button-secondary</code></td>
              <td>Transparent / 1px Blue</td>
              <td>11px × 22px</td>
              <td>Ghost Pill 형태</td>
            </tr>
            <tr>
              <td><code>search-input</code></td>
              <td>#ffffff / 1px Soft Hairline</td>
              <td>44px Height / Pill</td>
              <td>검색창도 Pill 규격 통일</td>
            </tr>
            <tr>
              <td><code>sub-nav-frosted</code></td>
              <td>Parchment 80% + Blur</td>
              <td>52px Height</td>
              <td>스크롤 시 상단 블러 고정</td>
            </tr>
          </tbody>
        </table>
        <div class="citation">출처: DESIGN-apple.md - Buttons & Inputs Spec</div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="footer-left">Apple UI/UX Architecture Analysis Report</span>
    <span class="page-number">PAGE 03</span>
  </div>
</div>

---

<!-- SLIDE 4 -->
<div class="slide-container">
  <div class="slide-header">
    <span class="chapter-name">CHAPTER 04 : RESPONSIVE LAYOUT & BREAKPOINTS</span>
    <span class="slide-title">디바이스 폭에 따라 유기적으로 반응하는 Grid 시스템이 멀티 디바이스 연속성을 보장한다</span>
    <span class="slide-subtitle">Multi-Breakpoint Grid Strategy & Layout Transitions</span>
  </div>

  <div class="slide-body">
    <div class="grid-2col">
      <div class="card">
        <h3>반응형 그리드 열(Column) 변화 추이</h3>
        <!-- Multi-bar/Grid Column Breakdown SVG -->
        <svg viewBox="0 0 480 190" class="chart-svg">
          <!-- Desktop >= 1069px -->
          <rect x="130" y="20" width="300" height="24" fill="#0066cc" rx="3"/>
          <text x="10" y="37" class="chart-label">Desktop (≥1069px)</text>
          <text x="440" y="37" class="chart-val">4~5 열</text>

          <!-- Small Desktop 1024-1068px -->
          <rect x="130" y="60" width="220" height="24" fill="#2997ff" rx="3"/>
          <text x="10" y="77" class="chart-label">Sm-Desktop (1024px)</text>
          <text x="360" y="77" class="chart-val">3 열</text>

          <!-- Tablet 736-1023px -->
          <rect x="130" y="100" width="150" height="24" fill="#7a7a7a" rx="3"/>
          <text x="10" y="117" class="chart-label">Tablet (736-1023px)</text>
          <text x="290" y="117" class="chart-val">2 열</text>

          <!-- Mobile <= 640px -->
          <rect x="130" y="140" width="80" height="24" fill="#1d1d1f" rx="3"/>
          <text x="10" y="157" class="chart-label">Mobile (≤640px)</text>
          <text x="220" y="157" class="chart-val">1 열</text>
        </svg>
        <div class="citation">출처: DESIGN-apple.md - Responsive Breakpoints Strategy</div>
      </div>

      <div class="card">
        <h3>구간별 레이아웃 및 폰트 축소 메커니즘</h3>
        <p>해상도가 줄어듦에 따라 패딩과 타이포그래피 크기가 단계적으로 축소됩니다 [출처: DESIGN-apple.md Responsive Behavior].</p>
        <table class="data-table">
          <thead>
            <tr>
              <th>구분</th>
              <th>Desktop (1440px)</th>
              <th>Tablet (834px)</th>
              <th>Mobile (419px)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Hero Title</td>
              <td>56px (Hero Display)</td>
              <td>40px (Display LG)</td>
              <td>28px (Lead Size)</td>
            </tr>
            <tr>
              <td>Tile Padding</td>
              <td>80px (Vertical)</td>
              <td>64px (Vertical)</td>
              <td>48px (Vertical)</td>
            </tr>
            <tr>
              <td>Global Nav</td>
              <td>전체 링크 수평 노출</td>
              <td>햄버거 메뉴로 전환</td>
              <td>로고+햄버거+쇼핑백</td>
            </tr>
            <tr>
              <td>Touch Target</td>
              <td>44px × 44px 이상</td>
              <td>44px × 44px 유지</td>
              <td>44px × 44px 유지</td>
            </tr>
          </tbody>
        </table>
        <div class="citation">출처: DESIGN-apple.md - Collapsing Strategy</div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="footer-left">Apple UI/UX Architecture Analysis Report</span>
    <span class="page-number">PAGE 04</span>
  </div>
</div>

---

<!-- SLIDE 5 -->
<div class="slide-container">
  <div class="slide-header">
    <span class="chapter-name">CHAPTER 05 : DO'S & DON'TS / SYSTEM RULES</span>
    <span class="slide-title">엄격한 금지 규정 준수가 브랜드 가치와 디자인 시스템의 순수성을 유지한다</span>
    <span class="slide-subtitle">Design System Compliance Guidelines & Anti-Patterns</span>
  </div>

  <div class="slide-body">
    <div class="grid-2col">
      <div class="card border-do">
        <h3 class="text-do">DO : 권장되는 핵심 설계 원칙</h3>
        <p>애플 고유의 가치를 전달하기 위해 반드시 지켜야 하는 구현 가이드입니다 [출처: DESIGN-apple.md Do's].</p>
        <ul class="rule-list">
          <li><strong>단일 액센트 컬러 사용:</strong> 모든 인터랙션 요소는 오직 <code>#0066cc</code>(Action Blue)만 적용한다.</li>
          <li><strong>17px 본문 기준 준수:</strong> 표준 16px이 아닌 17px 본문 서체로 브랜드 고유의 에디토리얼 호흡을 유지한다.</li>
          <li><strong>교차 풀블리드 타일:</strong> 라이트 타일과 다크 타일을 교차 배치하여 경계선 없이 영역을 구분한다.</li>
          <li><strong>그림자 제약:</strong> 그림자는 바닥에 놓인 제품 이미지(<code>rgba(0,0,0,0.22)</code>) 외 UI 카드/버튼에 절대 사용 금지.</li>
          <li><strong>Pill 모양 결합:</strong> 주요 CTA 및 검색 입력창에는 <code>rounded.pill</code> (9999px) 형태를 일관 적용한다.</li>
        </ul>
        <div class="citation">출처: DESIGN-apple.md - Do's Guideline</div>
      </div>

      <div class="card border-dont">
        <h3 class="text-dont">DON'T : 엄격히 금지되는 안티 패턴</h3>
        <p>시스템 순수성을 저해하는 디자인 구현 오류 항목입니다 [출처: DESIGN-apple.md Don'ts].</p>
        <ul class="rule-list">
          <li><strong>보조 액센트 컬러 추가 금지:</strong> Action Blue 외 제2의 브랜드 강조 색상을 절대로 정의하지 않는다.</li>
          <li><strong>장식용 그라데이션 사용 금지:</strong> CSS 장식용 그라데이션을 금지하고 분위기는 오직 제품 사진으로 전달한다.</li>
          <li><strong>Weight 500 사용 금지:</strong> 서체 굵기는 300, 400, 600, 700만 사용하며 500은 시스템에서 배제한다.</li>
          <li><strong>카드/타일 곡률 혼용 금지:</strong> 풀블리드 타일에 라운딩을 주지 않고 직각(0px) 상태를 유지한다.</li>
          <li><strong>다크 타일용 링크 오류:</strong> 다크 타일에서 Action Blue 대신 Sky Link Blue(<code>#2997ff</code>)를 반드시 사용한다.</li>
        </ul>
        <div class="citation">출처: DESIGN-apple.md - Don'ts Guideline</div>
      </div>
    </div>
  </div>

  <div class="slide-footer">
    <span class="footer-left">Apple UI/UX Architecture Analysis Report</span>
    <span class="page-number">PAGE 05</span>
  </div>
</div>
