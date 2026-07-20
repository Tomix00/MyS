Técnicas de validación estadística
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
9. [[#^ejercicio9|Ejercicio 9 - Resuelto-agente]]
10. [[#^ejercicio10|Ejercicio 10 - Resuelto-agente]]

---
<div style="page-break-after: always;"></div>

Bibliografía de uso:
[SciPy libary](https://relopezbriega.github.io/blog/2016/06/29/distribuciones-de-probabilidad-con-python/)

No utilice implementaciones personales de densidades a menos que el ejercicio se lo pida exactamente.

Convención general: al obtener valores decimales suponemos una distribución continua

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 1</u> ([[#^indice|Índice]])
^ejercicio1

<u>Enunciado:</u> De acuerdo con la teoría genética de Mendel, cierta planta de guisantes debe producir flores blancas, rosas o rojas con probabilidad $1/4, 1/2$ y $1/4$ respectivamente. Para verificar experimentalmente la teoría, se estudió una muestra de $564$ guisantes, donde se encontró que $141$ produjeron flores blancas, $291$ flores rosas y $132$ flores rojas. Aproximar el $p-$valor de esta muestra:
- a) utilizando la prueba de Pearson con aproximación chi-cuadrada,
- b) realizando una simulación.

<u>Solución:</u>

**a)** Prueba de Pearson: $\chi^2 = \sum (O_i - E_i)^2 / E_i = 0.8617$,  = P(\chi^2_2 > 0.8617) \approx 0.650$ (las diferencias no son significativas).

**b)** Simulación:  \approx 0.652$. Ver ej1.py en simulaciones_Pr7\.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 2</u> ([[#^indice|Índice]])
^ejercicio2

<u>Enunciado:</u> Para verificar que cierto dado no estaba trucado, se registraron $1000$ lanzamientos, resultando que el número de veces que el dado arrojó el valor $i$ ($i = 1,2,3,4,5,6$) fue, respectivamente, $158, 172, 164, 181, 160, 165$. Aproximar el $p-$valor de la prueba: "el dado es honesto"
- a) utilizando la prueba de Pearson con aproximación chi-cuadrada,
- b) realizando una simulación.

<u>Solución:</u>

**a)** $\chi^2 = 2.18$,  = P(\chi^2_5 > 2.18) \approx 0.824$ (el dado parece honesto).

**b)** Simulación:  \approx 0.824$. Ver ej2.py.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 3</u> ([[#^indice|Índice]])
^ejercicio3

<u>Enunciado:</u> Calcular una aproximación del $p-$valor de la hipótesis: "Los siguientes $10$ números son aleatorios": $$0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74$$

<u>Solución:</u>

Prueba de rachas (runs test). =10$, rachas observadas $=4$,  \approx 0.331$ (simulación). No hay evidencia suficiente para rechazar aleatoriedad. Ver ej3.py.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 4</u> ([[#^indice|Índice]])
^ejercicio4

<u>Enunciado:</u> Calcular una aproximación del $p-$valor de la hipótesis: "Los siguientes $13$ valores provienen de una distribución exponencial con media $50.0$": $$86.0, 133.0, 75.0, 22.0, 11.0, 144.0, 78.0, 122.0, 8.0, 146.0, 33.0, 41.0, 99.0$$

<u>Solución:</u>

Test KS:  = 0.392$,  = 0.026$. Con $\alpha=0.05$ se rechaza que los datos provengan de Exp(media 50). Ver ej4.py.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 5</u> ([[#^indice|Índice]])
^ejercicio5

<u>Enunciado:</u> Calcular un aproximación del $p-$valor de la prueba de que los siguientes datos corresponden a una distribución binomial con parámetros ($n = 8, p$), donde $p$ no se conoce: $$6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7$$

<u>Solución:</u>

Se estima  = \bar{x}/n = 0.618$. Test $\chi^2$ agrupando categorías: $\chi^2=23.46$,  \approx 0.0003$. Se rechaza la hipótesis binomial. Ver ej5.py.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 6</u> ([[#^indice|Índice]])
^ejercicio6

<u>Enunciado:</u> Un escribano debe validar un juego en cierto programa de televisión. El mismo consiste en hacer girar una rueda y obtener un premio según el sector de la rueda que coincida con una aguja. Hay $10$ premios posibles, y las áreas de la rueda ara los distintos premios, numerados del $1$ al $10$, son respectivamente: $$31\%, 22\%, 12\%, 10\%, 8\%, 6\%, 4\%, 4\%, 2\%, 1\%.$$
Los premios con número alto (e.j. un auto $0Km$) son mejores que los premios con número bajo (e.j. $2x1$ para entradas en el cine). El escribano hace girar la rueda hasta que se cansa, y anota cuántas veces sale cada sector. Los resultados, para los premios del $1$ al $10$, respectivamente, son: $$188, 138, 87, 65, 48, 32, 30, 34, 13, 2$$
- a) Construya una tabla con los datos disponibles
- b) Diseñe una prueba de hipótesis para determinar si la rueda es justa
- c) Defina el $p-$valor a partir de la hipótesis nula
- d) Calcule el $p-$valor bajo la hipótesis de que la rueda es justa, usando la aproximación chi cuadrado
- e) Calcule el $p-$valor bajo la hipótesis de que la rueda es justa, usando una simulación.

<u>Solución:</u>

**a-d)** $\chi^2 = 9.81$,  \approx 0.366$ (no se rechaza que la rueda sea justa).

**e)** Simulación:  \approx 0.369$. Ver ej6.py.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 7</u> ([[#^indice|Índice]])
^ejercicio7

<u>Enunciado:</u> Generar los valores correspondientes a $30$ variables aleatorias exponenciales independientes, cada una con media $1$. Luego, en base al estadístico de prueba de Kolmogórov-Smirnov, aproxime el $p-$valor de la prueba de que los datos realmente provienen de una distribución exponencial con media $1$.

<u>Solución:</u>

Generar 30 valores Exp(1), test KS:  = 0.167$,  \approx 0.333$. No se rechaza la hipótesis exponencial. Ver ej7.py.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 8</u> ([[#^indice|Índice]])
^ejercicio8

<u>Enunciado:</u> Se sortean elementos de un conjunto de datos que tiene una distribución $t-$Student de $11$ grados de libertad. El investigador, que no conoce la forma verdadera de la distribución, asume que la misma es normal.
Analice la validez de esta suposición para muestras de tamaños $10,20,100$ y $1000$ elementos, para ello realice simulaciones numéricas e implemente el test de Kolmogórov-Smirnov a los datos simulados, asumiendo una distribución $N(0,1)$. Presente los resultados en una tabla que contenga el número de elementos de la simulación, el valor del estadístico $D$ y el $p-$valor.

**Ayuda**: Función de probabilidad normal: Para obtener la función de probabilidad normal, se puede usar la función ```math.erf```. Por ejemplo, la cantidad ```math.erf(x/math-sqrt(2.))/2. +0.5 ``` equivale a $$\int_{-\infty}^{x} N(0,1)(t) dt$$

**Ayuda**: Generación de números aleatorios con una distribución t-Student: Utilice el siguiente código para generar números aleatorios que siguen una distribución t-Student: 
```python
import math
import random

def rt(df): # df grados de libertad
	x = random.gauss(0.0, 1.0)
	y = 2.0*random.gammavariate(0.5*df, 2.0)
	return x / (math.sqrt(y/df))
```

<u>Solución:</u>

Para =10,20,100$ el KS no detecta diferencias significativas (>0.05$). Para =1000$,  \approx 0.000$ (detecta la diferencia). La prueba tiene baja potencia con muestras chicas. Ver ej8.py.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 9</u> ([[#^indice|Índice]])
^ejercicio9

<u>Enunciado:</u> En un estudio de vibraciones, una muestra aleatoria de $15$ componentes del avión fueron sometidos a fuertes vibraciones hasta que se evidenciaron fallas estructurales. Los datos proporcionados son los minutos transcurridos hasta que se evidenciaron dichas fallas. $$1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7$$

Pruebe la hipótesis nula de que estas observaciones pueden ser consideradas como una muestra de la distribución exponencial.

<u>Solución:</u>

Media estimada $\bar{x} = 10.73$. Test KS:  = 0.270$,  \approx 0.188$. No se rechaza la distribución exponencial. Ver ej9.py.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 10</u> ([[#^indice|Índice]])
^ejercicio10

<u>Enunciado:</u> Decidir si los siguientes datos corresponden a una distribución Normal: $$91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7$$

Calcular una aproximación del $p-$valor.

<u>Solución:</u>

KS: =0.196$, =0.675$. Shapiro-Wilk: =0.923$, =0.313$. No se rechaza normalidad. Ver ej10.py.
<div style="page-break-after: always;"></div>