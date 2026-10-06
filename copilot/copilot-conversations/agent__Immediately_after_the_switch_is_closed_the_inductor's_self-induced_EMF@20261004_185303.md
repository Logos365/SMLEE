---
epoch: 1791107583244
mode: agent
backendId: claude
sessionId: "bc0f7f33-69ba-44aa-8bb4-2cac66ec7c59"
agentLabel: "Immediately after the switch is closed: the inductor's self-…"
usage: '{"usedTokens":94295,"contextWindow":1000000,"inputTokens":2,"outputTokens":647,"cacheReadTokens":91744,"cacheWriteTokens":1902,"updatedAt":1791276988327}'
tags:
  - copilot-conversation
---

**user**: Immediately after the switch is closed: the inductor's self-induced EMF **prevents current from flowing** 왜 이렇게 되나요?
[Timestamp: 2026/10/04 18:53:03]

**ai**: 이 문장은 **인덕터가 전류의 "변화"에 저항한다**는 성질(렌츠의 법칙)을 스위치를 닫는 순간에 적용한 것입니다. 다만 "전류가 흐르지 못하게 한다"는 표현은 약간 과장되어 있어서, 정확한 의미를 함께 정리해 드리겠습니다.

## 1. 핵심 원리: 인덕터는 전류의 "변화"를 싫어한다

인덕터의 자체유도 기전력은

$$\mathcal{E}_L = -L\frac{di}{dt}$$

입니다. 인덕터가 반응하는 대상은 전류의 **크기 $i$** 가 아니라 **변화율 $di/dt$** 입니다. 음의 부호는 렌츠의 법칙을 나타냅니다. 유도 기전력은 항상 전류 변화를 **방해하는 방향**으로 생깁니다.

## 2. 스위치를 닫는 순간에 무슨 일이 일어나나

- 스위치를 닫기 직전에는 전류가 $i = 0$ 입니다.
- 스위치를 닫으면 전지가 전류를 0에서 키우려고 합니다. 즉 $di/dt > 0$ 이 됩니다.
- 그러면 인덕터를 지나는 자기선속 $\Phi_B = Li$ 도 늘어나려고 합니다.
- 렌츠의 법칙에 따라 인덕터는 이 증가를 막는 방향, 즉 **전지와 반대 방향**으로 기전력을 만듭니다. 이것이 역기전력(back EMF)입니다.

## 3. 왜 전류가 순간적으로 0인가: 수식으로 보기

RL 회로에 키르히호프 전압 법칙을 적용하면

$$\mathcal{E} - iR - L\frac{di}{dt} = 0$$

입니다. 만약 전류가 $t=0$ 에서 갑자기 어떤 값으로 뛴다면, 그 순간 $di/dt \to \infty$ 가 되어 인덕터 양단에 **무한대의 전압**이 걸려야 합니다. 전지는 유한한 $\mathcal{E}$ 만 줄 수 있으므로 이런 일은 불가능합니다. 따라서 **인덕터에 흐르는 전류는 불연속적으로 바뀔 수 없고**, 스위치를 닫은 직후에도 $i(0^+) = 0$ 입니다.

이를 위 식에 넣으면

$$L\frac{di}{dt}\bigg|_{t=0} = \mathcal{E}$$

입니다. 즉 **전지 전압 전부가 인덕터에 걸리고, 저항에는 전압이 걸리지 않습니다** ($iR = 0$). 인덕터의 역기전력이 전지 기전력과 정확히 맞서고 있는 상태입니다.

**에너지로 보면:** 인덕터에 저장되는 에너지는 $U = \tfrac{1}{2}Li^2$ 입니다. 전류가 순간적으로 생기려면 이 에너지가 0초 만에 공급되어야 하니 무한대의 일률이 필요합니다. 그래서 불가능합니다.

## 4. 주의: "막는다"는 "영원히 막는다"가 아니다

$t=0$ 에서 전류는 0이지만 $di/dt = \mathcal{E}/L \neq 0$ 입니다. 그래서 전류는 **곧바로 증가하기 시작합니다**. 인덕터가 막는 것은 전류 자체가 아니라 **전류의 갑작스러운 변화**입니다. 결과는 다음과 같습니다.

