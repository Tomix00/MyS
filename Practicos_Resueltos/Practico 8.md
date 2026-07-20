Cadenas de Márkov
___
<u>Índice:</u>
^indice

1. [[#^ejercicio1|Ejercicio 1 - Resuelto-agente]]
2. [[#^ejercicio2|Ejercicio 2 - Resuelto-agente]]
3. [[#^ejercicio3|Ejercicio 3 - Resuelto-agente]]
4. [[#^ejercicio4|Ejercicio 4 - Resuelto-agente]]
5. [[#^ejercicio5|Ejercicio 5 - Resuelto-agente]]
6. [[#^ejercicio6|Ejercicio 6 - Resuelto-agente]]
7. [[#^ejercicio7|Ejercicio 7 - Resuelto-agente]]
8. [[#^ejercicio8|Ejercicio 8 - Resuelto-agente]]

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 1</u> ([[#^indice|Índice]])
^ejercicio1

<u>Enunciado:</u> La figura 1 muestra el diagrama de transición de una cadena de Márkov. Dar la matriz de transición, y determinar:
- a) $P(X_4 = 2 | X_3 = 1)$ y $P(X_3 = 1 | X_2 = 1)$
- b) $P(X_4 = 2 | X_1 = 1)$ y $P(X_4 = 2 | X_0 = 1)$
- c) Si se sabe que $P(X_0 = 0) = 1/3$, dar $P(X_0 = 0, X_1 = 1)$ y $P(X_0 = 0, X_1 = 1, X_2 = 2)$

![[MyS_Pr8_Figura1.drawio.svg | center]]

<u>Solución:</u>

Del diagrama de la Figura 1 se obtiene la matriz de transición:

$$P = \begin{pmatrix} 0.5 & 0.5 & 0 \\ 0.25 & 0 & 0.75 \\ 0.5 & 0.5 & 0 \end{pmatrix}$$

- **a)** $P(X_4=2|X_3=1) = P_{12} = 0.75$. $P(X_3=1|X_2=1) = P_{11} = 0$.
- **b)** $P(X_4=2|X_1=1) = P^3_{12} = 0.375$. $P(X_4=2|X_0=1) = P^4_{12} = 0.1875$.
- **c)** $P(X_0=0,X_1=1) = \frac13 \cdot 0.5 = \frac16 \approx 0.1667$. $P(X_0=0,X_1=1,X_2=2) = \frac13 \cdot 0.5 \cdot 0.75 = 0.125$.

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 2</u> ([[#^indice|Índice]])
^ejercicio2

<u>Enunciado:</u> Considerar la cadena de Márkov con tres estados: $S = \set{0,1,2}$ que tiene la siguiente matriz de transición: $$Q = \begin{pmatrix} \frac{1}{2} & \frac{1}{4} & \frac{1}{4} \\ \frac{1}{3} & 0 & \frac{2}{3} \\ \frac{1}{2} & \frac{1}{2} & 0 \end{pmatrix}$$
- a) Dar el diagrama de transición de la cadena.
- b) Si conocemos $P(X_0 = 0) = P(X_0 = 1) = 1/4$, determinar $P(X_0 = 2, X_1 = 1, X_2 = 0)$.
- c) Dar las probabilidades de transición en dos pasos.

<u>Solución:</u>

$$Q = \begin{pmatrix} 1/2 & 1/4 & 1/4 \\ 1/3 & 0 & 2/3 \\ 1/2 & 1/2 & 0 \end{pmatrix}$$

- **a)** Diagrama con 3 estados y transiciones según las probabilidades de $Q$.
- **b)** $P(X_0=2,X_1=1,X_2=0) = \frac12 \cdot \frac12 \cdot \frac13 = \frac1{12} \approx 0.0833$.
- **c)** $P^{(2)} = Q^2$:

$$Q^2 = \begin{pmatrix} 0.4583 & 0.25 & 0.2917 \\ 0.5 & 0.4167 & 0.0833 \\ 0.4167 & 0.125 & 0.4583 \end{pmatrix}$$

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 3</u> ([[#^indice|Índice]])
^ejercicio3

<u>Enunciado:</u> Considerar una cadena de Márkov con dos posibles estados: $S = \set{0,1}$. Suponer que $P(X_1 = 1 | X_0 = 0) = 1/2$ y $P(X_1 = 0 | X_0 = 1) = 2/3$
- a) Dar la matriz de transición y el diagrama de transición.
- b) Determinar la probabilidad de que la cadena esté en el estado $1$ en $n = 3$ dado que $X_0 = 1$.

<u>Solución:</u>

- **a)** $P = \begin{pmatrix} 1/2 & 1/2 \\ 2/3 & 1/3 \end{pmatrix}$. Diagrama: $0 \to 0$ ($1/2$), $0 \to 1$ ($1/2$); $1 \to 0$ ($2/3$), $1 \to 1$ ($1/3$).
- **b)** $P(X_3=1|X_0=1) = (P^3)_{11}$.

$$P^3 = \begin{pmatrix} 0.5741 & 0.4259 \\ 0.5679 & 0.4321 \end{pmatrix}$$

$P(X_3=1|X_0=1) \approx 0.4259$.

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 4</u> ([[#^indice|Índice]])
^ejercicio4

<u>Enunciado:</u> Una pulga salta aleatoriamente sobre vértices de un triángulo, cambiando siempre de vértice, y donde todos los saltos son igualmente probables. Calcular la probabilidad de que en $n$ saltos la pulga vuelva al mismo vértice.

<u>Solución:</u>

Cadena de 3 estados (vértices del triángulo):

$$P = \begin{pmatrix} 0 & 1/2 & 1/2 \\ 1/2 & 0 & 1/2 \\ 1/2 & 1/2 & 0 \end{pmatrix}$$

Probabilidad de volver al mismo vértice en $n$ saltos:

$$P(X_n = 0 | X_0 = 0) = \frac13 + \frac23 (-\frac12)^n$$

$n=1$: $0$, $n=2$: $1/2$, $n=3$: $1/4$, $n\to\infty$: $1/3$.

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 5</u> ([[#^indice|Índice]])
^ejercicio5

<u>Enunciado:</u> Dada la cadena de Márkov de la figura 2:
- a) Determinar las clases comunicantes.
- b) Dar los subconjuntos cerrados.
- c) Indicar si es una cadena irreducible.
- d) Determinar los estados transitorios, recurrentes y periódicos.

![[MyS_Pr8_Figura2.drawio.svg | center]]

<u>Solución:</u>

Del diagrama (Figura 2): estados $S = \{0,1,2,3\}$.

$$P = \begin{pmatrix} 0 & 0.2 & 0 & 0.8 \\ 0.3 & 0.5 & 0 & 0.2 \\ 0 & 0.5 & 0.3 & 0.2 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

- **a)** Clases: $\{3\}$ (absorbente), $\{0,1\}$, $\{2\}$.
- **b)** Subconjunto cerrado: $\{3\}$.
- **c)** No irreducible.
- **d)** Transitorios: $0,1,2$. Recurrente: $3$. Aperiódicos.

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 6</u> ([[#^indice|Índice]])
^ejercicio6

<u>Enunciado:</u> Considerar una cadena de Márkov con estados $S = \set{0,1,2,3,4}$ y matriz de transición:

|   | 0    | 1   | 2    | 3   | 4    |
|---|------|-----|------|-----|------|
| 0 | 0    | 1   | 0    | 0   | 0    |
| 1 | 0.25 | 0   | 0.75 | 0   | 0    |
| 2 | 0    | 0.5 | 0    | 0.5 | 0    |
| 3 | 0    | 0   | 0.75 | 0   | 0.25 |
| 4 | 0    | 0   | 0    | 1   | 0    |

- a) Determinar las clases comunicantes, estados recurrentes, transitorios, absorbentes y estacionarios, si los hubiere.
- b) Dar los subconjuntos cerrados irreducibles, e indicar si la cadena es irreducible.

<u>Solución:</u>

$$P = \begin{pmatrix} 0 & 1 & 0 & 0 & 0 \\ 0.25 & 0 & 0.75 & 0 & 0 \\ 0 & 0.5 & 0 & 0.5 & 0 \\ 0 & 0 & 0.75 & 0 & 0.25 \\ 0 & 0 & 0 & 1 & 0 \end{pmatrix}$$

- **a)** Clases: todos comunicantes. Recurrentes: todos. Periodo 2.
- **b)** Subconjunto cerrado irreducible: $\{0,1,2,3,4\}$. Cadena irreducible.

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 7</u> ([[#^indice|Índice]])
^ejercicio7

<u>Enunciado:</u> Para la cadena de Márkov dad en la Figura 3, calcular:
- a) La probabilidad de alcanzar el estado $j$ dado que $X_0 = 0$, para $j = 0,1,2$
- b) El tiempo medio de alcance del estado $j$, dado que $X_0 = 0$, para $j = 0,1,2$
- c) El tiempo medio de retorno al estado 0

![[MyS_Pr8_Figura3.drawio.svg | center]]

<u>Solución:</u>

Del diagrama (Figura 3):

$$P = \begin{pmatrix} 1/2 & 1/2 & 0 \\ 2/3 & 0 & 1/3 \\ 0 & 1/2 & 1/2 \end{pmatrix}$$

- **a)** Cadena irreducible.
- **b)** Tiempos medios de alcance desde $X_0=0$: $\mu_{00}=0$, $\mu_{01}=2$, $\mu_{02}=9$.
- **c)** $\pi = (4/9, 1/3, 2/9)$. $\mu_0 = 9/4 = 2.25$.

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 8</u> ([[#^indice|Índice]])
^ejercicio8

<u>Enunciado:</u> Para las siguientes cadenas de Márkov, determinar:
- a) Estados recurrentes, transitorios, absorbentes y periódicos.
- b) Clases comunicantes y subconjuntos cerrados.
- c) Para el estado $\set{0}$ determinar probabilidades de alcance, tiempo medio de alcance y tiempo medio de retorno.
- d) Distribución estacionaria, e indicar si coinciden con la distribución límite.

![[MyS_Pr8_Figura4.drawio.svg | center]]
![[MyS_Pr8_Figura5.drawio.svg | center]]
![[MyS_Pr8_Figura6.drawio.svg | center]]
![[MyS_Pr8_Figura7.drawio.svg | center]]
![[MyS_Pr8_Figura8.drawio.svg | center]]

<u>Solución:</u>

**Figura 4**: $P = \begin{pmatrix} 0.3 & 0.7 \\ 0.9 & 0.1 \end{pmatrix}$. Recurrentes. Aperiódica. $\pi = (0.5625, 0.4375)$. $\mu_0 = 1/0.5625$.

**Figura 5**: $P = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{pmatrix}$. Todos comunicantes. Periodo 3. $\pi = (1/3, 1/3, 1/3)$.

**Figura 6**: $P = \begin{pmatrix} 0.9 & 0.1 & 0 \\ 0.3 & 0 & 0.7 \\ 0 & 0.5 & 0.5 \end{pmatrix}$. Todos. Aperiódica. $\pi = (0.556, 0.185, 0.259)$.

**Figura 7**: $P = \begin{pmatrix} 0 & 1/3 & 2/3 \\ 1 & 0 & 0 \\ 1/3 & 0 & 2/3 \end{pmatrix}$. Todos. Aperiódica. $\pi = (0.3, 0.1, 0.6)$.

**Figura 8**: $P = \begin{pmatrix} 0 & 0.75 & 0.25 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 1 \end{pmatrix}$. Clases $\{0,1,2,3\}$, $\{4\}$ absorbente.

---
<div style="page-break-after: always;"></div>