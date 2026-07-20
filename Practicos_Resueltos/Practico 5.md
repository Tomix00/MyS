Generación de variables aleatorias continuas
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
8. [[#^ejercicio8|Ejercicio 8 - Resuelto]]
9. [[#^ejercicio9|Ejercicio 9 - Resuelto-agente]]
10. [[#^ejercicio10|Ejercicio 10 - Resuelto-agente]]
11. [[#^ejercicio11|Ejercicio 11 - Resuelto-agente]]
12. [[#^ejercicio12|Ejercicio 12 - Resuelto-agente]]
13. [[#^ejercicio13|Ejercicio 13 - Resuelto-agente]]
14. [[#^ejercicio14|Ejercicio 14 - Resuelto-agente]]

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 1</u> ([[#^indice|Índice]])
^ejercicio1

<u>Enunciado:</u> Desarrolle un método para generar una variable aleatoria cuya densidad de probabilidad es:
- a) $$\large f(x)=\begin{cases} \frac{x-2}{2}&\text{ si }2\le x\le3 \\ \frac{2-x/3}{2}&\text{ si }3\le x\le 6 \\ 0&\text{ en otro caso } \end{cases}$$
- b) $$\large f(x)=\begin{cases} \frac{6(x+3)}{35}&\text{ si }0\le x\le1 \\ \frac{6x^2}{35}&\text{ si }1\le x\le 2 \\ 0&\text{ en otro caso } \end{cases}$$
- c) $$\large f(x)=\begin{cases} \frac{exp(4x)}{4}&\text{ si }-\infty\lt x\le0 \\ \frac{1}{4}&\text{ si }0\lt x\le \frac{15}{4} \\ 0&\text{ en otro caso } \end{cases}$$

<u>Solución:</u>
- a) 
	- Necesitamos calcular $F(x)$:
	- Para $2\le x \le 3$: $$F(x)=\int_2^x {\frac{t-2}{2}} dt = \frac{1}{2}\left[ \frac{(t-2)^2}{2} \right]_2^x = \frac{(x-2)^2}{4}$$
	- Para $3\le x\le 6$: $$\begin{align}F(x)=&\,F(3)+\int_3^x {\frac{2-t/3}{2}} dt = \frac{1}{4}+\frac{1}{2}\left[ 2t-\frac{t^2}{6} \right]_3^x \\=&\, \frac{1}{4} + \frac{1}{2}\left( 2x-\frac{x^2}{6}-\left( 6-\frac{9}{6} \right) \right) \\=&\, \frac{1}{4} + \frac{1}{2}\left( 2x-\frac{x^2}{6}- \frac{27}{6} \right) \\=&\, \frac{1}{4} + \frac{1}{2}\left( 2x-\frac{x^2}{6}- \frac{9}{2} \right) \\=&\, \frac{1}{4} + x - \frac{x^2}{12} - \frac{9}{4} \\=&\, x - \frac{x^2}{12} - 2 \end{align}$$
	- Verificando: $$F(6) = 6 - \frac{36}{12} - 2 = 6 - 3 - 2 = 1$$
	- Ahora realizamos la inversa:
	- Para $0 \le u \le 1/4$: $$u = \frac{(x-2)^2}{4}\implies x = 2 + 2\sqrt{u}$$
	- Para $1/4\le u \le 1$: $$\begin{align} u =&\, x - \frac{x^2}{12} - 2 \\-12u=&\, -12x + x^2 + 12 \\0=&\, x^2 - 12x + 12u + 24 \end{align}$$
	- Tomando $a: 1$, $b:-12$ y $c:12u + 24$, $$x=\frac{12\pm \sqrt{144 - 4(12u + 24)}}{2} = 6\pm\sqrt{36 + 12u + 24} = 6\pm\sqrt{12 - 12u}$$
	- Para $x\in[3,6]$, tomamos la rama negativa: $$x = 6 - \sqrt{12(1-u)} = 6 - 2\sqrt{3(1-u)}$$
	- Ver algoritmo `ej1.py` en `MyS\simulaciones_Pr5\`
- b)
	- Necesitamos calcular $F(x)$:
	- Para $0\le x \le 1$: $$F(x) = \int_0^x {\frac{6(t+3)}{35}} dt = \frac{6}{35}\left[ \frac{t^2}{2} + 3t \right]_0^x = \frac{6}{35}\left( \frac{x^2}{2} + 3x \right) = \frac{3x^2 + 18x}{35}$$
	- Para $1\le x\le 2$: $$\begin{align} F(x) =&\, F(1) + \int_1^x {\frac{6t^2}{35}} dt \\=&\, \frac{3}{5} + \frac{6}{36} \cdot \left[ \frac{t^3}{3} \right]_1^x \\=&\, \frac{3}{5} + \frac{2}{35}(x^3 - 1) \\=&\, \frac{3}{5} + \frac{2x^3}{35} - \frac{2}{35} \\=&\, \frac{21}{35} + \frac{2x^3}{35} - \frac{2}{35} \\=&\, \frac{2x^3 + 19}{35} \end{align}$$
	- Ahora realizamos la inversa:
	- Para $0\le u \le 3/5$: $$u = \frac{3x^2 + 18x}{35} \implies 3x^2 + 18x - 35u = 0$$
	- $$x = \frac{-18 + \sqrt{324 + 420u}}{6} = \frac{-18 + \sqrt{36(9 + 35u/3)}}{6} = \frac{-18 + 6\sqrt{9 + 35u/3}}{6}$$
	- $$x = -3 + \sqrt{9 + \frac{35u}{3}}$$
	- Para $3/5 \le u \le 1$: $$u = \frac{2x^3 + 19}{35} \implies 2x^3 = 35u - 19 \implies x^3 = \frac{35u - 19}{2}$$
	- $$x = \left( \frac{35u - 19}{2} \right)^{1/3}$$
	- Ver algoritmo `ej1.py` en `MyS\simulaciones_Pr5\`
- c)
	- Necesitamos calcular $F(x)$:
	- Para $x\le 0$: $$F(x) = \int_{-\infty}^x {\frac{e^{4t}}{4}} dt = \frac{3^{4x}}{16}$$
	- Para $0 \lt x \le 15/4$: $$\begin{align} F(x) =&\, F(0) + \int_0^x {\frac{1}{4}} dt \\=&\, \frac{1}{16} + \int_0^x {\frac{1}{4}} dt \\=&\, \frac{1}{16} + \frac{x}{4} \end{align}$$
	- Ahora realizamos la inversa:
	- Para $0\le u \le 1/16$: $$u = \frac{e^{4x}}{16} \implies e^{4x} = 16u \implies x=\frac{1}{4}\ln(16u)$$
	- Para $1/16 \le u \le 1$: $$u = \frac{1}{16} + \frac{x}{4} \implies \frac{x}{4} = u - \frac{1}{16} \implies x = 4u - \frac{1}{4}$$
	- Ver algoritmo `ej1.py` en `MyS\simulaciones_Pr5\`

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 2</u> ([[#^indice|Índice]])
^ejercicio2

<u>Enunciado:</u>
- a) Desarrolle métodos para generar las siguientes variables aleatorias
	- i) Distribución Pareto $$f(x) = ax^{\large-(a+1)} \quad 1\le x \lt\infty, \quad a\gt0$$
	- ii) Distribución Erlang $$f(x)=\frac{x^{k-1}\exp(-x/\mu)}{(k-1)!\mu^{k}} \quad 0\le x\lt\infty,\quad \mu\gt0, \quad k\text{ entero}$$
	- iii) Distribución Weibull $$f(x) = \frac{\beta}{\lambda}\left( \frac{x}{\lambda} \right)^{\beta - 1}\exp(-(x/\lambda)^{\beta}) \quad x\ge0, \quad\lambda\gt0, \quad \beta\gt0 $$
	  Ayuda: La distribución Pareto y la distribución Weibull tienen distribución acumulada $F$ con forma cerrada, por lo cual puede aplicarse el método de la transformada Inversa. La distribución de Erlang pertenece a la familia de las Gammas. Puede simularse por rechazo o como suma de exponenciales.
- b) Estime la media de cada variable con $10.000$ repeticiones, usando parámetros $a = 2, \mu = 2, k = 2, \lambda = 1, \beta = 2$. Busque en la web los valores de las esperanzas para cada variable con estos parámetros(cuidado con las parametrizaciones) y compare los valores obtenidos.

<u>Solución:</u>
- a)
	- i) Distribución de Pareto:
		- Densidad: $$f(x) = ax^{\large-(a+1)} \quad 1\le x \lt\infty, \quad a\gt0$$
		- Función de distribución acumulada: $$F(x)=\int_1^x {at^{\large-(a+1)}} dt = 1 - x^{-a}, \quad x\ge 1$$
		- Para aplicar el método de la transformada inversa: $$U = F(X) = 1 - X^{-a} \implies X^{-a} = 1 - U \implies X = (1 - U)^{-1/a}$$
		- Como $1 - U \sim \rm{Uniforme}(0,1)$,  también podemos escribir: $$X = U^{-1/a}$$
		- Ver algoritmo `ej2.py` en `MyS\simulaciones_Pr5\`
	- ii) Distribución Erlang
		- Densidad: $$f(x)=\frac{x^{k-1}\exp(-x/\mu)}{(k-1)!\mu^{k}} \quad x\ge0, \quad \mu\gt0, \quad k\text{ entero}$$
		- La distribución Erlang es un caso especial de la distribución Gamma: $X\sim\rm{Gamma}(k,1/\mu)$ con **forma entera**. Por la propiedad de la suma de exponenciales: $$X = \sum^k_{i=1} {E_i},\quad E_i \sim \rm{Exp}(\lambda = 1/\mu)\, \rm{independientes}$$
		- Cada $E_i$ se genera por transformada inversa: $E_i = -\mu\ln(1-U_i)$.
		- Ver algoritmo `ej2.py` en `MyS\simulaciones_Pr5\`
	- iii) Distribución Weibull
		- Densidad: $$f(x) = \frac{\beta}{\lambda}\left( \frac{x}{\lambda} \right)^{\beta - 1}\exp(-(x/\lambda)^{\beta}) \quad x\ge0, \quad\lambda\gt0, \quad \beta\gt0$$
		- Función de distribución acumulada: $$F(x) = 1 - e^{\large -(x/\lambda)^{\beta}}$$
		- Método de transformada inversa: $$\begin{align} U = 1 - e^{\large -(X/\lambda)^{\beta}} \implies& e^{\large -(X/\lambda)^{\beta}} = 1 - U \\ -(X/\lambda)^{\beta} = \ln(1 - U) \implies& (X/\lambda)^{\beta} = -\ln(1 - U) \\ X = \,\lambda(-\ln(1& - U))^{\large 1/\beta}  \end{align}$$
		- Como $1 - U \sim\rm{Uniforme}(0,1)$: $$X = \,\lambda(-\ln(U))^{\large 1/\beta}$$
		- Ver algoritmo `ej2.py` en `MyS\simulaciones_Pr5\`
- b)
	- Distribución Pareto
		- Parámetros $a=2$
		- Esperanza teórica: $$E[X] = \frac{a}{a-1} = \frac{2}{1} = 2 \quad\text{(para }x\ge 1)$$
	- Distribución Erlang
		- Parámetros $k = 2$, $\mu = 2$
		- Esperanza teórica: $$E[X] = k\mu = 2\times 2 = 4$$
	- Distribución Weibull
		- Parámetros $\lambda = 1$, $\beta = 2$
		- Esperanza teórica: $$E[X] = \lambda\Gamma(1 + 1/\beta) = 1 \times \Gamma(1.5) = \frac{\sqrt{\pi}}{2}\approx 0.8862$$
	- Mediante el siguiente algoritmo obtenemos las estimaciones:
	- Ver algoritmo `ej2.py` en `MyS\simulaciones_Pr5\`
	- Obteniendo así los siguientes resultados:
	- | Distribución | Estimada | Teórica  |
|--------------|----------|----------|
| Pareto       | $1.9801$ | $2$      |
| Erlang       | $3.9819$ | $4$      |
| Weibull      | $0.8816$ | $0.8862$ |

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 3</u> ([[#^indice|Índice]])
^ejercicio3

<u>Enunciado:</u> Método de la composición:
- a) Suponga que es relativamente fácil generar $n$ variables aleatorias a partir de sus distribuciones de probabilidad $F_i$, $i = 1,...,n$. Implemente un método para generar una variable aleatoria cuya distribución de probabilidad es $$F(x) = \sum_{i=1}^n {p_i F_i(x)}$$ donde $p_i$, $i = 1,...,n$, son números no negativos cuya suma es $1$.
- b) Genere datos usando tres exponenciales independientes con media $3, 5$ y $7$ respectivamente y $p=(0.5, 0.3, 0.2)$. Calcule la esperanza exacta de la mezcla y estime con $10.000$ repeticiones. Tenga cuidado con la parametrización que este usando!!

<u>Solución:</u>
- a) Dado: $$F(x) = \sum_{i=1}^n {p_i F_i(x)}, \qquad \sum_{i=1}^n {p_i} = 1, \quad p_i\ge0$$
	- El método de composición dice:
		1. Generar $U\sim\rm{Uniforme}(0,1)$.
		2. Elegir un índice $i$ con probabilidad $p_i$.
		3. Generar $X$ a partir de la distribución $F_i$.
		4. Devolver $X$.
	- De esta manera, tenemos el siguiente algoritmo:
	- Ver algoritmo `ej3.py` en `MyS\simulaciones_Pr5\`
- b) 
	- Dados
		- $Exp_1$: media $3 \to$ parámetro $\lambda_1 = 1/3$
		- $Exp_2$: media $5 \to$ parámetro $\lambda_2 = 1/5$
		- $Exp_3$: media $7 \to$ parámetro $\lambda_3 = 1/7$
		- Probabilidades: $p=(0.5, 0.3, 0.2)$
	- Esperanza exacta de la mezcla: $$\begin{align}E[X] =&\, \sum_{i=1}^n {p_i \cdot E[X_i]} = 0.5\times3 + 0.3\times3 + 0.2\times7 \\ =&\, 1.5 + 1.5 + 1.4 \\=&\, 4.4 \end{align}$$
	- Ver algoritmo `ej3.py` en `MyS\simulaciones_Pr5\`

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 4</u> ([[#^indice|Índice]])
^ejercicio4

<u>Enunciado:</u> Desarrolle un método para generar la variable aleatoria con función de distribución $$F(x) = \int_0^{\infty} {x^y e^{-y}} dy, \quad 0\le x \le 1.$$ Piense en el método de composición del ejercicio anterior. En particular, sea $F$ la función de distribución de $X$ y suponga que la distribución condicional de $X$ dado $Y=y$  es $$P(X\le x | Y = y) = x^y, \quad 0\le x \le 1.$$

<u>Solución:</u>
- Identificación de la distribución marginal de $Y$
	- Si $$F(x) = \int_0^{\infty} {F_{X|Y}(x|y)f_Y(y)} dy$$comparando con la expresión dada: $$F(x) = \int_0^{\infty} {x^y e^{-y}} dy$$ se deduce que: $$f_Y(y) = e^{-y},\quad y\gt0$$es decir, $Y\sim\rm{Exp}(1)$(exponencial con media $1$, parámetro $\lambda = 1$).
- Método de composición:
	1. Generar $Y \sim \rm{Exp}(1)$.
	2. Dado $Y = y$, generar $X$ con distribución $P(X\le x|Y=y) = x^y$.
	   La generación de $X$ condicional a $Y = y$ se puede hacer por **transformada inversa**: $$U = X^y \implies X = U^{1/y}.$$Si $U \sim \rm{Uniforme}(0,1)$, entonces $P(U^{1/y}\le x) = P(U \le x^y) = x^y$.
- Algoritmo completo
	1. Generar $U_1 \sim\rm{Uniforme}(0,1)$
	2. Calcular $Y = -\ln(1 - U_1)$(método de transformada inversa para $\rm{Exp}(1)$).
	3. Generar $U_2 \sim\rm{Uniforme}(0,1)$ independiente.
	4. Calcular $X = U_2^{1/Y}$.
	5. Devolver $X$.
- Ver algoritmo `ej4.py` en `MyS\simulaciones_Pr5\`

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 5</u> ([[#^indice|Índice]])
^ejercicio5

<u>Enunciado:</u>
- a) Considere que es sencillo generar una variable aleatoria a partir de cualquiera de las distribuciones $F_i$, $i = 1,..,n$. Explique cómo generar variables aleatorias a partir de las siguientes distribuciones:
	- i) $F_M(x) = {\displaystyle \prod_{i=1}^n {F_i(x)}}$
	- ii) $F_m(x) = 1 - {\displaystyle \prod_{i=1}^n} {(1 - F_i(x))}$
	  **Sugerencia**: Si $X_i$, $i=1,...,n$, son variables aleatorias independientes, donde $X_i$ tiene distribución $F_i$, ¿Cuál variable tiene como distribución a $F$ en cada caso?
- b) Genere una muestra de $10$ valores de las variables $M$ y $m$ con distribuciones $F_M$ y $F_m$ si $X_i$ son exponenciales independientes con parámetros $1,2$ y $3$ respectivamente.

<u>Solución:</u>
Dadas $X_1,...,X_n$ independientes, con $X_i \sim F_i$.
- a) Identificación de $F_M$ y $F_m$
	- i) $F_M(x) = {\prod_{i=1}^n {F_i(x)}}$
		- Observamos que: $$P(\max(X_1,...,X_n)\le x) = P(X_1\le x,...,X_n\le x) = \prod_{i=1}^n {F_i(x)}$$
		- Por lo tanto: $$F_M(x) = F_{max}(x)$$
		- Conclusión: $M=\max(X_1,...,X_n)$ tiene distribución $F_M$.
		- Método de generación:
			- Generar $X_1,...,X_n$ independientes con distribuciones $F_i$ y devolver $M=\max(X_1,...,X_n)$.
	- ii) $F_m(x) = 1 - {\prod_{i=1}^n} {(1 - F_i(x))}$
		- Observamos que: $$1 - F_m(x) = {\prod_{i=1}^n} {(1 - F_i(x))}$$
		- Pero $1 - F_i(x) = P(X_i \gt x)$. Luego: $$\prod_{i=1}^n {P(X_i\gt x)} = P(X_1\gt,...,X_n\gt x) = P(\min(X_1,..,X_n)\gt x)$$
		- Por lo tanto: $$1 - F_m(x) = P(\min(X_1,...,X_n)\gt x) \implies F_m(x) = P(\min(X_1,...,X_n)\le x)$$
		- Conclusión: $m = \min(X_1,...,X_n)$ tiene distribución $F_m$.
		- Método de generación:
			- Generar $X_1,...,X_n$ independientes con distribución $F_i$ y devolver $m = \min(X_1,...,X_n)$.
- b) 
	- Datos:
		- $X_1 \sim \rm{Exp}(\lambda_1 = 1) \to$, media 1, función de distribución $F_1(x) = 1 - e^{-x}$
		- $X_2 \sim \rm{Exp}(\lambda_2 = 2) \to$, media $1/2$, $F_2(x) = 1 - e^{-2x}$
		- $X_3 \sim \rm{Exp}(\lambda_3 = 3) \to$, media $1/3$, $F_3(x) = 1 - e^{-3x}$
	- Mediante el siguiente algoritmo generamos las muestras:
	- Ver algoritmo `ej5.py` en `MyS\simulaciones_Pr5\`

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 6</u> ([[#^indice|Índice]])
^ejercicio6

<u>Enunciado:</u> Utilice el método del rechazo y los resultados del ejercicio anterior para desarrollar otros dos métodos, además del método de la transformada inversa, para generar una variable aleatoria con distribución de probabilidad $$F(x) = x^n, \quad 0\le x \le 1.$$Analice la eficiencia de los tres métodos para generar la variable a partir de $F$.

<u>Solución:</u>
- Método 1: Transformada inversa
	- $U = X^n \implies X = U^{1/n}$
	- Ver algoritmo `ej6.py` en `MyS\simulaciones_Pr5\`
- Método 2: Por composición usando el máximo
	- Del ejercicio 5, sabemos que: $$F_M(x) = \prod_{i=1}^n F_i(x) \implies M=\max(X_1,...,X_n)$$
	- Si tomamos $X_i \sim \rm{Uniforme}(0,1)$, entonces $F_i(x) = x$ para $0\le x \le 1$.
	- Por lo tanto: $$F_M(x) = x^n$$
	- Conclusión: Generar $n$ uniformes y tomar el máximo es equivalente.
	- Ver algoritmo `ej6.py` en `MyS\simulaciones_Pr5\`
- Método 3: Por aceptación y rechazo
	- Necesitamos la densidad: $$f(x) = nx^{n-1}, \quad 0\le x \le 1$$
	- Usamos una densidad candidata simple. Elegimos $g(x) = 1$ (uniforme en $[0,1]$).
	- La constante $c$ debe satisfacer: $$c\ge\frac{f(x)}{g(x)} = nx^{n-1},\quad \forall x\in[0,1]$$
	- El máximo de $nx^{n-1}$ en $[0,1]$ ocurre en $x=1$: $$\max_{x\in[0,1]} nx^{n-1} = n $$
	- Tomamos $c=n$.
	- Entonces: $$\frac{f(x)}{c\cdot g(x)} = \frac{nx^{n-1}}{n\cdot 1} = x^{n-1}$$
	- Ver algoritmo `ej6.py` en `MyS\simulaciones_Pr5\`
- Finalmente analizamos la eficiencia de cada uno:
	- Ver algoritmo `ej6.py` en `MyS\simulaciones_Pr5\`
	- | Método      | Tiempo   |
|-------------|----------|
| Inversa     | $0.0014$ |
| Composición | $0.0062$ |
| Rechazo     | $0.0126$ |

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 7</u> ([[#^indice|Índice]])
^ejercicio7

<u>Enunciado:</u>
- a) Desarrolle dos métodos para generar una variable aleatoria $X$ con densidad de probabilidad: $$f(x) = \begin{cases}\displaystyle \frac{1}{x}&\text{ si }1\le x\le e \\ 0&\text{ en otro caso} \end{cases}$$
	- i) Aplicando Transformada inversa.
	- ii) Aplicando el método de aceptación y rechazo con una variable uniforme.
- b) Compare la eficiencia de ambos métodos realizando $10.000$ simulaciones y comparando el promedio de los valores obtenidos. Compruebe que se obtiene un valor aproximado del valor esperando de $X$.
- c) Estime la probabilidad $P(X\le 2)$ y compárela con el valor real.

<u>Solución:</u>
- a) Métodos para generar $X$ con $f(x) = 1/x$, $1\le x\le e$
	- i) Método de la transformada inversa
		- Primero calculamos la función de distribución acumulada: $$F(x) = \int_1^x {\frac{1}{t}} dt = \ln t\bigg|_1^x = \ln x, \quad 1\le x\le e$$
		- Aplicamos transformada inversa: $$U = F(X) = \ln X \implies X = e^{U}$$donde $U\sim\rm{Uniforme}(0,1)$.
		- Sea el siguiente algoritmo:
	- ii) Método de aceptación y rechazo con una variable uniforme
		- Elegimos como variable candidata $Y\sim\rm{Uniforme}(1,e)$
		- Su densidad es $g(y) = \displaystyle\frac{1}{e-1}$ para $1\le y \le e$.
		- Buscamos una constante $c$ tal que: $$\frac{f(y)}{g(y)} = \frac{1/y}{1/(e-1)} = \frac{e-1}{y}\le c, \quad \forall y\in[1,e]$$
		- El cociente $\displaystyle\frac{e-1}{y}$ es máximo cuando $y$ es mínimo, es decir, $y = 1$: $$\max_{y\in[1,e]} \frac{e-1}{y} = e - 1$$
		- Tomamos $c = e - 1 \approx 1.71828$
		- Luego: $$\frac{f(y)}{c\cdot g(y)} = \frac{1/y}{(e-1)\cdot{\large\frac{1}{e-1}}} = \frac{1/y}{1} = \frac{1}{y}$$
		- Porque $c\cdot g(y) = (e-1)\cdot{\large\frac{1}{e-1}} = 1$
		- Ver algoritmo `ej7.py` en `MyS\simulaciones_Pr5\`
- b) Comparación de eficiencia
	- Valor exacto: $$E[X] = \int_1^e {x\left(\frac{1}{x}\right)} dx = \int_1^e {1} dx = e - 1 \approx 1.71828$$
	- Ver algoritmo `ej7.py` en `MyS\simulaciones_Pr5\`
- c) Estimación de $P(X\le 2)$
	- $$P(X\le 2) = F(2) = \ln 2 \approx 0.693147$$
	- Ver algoritmo `ej7.py` en `MyS\simulaciones_Pr5\`

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 8</u> ([[#^indice|Índice]])
^ejercicio8

<u>Enunciado:</u>
- a) Sean $U$ y $V$ dos variables aleatorias uniformes en $(0,1)$ e independientes. Pruebe que la variable $X = U + V$ tiene densidad _triangular_: $$f(x) = \begin{cases} x& 0\le x\lt 1 \\ 2-x& 1\le x\lt 2 \\ 0&\text{en otro caso.}\end{cases}$$
- b) Desarrolle tres algoritmos que simules la variable $X$:
	- i) Usando la propiedad que $X$ es suma de dos uniformes.
	- ii) Aplicando transformada inversa.
	- iii) Con el método de rechazo.
- c) Compare la eficiencia de los tres algoritmos. Para cada caso, estimar el valor esperado promediando $10.000$ valores simulados. ¿Para qué valor $x_0$ se cumple que $P(X\gt x_0) = 0.125$?
- d) Compare la proporción de veces que el algoritmo devuelve un número mayor que $x_0$ con esta probabilidad.

<u>Solución:</u>
- a) Sean $U,V \sim\rm{Uniforme}(0,1)$ independientes.
	- La densidad conjunta es $f_{U,V}(u,v)=1$ en el cuadrado unitario.
	- Queremos la densidad de $X = U + V$.
	- Usamos convolución: $$f_X(x) = \int_{-\infty}^{\infty} {f_U(t)f_V(x-t)} dt = \int_0^1 {f_V(x-t)} dt,\quad 0\le t\le 1$$
	- Caso $0\le x\le 1$:
		- Necesitamos $0\le t\le 1$ y $0\le x-t\le 1\implies t\le x$ y $t\ge x - 1$ (automático pues $x-1\le 0$).
		- Entonces $t\in[0,x]$
		- $$f_X(x) = \int_0^x {1} dt = x$$
	- Caso $1\le x\le 2$:
		- Necesitamos $0\le t\le 1$ y $0\le x-t\le 1 \implies t\ge x-1$ y $t\le x$ (automático pues $x\le 2$).
		- Necesitamos $t\in[x-1,1]$
		- $$f_X(x) = \int_{x-1}^1 {1} dt = 1 - (x-1) = 2 - x$$
	- Por lo tanto: $$f(x) = \begin{cases} x& 0\le x\lt 1 \\ 2-x& 1\le x\lt 2 \\ 0&\text{en otro caso.}\end{cases}$$
- b) Tres algoritmos para simular $X$
	- i) Suma de dos uniformes
		- Ver algoritmo `ej8.py` en `MyS\simulaciones_Pr5\`
	- ii) Transformada inversa
		- Primero calculamos $F(x)$: $$f(x) = \begin{cases}\displaystyle \frac{x^2}{2}& 0\le x\le 1 \\\displaystyle 2x-\frac{x^2}{2}-1& 1\le x\le 2\end{cases}$$
		- Realizamos la inversa:
			- Si $0\le u\le 0.5$: $$u = \frac{x^2}{2} \implies x = \sqrt{2u}$$
			- Si $0.5\le u \le 1$: $$\begin{align}u =&\, 2x - \frac{x^2}{2}-1 \\ x^2 -4x +2(u+1) =&\, 0 \\ x =&\, 2\pm \sqrt{4-2(u+1)} \\ =&\, 2\pm\sqrt{2-2u}  \end{align}$$
			- Para $x\in[1,2]$ tomamos la rama negativa: $$2 - \sqrt{2(1-u)}$$
			- Ver algoritmo `ej8.py` en `MyS\simulaciones_Pr5\`]]
	- iii) Método de aceptación y rechazo
		- Queremos generar $X$ con densidad $f$ triangular en $[0,2]$.
		- Usamos $Y \sim\rm{Uniforme}(0,2)$ con densidad $g(y) = 1/2$.
		- Buscamos $c$ tal que $\displaystyle \frac{f(y)}{g(y)} \le c$: $$\frac{f(y)}{g(y)} = \frac{f(y)}{1/2} = 2f(y)\le c$$
		- El máximo de $f(y)$ es $1$ (en $x=1$), entonces $2\cdot 1 = 2$.
		- Tomamos $c = 2$.
		- Luego: $$\frac{f(y)}{c\cdot g(y)} = \frac{f(y)}{2\cdot (1/2))} = f(y)$$
		- Ver algoritmo `ej8.py` en `MyS\simulaciones_Pr5\`
- c) Comparación de eficiencia y estimación de $E[X]$
	- La esperanza exacta de la distribución triangular es: $$E[X] = \int_0^1 {x\cdot x} dx + \int_1^2 {x\cdot(2-x)} dx = \left[\frac{x^3}{3}\right]_0^1 + \left[x^2-\frac{x^3}{3}\right]_1^2 = \frac{1}{3} + \frac{2}{3} = 1$$
	- Sea el siguiente algoritmo para comparar la eficiencia:
	- Ver algoritmo `ej8.py` en `MyS\simulaciones_Pr5\`
	- Calculo de $x_0$ tal que $P(X\gt x_0) = 0.125$
		- $$P(X\gt x_0) = 1 - F(x_0) = 0.125 \implies F(x_0) = 0.875$$
		- Como $F(1) = 0.5$ y $F(2)=1$, buscamos en el segundo tramo: $$\begin{align} F(x_0) = 2x_0 - \frac{x_0^2}{2} -1 =&\, 0.875 \\ 2x_0 - \frac{x_0^2}{2} =&\, 1.875 \end{align}$$
		- Multiplicando por $2$: $$ 4x_0 - x_0^2 = 3.75 \implies x_0^2 - 4x_0 + 3.75 = 0 $$
		- $$ x_0 = 2\pm\sqrt{4 - 3.75} = 2\pm\sqrt{0.25} = 2\pm 0.5 $$
		- La solución en $[1,2]$ es $x_0 = 2 - 0.5 = 1.5$
- d) Comparación de la proporción $P(X\gt 1.5)$ con el valor teórico
	- Ver algoritmo `ej8.py` en `MyS\simulaciones_Pr5\`

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 9</u> ([[#^indice|Índice]])
^ejercicio9

<u>Enunciado:</u> Escriba tres programas para generar una variable aleatoria normal patrón, usando:
- a) Generación de variables exponenciales según el ejemplo 5f del libro simulación de S. M. Ross
- b) El método polar
- c) El método de razón entre uniformes.

Pruebe los códigos calculando la media muestral y varianza muestral de $10.000$ valores generados con los tres métodos.

<u>Solución:</u>

- **a) Box-Muller (Ross):** generar $U_1,U_2 \sim \mathcal{U}(0,1)$, luego
  $$Z_1 = \sqrt{-2\ln U_1}\,\cos(2\pi U_2),\quad Z_2 = \sqrt{-2\ln U_1}\,\sin(2\pi U_2)$$
  produce dos normales estándar independientes. Se basa en que la coordenada angular de un punto $(Z_1,Z_2)$ es uniforme en $[0,2\pi)$ y el radio al cuadrado es $\chi^2_2 \equiv \text{Exp}(1/2)$.

- **b) Polar (Marsaglia):** generar $V_1,V_2 \sim \mathcal{U}(-1,1)$ hasta que $W = V_1^2+V_2^2 \le 1$. Luego
  $$Z_1 = V_1\sqrt{-2\ln W/W},\quad Z_2 = V_2\sqrt{-2\ln W/W}.$$
  Evita el cálculo de funciones trigonométricas a costa de generar pares hasta caer dentro del círculo unitario.

- **c) Razón entre uniformes (Kinderman-Monahan):** generar $U \sim \mathcal{U}(0,1)$, $V \sim \mathcal{U}(-a,a)$ con $a = \sqrt{2/e}$, hasta que $V^2 \le -4U^2\ln U$. Devolver $X = V/U$.

Ver `ej9.py`. Resultados con $10.000$ simulaciones:

| Método           | Media  | Varianza | Tiempo |
|------------------|--------|----------|--------|
| Ross (Box-Muller)| -0.02  | 1.02     | 0.003s |
| Polar            | 0.00   | 1.00     | 0.005s |
| Razón uniformes  | 0.00   | 1.00     | 0.006s |

Los tres métodos producen muestras con media $\approx 0$ y varianza $\approx 1$, consistentes con $N(0,1)$.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 10</u> ([[#^indice|Índice]])
^ejercicio10

<u>Enunciado:</u> Una variable aleatoria $X$ tiene distribución de Cauchy con parámetro $\lambda\gt 0$ si su densidad es $$f(x) = \frac{1}{\lambda\pi(1 + (x/\lambda)^2)},\quad x\in\mathbb{R}$$
- a) Implemente el método de razón entre uniformes para simular $X$ con parámetro $\lambda = 1$. Para esto:
	1. Pruebe que el conjunto $C_f = \set{(u,v) |0\lt u\lt \sqrt{f(v/u)}}$ es el conjunto derecho centrado en $(0,0)$ de radio $\sqrt{1/\pi}$.
	2. Desarrolle un algoritmo $\text{CAUCHY()}$ que genere pares $(U,V)$ con distribución uniforme en $C_f$, y devuelva $X=V/U$. Entonces $X$ tiene distribución deseada. ¿Es necesario utilizar el valor de $\pi$?
- b) Pruebe que si $X$ tiene distribución de Cauchy con parámetro $1$, entonces $\lambda X$ tiene distribución de Cauchy con parámetro $\lambda$.
- c) Utilice esta propiedad para modificar el algoritmo anterior, e implementar $\text{CAUCHY(LAMBDA)}$ que simule una variable $X$ con distribución de Cauchy de parámetro $\lambda$.
- d) Realice $10.000$ simulaciones y calcule la proporción de veces que el resultado cae en el intervalo $(-\lambda,\lambda)$, para $\lambda = 1,\lambda = 2.5$ y $\lambda = 0.3$. Compare con la probabilidad teórica.

<u>Solución:</u>

- **a)** Para $\lambda=1$, $f(x) = 1/(\pi(1+x^2))$. El conjunto $C_f$ es:
  $$0 < u < \sqrt{f(v/u)} \; \Longleftrightarrow \; u^2 < \frac{1}{\pi(1+(v/u)^2)} \; \Longleftrightarrow \; u^2 + v^2 < \frac{1}{\pi}.$$
  Es decir, $C_f$ es el semicírculo derecho ($u>0$) de radio $\sqrt{1/\pi}$ centrado en $(0,0)$. No es necesario usar $\pi$ explícitamente: muestrear $(U,V)$ uniformes en el círculo unitario $U^2+V^2\le 1$ con $U>0$ y devolver $X=V/U$ produce la misma distribución (escalar por $\sqrt{1/\pi}$ cancela en el cociente).

- **b)** Si $X \sim \text{Cauchy}(1)$, entonces $Y = \lambda X$ tiene densidad:
  $$f_Y(y) = f_X(y/\lambda) \cdot \frac{1}{\lambda} = \frac{1}{\pi(1+(y/\lambda)^2)} \cdot \frac{1}{\lambda} = \frac{1}{\lambda\pi(1+(y/\lambda)^2)},$$
  que es Cauchy($\lambda$). 

- **c)** $\text{CAUCHY(LAMBDA)}$: generar $(U,V)$ uniforme en círculo unitario con $U>0$, devolver $\lambda \cdot V/U$.

- **d)** $P(-\lambda < X < \lambda) = F(\lambda) - F(-\lambda) = \frac{1}{2}$ para cualquier $\lambda$. Ver `ej10.py`:

| $\lambda$ | $P(-\lambda<X<\lambda)$ obs | Teórica |
|-----------|----------------------------|---------|
| 1.0       | 0.494                      | 0.5     |
| 2.5       | 0.497                      | 0.5     |
| 0.3       | 0.501                      | 0.5     |
<div style="page-break-after: always;"></div>

## <u>Ejercicio 11</u> ([[#^indice|Índice]])
^ejercicio11

<u>Enunciado:</u> Sea $X$ una variable aleatoria con distribución de Cauchy de parámetro $\lambda$.
- a) Calcule la función de distribución acumulada de $F_X$.
- b) Simule $X$ aplicando el método de la transformada inversa.
- c) Indique si es posible generar $X$ por el método de aceptación y rechazo, rechazando con una variable aleatoria normal.
- d) Realice $10.000$ simulaciones y calcular la proporción de veces que el resultado cae en el intervalo $(-\lambda,\lambda)$, para $\lambda = 1, \lambda = 2.5$ y $\lambda = 0.3$. Compare con la probabilidad teórica.
- e) Compare la eficiencia de este algoritmo con el método de razón entre uniformes.

<u>Solución:</u>

- **a)** La FDA de Cauchy($\lambda$) es:
  $$F_X(x) = \int_{-\infty}^{x} \frac{1}{\lambda\pi(1+(t/\lambda)^2)} dt = \frac{1}{\pi}\arctan\!\left(\frac{x}{\lambda}\right) + \frac{1}{2}.$$

- **b)** Transformada inversa: $U = F(X) \implies X = \lambda \tan(\pi(U - 1/2))$.

- **c)** No es eficiente usar rechazo con normal. Cauchy($\lambda$) tiene colas pesadas ($f(x) \sim 1/(\pi x^2)$) mientras que la normal decae exponencialmente ($e^{-x^2/2}$). La constante $c$ sería enorme y la tasa de aceptación prácticamente nula.

- **d)** Ver `ej11.py`:

| $\lambda$ | $P(-\lambda<X<\lambda)$ obs | Teórica |
|-----------|----------------------------|---------|
| 1.0       | 0.504                      | 0.5     |
| 2.5       | 0.502                      | 0.5     |
| 0.3       | 0.498                      | 0.5     |

- **e)** La transformada inversa (1 generación = 1 tan + 1 escalado) es más rápida que el método de razón entre uniformes (requiere generar múltiples pares hasta aceptar). En $100.000$ generaciones: inversa $0.024$s, razón $0.036$s (razón es $\sim 0.67\times$ la velocidad de inversa).
<div style="page-break-after: always;"></div>

## <u>Ejercicio 12</u> ([[#^indice|Índice]])
^ejercicio12

<u>Enunciado:</u> Escriba un programa que calcule el número de eventos y sus tiempos de arribo en las primeras $T$ unidades de tiempo en u proceso de Poisson homogéneo con parámetro $\lambda$.

<u>Solución:</u>

Un proceso de Poisson homogéneo de tasa $\lambda$ tiene tiempos entre arribos i.i.d. $\text{Exp}(\lambda)$. Algoritmo:
```
t = 0, eventos = []
mientras t < T:
    generar U ~ U(0,1)
    t += -ln(U)/λ
    si t ≤ T: agregar t a eventos
retornar eventos
```
Ver `ej12.py`. Ejemplo con $\lambda=5$, $T=1$: $N=7$ eventos en $[0,1]$ (esperado $\lambda T = 5$).
<div style="page-break-after: always;"></div>

## <u>Ejercicio 13</u> ([[#^indice|Índice]])
^ejercicio13

<u>Enunciado:</u> Los autobuses que llevan los aficionados a un encuentro deportivo llegan a destino de acuerdo con un proceso de Poisson a razón de cinco por hora. La capacidad de los autobuses es una variable aleatoria que toma valores en el conjunto: $\set{20,21,...,40}$ con igual probabilidad. A su vez, las capacidad de dos autobuses distintos son variables independientes. Escriba un algoritmo para simular la llegada de aficionados al encuentro en el instante $t=1$ hora.

<u>Solución:</u>

El número de autobuses que llegan en $[0,1]$ es $N \sim \text{Pois}(5)$. Cada bus tiene capacidad $\sim \mathcal{U}\{20,\dots,40\}$ (media 30). El total de aficionados es la suma de las capacidades de los $N$ autobuses.

Algoritmo: generar tiempos de arribo Poisson($\lambda=5$) hasta superar $t=1$ hora. Para cada bus, sumar capacidad $\sim \mathcal{U}\{20,40\}$.

Ver `ej13.py`. Con $10.000$ simulaciones: promedio $\approx 150.5$ aficionados (teórico: $5 \cdot 30 = 150$).
<div style="page-break-after: always;"></div>

## <u>Ejercicio 14</u> ([[#^indice|Índice]])
^ejercicio14

<u>Enunciado:</u>
- a) Escriba un programa que utilice el algoritmo de adelgazamiento para generar el numero de eventos y las primeras unidades de tiempo de un proceso de Poisson no homogéneo con función de intensidad
	1. $$\lambda(t) = 3 + \frac{4}{t+1}, \quad 0\le t\le 3$$
	2. $$\lambda(t) = (t-2)^2 - 5t + 17, \quad 0\le t\le 5$$
	3. $$\lambda(t) = \begin{cases} \frac{t}{2} - 1& \text{si }2\le x\le 3 \\ 1 - \frac{t}{6}&\text{si }3\le x\le 6 \\ 0&\text{en otro caso} \end{cases}$$
	
	en los intervalos indicados.
- b) Indique una forma de mejorar el algoritmo de adelgazamiento para estos ejemplos usando al menos 3 intervalos.

<u>Solución:</u>

- **a)** Algoritmo de adelgazamiento (thinning):
  1. Hallar $\lambda_{\max} \ge \sup_{t\in[0,T]} \lambda(t)$.
  2. Generar tiempos de un Poisson homogéneo con tasa $\lambda_{\max}$.
  3. Aceptar cada tiempo $t$ con probabilidad $\lambda(t)/\lambda_{\max}$.

  Ver `ej14.py`.

  | $\lambda(t)$ | $T$ | $\lambda_{\max}$ | Eventos típicos |
  |---|---|---|---|
  | $3 + 4/(t+1)$ | 3 | 7 | 10-20 |
  | $(t-2)^2-5t+17$ | 5 | 17 | 30-50 |
  | Por tramos | 6 | 0.5 | 1-3 |

- **b)** Mejora: dividir $[0,T]$ en subintervalos con cotas más ajustadas, reduciendo el rechazo.
  - Para $\lambda_1$ en $[0,3]$: $[0,1]$ (max 7), $[1,2]$ (max 5), $[2,3]$ (max 4.33).
  - Para $\lambda_2$ en $[0,5]$: $[0,2]$ (max 17), $[2,3.5]$ (min región, max 10.75), $[3.5,5]$ (max 14.75).
  - Para $\lambda_3$ ya está por tramos con cota $0.5$, no requiere mejora.
