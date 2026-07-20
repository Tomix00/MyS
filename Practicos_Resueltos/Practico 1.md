
--- 
<u>Índice</u>
^indice

1. [[#^ejercicio1|Ejercicio 1 - Resuelto-agente]]
2. [[#^ejercicio2|Ejercicio 2 - Resuelto-agente]]
3. [[#^ejercicio3|Ejercicio 3 - Resuelto-agente]]
4. [[#^ejercicio4|Ejercicio 4 - Resuelto-agente]]
5. [[#^ejercicio5|Ejercicio 5 - Resuelto-agente]]
6. [[#^ejercicio6|Ejercicio 6 - Resuelto-agente]]
7. [[#^ejercicio7|Ejercicio 7 - Resuelto-agente]]
8. [[#^ejercicio8|Ejercicio 8 - Resuelto-agente]]
9. [[#^ejercicio9|Ejercicio 9 - Resuelto-agente]]
10. [[#^ejercicio10|Ejercicio 10 - Resuelto-agente]]
11. [[#^ejercicio11|Ejercicio 11 - Resuelto-agente]]
12. [[#^ejercicio12|Ejercicio 12 - Resuelto-agente]]
13. [[#^ejercicio13|Ejercicio 13 - Resuelto-agente]]
14. [[#^ejercicio14|Ejercicio 14 - Resuelto-agente]]
15. [[#^ejercicio15|Ejercicio 15 - Resuelto-agente]]

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 1</u> ([[#^indice|Índice]])
^ejercicio1

<u>Enunciado:</u> Considere un experimento que consta de una carrera de cuatro caballos, numerados del $1$ al $4$, y suponga que el espacio muestral está dado por todas las permutaciones de esos números, donde $(1,2,3,4)$ significa que el caballo $1$ llego primero, el $2$ segundo, $3$ tercero y el $4$ cuarto, por ejemplo.
Sean $A$ el evento en el que el caballo número $1$ está entre los tres primeros finalistas, $B$ el evento que el caballo número $2$ llegue en segundo lugar, y $C$ el evento que el caballo número $3$ llegue en tercer lugar.
- a) Describa el evento $AB$. ¿Cuántos resultados están contenidos en este evento?
- b) ¿Cuántos resultados están contenidos en el evento $A\cup B$?
- c) ¿Cuántos resultados están contenidos en el evento $ABC$?
- d) ¿Cuántos resultados están contenidos en el evento $A\cup(BC)$?

<u>Solución:</u>

El espacio muestral $\Omega$ consiste de las $4! = 24$ permutaciones de $\{1,2,3,4\}$, todas equiprobables.

**a)** $AB = A \cap B$: el caballo $1$ está entre los tres primeros **y** el caballo $2$ llega en segundo lugar.

Fijamos el caballo $2$ en la posición $2$. El caballo $1$ debe ocupar la posición $1$ o la $3$ (no puede estar en $4$). Para cada una de esas dos opciones, los dos caballos restantes ($3$ y $4$) se ordenan en las dos posiciones libres de $2! = 2$ maneras.

Por tanto, $|AB| = 2 \times 2 = 4$ resultados.

**b)** Usamos el principio de inclusión-exclusión:

$$
|A \cup B| = |A| + |B| - |A \cap B|
$$

- $|A|$: caballo $1$ entre los tres primeros, es decir, **no** está en $4^{\text{to}}$ lugar. De $24$ totales, aquellos con $1$ en $4^{\text{to}}$ son $3! = 6$, luego $|A| = 24 - 6 = 18$.
- $|B|$: caballo $2$ en segundo lugar; fijamos esa posición: $|B| = 3! = 6$.
- $|A \cap B| = 4$ (calculado en (a)).

Entonces:
$$
|A \cup B| = 18 + 6 - 4 = 20.
$$

**c)** $ABC = A \cap B \cap C$: caballo $1$ entre los tres primeros, $2$ en segundo y $3$ en tercero.

Fijamos $2$ en $2^{\text{do}}$ y $3$ en $3^{\text{er}}$. Para que $1$ esté entre los tres primeros, solo puede ir en $1^{\text{er}}$ lugar (pues $2^{\text{do}}$ y $3^{\text{er}}$ ya están ocupados). Entonces la única permutación posible es $(1,2,3,4)$.

$$
|ABC| = 1.
$$

**d)** $A \cup (BC)$ donde $BC = B \cap C$: $2$ en segundo y $3$ en tercero.

$|BC|$: fijamos $2$ en $2^{\text{do}}$ y $3$ en $3^{\text{er}}$; las posiciones $1$ y $4$ se ocupan con $\{1,4\}$ de $2! = 2$ maneras.
Luego $|BC| = 2$, y sus elementos son $(1,2,3,4)$ y $(4,2,3,1)$.

Ahora:
$$
|A \cup (BC)| = |A| + |BC| - |A \cap (BC)|
$$

$A \cap (BC)$: de los $2$ elementos de $BC$, ¿cuáles tienen a $1$ entre los tres primeros? Solo $(1,2,3,4)$, pues en $(4,2,3,1)$ el caballo $1$ está en $4^{\text{to}}$. Por tanto $|A \cap (BC)| = 1$.

$$
|A \cup (BC)| = 18 + 2 - 1 = 19.
$$

---

<div style="page-break-after: always;"></div>

## <u>Ejercicio 2</u> ([[#^indice|Índice]])
^ejercicio2

<u>Enunciado:</u> Cualesquiera sean los evento $A$ y $B$, muestre que
- a) $A\cup B=A\cup (A^cB)$, y que $A=(AB)\cup(AB^c)$(Ayuda: Trazar diagramas de Venn)
- b) $P(A\cup B)=P(A)+P(B)-P(AB)$

<u>Solución:</u>

**a)** Identidades de conjuntos mediante diagramas de Venn.

- $A \cup B = A \cup (A^c B)$: El conjunto $A \cup B$ se puede particionar en los elementos que están en $A$ y los que están en $B$ pero no en $A$, es decir, $A^c \cap B$. Ambas regiones son disjuntas, por lo que $A \cup B = A \cup (A^c B)$.

- $A = (AB) \cup (AB^c)$: El conjunto $A$ se puede particionar en los elementos de $A$ que también están en $B$ ($AB$) y los que están en $A$ pero no en $B$ ($AB^c$). Ambas regiones son disjuntas y su unión es exactamente $A$.

**b)** Demostración de $P(A \cup B) = P(A) + P(B) - P(AB)$.

Del inciso (a) sabemos que $A \cup B = A \cup (A^c B)$, con $A$ y $A^c B$ disjuntos. Por el axioma de aditividad finita:

$$
P(A \cup B) = P(A) + P(A^c B) \tag{1}
$$

Por otro lado, $B = (AB) \cup (A^c B)$, donde $AB$ y $A^c B$ también son disjuntos. Luego:

$$
P(B) = P(AB) + P(A^c B) \implies P(A^c B) = P(B) - P(AB) \tag{2}
$$

Sustituyendo (2) en (1):

$$
P(A \cup B) = P(A) + P(B) - P(AB)
$$

que es la fórmula de inclusión-exclusión para dos eventos.

---


<div style="page-break-after: always;"></div>

## <u>Ejercicio 3</u> ([[#^indice|Índice]])
^ejercicio3

<u>Enunciado:</u> Se extraen dos bolas de una caja que contiene $9$ bolas azules y $7$ bolas amarillas, y el experimento es sin reposición. Si las bolas tienen todas la misma probabilidad de ser extraídas,
- a) ¿Cuál es la probabilidad de sacar dos bolas azules?
- b) ¿Cuál es la probabilidad de sacar la primera azul y la segunda amarilla?

<u>Solución:</u>

Total de bolas: $9$ azules + $7$ amarillas = $16$. La extracción es sin reposición.

**a)** $P(\text{2 azules}) = P(\text{1ª azul}) \times P(\text{2ª azul} \mid \text{1ª azul})$.

$$
P(\text{1ª azul}) = \frac{9}{16}, \qquad
P(\text{2ª azul} \mid \text{1ª azul}) = \frac{8}{15}.
$$

Por lo tanto:

$$
P(\text{2 azules}) = \frac{9}{16} \times \frac{8}{15} = \frac{72}{240} = \frac{3}{10} = 0.3.
$$

**b)** $P(\text{1ª azul y 2ª amarilla}) = P(\text{1ª azul}) \times P(\text{2ª amarilla} \mid \text{1ª azul})$.

Después de extraer una azul, quedan $15$ bolas: $8$ azules y $7$ amarillas. Luego:

$$
P(\text{2ª amarilla} \mid \text{1ª azul}) = \frac{7}{15}.
$$

Por lo tanto:

$$
P(\text{1ª azul y 2ª amarilla}) = \frac{9}{16} \times \frac{7}{15} = \frac{63}{240} = \frac{21}{80} = 0.2625.
$$

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 4</u> ([[#^indice|Índice]])
^ejercicio4

<u>Enunciado:</u> Un bolillero, rotulado $A$, contiene seis $(6)$ bolas rojas y cuatro $(4)$ verdes, y un segundo bolillero, rotulado $B$, contiene siete$ (7)$ bolas rojas y tres $(3)$ verdes. Se realiza el siguiente experimento: Se extrae al azar una bola de $A$ y se coloca en el bolillero $B$. Luego, se extrae al azar una bola de $B$ y se la coloca en el bolillero $A$.
- a) ¿Cuáles son la probabilidades, $P(R_A)$ y $P(V_A)$ de extraer, respectivamente, una bola roja o una verde de $A$, en la primera parte del experimento?
- b) Calcule las probabilidades condicionales, $P(R_B|R_A)$, de obtener una bola roja de $B$ dado que se extrajo una roja de $A$ y $P(R_B|V_A)$, de obtener una bola roja de $B$ dado que se extrajo una verde de $A$.
  Ayuda: Analice el contenido del bolillero $B$ luego de agregarle la bola proveniente de $A$.
- c) Calcule la probabilidad conjunta de obtener una bola roja de $A$ y también una roja de $B$.
  Ayuda: Aplique la definición de probabilidad condicional.
- d) ¿Cuál es la probabilidad, $P(R_B)$, de extraer una bola roja de $B$?
- e) ¿Cuál es la probabilidad de que al finalizar el experimento el bolillero $A$ recupere exactamente la composición de bolas que tenía declarada al comienzo?

<u>Solución:</u>

Sean $R_A$ y $V_A$ los eventos de extraer una bola roja o verde de $A$ en el primer paso, respectivamente. Análogamente, $R_B$ y $V_B$ para el segundo paso (de $B$).

**a)** En $A$ hay inicialmente $6$ rojas y $4$ verdes, total $10$ bolas equiprobables.

$$
P(R_A) = \frac{6}{10} = \frac{3}{5} = 0.6, \qquad
P(V_A) = \frac{4}{10} = \frac{2}{5} = 0.4.
$$

**b)** Analizamos la composición de $B$ luego de agregarle la bola extraída de $A$.

- Si se extrajo roja de $A$ ($R_A$): $B$ pasa a tener $7+1=8$ rojas y $3$ verdes, total $11$ bolas.
  $$
  P(R_B \mid R_A) = \frac{8}{11}.
  $$

- Si se extrajo verde de $A$ ($V_A$): $B$ pasa a tener $7$ rojas y $3+1=4$ verdes, total $11$ bolas.
  $$
  P(R_B \mid V_A) = \frac{7}{11}.
  $$

**c)** Por definición de probabilidad condicional: $P(R_A \cap R_B) = P(R_A) \cdot P(R_B \mid R_A)$.

$$
P(R_A \cap R_B) = \frac{6}{10} \times \frac{8}{11} = \frac{48}{110} = \frac{24}{55}.
$$

**d)** Usamos el teorema de probabilidad total particionando según el resultado de la primera extracción:

$$
P(R_B) = P(R_A) \cdot P(R_B \mid R_A) + P(V_A) \cdot P(R_B \mid V_A).
$$

Sustituyendo:

$$
P(R_B) = \frac{6}{10} \cdot \frac{8}{11} + \frac{4}{10} \cdot \frac{7}{11}
= \frac{48}{110} + \frac{28}{110} = \frac{76}{110} = \frac{38}{55}.
$$

**e)** El bolillero $A$ recupera su composición original ($6$ rojas, $4$ verdes) en dos situaciones:

1. Se extrae roja de $A$ **y** roja de $B$ ($R_A \cap R_B$): $A$ pierde una roja y gana una roja, composición intacta.
2. Se extrae verde de $A$ **y** verde de $B$ ($V_A \cap V_B$): $A$ pierde una verde y gana una verde, composición intacta.

Calculamos $P(V_A \cap V_B) = P(V_A) \cdot P(V_B \mid V_A)$. Como $P(V_B \mid V_A) = 1 - P(R_B \mid V_A) = 1 - \frac{7}{11} = \frac{4}{11}$:

$$
P(V_A \cap V_B) = \frac{4}{10} \times \frac{4}{11} = \frac{16}{110} = \frac{8}{55}.
$$

Por lo tanto:

$$
P(\text{composición original}) = P(R_A \cap R_B) + P(V_A \cap V_B)
= \frac{48}{110} + \frac{16}{110} = \frac{64}{110} = \frac{32}{55}.
$$

---


<div style="page-break-after: always;"></div>

## <u>Ejercicio 5</u> ([[#^indice|Índice]])
^ejercicio5

<u>Enunciado:</u> La variable aleatoria $X$ toma valores en el conjunto $\set{1, 2, 3, 4}$ con la siguiente probabilidad: $$P_i=P(X=i)=ci \qquad\text{para }i=1,2,3,4$$
- a) Determine el valor de $c$.
- b) Calcule $P(2 \le X \le 3)$.
- c) Calcule $E[X]$.

<u>Solución:</u>

**a)** La función de probabilidad debe satisfacer $\sum_{i=1}^{4} P(X=i) = 1$. Entonces:

$$
\sum_{i=1}^{4} c \cdot i = c \cdot (1 + 2 + 3 + 4) = c \cdot 10 = 1.
$$

Por lo tanto:

$$
c = \frac{1}{10}.
$$

**b)** $P(2 \le X \le 3) = P(X=2) + P(X=3) = c \cdot 2 + c \cdot 3 = 5c$.

Sustituyendo $c = 1/10$:

$$
P(2 \le X \le 3) = \frac{5}{10} = \frac{1}{2} = 0.5.
$$

**c)** El valor esperado para una variable aleatoria discreta es $E[X] = \sum_{i} i \cdot P(X=i)$.

$$
E[X] = \sum_{i=1}^{4} i \cdot (c \cdot i) = c \sum_{i=1}^{4} i^2 = c \cdot (1^2 + 2^2 + 3^2 + 4^2) = c \cdot (1 + 4 + 9 + 16) = c \cdot 30.
$$

Sustituyendo $c = 1/10$:

$$
E[X] = \frac{30}{10} = 3.
$$

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 6</u> ([[#^indice|Índice]])
^ejercicio6

<u>Enunciado:</u> Muestre que para toda variable aleatoria $X$ se cumple: $Var[a X + b] = a^2 Var[X]$.

<u>Solución:</u>

Por definición de varianza:

$$
Var[aX + b] = \mathbb{E}\left[(aX + b - \mathbb{E}[aX + b])^2\right].
$$

Por linealidad del valor esperado: $\mathbb{E}[aX + b] = a\mathbb{E}[X] + b$. Entonces:

$$
aX + b - \mathbb{E}[aX + b] = aX + b - a\mathbb{E}[X] - b = a(X - \mathbb{E}[X]).
$$

Sustituyendo en la definición:

$$
Var[aX + b] = \mathbb{E}\left[\left(a(X - \mathbb{E}[X])\right)^2\right]
= \mathbb{E}\left[a^2 (X - \mathbb{E}[X])^2\right]
= a^2 \, \mathbb{E}\left[(X - \mathbb{E}[X])^2\right].
$$

La última expresión es precisamente $a^2 \, Var[X]$, por definición de varianza. Por lo tanto:

$$
Var[aX + b] = a^2 \, Var[X].
$$

---


<div style="page-break-after: always;"></div>

## <u>Ejercicio 7</u> ([[#^indice|Índice]])
^ejercicio7

<u>Enunciado:</u> Defina una relación de recurrencia $P_{n+1} = f(P_n)$ para la función de probabilidad de masa de Poisson con un parámetro $\lambda$. Usar esta relación para calcular el/los valores mas probables de la variable.

<u>Solución:</u>

La función de probabilidad de masa de una variable $X \sim \text{Pois}(\lambda)$ es:

$$
P_n = P(X = n) = \frac{e^{-\lambda} \lambda^n}{n!}, \qquad n = 0, 1, 2, \dots
$$

La relación de recurrencia surge del cociente entre términos consecutivos:

$$
\frac{P_{n+1}}{P_n} = \frac{e^{-\lambda} \lambda^{n+1} / (n+1)!}{e^{-\lambda} \lambda^n / n!}
= \frac{\lambda}{n+1}.
$$

Despejando:

$$
P_{n+1} = P_n \cdot \frac{\lambda}{n+1}, \qquad n \geq 0.
$$

Esta es la relación $P_{n+1} = f(P_n)$ con $f(x) = x \cdot \frac{\lambda}{n+1}$ (dependiente de $n$).

Para hallar la moda, analizamos cuándo $P_{n+1} \ge P_n$:

$$
P_{n+1} \ge P_n \iff \frac{\lambda}{n+1} \ge 1 \iff n+1 \le \lambda \iff n \le \lambda - 1.
$$

Es decir, la probabilidad $P_n$ crece mientras $n \le \lambda - 1$ y decrece cuando $n > \lambda - 1$.

**Caso 1:** $\lambda$ es entero. Cuando $n = \lambda - 1$, se cumple $P_{n+1} = P_n$ (pues $\lambda/(n+1) = 1$). Por lo tanto existen dos modas: $n = \lambda - 1$ y $n = \lambda$.

**Caso 2:** $\lambda$ no es entero. La probabilidad crece hasta $n = \lfloor \lambda \rfloor$ y luego decrece. La moda única es $n = \lfloor \lambda \rfloor$.

En resumen:

$$
\text{Moda} =
\begin{cases}
\lfloor \lambda \rfloor, & \text{si } \lambda \notin \mathbb{Z}, \\[4pt]
\{\lambda - 1,\, \lambda\}, & \text{si } \lambda \in \mathbb{Z}.
\end{cases}
$$

---


<div style="page-break-after: always;"></div>

## <u>Ejercicio 8</u> ([[#^indice|Índice]])
^ejercicio8

<u>Enunciado:</u> Sean $X$ e $Y$ variables aleatorias independientes con distribución Poisson con parámetros $\lambda_1$ y $\lambda_2$ respectivamente. Demuestre que la variable $Z = X +Y$ tiene distribución Poisson con parámetro $\lambda_1 + \lambda_2$.

<u>Solución:</u>

Queremos demostrar que $Z = X+Y \sim \text{Pois}(\lambda_1 + \lambda_2)$. Para todo $z \in \{0,1,2,\dots\}$:

$$
P(Z = z) = P(X + Y = z) = \sum_{k=0}^{z} P(X = k,\; Y = z - k).
$$

Por independencia de $X$ e $Y$, la probabilidad conjunta factoriza:

$$
P(Z = z) = \sum_{k=0}^{z} P(X = k) \cdot P(Y = z - k).
$$

Sustituimos las funciones de probabilidad Poisson:

$$
P(Z = z) = \sum_{k=0}^{z}
\frac{e^{-\lambda_1} \lambda_1^k}{k!} \cdot
\frac{e^{-\lambda_2} \lambda_2^{z-k}}{(z-k)!}.
$$

Sacamos factor común $e^{-(\lambda_1 + \lambda_2)}$:

$$
P(Z = z) = e^{-(\lambda_1 + \lambda_2)} \sum_{k=0}^{z}
\frac{\lambda_1^k \lambda_2^{z-k}}{k!\,(z-k)!}.
$$

Multiplicamos y dividimos por $z!$ para formar un coeficiente binomial:

$$
P(Z = z) = \frac{e^{-(\lambda_1 + \lambda_2)}}{z!} \sum_{k=0}^{z}
\frac{z!}{k!\,(z-k)!} \, \lambda_1^k \lambda_2^{z-k}
= \frac{e^{-(\lambda_1 + \lambda_2)}}{z!} \sum_{k=0}^{z}
\binom{z}{k} \lambda_1^k \lambda_2^{z-k}.
$$

La suma es el desarrollo del binomio de Newton:

$$
\sum_{k=0}^{z} \binom{z}{k} \lambda_1^k \lambda_2^{z-k} = (\lambda_1 + \lambda_2)^z.
$$

Por lo tanto:

$$
P(Z = z) = \frac{e^{-(\lambda_1 + \lambda_2)} (\lambda_1 + \lambda_2)^z}{z!},
\qquad z = 0, 1, 2, \dots
$$

que es precisamente la función de probabilidad de una variable Poisson con parámetro $\lambda_1 + \lambda_2$. Queda demostrado que $Z \sim \text{Pois}(\lambda_1 + \lambda_2)$.

---


<div style="page-break-after: always;"></div>

## <u>Ejercicio 9</u> ([[#^indice|Índice]])
^ejercicio9

<u>Enunciado:</u> Un geólogo ha recolectado $10$ especímenes de roca basáltica y $12$ de granito. Si instruye a un asistente de laboratorio para que seleccione al azar $15$ de los especímenes para analizarlos, ¿Cuál es la función de probabilidad de masa del numero de especímenes de basalto seleccionados?

<u>Solución:</u>

Sea $X$ el número de especímenes de basalto entre los $15$ seleccionados. La selección es sin reposición de una población finita de $N = 22$ especímenes ($10$ de basalto, $12$ de granito). Por lo tanto, $X$ sigue una **distribución hipergeométrica** con parámetros:

$$
N = 22,\qquad K = 10,\qquad n = 15.
$$

La función de probabilidad de masa es:

$$
P(X = k) = \frac{\displaystyle\binom{K}{k}\binom{N-K}{n-k}}{\displaystyle\binom{N}{n}}
        = \frac{\displaystyle\binom{10}{k}\binom{12}{15-k}}{\displaystyle\binom{22}{15}},
\qquad k \in \{\max(0,\, n - (N-K)),\; \dots,\; \min(n,\, K)\}.
$$

Para nuestros valores:

- El mínimo de $k$ es $\max(0,\, 15 - 12) = \max(0, 3) = 3$.
- El máximo de $k$ es $\min(15,\, 10) = 10$.

Por lo tanto, el rango de $X$ es $k = 3, 4, \dots, 10$, y su función de probabilidad de masa es:

$$
\boxed{P(X = k) = \frac{\displaystyle\binom{10}{k}\binom{12}{15-k}}{\displaystyle\binom{22}{15}},\qquad k = 3,4,\dots,10}.
$$

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 10</u> ([[#^indice|Índice]])
^ejercicio10

<u>Enunciado:</u> Pruebe que si $X \sim \mathbb{P}(λ)$. Entonces $$E[X]=\lambda \qquad Var[X]=\lambda$$
Ayuda: $E[X^2] = E[X(X − 1)] + E[X]$

<u>Solución:</u>

Sea $X \sim \text{Pois}(\lambda)$, con función de probabilidad:

$$
P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!},\qquad k = 0, 1, 2, \dots
$$

**Esperanza.** Por definición:

$$
E[X] = \sum_{k=0}^{\infty} k \cdot \frac{e^{-\lambda} \lambda^k}{k!}
      = e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^k}{(k-1)!}
      = e^{-\lambda} \lambda \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!}.
$$

Haciendo el cambio de índice $j = k-1$, la suma resulta ser el desarrollo en serie de Taylor de $e^{\lambda}$:

$$
E[X] = e^{-\lambda} \lambda \sum_{j=0}^{\infty} \frac{\lambda^{j}}{j!}
      = e^{-\lambda} \lambda \, e^{\lambda}
      = \boxed{\lambda}.
$$

**Varianza.** Usamos la identidad $E[X^2] = E[X(X-1)] + E[X]$. Primero calculamos $E[X(X-1)]$:

$$
E[X(X-1)] = \sum_{k=0}^{\infty} k(k-1) \frac{e^{-\lambda} \lambda^k}{k!}
          = e^{-\lambda} \sum_{k=2}^{\infty} \frac{\lambda^k}{(k-2)!}
          = e^{-\lambda} \lambda^2 \sum_{k=2}^{\infty} \frac{\lambda^{k-2}}{(k-2)!}.
$$

Con el cambio $j = k-2$, nuevamente aparece la serie de $e^{\lambda}$:

$$
E[X(X-1)] = e^{-\lambda} \lambda^2 \sum_{j=0}^{\infty} \frac{\lambda^{j}}{j!}
          = e^{-\lambda} \lambda^2 \, e^{\lambda}
          = \lambda^2.
$$

Por lo tanto:

$$
E[X^2] = \lambda^2 + \lambda.
$$

Finalmente:

$$
Var[X] = E[X^2] - (E[X])^2
       = (\lambda^2 + \lambda) - \lambda^2
       = \boxed{\lambda}.
$$

Queda demostrado que $E[X] = \lambda$ y $Var[X] = \lambda$.

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 11</u> ([[#^indice|Índice]])
^ejercicio11

<u>Enunciado:</u> Sean $X$ e $Y$ variables aleatorias independientes distribuidas exponencialmente $$f_X(x)=\lambda exp(-\lambda x),(x\gt 0) \qquad f_Y(y)=\mu exp(-\mu y),(y\gt 0)$$
- a) Calcule $f_{X|Y} (x|y)$.
- b) Calcule $P(X \lt Y)$

<u>Solución:</u>

**a)** Por definición de densidad condicional:

$$
f_{X|Y}(x \mid y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}.
$$

Como $X$ e $Y$ son independientes, la densidad conjunta factoriza:

$$
f_{X,Y}(x,y) = f_X(x) \, f_Y(y).
$$

Sustituyendo:

$$
f_{X|Y}(x \mid y) = \frac{f_X(x) \, f_Y(y)}{f_Y(y)} = f_X(x), \qquad x > 0.
$$

Es decir, por independencia, la densidad condicional de $X$ dado $Y = y$ coincide con su densidad marginal. Por lo tanto:

$$
\boxed{f_{X|Y}(x \mid y) = \lambda e^{-\lambda x},\qquad x > 0}.
$$

**b)** Para calcular $P(X < Y)$, integramos la densidad conjunta sobre la región $x < y$:

$$
P(X < Y) = \int_{0}^{\infty} \int_{0}^{y} f_X(x) \, f_Y(y) \; dx \, dy
         = \int_{0}^{\infty} f_Y(y) \left( \int_{0}^{y} f_X(x) \, dx \right) dy.
$$

La integral interior es la función de distribución acumulada de $X$:

$$
\int_{0}^{y} \lambda e^{-\lambda x} \, dx = 1 - e^{-\lambda y}.
$$

Sustituyendo:

$$
P(X < Y) = \int_{0}^{\infty} \mu e^{-\mu y} \left( 1 - e^{-\lambda y} \right) dy
         = \mu \int_{0}^{\infty} e^{-\mu y} \, dy - \mu \int_{0}^{\infty} e^{-(\mu + \lambda) y} \, dy.
$$

Cada integral es una exponencial:

$$
\mu \int_{0}^{\infty} e^{-\mu y} \, dy = \mu \cdot \frac{1}{\mu} = 1,
$$
$$
\mu \int_{0}^{\infty} e^{-(\mu + \lambda) y} \, dy = \mu \cdot \frac{1}{\mu + \lambda} = \frac{\mu}{\mu + \lambda}.
$$

Por lo tanto:

$$
P(X < Y) = 1 - \frac{\mu}{\lambda + \mu} = \boxed{\frac{\lambda}{\lambda + \mu}}.
$$

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 12</u> ([[#^indice|Índice]])
^ejercicio12

<u>Enunciado:</u> Sean $X$ e $Y$ variables aleatorias independientes e idénticamente distribuidas de forma exponencial. Calcule la densidad de probabilidad condicional de $X$ dado que $X +Y = t$.

<u>Solución:</u>

Sean $X, Y \sim \text{Exp}(\lambda)$ independientes, con densidad marginal $f_X(x) = \lambda e^{-\lambda x}$ para $x > 0$ (análogamente para $Y$). La densidad conjunta es:

$$
f_{X,Y}(x,y) = \lambda^2 e^{-\lambda (x+y)},\qquad x > 0,\; y > 0.
$$

**Paso 1: Densidad de $V = X+Y$ mediante convolución.**

Como $X$ e $Y$ son independientes, la densidad de la suma es la convolución de las densidades marginales:

$$
f_V(v) = \int_{0}^{v} f_X(x) \, f_Y(v-x) \, dx
       = \int_{0}^{v} \lambda e^{-\lambda x} \cdot \lambda e^{-\lambda (v-x)} \, dx
       = \lambda^2 e^{-\lambda v} \int_{0}^{v} dx
       = \lambda^2 v \, e^{-\lambda v}, \qquad v > 0.
$$

**Paso 2: Función de distribución condicional $F_{X \mid V}(x \mid t)$ mediante un límite.**

Para $x > 0$, $t > 0$ y un $h > 0$ pequeño, consideramos:

$$
F_{X \mid V}(x \mid t) = P(X \le x \mid V = t)
    = \lim_{h \to 0} P(X \le x \mid t \le V \le t+h).
$$

Por definición de probabilidad condicional:

$$
P(X \le x \mid t \le V \le t+h) = \frac{P(X \le x,\; t \le V \le t+h)}{P(t \le V \le t+h)}.
$$

Calculamos el numerador integrando la densidad conjunta sobre la región $0 < u \le x$ y $t \le u+v \le t+h$, lo que equivale a $0 < u \le x$, $t-u \le v \le t+h-u$:

$$
\begin{aligned}
P(X \le x,\; t \le V \le t+h)
&= \int_{0}^{x} \int_{t-u}^{t+h-u} \lambda^2 e^{-\lambda (u+v)} \, dv \, du \\
&= \int_{0}^{x} \lambda^2 e^{-\lambda u} \left[ \frac{e^{-\lambda v}}{-\lambda} \right]_{v=t-u}^{v=t+h-u} du \\
&= \int_{0}^{x} \lambda e^{-\lambda u} \left( e^{-\lambda (t-u)} - e^{-\lambda (t+h-u)} \right) du \\
&= \int_{0}^{x} \lambda e^{-\lambda t} \bigl(1 - e^{-\lambda h}\bigr) \, du \\
&= \lambda e^{-\lambda t} \bigl(1 - e^{-\lambda h}\bigr) \, x.
\end{aligned}
$$

El denominador es:

$$
P(t \le V \le t+h) = \int_{t}^{t+h} f_V(v) \, dv
                  \approx f_V(t) \cdot h = \lambda^2 t \, e^{-\lambda t} \, h,
$$

para $h$ suficientemente pequeño. Usando la expansión $1 - e^{-\lambda h} \approx \lambda h$ cuando $h \to 0$:

$$
\lim_{h \to 0} P(X \le x \mid t \le V \le t+h)
= \lim_{h \to 0} \frac{\lambda e^{-\lambda t} \cdot \lambda h \cdot x}{\lambda^2 t \, e^{-\lambda t} \, h}
= \frac{x}{t}.
$$

Por lo tanto, la función de distribución condicional es:

$$
F_{X \mid X+Y = t}(x) = \frac{x}{t}, \qquad 0 < x < t.
$$

**Paso 3: Densidad condicional.**

Derivando la CDF condicional respecto a $x$:

$$
f_{X \mid X+Y = t}(x) = \frac{d}{dx} F_{X \mid X+Y = t}(x) = \frac{1}{t}, \qquad 0 < x < t.
$$

Es decir:

$$
\boxed{f_{X \mid X+Y = t}(x) = \frac{1}{t},\qquad 0 < x < t}.
$$

Esto significa que, condicional a que $X + Y = t$, la variable $X$ se distribuye **uniformemente** en el intervalo $(0, t)$.

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 13</u> ([[#^indice|Índice]])
^ejercicio13

<u>Enunciado:</u> La vida útil de cierto refrigerador esta distribuida de manera aproximadamente normal con media $4.8$ años y desvió $1.4$ años.
- a) Si el aparato tiene garantía por dos años. ¿Cuál es la probabilidad de que un refrigerador del tipo especificado elegido al azar, deba reemplazarse dentro del periodo de garantía?
- b) Si el fabricante está dispuesto a reponer sólo el $0.5\%$ de los refrigeradores. ¿Cuál es el periodo de garantía que debe ofrecer?

<u>Solución:</u>

Sea $X$ la vida útil del refrigerador, con distribución $X \sim \mathcal{N}(\mu = 4.8,\; \sigma = 1.4)$ años.

**a)** El refrigerador debe reemplazarse dentro del periodo de garantía si su vida útil es menor a $2$ años:

$$
P(X < 2) = P\!\left( Z < \frac{2 - 4.8}{1.4} \right)
         = P\!\left( Z < \frac{-2.8}{1.4} \right)
         = P(Z < -2.0),
$$

donde $Z \sim \mathcal{N}(0,1)$ es la variable normal estándar. Por simetría de la distribución normal:

$$
P(Z < -2.0) = \Phi(-2.0) = 1 - \Phi(2.0).
$$

Consultando la tabla normal estándar, $\Phi(2.0) \approx 0.9772$. Por lo tanto:

$$
P(X < 2) = 1 - 0.9772 = \boxed{0.0228}.
$$

La probabilidad de que un refrigerador elegido al azar falle dentro de la garantía de $2$ años es aproximadamente $2.28\%$.

**b)** Buscamos el valor $t$ tal que $P(X < t) = 0.005$ (el $0.5\%$ inferior de la distribución):

$$
P(X < t) = 0.005 \;\Longrightarrow\; P\!\left( Z < \frac{t - 4.8}{1.4} \right) = 0.005.
$$

El percentil $0.005$ de la normal estándar es $z_{0.005} = \Phi^{-1}(0.005)$. De tablas:

$$
\Phi^{-1}(0.005) \approx -2.576.
$$

Igualando:

$$
\frac{t - 4.8}{1.4} = -2.576 \;\Longrightarrow\;
t = 4.8 + 1.4 \times (-2.576) = 4.8 - 3.6064 = \boxed{1.19}.
$$

El fabricante debe ofrecer una garantía de aproximadamente **$1.19$ años** para que sólo el $0.5\%$ de los refrigeradores requiera reemplazo.

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 14</u> ([[#^indice|Índice]])
^ejercicio14

<u>Enunciado:</u> Encuentre una aproximación a la probabilidad de que el número de unos obtenidos al arrojar $12000$ veces un dado esté entre $1900$ y $2150$.

<u>Solución:</u>

Sea $X$ el número de unos en $n = 12000$ tiradas de un dado equilibrado. Cada tirada es independiente y la probabilidad de obtener un $1$ es $p = 1/6$. Por lo tanto:

$$
X \sim \text{Bin}\!\left(n = 12000,\; p = \frac{1}{6}\right).
$$

**Parámetros de la distribución:**

$$
\mu = n p = 12000 \times \frac{1}{6} = 2000,
$$

$$
\sigma^2 = n p (1-p) = 12000 \times \frac{1}{6} \times \frac{5}{6}
         = 12000 \times \frac{5}{36}
         = \frac{10000}{6} \approx 1666.\overline{6},
$$

$$
\sigma = \sqrt{\frac{10000}{6}} = \frac{100}{\sqrt{6}} \approx 40.82.
$$

**Aproximación normal con corrección por continuidad.** Dado que $n$ es grande, $X$ puede aproximarse por una normal $\mathcal{N}(\mu, \sigma^2)$. Para mejorar la aproximación al calcular $P(1900 \le X \le 2150)$, aplicamos la corrección por continuidad:

$$
P(1900 \le X \le 2150) \approx P(1899.5 < X^* < 2150.5),
$$

donde $X^* \sim \mathcal{N}(\mu, \sigma^2)$. Tipificamos:

$$
z_1 = \frac{1899.5 - 2000}{\sigma} = \frac{-100.5}{40.82} \approx -2.46,
$$

$$
z_2 = \frac{2150.5 - 2000}{\sigma} = \frac{150.5}{40.82} \approx 3.69.
$$

Por lo tanto:

$$
P(1900 \le X \le 2150) \approx \Phi(3.69) - \Phi(-2.46)
                     = \Phi(3.69) - \bigl(1 - \Phi(2.46)\bigr).
$$

De la tabla normal estándar:

- $\Phi(3.69) \approx 0.9999$ (virtualmente $1$ para $z > 3.5$),
- $\Phi(2.46) \approx 0.9931$.

Entonces:

$$
P(1900 \le X \le 2150) \approx 0.9999 - (1 - 0.9931)
                       = 0.9999 - 0.0069
                       = \boxed{0.9930}.
$$

La probabilidad aproximada de obtener entre $1900$ y $2150$ unos en $12000$ tiradas es de aproximadamente $0.993$ (un $99.3\%$).

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 15</u> ([[#^indice|Índice]])
^ejercicio15

<u>Enunciado:</u> Una persona juega a la quiniela una vez al día. Apuesta una cantidad $c$ a un número entre $0,1,...,99$. Se le paga $\$70$ si sale el número que eligió y nada en caso contrario. Sea $G$ la V.A. que da la ganancia del juego.
- a) Si el valor de la apuesta es de $\$1$, ¿Cuál es la ganancia esperada?
- b) La persona juega todos los días durante dos meses (o sea $60$ días en total). ¿Cuál es la probabilidad aproximada que pierda mas de $15$ pesos en esos dos meses?
- c) ¿Cuánto debería valer la apuesta $c$ para que el valor esperado de la ganancia sea $0$?

<u>Solución:</u>

**a)** Con $c = 1$, la ganancia $G$ (en pesos) toma dos valores:

- Si el número sale: gana $\$70$ pero pagó $\$1$, por lo que $G = 70 - 1 = 69$, con probabilidad $1/100$.
- Si no sale: pierde la apuesta, $G = -1$, con probabilidad $99/100$.

Por lo tanto, la ganancia esperada es:

$$
E[G] = 69 \cdot \frac{1}{100} + (-1) \cdot \frac{99}{100}
     = \frac{69 - 99}{100}
     = \frac{-30}{100}
     = \boxed{-0.30}.
$$

En promedio, la persona pierde $30$ centavos por día.

---

**b)** Para dos meses ($60$ días), sean $G_1, G_2, \dots, G_{60}$ las ganancias diarias, i.i.d. con la distribución del inciso (a). La ganancia total es $S = \sum_{i=1}^{60} G_i$.

Por el Teorema Central del Límite, $S$ se aproxima por una distribución normal con:

$$
E[S] = 60 \cdot E[G] = 60 \times (-0.30) = -18,
$$

$$
Var[G] = E[G^2] - (E[G])^2.
$$

Calculamos $E[G^2]$:

$$
E[G^2] = 69^2 \cdot \frac{1}{100} + (-1)^2 \cdot \frac{99}{100}
       = \frac{4761}{100} + \frac{99}{100}
       = \frac{4860}{100}
       = 48.60.
$$

Entonces:

$$
Var[G] = 48.60 - (0.30)^2 = 48.60 - 0.09 = 48.51,
$$

$$
Var[S] = 60 \cdot 48.51 = 2910.60,
\qquad
\sigma_S = \sqrt{2910.60} \approx 53.95.
$$

"Perder más de $15$ pesos" significa que la ganancia total es menor a $-15$, es decir, $S < -15$. Tipificando:

$$
P(S < -15) = P\!\left( Z < \frac{-15 - (-18)}{53.95} \right)
           = P\!\left( Z < \frac{3}{53.95} \right)
           = P(Z < 0.0556).
$$

De la tabla normal estándar:

$$
\Phi(0.0556) \approx 0.522.
$$

Por lo tanto:

$$
\boxed{P(\text{pierde más de } \$15) \approx 0.522}.
$$

Hay aproximadamente un $52.2\%$ de probabilidad de perder más de $15$ pesos en los dos meses.

---

**c)** Para una apuesta genérica $c$, la ganancia esperada es:

$$
E[G] = (70 - c) \cdot \frac{1}{100} + (-c) \cdot \frac{99}{100}
     = \frac{70 - c - 99c}{100}
     = \frac{70 - 100c}{100}.
$$

Igualamos a cero para que el juego sea justo (esperanza nula):

$$
\frac{70 - 100c}{100} = 0 \;\Longrightarrow\; 70 - 100c = 0
\;\Longrightarrow\; 100c = 70
\;\Longrightarrow\; \boxed{c = 0.70}.
$$

Si la apuesta es de $70$ centavos, el valor esperado de la ganancia es cero.

---