$$i(t) = \frac{\mathcal{E}}{R}\left(1 - e^{-t/\tau}\right), \qquad \tau = \frac{L}{R}$$

| 시점 | 전류 $i$ | 인덕터 전압 | 인덕터의 역할 |
| --- | --- | --- | --- |
| $t = 0^+$ | $0$ | $\mathcal{E}$ (전부) | 끊어진 회로처럼 동작 |
| $t \to \infty$ | $\mathcal{E}/R$ | $0$ | 단순한 도선처럼 동작 |

노트의 다음 줄 "After a long time ... acts as a plain wire"가 바로 이 표의 아래 행입니다. 전류가 일정해지면 $di/dt = 0$ 이 되어 유도 기전력도 사라집니다.

## 5. 직관적인 비유: 관성

인덕터는 전기 회로에서 **질량(관성)** 과 같은 역할을 합니다.

- 멈춰 있는 무거운 물체를 밀어도 속도가 순간적으로 생기지 않고 서서히 빨라집니다. 처음 그 순간 속도는 0이지만 가속도는 0이 아닙니다.
- 마찬가지로 $L$ 은 질량, $i$ 는 속도, $\mathcal{E}$ 는 힘에 해당합니다. $L\,di/dt = \mathcal{E}$ 는 $m\,dv/dt = F$ 와 같은 꼴입니다.

---

**한 줄 요약:** 인덕터의 전류는 순간적으로 바뀔 수 없습니다. 그래서 스위치를 닫는 순간 $i = 0$ 이고, 역기전력이 전지 전압과 정확히 맞섭니다. 그 뒤 전류는 시상수 $\tau = L/R$ 에 따라 서서히 $\mathcal{E}/R$ 까지 커집니다. 노트의 "prevents current from flowing"은 "**전류가 즉시 흐르는 것을 막는다**"로 읽는 것이 정확합니다.
[Timestamp: 2026/10/04 18:53:03]

**user**: 인덕터가 뭐죠?
[Timestamp: 2026/10/04 18:54:28]

**ai**: ## 인덕터란?

**인덕터(inductor)** 는 **도선을 코일 모양으로 감아 만든 회로 소자**입니다. 회로도 기호는 꼬불꼬불한 선(⌇⌇⌇)이고, 성질은 **인덕턴스 $L$** 로 나타냅니다. 단위는 헨리(H)입니다.

한 문장으로 말하면, 인덕터는 **전류가 만든 자기장 속에 에너지를 저장하고, 전류가 갑자기 변하는 것에 저항하는 소자**입니다.

## 1. 왜 코일 모양인가

전류가 흐르는 도선 주위에는 자기장이 생깁니다(앙페르 법칙). 도선을 여러 번 감으면 각 고리가 만든 자기장이 코일 안쪽에서 겹쳐 **강한 자기장**이 됩니다. 이것이 솔레노이드이고, 인덕터의 기본 형태입니다.

코일을 지나는 자기선속은 전류에 비례합니다.

$$N\Phi_B = Li$$

이 비례상수 $L$ 이 **인덕턴스**입니다. "같은 전류로 자기선속을 얼마나 많이 만드는가"를 나타냅니다. 길이 $l$, 단면적 $A$, 감은 수 $N$ 인 솔레노이드의 인덕턴스는 다음과 같습니다.

$$L = \frac{\mu_0 N^2 A}{l}$$

많이 감을수록($N^2$), 단면적이 클수록 $L$ 이 커집니다. 철심을 넣으면 $\mu_0$ 대신 더 큰 투자율 $\mu$ 가 들어가서 $L$ 이 크게 늘어납니다.

## 2. 핵심 성질: 자체유도(self-induction)

전류가 변하면 코일 자신의 자기선속이 변합니다. 패러데이 법칙에 따라 그 코일에 **자기 자신이 만든 기전력**이 유도됩니다.

$$\mathcal{E}_L = -\frac{d(N\Phi_B)}{dt} = -L\frac{di}{dt}$$

- 전류가 **증가**하면 증가를 막는 방향으로 기전력이 생깁니다(역기전력).
- 전류가 **감소**하면 감소를 막는, 즉 전류를 유지하려는 방향으로 기전력이 생깁니다.
- 전류가 **일정**하면 $di/dt = 0$ 이므로 기전력이 없고, 그냥 도선입니다.

