Números aleatorios y Método de Monte Carlo
___
<u>Índice:</u>
^indice

1. [[#^ejercicio1|Ejercicio 1 - Resuelto]]
2. [[#^ejercicio2|Ejercicio 2 - Resuelto]]
3. [[#^ejercicio3|Ejercicio 3 - Resuelto]]
4. [[#^ejercicio4|Ejercicio 4 - Resuelto]]
5. [[#^ejercicio5|Ejercicio 5 - Resuelto]]
6. [[#^ejercicio6|Ejercicio 6 - Resuelto]]
7. [[#^ejercicio7|Ejercicio 7 - Resuelto]]
8. [[#^ejercicio8|Ejercicio 8 - Resuelto-agente]]
9. [[#^ejercicio9|Ejercicio 9 - Resuelto]]

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 1</u> ([[#^indice|Índice]])
^ejercicio1

<u>Enunciado:</u> Para el estudio mediante simulación es necesario generar muchos números aleatorios en la computadora. Estos corresponden a variables aleatorias uniformemente distribuidas en el intervalo $(0, 1)$.
Existen en la literatura varias rutinas portables, optimizadas para generar enormes cantidades de números pseudo-aleatorios con velocidad razonable.
- a) Determinar el período de la secuencia de von Neumann generada a partir de la semilla:
	1. $3009$
	2. $7600$
	3. $1234$
	4. $4321$
- b) Dar el valor de $c$  y $a$ para que cada generador tenga periodo máximo.
	1. $y_{i+1}=5y_i +c\quad mod(2^5)$
	2. $x_{i+1}=ax_i\quad mod(31)$
	3. Considerar el generador $z_i=y_i+x_i\quad mod(2^5)$ y calcular su periodo.
	4. Representar en tres gráficos separados pares $(y_i,y_{i+1})$, $(x_i,x_{i+1})$ y $(z_i,z_{i+1})$
- c) Indicar en cuales de los siguientes casos el generador $$y_{i+1}=ay_i +c\quad mod(M)$$ genera una secuencia de periodo máximo.
	1. $a=125, c=3, M=2^9$
	2. $a=123, c=3, M=2^9$
	3. $a=5, c=3, M=71$
	4. $a=7, c=0, M=71$
- d) Utilice el generador RANDU $$u_i=au_{i-1}\quad mod(M)\qquad a=2^{16}+3, M=2^{31}$$ para generar puntos aleatorios en el cubo $[0,M)\times[0,M)\times[0,M)$, de la forma: $$(u_1,u_2,u_3),(u_4,u_5,u_6),...$$ y estimar el porcentaje de puntos que caen en la esfera centrada en $(M/2,M/2,M/2)$ de radio $M/10$.
  Repetir el procedimiento con el generador $$y_i=ay_{i-1}\quad mod(M)\qquad a=7^5, M=2^{31}-1$$ ¿Cuál es los dos generadores estima mejor el valor real?

<u>Solución:</u> 

- a)
	1. Para $3009$, el periodo es $5$
	2. Para $7600$, el periodo es $1$
	3. Para $1234$, el periodo es $57$
	4. Para $4321$, el periodo es $71$
- b) 
	1. Dado que es un generador mixto, debemos comprobar las propiedades para que tenga periodo $2^5$.
		- $mcd(c,2^5)=1 \rightarrow c=1$.
	2. Dado que es un generado multiplicativo, debemos comprobar las propiedades para que tenga periodo máximo.
		- $a$ debe ser raíz primitiva de $31$.
		- Tenemos que $30=2\cdot 3\cdot 5$.
		- Tomando $a=3$, tenemos que $$\begin{align}&a^{30/2}=a^{15}\not{\equiv}\, 1\quad mod(31) \\& a^{30/3}=a^{10}\not{\equiv}\,1\quad mod(31) \\& a^{30/5}=a^{6}\not{\equiv}\,1\quad mod(31)  \end{align}$$
	3. Tenemos que $y_i$ tiene periodo $32$, $x_i$ periodo $30$, de modo que el periodo de la suma $y_i+x_i\quad mod(32)$ es $$mcm(32,30) = 480$$
	4. Gráficos:
		- Para el generador $y_i$ con $y_0 = 1, a=5, c=1, M=32$ en $n=100$ iteraciones,
		  ![[Pasted image 20260409041931.png|center]]
		- Para el generador $x_i$ con $x_0=1, a=3, c=0, M=31$ en $n=100$ iteraciones,
		  ![[Pasted image 20260409042137.png|center]]
		- Para el generador $z_i$ con $x_0=y_0=1, a=3, c=1, M=32$ en $n=100$ iteraciones,
		  ![[Figure_1.png|center]]
- c) Dado el generador $y_{i+1}=ay_i +c\quad mod(M)$, 
	1. tipo mixto, tiene periodo $K=2^9$
	2. tipo mixto, tiene periodo $K=2^8+1$
	3. tipo multiplicativo, tiene periodo $K=6$
	4. tipo multiplicativo, tiene periodo $K=71$
- d) Teniendo en cuenta los siguientes datos $$V_{esfera}=\frac{4}{3}\pi R^3 = \frac{4}{3}\pi \left(\frac{M}{10}\right)^3$$
  Tenemos que el volumen del cubo $[0,M]^3$ es $M^3$, el porcentaje teórico(si los puntos fueran uniformes e independientes): $$\begin{align}& P_{teo}=\frac{V_{esfera}}{M^3}\cdot 100 = \frac{4\pi}{3}\cdot \frac{1}{1000}\cdot 100\\& P_{teo} = \frac{2\pi}{15}\approx 0.418879\% \end{align}$$
  
  Ahora, realizando simulaciones en ambos generadores para $u_0/y_0=1,1234,4321$ en $n=100.000$ iteraciones, tenemos resultados $$\begin{align}& u_0=y_0=1 \rightarrow\begin{cases}u_i\approx 0.378000\% \\ y_i\approx 0.413000\% \end{cases} \\& u_0=y_0=1234 \rightarrow\begin{cases}u_i\approx 0.352000\% \\ y_i\approx 0.381000\% \end{cases}\\& u_i=y_i=4321 \rightarrow\begin{cases}u_i\approx 0.384000\% \\ y_i\approx 0.422000\% \end{cases} \end{align}$$de modo que podemos concluir que el segundo generador es mejor.

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 2</u> ([[#^indice|Índice]])
^ejercicio2

<u>Enunciado:</u> Se propone el siguiente juego en el cual todas las variables aleatorias que se generan son independientes e idénticamente distribuidas $\mathcal{U}(0,1)$: Se simula la variable aleatoria $U$. Si $U\lt \frac{1}{2}$, se suman dos nuevos números aleatorios $W_1+W_2$. Pero si $U\ge\frac{1}{2}$, se suman tres números aleatorios. El resultado de la suma, en cualquiera de los casos, es una variable aleatoria $X$. Se gana el juego si $X\ge1$.
- a) ¿Cuál es la probabilidad de ganar?
- b) Implementar un algoritmo en computadora que estime la probabilidad de ganar, esto es, la fracción de veces que se gana en $n$ realizaciones del juego. Completar la siguiente tabla:

| n           | 100 | 1.000 | 10.000 | 100.000 | 1.000.000 |
|-------------|-----|------|-------|--------|---------|
| $P[X\ge 1]$ |     |      |       |        |         |

<u>Solución:</u> 

- a) Mediante probabilidad total, se pregunta $$P(X\ge 1) = P(U\lt\frac{1}{2})\cdot P(W_1+W_2\ge 1) + P(U\ge\frac{1}{2})\cdot P(W_1+W_2+W_3\ge 1)$$
  
  - Calculamos por partes,
	  - $P(W_1+W_2\ge 1)$, $W_1+W_2$ tiene distribución triangular con densidad $$f_X(x)=\begin{cases}x& 0\le x\le 1 \\ 2-x & 1\le x \le 2\end{cases}$$por lo tanto $$P(W_1+W_2\ge 1) = \int_1^2 {2-x} \,dx = 0.5$$
	  - $P(W_1+W_2+W_3\ge 1)$, $W_1+W_2+W_3$ tiene distribución para el caso $n=3$ de Irwin-Hall, su densidad es $$\large f_X(x)=\begin{cases} \frac{1}{2}x^2 & 0\le x\le 1 \\ \frac{1}{2}(-2x^2+6x-3) & 1\le x \le 2 \\ \frac{1}{2}(3-x)^2 & 2\le x \le 3 \end{cases}$$por lo tanto $$\begin{align}P(W_1+W_2+W_3\ge 1) =\,& \int_1^2 {\frac{1}{2}(-2x^2+6x-3)} \,dx + \int_2^3 {\frac{1}{2}(3-x)^2} \,dx \\=\,& \frac{2}{3} + \frac{1}{6} \\=\,& \frac{5}{6} \end{align}$$
	  - $\displaystyle P(U\lt \frac{1}{2}) = P(U\ge \frac{1}{2}) = \frac{1}{2}$
  - De esta manera, $$P(X\ge 1)=\frac{1}{2}\cdot 0.5 + \frac{1}{2}\cdot\frac{5}{6} = \frac{2}{3}$$

- b) Ver algoritmo `ej2.py` en `MyS\simulaciones_Pr3\`, tenemos que, 
  
| n           | 100 | 1.000 | 10.000 | 100.000 | 1.000.000 |
|-------------|-----|------|-------|--------|---------|
| $P[X\ge 1]$ | 0.700 | 0.6660 | 0.6694 | 0.6657 | 0.6659 |


---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 3</u> ([[#^indice|Índice]])
^ejercicio3

<u>Enunciado:</u> Las maquinas tragamonedas usualmente generan un premio cuando hay un acierto. Supongamos que se genera el acierto con le siguiente esquema: se genera un número aleatorio, y
1. si es menor a un tercio, se suman dos nuevos número aleatorios
2. si es mayor o igual a un tercio, se suman tres números aleatorios.
  Si el resultado de la suma es menor o igual a $2$, se genera un acierto.
- a) ¿Cuál es la probabilidad de acertar?
- b) Implementar un algoritmo en computadora que estime la probabilidad de acertar, esto es, la fracción de veces que se acierta en $n$ realizaciones del juego. Completar la siguiente tabla:
  
| n           | 100 | 1.000 | 10.000 | 100.000 | 1.000.000 |
|-------------|-----|------|-------|--------|---------|
| $P[X\le 2]$ |     |      |       |        |         |

<u>Solución:</u> 

Sean los números aleatorios $U,W_1,W_2,W_3$ generados en una $\mathcal{U}(0,1)$.
Sea la variable aleatoria $X$ que representa la suma de los números aleatorios en cada caso.

- a) Se pregunta $$P(X\le 2) = P(U\lt 1/3)\cdot P(W_1+W_2\le 2) + P(U\ge 1/3)\cdot P(W_1+W_2+W_3\le 2)$$si tomamos $P(W_1+W_2\le 2)$ y $P(W_1+W_2+W_3\le 2)$ de la siguiente manera, $$P(X\le 2) = P(U\lt 1/3)\cdot [1-P(W_1+W_2\gt 2)] + P(U\ge 1/3)\cdot [1-P(W_1+W_2+W_3\gt 2)]$$calculamos por partes utilizando las herramientas del ejercicio anterior,
	- $P(W_1+W_2\gt 2)$: $$P(W_1+W_2\gt 2) = 0$$
	- $P(W_1+W_2+W_3\gt 2)$: $$P(W_1+W_2+W_3\gt 2) = \int_2^3 {\frac{1}{2}(3-x)^2} \,dx = \frac{1}{6}$$
	- $P(U\lt 1/3)$: $$P(U\lt 1/3)=\int_0^{1/3} {1} \,dx = \frac{1}{3}$$
	- $P(U\ge 1/3)$: $$P(U\ge 1/3)=1-P(U\lt 1/3)=1-\frac{1}{3}=\frac{2}{3}$$ luego $$\begin{align} P(X\le 2) =\,& \frac{1}{3}\cdot [1-0] + \frac{2}{3}\cdot [1-\frac{1}{6}] \\=\,& \frac{8}{9} \end{align}$$
- b) Ver algoritmo `ej3.py` en `MyS\simulaciones_Pr3\`, tenemos que, 
  
| n           | 100 | 1.000 | 10.000 | 100.000 | 1.000.000 |
|-------------|-----|------|-------|--------|---------|
| $P[X\le 2]$ | 0.9400 | 0.8890 | 0.8901 | 0.8886 | 0.8890 |


---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 4</u> ([[#^indice|Índice]])
^ejercicio4

<u>Enunciado:</u> Un supermercado posee 3 cajas. Por una cuestión de ubicación, el $40\%$ de los clientes eligen la caja $1$ para pagar, el $32\%$ la caja 2, y el $28\%$ la caja 3. El tiempo que espera una persona para ser atendida en cada caja distribuye exponencial con medias de $3,4$ y $5$ minutos respectivamente.
- a) ¿Cuál es la probabilidad de que un cliente espere menos de 4 minutos para ser atendido?
- b) Si el cliente tuvo que esperar más de 4 minutos. ¿Cuál es la probabilidad de que el cliente haya elegido cada una de las cajas?
- c) Simule el problema y estime las probabilidades anteriores con $1.000$ iteraciones.

<u>Solución:</u> 

Sean $C_i$ el evento de que se elige la caja $i=1,2,3$, cada una con $P(C_1)=0.4$, $P(C_2)=0.32$ y $P(C_3)=0.28$ respectivamente.
Sea $T_i$ el tiempo que espera $i=1,2,3$ en que una persona es atendida, cada una con distribución $T_1 \sim \mathcal{E}(1/3)$, $T_2 \sim \mathcal{E}(1/4)$ y $T_3 \sim \mathcal{E}(1/5)$. Sea $T$ el tiempo total de espera de un cliente.

- a) Se pregunta, $$\begin{align} P(T\lt 4) =\,& P(C_1)\cdot P(T_1 \lt 4) + P(C_2)\cdot P(T_2 \lt 4) + P(C_3)\cdot P(T_3 \lt 4) \\=\,& 0.4 \cdot (1-e^{\large -4/3}) + 0.32 \cdot (1-e^{\large -4/4}) + 0.28 \cdot (1-e^{\large - 4/5}) \\\approx\,& 0.6510 \end{align}$$
- b) Se pregunta, $$\begin{align} P(C_k \,|\, T\gt 4) =\,& \frac{P(C_k\,|\, T\gt 4)}{P(T\gt 4)} \qquad\text{por bayes} \\=\,& \frac{P(T\ge 4 \,|\, C_k)\cdot P(C_k)}{P(T\gt 4)} \\=\,& \frac{P(T_k \gt 4)\cdot P(C_k)}{P(T\gt 4)}\end{align}$$Ahora necesito calcular $P(T\gt 4)$: $$P(T\gt 4)=1-(T\le 4) \approx 1-0.6510 \approx 0.3489$$y ahora, calculo para cada caja $C_i$: $$\begin{align}& P(C_1 \,|\, T\gt 4) = \frac{P(T_1 \gt 4)\cdot P(C_1)}{P(T\gt 4)} \approx \frac{(e^{\large -4/3})\cdot 0.4}{0.3489} \approx 0.3022 \\& P(C_2 \,|\, T\gt 4) = \frac{P(T_2 \gt 4)\cdot P(C_2)}{P(T\gt 4)} \approx \frac{(e^{\large -4/4}) \cdot 0.32}{0.3489} \approx 0.3374 \\& P(C_3 \,|\, T\gt 4) = \frac{P(T_3 \gt 4)\cdot P(C_3)}{P(T\gt 4)} \approx \frac{(e^{\large -4/5}) \cdot 0.28}{0.3489} \approx 0.3604 \end{align}$$
- c) Ver algoritmo `ej4.py` en `MyS\simulaciones_Pr3\`, tenemos que, para $n=1.000$, $$\begin{align}& P(T\lt 4) \approx 0.6410 \\& P(C_1 \,|\, T\gt 4) \approx 0.2981 \\& P(C_2 \,|\, T\gt 4) \approx 0.3482 \\& P(C_3 \,|\, T\gt 4) \approx 0.3538 \end{align}$$

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 5</u> ([[#^indice|Índice]])
^ejercicio5

<u>Enunciado:</u> Calcule exactamente el valor de las siguientes integrales. Mediante una simulación de Monte Carlo con $n=1000, 5000, 10.000$ iteraciones, calcule a su vez un valor aproximado y compare con el valor exacto.
- a) $\displaystyle \int_0^1 {(1-x^2)^{3/2}} dx$
- b) $\displaystyle \int_2^3 {\frac{x}{x^2-1}} dx$
- c) $\displaystyle \int_0^{\infty} {x(1+x^2)^{-2}} dx$
- d) $\displaystyle \int_{-\infty}^{\infty} {e^{-x^2}} dx$
- e) $\displaystyle \int_0^1 {\left[\int_0^1 {e^{(x+y)^2}} dx\right]} dy$
- f) $\displaystyle \int_0^{\infty} {\left[\int_0^x {e^{-(x+y)}} dy\right]} dx$
  
  Ayuda: Sea $I_y(x)=\begin{cases}1& \text{si }y\lt x \\ 0&\text{si }y\ge x\end{cases}$. Utilice esta función para igualar la integral del ítem f) a otra cuyos términos vayan de $0$ a $\infty$.
  
  Completar la siguiente tabla:
  
| n\ integral $\rightarrow$ | (a) | (b) | (c) | (d) | (e) | (f) |
|---------------------------|-----|-----|-----|-----|-----|-----|
| 100                       |     |     |     |     |     |     |
| 1.000                     |     |     |     |     |     |     |
| 10.000                    |     |     |     |     |     |     |
| 100.000                   |     |     |     |     |     |     |
| 1.000.000                 |     |     |     |     |     |     |

<u>Solución:</u> 

- a) El valor exacto es, $\displaystyle \int_0^1 {(1-x^2)^{3/2}} \,dx = \frac{3\pi}{16}$, mediante Montecarlo, sean las variables aleatorias uniformes independientes, $U_1 = u_1, U_2 = u_2,..., U_N=u_N$, aproximamos, $$\int_0^1 {(1-x^2)^{3/2}} \,dx \sim \frac{1}{N}\sum_{i=1}^N {(1-u_i^2)^{3/2}}$$
- b) El valor exacto es, $\displaystyle \int_2^3 {\frac{x}{x^2-1}} dx = \frac{1}{2}\cdot (ln(8)-ln(3))$, mediante Montecarlo, tenemos el caso de el intervalo $(a,b)$, en este caso $a=2$ y $b=3$, realizamos la transformación de la función para llevarla al intervalo $(0,1)$, $$\int_2^3 {\frac{x}{x^2-1}} dx = \int_0^1 {\frac{y+2}{(y+3)(y+1)}} \,dy$$,ahora sean las variables aleatorias uniformes independientes, $U_1 = u_1, U_2 = u_2,..., U_N=u_N$, aproximamos, $$\int_0^1 {\frac{y+2}{(y+3)(y+1)}} \,dy \sim \frac{1}{N}\sum_{i=1}^N \frac{u_i+2}{(u_i+3)(u_i+1)}$$
- c) El valor exacto es, $\displaystyle \int_0^{\infty} {x(1+x^2)^{-2}} dx = \frac{1}{2}$, mediante Montecarlo, tenemos el caso de el intervalo $(0,\infty)$, realizamos la transformación de la función para llevarla al intervalo $(0,1)$, $$\int_0^{\infty} {x(1+x^2)^{-2}} dx = \int_0^1 {\frac{(1-y)y}{(2y^2 -2y+1)^2}} \,dy$$, ahora sean las variables aleatorias uniformes independientes, $U_1 = u_1, U_2 = u_2,..., U_N=u_N$, aproximamos, $$\int_0^1 {\frac{(1-y)y}{(2y^2 -2y+1)^2}} \,dy \sim \frac{1}{N}\sum_{i=1}^N {\frac{(1-u_i)u_i}{(2u_i^2 -2u_i+1)^2}}$$
- d) El valor exacto es $\displaystyle \int_{-\infty}^{\infty} {e^{-x^2}} dx = \sqrt{\pi}$, mediante Montecarlo, podemos reescribir la integral de la siguiente manera, $$\int_{-\infty}^{\infty} {e^{-x^2}} dx = 2\int_0^{\infty} {e^{-x^2}} dx$$y así tenemos el caso de $(0,\infty)$ de Montecarlo, realizamos la transformación de la función, $$2\int_0^{\infty} {e^{-x^2}} dx = 2\int_0^1 {exp\left({-\frac{(1-y)^2}{y^2}}\right)\cdot \left(\frac{1}{y^2}\right)} \,dy$$, ahora sean las variables aleatorias uniformes independientes, $U_1 = u_1, U_2 = u_2,..., U_N=u_N$, aproximamos, $$2\int_0^1 {exp\left({-\frac{(1-y)^2}{y^2}}\right)\cdot \left(-\frac{1}{y^2}\right)} \,dy \sim \frac{2}{N}\sum_{i=1}^N {exp\left({-\frac{(1-u_i)^2}{u_i^2}}\right)\cdot \left(-\frac{1}{u_i^2}\right)}$$
- e) El valor exacto es $\displaystyle \int_0^1 {\left[\int_0^1 {e^{(x+y)^2}} dx\right]} dy = e-\frac{1}{2}-\frac{e^4}{2}+\sqrt{\pi}(erfi(2)-erfi(1)) \approx 4.8922$ donde $\displaystyle erfi(z)=\frac{2}{\sqrt{\pi}}\int_0^z e^{t^2}dt$, mediante Montecarlo, tenemos el caso de integrales múltiples, pero precisamente tenemos el intervalo de las integrales a nuestro favor, por lo tanto, solo debemos aplicar la transformación de la función, $$\int_0^1 {\left[\int_0^1 {e^{(x+y)^2}} dx\right]} dy \sim \frac{1}{N}\sum_{i=1}^N e^{\Large(u_{i^1}+u_{i^2})^2}$$ para dos conjuntos de variables aleatorias uniformes independientes.
- f) El valor exacto es $\displaystyle \int_0^{\infty} {\left[\int_0^x {e^{-(x+y)}} dy\right]} dx = \frac{1}{2}$, mediante Montecarlo, necesitamos usar la función indicadora para realizar una transformación en un intervalo, $$\int_0^{\infty} {\left[\int_0^x {e^{-(x+y)}} dy\right]} dx = \int_0^{\infty} {\left[\int_0^{\infty} {e^{-(x+y)}}\cdot \mathbb{I}_y(x) \,dy\right]} dx$$, ahora podemos interpretar $e^{-x}e^{-y}$  como densidad de dos exponenciales independientes de tasa 1(en $x\gt0,y\gt0$): $$\int_0^{\infty} {\left[\int_0^{\infty} {e^{-(x+y)}}\cdot \mathbb{I}_y(x) \,dy\right]} dx = E[\mathbb{I}_y(x)]$$, sean las variables aleatorias independientes $\large u_{i^1}$ y $\large u_{i^2}$ con distribución $\mathcal{E}(1)$, entonces, $$\int_0^{\infty} {\left[\int_0^{\infty} {e^{-(x+y)}}\cdot \mathbb{I}_y(x) \,dy\right]} dx \sim \frac{1}{N}\sum_{i=1}^N {\mathbb{I}_y(x)}$$tal que, $$\mathbb{I}_y(x)=\begin{cases} 1& {\large u_{i^1}}\lt{\large u_{i^2}} \\ 0& \text{caso contrario} \end{cases}$$

Ahora con los cálculos, completamos la tabla,

| n\ integral $\rightarrow$ | (a) | (b) | (c) | (d) | (e) | (f) |
|---------------------------|-----|-----|-----|-----|-----|-----|
| 100                       | 0.5162 | 0.4931 | 0.4384 | 1.9541 | 4.5747 | 0.6000 |
| 1.000                     | 0.5701 | 0.4824 | 0.4957 | 1.7669 | 4.8408 | 0.5070 |
| 10.000                    | 0.5910 | 0.4914 | 0.5032 | 1.7553 | 4.9566 | 0.4957 |
| 100.000                   | 0.5888 | 0.4902 | 0.5015 | 1.7726 | 4.9091 | 0.5039 |
| 1.000.000                 | 0.5891 | 0.4903 | 0.5000 | 1.7732 | 4.8933 | 0.4997 |

Ver algoritmos en `ej5.py` en `MyS\simulaciones_Pr3\`

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 6</u> ([[#^indice|Índice]])
^ejercicio6

<u>Enunciado:</u> Es posible aproximar el valor de $\pi$ calculando el área de un círculo de radio $1$ centrado en $0$. Para eso, se necesitan generar $N$ puntos aleatorios en la caja $[-1,1]\times[-1,1]$ y contar la cantidad de veces que los mismos caen dentro del círculo. El cociente entre número y $N$, multiplicando por $4$(el área del cuadrado donde está contenido el cirulo) es una aproximación de $\pi$.

Completar la siguiente tabla con los valores obtenidos para distintos $N$ y compararlos con ``` numpy.pi``` o ```math.pi```: 

| n       | $\pi$ |
|---------|-------|
| 1.000   |       |
| 10.000  |       |
| 100.000 |       |

<u>Solución:</u> 

Ver algoritmo `ej6.py` en `MyS\simulaciones_Pr3\`.

llenamos la tabla, pero con un campo extra que calcula el valor absoluto de la diferencia entre el valor real de ``` numpy.pi``` y el estimado,

|    n    | $\pi$ | Diferencia |
|:-------:|:-----:|------------|
| 1.000   | 3.088 | 0.05359265 |
| 10.000  | 3.1548 | 0.01320734 |
| 100.000 | 3.14484 | 0.00324734 |

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 7</u> ([[#^indice|Índice]])
^ejercicio7

<u>Enunciado:</u> Para $U_1,U_2,...$ variables aleatorias uniformemente distribuidas en el intervalo $(0,1)$, se define: $$N=Minimo\{n:\sum_{i=1}^n {U_i}\gt 1 \}$$ Es decir, $N$ es igual a la cantidad de números aleatorios que deben sumarse para exceder a $1$.
- a) Estimar $E[N]$ generando $n$ valores de $N$ y completar la siguiente tabla: 
  
| n    | 100 | 1.000 | 10.000 | 100.000 | 1.000.000 |
|------|-----|-------|--------|---------|-----------|
| $E[N]$ |     |       |        |         |           |

- b) Calcular el valor exacto de $E[N]$.

<u>Solución:</u> 

- a) Mediante el siguiente algoritmo, estimamos $E[N]$, ver algoritmo `ej7.py` en `MyS\simulaciones_Pr3\`,
  
  y completamos la tabla,
  
| n    | 100 | 1.000 | 10.000 | 100.000 | 1.000.000 |
|------|-----|-------|--------|---------|-----------|
| $E[N]$ | 2.8 | 2.718 | 2.7152 | 2.71775 | 2.718282 |

- b) Sabiendo que $P(N\gt k) = P(U_1+U_2+...+U_k \le 1)$, para $k$ uniformes idénticamente distribuidas en $(0,1)$, el volumen de la región $\displaystyle \sum_{i=1}^k u_i\le 1$ en el cubo $[0,1]^k$ es $\displaystyle \frac{1}{k!}$, entonces $$P(N\gt k) = \frac{1}{k!},\qquad k=0,1,2,...$$luego, $$E[N]=\sum_{k=0}^N P(N\gt k) = \sum_{k=0}^N \frac{1}{k!} = e$$, por lo tanto el valor exacto es $$E[N]=e$$


---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 8</u> ([[#^indice|Índice]])
^ejercicio8

<u>Enunciado:</u> Para $U_1,U_2,...$ números aleatorios, se define: $$N=Maximo\{n:\prod_{i=1}^n {U_i}\ge e^{-3} \}$$ donde: $\displaystyle \prod_{i=1}^0 {U_i}=1$. Mediante $n$ simulaciones determinar: 
- a) 
  
| n    | 100 | 1.000 | 10.000 | 100.000 | 1.000.000 |
|------|-----|-------|--------|---------|-----------|
| E[N] |     |       |        |         |           |

- b) $P(N=i)$ para $i=0,1,2,3,4,5,6$, usando $n=1.000.000$.

<u>Solución:</u>

Definimos $Y_i = -\ln(U_i)$. Como $U_i \sim \mathcal{U}(0,1)$, entonces $Y_i \sim \text{Exp}(1)$ independientes. La condición del producto se transforma en:
$$
\prod_{i=1}^{n} U_i \ge e^{-3} \;\Longleftrightarrow\; \sum_{i=1}^{n} (-\ln U_i) \le 3 \;\Longleftrightarrow\; \sum_{i=1}^{n} Y_i \le 3.
$$
Por lo tanto,
$$
N = \max\left\{n : \sum_{i=1}^{n} Y_i \le 3\right\},
\qquad Y_i \overset{\text{i.i.d.}}{\sim} \text{Exp}(1).
$$
En un proceso de Poisson de tasa $1$, los tiempos de llegada son sumas de exponenciales de tasa $1$, y el número de llegadas en $[0,3]$ es $\text{Pois}(3)$. Así,
$$
N \sim \text{Pois}(3), \qquad 
E[N] = 3, \qquad
P(N = k) = \frac{e^{-3}\, 3^{k}}{k!},\; k = 0,1,2,\dots
$$

- a) Ver algoritmo `ej8.py` en `MyS\simulaciones_Pr3\`,

| n         | 100   | 1.000  | 10.000  | 100.000  | 1.000.000 |
|-----------|-------|--------|---------|----------|-----------|
| $E[N]$    | 2.790 | 3.033  | 2.988   | 3.006    | 2.999     |

- b) Estimación con $n=1.000.000$,

| $i$ | $P(N=i)$ estimado | $P(N=i)$ teórico (Poisson(3)) |
|-----|-------------------|-------------------------------|
| 0   | 0.04996           | 0.04979 |
| 1   | 0.14930           | 0.14936 |
| 2   | 0.22422           | 0.22404 |
| 3   | 0.22419           | 0.22404 |
| 4   | 0.16754           | 0.16803 |
| 5   | 0.10078           | 0.10082 |
| 6   | 0.05050           | 0.05041 |

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 9</u> ([[#^indice|Índice]])
^ejercicio9

<u>Enunciado:</u> Un juego consiste en dos pasos. En el primer paso se tira un dado convencional. Si sale $1$ o $6$ tira un nuevo dado y se le otorga al jugador como puntaje el doble del resultado obtenido en esta nueva tirada; pero si sale $2,3,4$ o $5$ en la primer tirada, el jugador debería tirar dos nuevos dados, y recibiría como puntaje la suma de los dados. Si el puntaje del jugador excede los $6$ puntos, entonces gana.

- a) Realizar un cálculo teórico de la probabilidad de que un jugador gane.
- b) Estime la probabilidad de que un jugador gane mediante una simulación.

<u>Solución:</u> 


Sea $D \sim \mathcal{U}\set{1,2,3,4,5,6}$, tal que $P(D=k)=\frac{1}{6}$ y sea $S$ el resultado de sumar en cada caso.
Sea $D_k$ el resultado de la tirada $k$.
- a) Se pregunta, $$P(S\gt 6) = P(S\gt 6 \,|\, D_1\in\set{1,6})\cdot P(D_1\in\set{1,6}) + P(S\gt 6 \,|\, D_2\in\set{2,3,4,5})\cdot P(D_2\in\set{2,3,4,5})$$Calculamos por casos,
	- $P(S\gt 6 \,|\, D_1\in\set{1,6})$: $$P(S\gt 6 \,|\, D_1\in\set{1,6}) = P(2D_2 \gt 6) = P(D_2\gt 3) = P(D_2\in\set{4,5,6}) = \frac{3}{6}=\frac{1}{2}$$
	- $P(S\gt 6 \,|\, D_1\in\set{2,3,4,5})$: $$P(S\gt 6 \,|\, D_1\in\set{2,3,4,5}) = P(D_2+D_3 \gt 6) = \frac{21}{36} = \frac{7}{12}$$
	- $P(D_1\in\set{1,6})$: $$P(D_1\in\set{1,6}) = \frac{2}{6} = \frac{1}{3}$$
	- $P(D_2\in\set{2,3,4,5})$: $$P(D_2\in\set{2,3,4,5}) = \frac{4}{6} = \frac{2}{3}$$
	Por lo tanto, $$P(S\gt 6) = \frac{1}{2} \cdot \frac{1}{3} + \frac{7}{12}\cdot \frac{2}{3} = \frac{1}{6} + \frac{7}{18} = \frac{5}{9}$$

- b) Ver algoritmo `ej9.py` en `MyS\simulaciones_Pr3\`, 
  
  Completamos la siguiente tabla para las respectivas iteraciones,
  
| n           | 100 | 1.000 | 10.000 | 100.000 | 1.000.000 |
|-------------|-----|-------|--------|---------|-----------|
| $P(S\gt 6)$ | 0.6000 | 0.5670 | 0.5497 | 0.5557 | 0.5557 |

---