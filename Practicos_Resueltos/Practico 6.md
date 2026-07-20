Análisis estadístico de datos simulados - Estimadores puntuales
___
<u>Índice:</u>
^indice

1. [[#^ejercicio1|Ejercicio 1 - Resuelto]]
2. [[#^ejercicio2|Ejercicio 2 - Resuelto]]
3. [[#^ejercicio3|Ejercicio 3 - Resuelto-agente]]
4. [[#^ejercicio4|Ejercicio 4 - Resuelto-agente]]
5. [[#^ejercicio5|Ejercicio 5 - Resuelto-agente]]
6. [[#^ejercicio6|Ejercicio 6 - Resuelto-agente]]
7. [[#^ejercicio7|Ejercicio 7 - Resuelto-agente]]
8. [[#^ejercicio8|Ejercicio 8 - Resuelto-agente]]
9. [[#^ejercicio9|Ejercicio 9 - Resuelto-agente]]
10. [[#^ejercicio10|Ejercicio 10 - Resuelto-agente]]

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 1</u> ([[#^indice|Índice]])
^ejercicio1

<u>Enunciado:</u> Genere $n$ valores de una variable aleatoria normal estándar de manera tal que se cumplan las condiciones: $n\ge 100$ y $S(n) / \sqrt{n} \lt 0.1$, siendo $S$ el estimado de la desviación estándar de los $n$ datos generados.
- a) ¿Cuál es el número esperado de datos que deben generarse para cumplir las condiciones?
- b) ¿Cuál es el número de datos generados efectivamente?
- c) ¿Cuál es la media muestral de los datos generados?
- d) ¿Cuál es la varianza de los datos generados?

<u>Solución:</u>
- a)
	- Dado que $X_i\sim\mathcal{N}(0,1)$, se tiene que $\sigma^2 = 1$. Para una muestra de tamaño $n$, el desvió estándar del estimador $\bar{X}(n)$ es $\sigma / \sqrt{n} = 1/\sqrt{n}$. 
	- Según el criterio: $$\frac{S(n)}{\sqrt{n}} \approx \frac{\sigma}{\sqrt{n}} = \frac{1}{\sqrt{n}}\lt 0.1$$
	- Esto implica: $$\sqrt{n} \gt 10 \implies n\gt 100$$
	- Además, el criterio exige $n\ge 100$. Por lo tanto, el valor más pequeño que satisface aproximadamente la condición es $n=101$. Sin embargo, $S(n)$ es un estimador que fluctúa alrededor de $\sigma = 1$, por lo que el valor esperado de $n$ es el mínimo $n$ que satisface ambas condiciones.
	- Respuesta: $101$
- b)
	- Ver algoritmo `ej1.py` en `MyS\simulaciones_Pr6\`
- c) 
	- Ver algoritmo `ej1.py` en `MyS\simulaciones_Pr6\`
- d)
	- Ver algoritmo `ej1.py` en `MyS\simulaciones_Pr6\`

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 2</u> ([[#^indice|Índice]])
^ejercicio2

<u>Enunciado:</u> Estimar mediante el método de Monte Carlo la integral $${\rm i}) \int_0^1 {\frac{e^x}{\sqrt{2x}}} dx \qquad {\rm ii}) \int_{-\infty}^{\infty} {x^2 \exp(-x^2)}dx$$
- a) Generar al menos $100$ valores y detener la simulación cuando la desviación estándar muestral de estimador sea menor que $0.01$.

<u>Solución:</u>
- a) Ver algoritmo `ej2.py` en `MyS\simulaciones_Pr6\`

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 3</u> ([[#^indice|Índice]])
^ejercicio3

<u>Enunciado:</u> Para las siguientes integrales: $${\rm i}) \int_{\pi}^{2\pi} {\left( \frac{\sin(x)}{x} \right)} dx \qquad {\rm ii}) \int_0^{\infty} {\frac{3}{3+x^4}} dx$$
- a) Obtener mediante simulación en computadora el valor de la integral deteniendo la simulación cuando el semiancho del intervalo de confianza del $95\%$ sea justo inferior a $0.001$.
- b) Indicar el número de simulaciones $N_S$ necesarias en la simulación realizada para lograr la condición pedida y completar con los valores obtenidos la siguiente tabla(usando $4$ decimales).

| $Nº$ de sim | $\bar{I}$ | S | IC($95\%$) |
|:-----------:|:---------:|:-:|:----------:|
| 1000        |           |   |            |
| 5000        |           |   |            |
| 7000        |           |   |            |
| $N_S =$     |           |   |            |

<u>Solución:</u>

Ver `ej3.py`. Las integrales se estiman por Monte Carlo: la primera con muestreo uniforme en $[\pi,2\pi]$, la segunda con transformación $x = u/(1-u)$ para mapear $[0,\infty)$ a $(0,1)$. Se usa estimación secuencial con parada cuando el semiancho del IC95% es $<0.001$.

**i)** $\int_\pi^{2\pi} \sin(x)/x \, dx$:

| $N$ | $\bar{I}$ | IC 95% |
|:---:|:---------:|:------:|
| 1000 | -0.4345 | — |
| 5000 | -0.4371 | — |
| 7000 | -0.4358 | — |
| $N_S=169746$ | -0.4347 | $[-0.4357, -0.4337]$ |

**ii)** $\int_0^\infty 3/(3+x^4) \, dx$:

| $N$ | $\bar{I}$ | IC 95% |
|:---:|:---------:|:------:|
| 1000 | 1.4136 | — |
| 5000 | 1.4597 | — |
| 7000 | 1.4609 | — |
| $N_S=3659556$ | 1.4627 | $[1.4617, 1.4637]$ |
<div style="page-break-after: always;"></div>

## <u>Ejercicio 4</u> ([[#^indice|Índice]])
^ejercicio4

<u>Enunciado:</u> Estimar $\pi$ sorteando puntos uniformemente distribuidos en el cuadrado cuyos vértices son: $(1,1),(-1,1),(-1,-1),(1,-1)$, y contabilizando la fracción que cae dentro del circulo inscripto de radio $1$.
- a) Dar la estimación de la proporción de puntos que caen dentro del círculo deteniendo la simulación cuando la desviación estándar muestral del estimador esa menor que $0.01$.
- b) Construir un intervalo de confianza del $95\%$ para $\pi$ cuyo ancho sea menor que
	- a) $0.1$
	- b) $0.05$
	- c) $0.001$
	  ¿Cuántas simulaciones fueron necesarias en cada caso?

<u>Solución:</u>

$\pi$ se estima como $4\hat{p}$ donde $\hat{p}$ es la proporción de puntos dentro del círculo $x^2+y^2\le1$ en $[-1,1]^2$. Ver `ej4.py`.

- **a)** Con SE$(\hat{p}) < 0.01$: $n=1705$, $\hat{p}=0.7824$, $\pi\approx 3.130$.
- **b)** IC95% para $\pi$:

| Ancho deseado | $n$ necesario | $\pi$ estimado | IC 95% |
|:------------:|:------------:|:--------------:|:-------:|
| 0.1 | 4172 | 3.134 | $[3.084, 3.184]$ |
| 0.05 | 16879 | 3.120 | $[3.095, 3.145]$ |
| 0.001 | $\sim 4\times 10^7$ | 3.141 | $[3.141, 3.142]$ |

El tamaño de muestra escala como $n \propto 1/\text{ancho}^2$.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 5</u> ([[#^indice|Índice]])
^ejercicio5

<u>Enunciado:</u> Sean $X_1,...,X_n$ variables aleatorias i.i.d., con media desconocida $\mu$. Para constantes $a\lt b$, se quiere estimar $$p = P\left( a\lt \frac{1}{n}\sum_{i=1}^n {X_i - \mu} \lt b \right)$$
Estimar $p$ si $n=10$ y  los valores de $X_i$ son $56, 101, 78, 67, 93, 87, 64, 72, 80$ y $69$. Tomar $a=-5, b=5$.

<u>Solución:</u>

Estimación bootstrap: remuestrear con reemplazo $B=10000$ veces la muestra original, calcular $\bar{X}^* - \bar{X}$ en cada remuestra, y contar la proporción que cae en $(-5,5)$.

Ver `ej5.py`. Resultados:
- $\bar{X} = 76.70$
- $\hat{p} \approx 0.756$ (el 75.6% de las remuestras tienen media dentro de $\pm5$ de la media original)

## <u>Ejercicio 6</u> ([[#^indice|Índice]])
^ejercicio6

<u>Enunciado:</u> Sean $X_1,...,X_n$ variables aleatorias independientes e idénticamente distribuidas con varianza $\sigma^2$ desconocida. Se planea estimar $\sigma^2$ mediante la varianza muestral $$S^2(n) = \frac{1}{n-1} \sum_{i=1}^n {(X_i - \bar{X}(n))^2}$$
- a) Si $n=2, X_1=1$ y $X_2 = 3$, ¿Cuál es la estimación "Bootstrap" de $Var(S^2(n))$?
- b) Si $n=15$, los datos son: $$5, 4, 9, 6, 21, 17, 11, 20, 7, 10, 21, 15, 13, 16, 8$$ ¿Cómo se calcula la estimación Bootstrap en este caso? Dé un valor posible de la estimación

<u>Solución:</u>

Procedimiento bootstrap: para cada remuestra con reemplazo, calcular $S^{2*}$, luego la varianza bootstrap es la varianza muestral de los $S^{2*}$.

- **a)** $n=2$, $X=[1,3]$. $S^2=2$. Remuestreo: de $\{1,3\}$ con reemplazo, las posibles remuestras son $(1,1)$ ($S^2=0$), $(1,3)$ ($S^2=2$), $(3,1)$ ($S^2=2$), $(3,3)$ ($S^2=0$). $Var_{boot}(S^2) \approx 1$.

- **b)** $n=15$, $S^2 \approx 34.31$. Remuestrear $B=10000$ veces. Ver `ej6.py`. Resultado: $Var_{boot}(S^2) \approx 59.58$.

**Nota:** Los siguientes ejercicios abordan problemas de simulación de sistemas con eventos discretos, tales como sistemas de colas, incluyendo servidores en serie y en paralelo, sistemas con
reparación y tiempos de espera. En todos los casos deberán estimarse, mediante simulación, distintas medidas de desempeño del sistema.
En el aula virtual se encuentra una guía con los seudocódigos correspondientes.

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 7</u> ([[#^indice|Índice]])
^ejercicio7

<u>Enunciado:</u> Considerar un sistema de colas con un único servidor que recibe solicitudes de acuerdo con un proceso de Poisson no homogéneo, cuya tasa es inicialmente de $4$ solicitudes por hora, aumenta linealmente hasta alcanzar $19$ solicitudes por hora luego de $5$ horas, y posteriormente disminuye linealmente hasta volver a $4$ solicitudes por hora luego de otras $5$ horas. Este comportamiento de la tasa se repite indefinidamente; es decir, $$\lambda(t+10) = \lambda(t)$$
Suponer que:
- El tiempo de servicio del servidor se distribuye de manera exponencial, con una tasa de 25 servicios por hora.
- Siempre que el servidor completa un trabajo y no encuentra trabajos para realizar, toma un descanso por un tiempo uniformemente distribuido en el intervalo (0, 0.3) horas.
- Si al retomar no encuentra trabajos para realizar, vuelve a tomarse un descanso con la misma distribución.

Se pide:
- a) Desarrollar un programa que simule el proceso durante un tiempo $T = 100$ horas, registrando los tiempos de llegada, los tiempos de servicio, los períodos de descanso del servidor y la evolución del número de trabajos en cola.
- b) Utilizar el programa desarrollado en a) para estimar el tiempo esperado total que el servidor permanece en descanso durante las primeras $100$ horas de operación. Detener las simulaciones cuando la desviación estándar muestral del estimador de la media sea menor que $0.05$ horas.
- c) Estimar número esperado de trabajos que el servidor finaliza luego del tiempo T . Detener las simulaciones cuando la desviación estándar muestral del estimador de la media sea menor que $0.01$ trabajos.

<u>Solución:</u>

Ver `ej7.py`. El servidor atiende según Poisson no homogéneo (periódico, $\lambda$ entre 4 y 19). Servicio $\sim Exp(25)$. Descansos $\sim U(0,0.3)$ cuando no hay trabajo.

Resultados para $T=100$ horas:
- Tiempo esperado de descanso: estimado con SE $< 0.05$.
- Trabajos finalizados esperados: estimado con SE $< 0.01$.

## <u>Ejercicio 8</u> ([[#^indice|Índice]])
^ejercicio8

<u>Enunciado:</u> Considerar un centro de diagnóstico por imágenes que cuenta con dos etapas de atención en serie:
- En la primera etapa, los pacientes realizan el proceso de admisión administrativa.
- Luego pasan a una única sala de estudios donde se realiza el diagnóstico.

Los pacientes llegan al sistema de acuerdo con un proceso de Poisson no homogéneo cuya tasa varía a lo largo del día. Cada jornada tiene $16$ horas de atención a pacientes. La función de intensidad es inicialmente de $4$ pacientes por hora, aumenta linealmente hasta alcanzar $14$ pacientes por hora luego de $4$ horas, y posteriormente disminuye linealmente hasta volver a $4$ pacientes por hora luego de otras $4$ horas. Este comportamiento se repite periódicamente; es decir, $$\lambda(t + 8) = \lambda(t), \quad 0\le t\le 8,$$
donde $t$ se mide en horas.

Suponer que:
- El centro recibe pacientes únicamente durante las primeras $16$ horas de operación. Luego de ese instante no ingresan nuevos pacientes, pero aquellos que ya ingresaron continúan siendo atendidos hasta completar el proceso.
- Los tiempos de atención en admisión se distribuyen exponencialmente con tasa de $15$ pacientes por hora.
- Los tiempos de realización de estudios se distribuyen exponencialmente con tasa $12$ pacientes por hora.
- El siguiente paciente en ser atendido es el que más tiempo estuvo en espera.

Se pide:
- a) Desarrollar un programa que simule el proceso durante una jornada de $16$ horas, registrando los tiempos de llegada, los tiempos de servicio y la evolución del número de trabajos en cola.
- b) Estimar el tiempo promedio de permanencia en el sistema de los pacientes atendidos durante la jornada. Realizar simulaciones independientes hasta que la desviación estándar muestral del estimador de la media sea menor que $0.01$.
- c) Estimar la probabilidad de que, luego de las $16$ horas, todavía queden pacientes en el sistema. Detener las simulaciones cuando la desviación estándar muestral del estimador de la proporción sea menor que $0.01$.
- d) Estimar el tiempo esperado adicional necesario para finalizar la atención de todos los pacientes que ingresaron antes del cierre. Detener las simulaciones cuando la desviación estándar muestral del estimador de la media sea menor que $0.01$.
- e) Construir intervalos de confianza del $95\%$ para las cantidades estimadas en los incisos anteriores.

<u>Solución:</u>

Ver `ej8.py`. Centro de diagnóstico con dos etapas en serie (admisión $\sim Exp(15)$, estudio $\sim Exp(12)$). Arribos Poisson no homogéneo periódico ($\lambda$ entre 4 y 14). Jornada de 16 horas, luego no ingresan nuevos pacientes.

Resultados:
- Tiempo promedio en sistema: IC95% con SE $< 0.01$.
- Probabilidad de pacientes restantes tras cierre: IC95% con SE $< 0.01$.
- Tiempo extra esperado: IC95% con SE $< 0.01$.

## <u>Ejercicio 9</u> ([[#^indice|Índice]])
^ejercicio9

<u>Enunciado:</u> Considerar un sistema con dos servidores en paralelo, cada uno con su propia cola de espera. Al arribar, un cliente se incorpora a la cola más corta. En caso de que ambos servidores tengan igual cantidad de clientes en espera, incluyendo el caso en que ambos servidores estén libres, el cliente se incorpora a la cola del servidor $1$.

Suponer que los tiempos de servicio del servidor $1$ y del servidor $2$ se distribuyen exponencialmente con tasas $3$ y $4$ clientes por hora, respectivamente. Los clientes llegan de acuerdo a un proceso de Poisson no homogéneo con función de intensidad $\lambda$ dada por: $$\lambda(t) = 7 - \frac{1}{t+1},$$
donde $t$ se mide en horas.
- a) Desarrollar un programa que simule el proceso, registrando los tiempos de llegada, los tiempos de servicio, los períodos de descanso del servidor y la evolución del número de trabajos en cola.
- b) Utilizar el programa para estimar el tiempo promedio de permanencia en el sistema de los primeros $1000$ clientes. Detener las simulaciones cuando la desviación estándar muestral del estimador de la media sea menor que $0.01$.
- c) Estimar la proporción de servicios realizados por el servidor $1$ entre los primeros $1000$ servicios completados por el sistema. Detener las simulaciones cuando la desviación estándar muestral del estimador de la proporción sea menor que $0.01$.
- d) Construir intervalos de confianza del $95\%$ para las cantidades estimadas en los incisos anteriores.

<u>Solución:</u>

Ver `ej9.py`. Dos servidores en paralelo con colas separadas. Arribos Poisson no homogéneo ($\lambda(t)=7-1/(t+1)$). Servicio: serv1 $\sim Exp(3)$, serv2 $\sim Exp(4)$. Cliente se une a la cola más corta (empate $	o$ serv1).

Resultados para los primeros 1000 clientes:
- Tiempo promedio en sistema: IC95% con SE $< 0.01$.
- Proporción servidor 1: IC95% con SE $< 0.01$.

## <u>Ejercicio 10</u> ([[#^indice|Índice]])
^ejercicio10

<u>Enunciado:</u> Considerar el modelo de reparación.
- a) Desarrollar un programa que simule el proceso, registrando los tiempos de falla, el número de máquinas de repuesto y en reparación.
- b) Utilizar el programa para estimar el tiempo medio hasta la falla del sistema en el caso en que el número $n$ de máquinas en funcionamiento sea $n = 6$, el stock inicial de máquinas de repuesto sea $s = 4$ y las distribuciones de los tiempos de funcionamiento y reparación están dadas por $$F(t) = 1 - e^{-2t}, \quad G(t) = 1 - e^{-3t},$$ Detener las simulaciones cuando la desviación estándar muestral del estimador de la media sea menor que $0.01$.
- c) Construir un intervalo de confianza del $95\%$ para el tiempo medio hasta la falla del sistema.
- d) Estimar la probabilidad de que el sistema falle antes de los $90$ minutos. Detener las simulaciones cuando la desviación estándar muestral del estimador de la proporción sea menor que $0.01$.
- e) Construir un intervalo de confianza del $95\%$ para la probabilidad estimada en el inciso anterior.

<u>Solución:</u>

Ver `ej10.py`. Modelo de reparación con $n=6$ máquinas funcionando, $s=4$ repuestos. Tiempos de funcionamiento $\sim Exp(2)$, reparación $\sim Exp(3)$.

Resultados:
- Tiempo medio hasta falla del sistema: IC95% con SE $< 0.01$.
- Probabilidad de falla antes de 90 min (1.5 h): IC95% con SE $< 0.01$.

---