앞 질문의 "스위치를 닫는 순간 전류가 바로 흐르지 못한다"는 현상이 바로 이 성질에서 나옵니다.

## 3. 에너지 저장

인덕터에 전류 $i$ 를 흘리려면 역기전력을 이기며 일을 해야 합니다. 그 일은 **자기장 에너지**로 저장됩니다.

$$U_B = \frac{1}{2}Li^2$$

스위치를 끊을 때 스파크가 튀는 이유도 이것입니다. 저장된 에너지가 갈 곳을 찾으면서 순간적으로 큰 전압이 생깁니다.

## 4. 커패시터와 비교

인덕터는 커패시터와 짝을 이루는 개념이라 함께 보면 이해하기 쉽습니다.

| 구분 | 커패시터 (C) | 인덕터 (L) |
| --- | --- | --- |
| 구조 | 마주 보는 두 도체판 | 감은 코일 |
| 에너지 저장 장소 | 전기장 | 자기장 |
| 저장 에너지 | $\frac{1}{2}CV^2$ | $\frac{1}{2}Li^2$ |
| 급변을 허용하지 않는 양 | **전압** | **전류** |
| 기본 관계식 | $i = C\,\dfrac{dV}{dt}$ | $V = L\,\dfrac{di}{dt}$ |
| 직류 정상상태 | 끊어진 회로 | 단순 도선 |

## 5. 어디에 쓰이나

- **변압기**: 두 코일 사이의 상호유도로 전압을 바꿉니다.
- **전원 회로(SMPS)**: 전류를 매끄럽게 하고 에너지를 잠시 저장합니다.
- **필터**: 고주파 노이즈를 막습니다(초크 코일).
- **LC 공진 회로**: 라디오에서 원하는 주파수를 고르는 데 씁니다.
- **무선 충전, 모터, 릴레이** 등 전자기 장치 전반에 쓰입니다.

---

**요약:** 인덕터는 코일로 된 소자입니다. 전류 → 자기장 → 자기선속 → (전류가 변하면) 자체유도 기전력으로 이어지는 과정 때문에 **전류의 관성** 같은 역할을 합니다. 역학의 질량 $m$ 처럼, 인덕턴스 $L$ 이 클수록 전류를 바꾸기 어렵습니다.
[Timestamp: 2026/10/04 18:54:28]

**user**: "적분가능 형태" 를 영어로?
[Timestamp: 2026/10/04 19:11:24]

**ai**: "적분가능 형태"는 영어로 보통 **integrable form**이라고 합니다.

다만 문맥에 따라 더 정확한 표현이 따로 있습니다.

| 문맥 | 영어 표현 | 의미 |
| --- | --- | --- |
| 일반적인 표현 | **integrable form** | 적분할 수 있는 꼴 |
| 미분방정식을 변수분리한 경우 | **separable form** / **separated form** | $f(y)\,dy = g(x)\,dx$ 꼴 |
| 바로 적분할 수 있게 정리한 경우 | **a form ready for integration** | 양변을 바로 적분할 수 있는 상태 |
| 완전미분방정식 | **exact form** (exact differential) | $M\,dx + N\,dy = dF$ 꼴 |

강의의 RL 회로 풀이라면 **separable form**이 가장 자연스럽습니다. 키르히호프 식을 정리하면

$$\frac{di}{\mathcal{E}/R - i} = \frac{R}{L}\,dt$$

가 되는데, 영어 교재에서는 이 단계를 "rearranging into **separable form** and integrating both sides…"처럼 씁니다.

참고로 수학에서 "integrable"만 단독으로 쓰면 "적분 가능한 함수"(예: Riemann integrable)라는 뜻이 됩니다. 식을 적분할 수 있게 정리했다는 뜻을 분명히 하려면 separable form이나 a form ready for integration을 쓰는 편이 오해가 적습니다.
[Timestamp: 2026/10/04 19:11:24]

**user**: "축전기에 대전된 전하" 영어로
[Timestamp: 2026/10/05 15:23:51]

**ai**: "축전기에 대전된 전하"는 영어로 보통 **the charge on the capacitor**라고 합니다.

| 표현 | 쓰임 |
| --- | --- |
| **the charge on the capacitor** | 가장 흔한 교과서식 표현 |
| **the charge stored on (in) the capacitor** | "저장된" 의미를 강조할 때 |
| **the charge on the capacitor plates** | 극판 위의 전하임을 분명히 할 때 |
| **the capacitor's charge** | 짧게 쓸 때 |

예문:

- "The **charge on the capacitor** is $Q = CV$."
- "When the switch is closed, the **charge stored on the capacitor** decreases exponentially."

"대전된"을 살려 **the charge accumulated on the capacitor**라고 해도 되지만, 물리 교재에서는 거의 the charge on the capacitor 하나로 통일해서 씁니다.

한 가지 주의할 점이 있습니다. 축전기 전체의 알짜 전하(net charge)는 항상 0입니다. 한쪽 극판에 $+Q$, 다른 쪽 극판에 $-Q$가 있기 때문입니다. "the charge on the capacitor"는 관례적으로 **한쪽 극판에 있는 전하의 크기 $Q$** 를 뜻합니다. 이 점을 분명히 하고 싶다면 "the magnitude of the charge on each plate"라고 쓰면 됩니다.
[Timestamp: 2026/10/05 15:23:51]

**user**: 95 페이지에서, 왜 | $U_E = \dfrac{q^2}{2C} = \dfrac{1}{2}C(\Delta\phi)^2$ | $U_B = \dfrac{\Phi_B^2}{2L} = \dfrac{1}{2}Li^2$ |
| ----------------------------------------------------- | ----------------------------------------------- | 이지?
[Timestamp: 2026/10/06 12:22:39]

**ai**: 95페이지의 두 식은 **"저장된 에너지 = 그 상태를 만드는 데 한 일"** 이라는 같은 논리로 유도됩니다. 축전기와 인덕터가 수학적으로 똑같은 구조이기 때문에 식 모양도 똑같습니다.

## 1. 축전기: $U_E = \dfrac{q^2}{2C} = \dfrac{1}{2}C(\Delta\phi)^2$

여기서 $\Delta\phi$ 는 **극판 사이의 전위차**(보통 교재의 $V$)입니다.

**유도 과정**

- 축전기에 이미 전하 $q'$ 가 있으면 극판 사이 전위차는 $\Delta\phi' = q'/C$ 입니다.
- 여기에 전하 $dq'$ 를 더 옮기려면 이 전위차를 거슬러 일을 해야 합니다.
$$dW = \Delta\phi'\,dq' = \frac{q'}{C}\,dq'$$
- 전하를 $0$부터 $q$ 까지 채우는 동안 한 일을 모두 더하면
$$U_E = \int_0^q \frac{q'}{C}\,dq' = \frac{q^2}{2C}$$

**두 번째 형태**: $q = C\,\Delta\phi$ 를 대입하면

$$U_E = \frac{(C\Delta\phi)^2}{2C} = \frac{1}{2}C(\Delta\phi)^2$$

## 2. 인덕터: $U_B = \dfrac{\Phi_B^2}{2L} = \dfrac{1}{2}Li^2$

**유도 과정** (96페이지 내용)

- 전류가 $i'$ 일 때 전류를 늘리면 역기전력 $\mathcal{E}_L = L\,di'/dt$ 가 생깁니다.
- 전원은 이 역기전력을 거슬러 전하를 밀어야 하므로, 인덕터에 공급되는 일률은
$$P = \mathcal{E}_L\, i' = L\frac{di'}{dt}\,i'$$
- 따라서 $dW = P\,dt = L\,i'\,di'$ 이고, 전류를 $0$부터 $i$ 까지 키우는 동안 한 일은
$$U_B = \int_0^i L\,i'\,di' = \frac{1}{2}Li^2$$

**두 번째 형태**: 인덕턴스의 정의 $\Phi_B = Li$ 에서 $i = \Phi_B / L$ 을 대입하면

$$U_B = \frac{1}{2}L\left(\frac{\Phi_B}{L}\right)^2 = \frac{\Phi_B^2}{2L}$$

여기서 $\Phi_B$ 는 코일 전체의 **쇄교 자기선속**(flux linkage, $N\Phi$)입니다. 감은 수 $N$ 이 포함된 값입니다.

## 3. 두 식이 똑같이 생긴 이유: 대응 관계

두 소자 모두 "**한 양이 다른 양에 비례**"하는 선형 관계를 가집니다.

| 축전기 | 인덕터 |
| --- | --- |
| $q = C\,\Delta\phi$ | $\Phi_B = L\,i$ |
| 전하 $q$ | 자기선속 $\Phi_B$ |
| 전위차 $\Delta\phi$ | 전류 $i$ |
| 전기용량 $C$ | 인덕턴스 $L$ |
| $U_E = \dfrac{q^2}{2C} = \dfrac{1}{2}C(\Delta\phi)^2$ | $U_B = \dfrac{\Phi_B^2}{2L} = \dfrac{1}{2}Li^2$ |

표에서 $q \leftrightarrow \Phi_B$, $\Delta\phi \leftrightarrow i$, $C \leftrightarrow L$ 로 바꾸면 한쪽 식이 다른 쪽 식으로 그대로 바뀝니다.

**그래프로 보면**: $\Delta\phi$–$q$ 그래프와 $i$–$\Phi_B$ 그래프는 둘 다 원점을 지나는 직선입니다. 에너지는 그 아래 **삼각형의 넓이**(밑변 × 높이 × ½)이므로 두 경우 모두 $\frac{1}{2}$ 이 붙습니다.

$$U_E = \frac{1}{2}\,q\,\Delta\phi, \qquad U_B = \frac{1}{2}\,\Phi_B\, i$$

이 "½ × 두 양의 곱" 형태에 비례 관계를 대입해서 한 변수를 없애면 표의 두 가지 형태가 나옵니다.

## 4. 역학과의 비유

용수철 에너지 $\frac{1}{2}kx^2$ 과 운동에너지 $\frac{1}{2}mv^2$ 에 대응시켜 보면 이해가 더 쉽습니다.

- 축전기의 $\dfrac{q^2}{2C}$ 는 **용수철 퍼텐셜 에너지** $\dfrac{1}{2}kx^2$ 에 대응합니다. ($q \leftrightarrow x$, $1/C \leftrightarrow k$)
- 인덕터의 $\dfrac{1}{2}Li^2$ 은 **운동에너지** $\dfrac{1}{2}mv^2$ 에 대응합니다. ($i \leftrightarrow v$, $L \leftrightarrow m$)

앞에서 말한 "인덕터 = 전류의 관성"과 같은 맥락입니다. LC 회로에서 에너지가 축전기와 인덕터를 오가며 진동하는 것도, 용수철–질량계에서 퍼텐셜 에너지와 운동에너지가 서로 바뀌는 것과 같은 현상입니다.
[Timestamp: 2026/10/06 12:22:39]

**user**: energy density 는 어떻게 유도하나요?
[Timestamp: 2026/10/06 13:50:03]

**ai**: 노트 98–100페이지가 바로 이 유도 과정입니다. 방법은 하나입니다.

**에너지 밀도 = 저장된 전체 에너지 ÷ 장이 차 있는 부피**

다만 장이 균일해야 이렇게 단순히 나눌 수 있습니다. 그래서 장이 **균일하게 한 영역에만 갇혀 있는** 두 가지 이상적인 장치를 씁니다(98페이지).

- **평행판 축전기**: 판 면적 $S$, 간격 $d$ ($\sqrt{S} \gg d$)입니다. 균일한 $E$ 가 판 사이에만 있습니다.
- **긴 솔레노이드**: 길이 $l$, 단면적 $S$ ($l \gg a$)입니다. 균일한 $B$ 가 내부에만 있습니다.

## 1. 전기장 에너지 밀도 $u_E = \dfrac{1}{2}\varepsilon_0 E^2$

**① 필요한 관계식**

- 전기용량: $C = \dfrac{\varepsilon_0 S}{d}$
- 균일한 전기장에서 전위차: $\Delta\phi = Ed$

**② 에너지 식에 대입**

$$U_E = \frac{1}{2}C(\Delta\phi)^2 = \frac{1}{2}\cdot\frac{\varepsilon_0 S}{d}\cdot(Ed)^2 = \frac{1}{2}\varepsilon_0 E^2\cdot(Sd)$$

**③ 부피로 나누기**

장이 차 있는 부피는 판 사이 공간 $Sd$ 입니다.

$$u_E = \frac{U_E}{Sd} = \frac{1}{2}\varepsilon_0 E^2$$

## 2. 자기장 에너지 밀도 $u_B = \dfrac{B^2}{2\mu_0}$

**① 필요한 관계식** ($n = N/l$: 단위 길이당 감은 수)

- 인덕턴스: $L = \mu_0 n^2 l S$
- 솔레노이드 내부 자기장: $B = \mu_0 n i$ 이므로 $i = \dfrac{B}{\mu_0 n}$

**② 에너지 식에 대입**

$$U_B = \frac{1}{2}Li^2 = \frac{1}{2}\cdot\mu_0 n^2 lS\cdot\frac{B^2}{\mu_0^2 n^2} = \frac{B^2}{2\mu_0}\cdot(Sl)$$

$n^2$ 이 약분되고 $\mu_0$ 가 하나 남습니다.

**③ 부피로 나누기**

장이 차 있는 부피는 솔레노이드 내부 $Sl$ 입니다.

$$u_B = \frac{U_B}{Sl} = \frac{B^2}{2\mu_0}$$

## 3. 유도 과정 나란히 보기

| 단계 | 평행판 축전기 | 솔레노이드 |
| --- | --- | --- |
| 회로 에너지 | $\frac{1}{2}C(\Delta\phi)^2$ | $\frac{1}{2}Li^2$ |
| 기하 공식 | $C = \varepsilon_0 S/d$ | $L = \mu_0 n^2 lS$ |
| 회로량 → 장 | $\Delta\phi = Ed$ | $i = B/(\mu_0 n)$ |
| 결과 | $\frac{1}{2}\varepsilon_0 E^2 \times (Sd)$ | $\frac{B^2}{2\mu_0}\times(Sl)$ |
| 에너지 밀도 | $u_E = \frac{1}{2}\varepsilon_0 E^2$ | $u_B = \frac{B^2}{2\mu_0}$ |

핵심은 **회로량($\Delta\phi$, $i$, $C$, $L$)을 장($E$, $B$)과 기하 크기로 바꾸면 기하 크기가 정확히 "부피"로만 남는다**는 점입니다. 그래서 남은 계수가 장치 모양과 무관한, 장 자체의 성질이 됩니다.

## 4. 왜 이 결과가 일반적인가

특수한 장치로 유도했지만, 결과에는 $S$, $d$, $l$, $n$ 같은 장치 정보가 전혀 남지 않습니다. 이는 에너지가 극판이나 도선이 아니라 **공간의 장 자체에 저장된다**는 뜻입니다. 따라서 장이 균일하지 않은 일반적인 경우에도 각 점에서 이 밀도를 쓰고 부피 적분하면 됩니다.

$$U = \int \left(\frac{1}{2}\varepsilon_0 E^2 + \frac{B^2}{2\mu_0}\right) dV$$

(더 엄밀한 일반 증명은 맥스웰 방정식에서 나오는 포인팅 정리로 합니다.)

**참고로 하나 더:** 전자기파에서는 $E = cB$ 이고 $c^2 = 1/(\varepsilon_0\mu_0)$ 입니다. 이를 대입하면 $\frac{1}{2}\varepsilon_0 E^2 = \frac{B^2}{2\mu_0}$ 이 됩니다. 즉 빛 속에서는 전기장 에너지와 자기장 에너지가 정확히 반씩 나뉩니다.
[Timestamp: 2026/10/06 13:50:03]

**user**: 아래 내용을 각각 영어로번역해줘.
[Timestamp: 2026/10/06 17:27:38]

**ai**: 슬라이드의 왼쪽(축전기)과 오른쪽(인덕터) 문장을 각각 번역했습니다.

## 왼쪽: 축전기 (Capacitor)

**전기용량이 $C$인 축전기를 기전력이 $\mathcal{E}$인 전지로 충전**
- Charging a capacitor of capacitance $C$ with a battery of EMF $\mathcal{E}$

**축전기의 전하가 $q'$일 때, 축전기 양단의 전위차**
- When the charge on the capacitor is $q'$, the potential difference across the capacitor is
$$\Delta\phi = \frac{q'}{C}$$

**전위차가 $\Delta\phi$인 축전기에 전하 $dq'$을 더하는 데 전지가 축전기에 하는 일**
- The work done by the battery on the capacitor to add charge $dq'$ to the capacitor at potential difference $\Delta\phi$ is
$$dW = \Delta\phi\,dq' = \frac{q'}{C}\,dq'$$

## 오른쪽: 인덕터 (Inductor)

**인덕턴스가 $L$인 인덕터를 기전력이 $\mathcal{E}$인 전지에 연결**
- Connecting an inductor of inductance $L$ to a battery of EMF $\mathcal{E}$

**인덕터에 흐르는 전류가 $i'$일 때, 인덕터 양단의 전위차**
- When the current through the inductor is $i'$, the potential difference across the inductor is
$$\Delta\phi = L\frac{di'}{dt}$$

**전위차가 $\Delta\phi$인 인덕터에 전하 $dq'$을 더 이동시키는 데 전지가 인덕터에 하는 일**
- The work done by the battery on the inductor to move an additional charge $dq'$ through the inductor at potential difference $\Delta\phi$ is
$$dW = \Delta\phi\,dq' = L\frac{di'}{dt}\,dq' = L\,di'\,\frac{dq'}{dt} = L\,i'\,di'$$

## 번역 메모

- "충전"은 **charging**입니다. "전지에 연결"은 **connecting ... to a battery**입니다.
- "양단의 전위차"는 **the potential difference across**입니다. 영어 교재에서는 흔히 *the voltage across*라고도 씁니다.
- 축전기에서는 전하가 극판에 **쌓이므로** "add charge to"를 썼습니다. 인덕터에서는 전하가 코일을 **통과하므로** "move charge through"를 썼습니다. 원문의 "더하는"과 "더 이동시키는"의 차이를 살린 것입니다.
- 마지막 단계 $L\,di'\,\dfrac{dq'}{dt} = L\,i'\,di'$ 는 $\dfrac{dq'}{dt} = i'$ (전류의 정의)를 쓴 것입니다. 설명을 덧붙인다면 "using $dq'/dt = i'$"라고 쓰면 됩니다.
[Timestamp: 2026/10/06 17:27:38]

**user**: page 96의 내용을 위에서 번역한 내용으로 바꾸어 주세요.
[Timestamp: 2026/10/06 17:40:35]

**ai**: [[차동우 일반물리2 19_전자기유도_EN]]의 Page 96 본문을 앞에서 번역한 슬라이드 내용으로 바꿨습니다.

새 본문은 슬라이드처럼 두 부분입니다.

- **Capacitor**: 충전 상황, $\Delta\phi = q'/C$, $dW = \dfrac{q'}{C}\,dq'$
- **Inductor**: 전지에 연결한 상황, $\Delta\phi = L\,di'/dt$, $dW = L\,i'\,di'$

바뀐 점 두 가지를 알려 드립니다.

- **삭제된 내용**: 원래 있던 일률 식 $P = L\dfrac{di}{dt}\cdot i$ 와 적분 결과 $W = \int_0^i L\,i'\,di' = \frac{1}{2}Li^2$ 은 지웠습니다. 다만 적분 결과는 Page 97에 $U_B = \frac{1}{2}Li^2$ 로 그대로 남아 있습니다.
- **제목은 그대로 두었습니다**: 섹션 제목이 아직 "Magnetic Energy Stored in Inductor (Derivation Setup)"입니다. 이제 축전기 내용도 들어 있으므로 "Work Done by the Battery: Capacitor vs. Inductor" 같은 제목이 더 맞을 수 있습니다. 원하시면 바꿔 드리겠습니다.
[Timestamp: 2026/10/06 17:40:35]

**user**: 위 내용도 영어로 각각 번역해 주세요. page 97의 내용입니다.
[Timestamp: 2026/10/06 17:41:41]

**ai**: Page 97 슬라이드의 왼쪽(축전기)과 오른쪽(인덕터)을 각각 번역했습니다.

## 왼쪽: 축전기 (Capacitor)

$$dW = \frac{q'}{C}\,dq'$$

**축전기에 대전된 전하가 0에서 시작해서 $q$가 될 때까지 전지가 축전기에 해준 전체 일**
- The total work done by the battery on the capacitor as the charge on the capacitor increases from 0 to $q$
$$W = \int_0^q \frac{q'}{C}\,dq' = \frac{q^2}{2C}$$

**전지가 축전기를 충전하며 한 일이 축전기에 전기에너지로 저장됨**
- The work done by the battery in charging the capacitor is stored in the capacitor as electric energy.
$$U_E = \frac{q^2}{2C} = \frac{1}{2}C(\Delta\phi)^2 \qquad (q = C\Delta\phi)$$

## 오른쪽: 인덕터 (Inductor)

$$dW = L\,i'\,di'$$

**인덕터에 흐르는 전류가 0에서 시작해서 $i$가 될 때까지 전지가 인덕터에 해준 전체 일**
- The total work done by the battery on the inductor as the current through the inductor increases from 0 to $i$
$$W = \int_0^i L\,i'\,di' = \frac{1}{2}Li^2$$

**전지가 인덕터에 전류를 흐르게 하며 한 일이 인덕터에 자기에너지로 저장됨**
- The work done by the battery in driving current through the inductor is stored in the inductor as magnetic energy.
$$U_B = \frac{1}{2}Li^2 = \frac{\Phi_B^2}{2L} \qquad (\Phi_B = Li)$$

## 번역 메모

- 슬라이드 맨 위 왼쪽 식은 이미지에서 분자 $q'$ 가 빠져 "$dW = {}_C\,dq'$"처럼 보입니다. 적분 기호도 깨져 보입니다. 렌더링 오류로 보여서 Page 96과 같은 $dW = \dfrac{q'}{C}\,dq'$ 로 복원했습니다.
- "0에서 시작해서 ~가 될 때까지"는 **increases from 0 to ~** 로 간결하게 옮겼습니다.
- "전류를 흐르게 하며"는 **driving current through** 입니다. 회로에서 전원이 전류를 흘려보낸다는 뜻으로 영어 교재에서 많이 쓰는 표현입니다.
- "전기에너지/자기에너지로 저장됨"은 **is stored ... as electric / magnetic energy** 입니다.

Page 96처럼 이 번역으로 노트의 Page 97 본문을 바꾸길 원하시면 말씀해 주세요.
[Timestamp: 2026/10/06 17:41:41]

**user**: 위 번역을 바탕으로, 97페이지를 업데이트 해주세요.
[Timestamp: 2026/10/06 17:56:02]

**ai**: [[차동우 일반물리2 19_전자기유도_EN]]의 Page 97 본문을 번역 내용으로 바꿨습니다. 형식은 Page 96과 같습니다.

- **Capacitor**: $dW = \dfrac{q'}{C}\,dq'$ 를 $0$에서 $q$까지 적분해 $W = \dfrac{q^2}{2C}$ 를 구합니다. 전지가 한 일이 전기에너지로 저장되므로 $U_E = \dfrac{q^2}{2C} = \dfrac{1}{2}C(\Delta\phi)^2$ 입니다(using $q = C\Delta\phi$).
- **Inductor**: $dW = L\,i'\,di'$ 를 $0$에서 $i$까지 적분해 $W = \frac{1}{2}Li^2$ 을 구합니다. 전지가 한 일이 자기에너지로 저장되므로 $U_B = \frac{1}{2}Li^2 = \dfrac{\Phi_B^2}{2L}$ 입니다(using $\Phi_B = Li$).

원래 노트에서 $U_B$ 결과에 쳐져 있던 박스는 유지했고, 짝을 맞추려고 $U_E$ 결과에도 박스를 쳤습니다.

**제목은 그대로입니다**: 섹션 제목이 아직 "Magnetic Energy (Result)"인데, 이제 전기에너지 내용도 들어 있습니다. Page 96 제목과 함께 바꿀 만합니다. 예를 들면 다음과 같습니다.

- Page 96: "Work Done by the Battery: Capacitor vs. Inductor"
- Page 97: "Electric Energy and Magnetic Energy (Result)"

원하시면 두 제목을 함께 바꿔 드리겠습니다.
[Timestamp: 2026/10/06 17:56:02]