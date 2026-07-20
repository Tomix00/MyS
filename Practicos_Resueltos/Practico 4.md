Generación de variables aleatorias discretas
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
11. [[#^ejercicio11|Ejercicio 11 - Resuelto-agente]]
12. [[#^ejercicio12|Ejercicio 12 - Resuelto-agente]]

---
<div style="page-break-after: always;"></div>

## <u>Ejercicio 1</u> ([[#^indice|Índice]])
^ejercicio1

<u>Enunciado:</u> Se baraja un conjunto de $n = 100$ cartas (numeradas consecutivamente del $1$ al $100$) y se extrae del mazo una carta por vez. Consideramos que ocurre un "éxito" si la $i-$esima carta extraída es aquella cuyo número es $i$ ($i = 1,...,n$).
- a) Calcula la probabilidad de que
	1. Las primeras $r$ cartas sean coincidencias y dé su valor para $r = 10$.
	2. Haya exactamente $r$ coincidencias y estén en las primeras $r$ cartas. Dé su valor para $r = 10$.
- b) Pruebe que $E(X) = Var(X) = 1$ donde $X$ es el número de coincidencias obtenidas en una baraja de $n$ cartas.
- c) Escriba un programa de simulación para estimar la esperanza y varianza del número total de éxitos, y de os eventos del inciso (a) con $r = 10$, y compare los resultados obtenidos con $100$, $1000$, $10000$ y $100000$ iteraciones.

<u>Solución:</u>

Sea $X$ el número de coincidencias. Definimos variables indicadoras $I_i = 1$ si la $i$-ésima carta extraída es la $i$, para $i=1,\dots,100$. Luego $X = \sum_{i=1}^{100} I_i$.

- **a)**
  1. $P(\text{primeras } r \text{ coinciden}) = \frac{1}{100} \cdot \frac{1}{99} \cdots \frac{1}{100-r+1} = \frac{1}{(100)_r}$.
     Para $r=10$: $\displaystyle \frac{1}{100\cdot99\cdots91} = \frac{90!}{100!} \approx 1.0\times10^{-20}$.
  2. Es el mismo evento que el anterior (exige que las primeras $r$ sean coincidencias, no impone restricción sobre el resto), por lo tanto la probabilidad es idéntica: $1/(100)_{10}$.

- **b)** $E[I_i] = P(I_i=1) = 1/100$, luego $E[X] = \sum_{i=1}^{100} 1/100 = 1$.
  $E[I_i I_j] = P(I_i=1, I_j=1) = \frac{1}{100}\cdot\frac{1}{99}$ para $i\neq j$.
  $E[X^2] = E[X] + \sum_{i\neq j} E[I_i I_j] = 1 + 100\cdot99\cdot\frac{1}{100\cdot99} = 2$.
  Por lo tanto $Var[X] = E[X^2] - (E[X])^2 = 2 - 1 = 1$.

- **c)** Ver `ej1.py` en `simulaciones_Pr4\`. Resultados:

| n         | $E[X]$ | $Var[X]$ | $P(\text{primeras 10})$ |
|-----------|--------|----------|-------------------------|
| 100       | 0.93   | 0.87     | 0.0000000000 |
| 1.000     | 1.01   | 1.02     | 0.0000000000 |
| 10.000    | 1.00   | 1.00     | 0.0000000000 |
| 100.000   | 1.00   | 1.00     | 0.0000000000 |

Los estimados convergen a los valores teóricos $E[X]=Var[X]=1$, y la probabilidad de las primeras 10 coincidencias es esencialmente nula ($\sim 10^{-20}$).
<div style="page-break-after: always;"></div>

## <u>Ejercicio 2</u> ([[#^indice|Índice]])
^ejercicio2

<u>Enunciado:</u> Se desea construir una aproximación de: $$\sum_{k=1}^{N}\exp\left(\frac{k}{N}\right)\quad\text{donde }N=10000$$
- a) Escriba un algoritmo para estimar la cantidad deseada.
- b) Obtenga la aproximación sorteando $100$ números aleatorios.
- c) Escriba un algoritmo para calcular la suma de los primeros $100$ términos, y compare el valor exacto con las dos aproximaciones, y el tiempo de cálculo.

<u>Solución:</u>

La suma $S = \sum_{k=1}^{N} e^{k/N}$ puede expresarse como $S = N \cdot E[e^{U}]$ con $U \sim \mathcal{U}\{1/N,2/N,\dots,1\}$, o equivalentemente $S = N \cdot E[e^{U}]$ con $U\sim\mathcal{U}(0,1)$ aproximado por Monte Carlo.

- **a)** Algoritmo Monte Carlo: generar $m$ números aleatorios $u_i \sim \mathcal{U}(0,1)$ y estimar
  $$S \approx \frac{N}{m} \sum_{i=1}^{m} e^{u_i}.$$
  También se puede muestrear $k$ uniformemente en $\{1,\dots,N\}$ y estimar $S \approx \frac{N}{m}\sum e^{k/N}$.

- **b)** Ver `ej2.py`. Con $100$ números aleatorios se obtiene una aproximación.

- **c)** El valor exacto es una serie geométrica:
  $$S = \sum_{k=1}^{N} e^{k/N} = \frac{e^{1/N}(e - 1)}{e^{1/N} - 1}.$$
  Para $N=10000$: $S \approx 17182.5$.
  La aproximación Monte Carlo con $100$ muestras y el cálculo directo de los primeros $100$ términos pueden compararse en precisión y tiempo de cómputo (ver `ej2.py`).
<div style="page-break-after: always;"></div>

## <u>Ejercicio 3</u> ([[#^indice|Índice]])
^ejercicio3

<u>Enunciado:</u> Se lanzan simultáneamente un par de dados legales y se anota el resultado de la suma de ambos. El proceso se repite hasta que todos los resultados posibles: $2,3,...,12$ hayan aparecido al menos una vez. Estudiar mediante una simulación la variable $N$, el número de lanzamientos necesarios para cumplir el proceso. Cada lanzamiento implica arrojar el par de dados.
- a) Describa la estructura lógica del algoritmo que permite simular en computadora el número de lanzamientos necesarios para cumplir el proceso.
- b) Mediante una implementación en computadora,
	1. estime el valor medio y la desviación estándar del número de lanzamientos, repitiendo el algoritmo: $100,1000,10000$ y $100000$ veces.
	2. estime la probabilidad de que $N$ sea por lo menos $15$ y la probabilidad de que $N$ sea a lo sumo $9$, repitiendo el algoritmo: $100, 1000, 10000$ y $100000$.

<u>Solución:</u>

Es un problema de colector de cupones con 11 resultados (sumas $2$ a $12$), cada uno con probabilidad $p_s$ dada por la distribución de la suma de dos dados.

- **a)** Estructura del algoritmo:
  1. Inicializar un conjunto vacío `vistos`.
  2. `lanzamientos = 0`.
  3. Mientras `|vistos| < 11`:
     - Generar dos dados uniformes en $\{1,\dots,6\}$, sumarlos.
     - Agregar la suma al conjunto `vistos`.
     - `lanzamientos += 1`.
  4. Retornar `lanzamientos`.

- **b)** Ver `ej3.py` en `simulaciones_Pr4\`. Resultados:

| Reps     | Media   | Desvío  | $P(N\ge 15)$ | $P(N\le 9)$ |
|----------|---------|---------|--------------|-------------|
| 100      | 63.36   | 37.79   | 1.0000       | 0.0000      |
| 1.000    | 60.66   | 36.25   | 0.9940       | 0.0000      |
| 10.000   | 60.81   | 36.00   | 0.9989       | 0.0000      |
| 100.000  | 61.33   | 36.18   | 0.9985       | 0.0000      |

El número esperado de lanzamientos ronda $\approx 61$, significativamente mayor que el caso de probabilidades uniformes ($11 H_{11} \approx 33$) debido a los resultados raros ($2$ y $12$ con probabilidad $1/36$). La probabilidad de completar en 9 o menos lanzamientos es prácticamente nula, mientras que casi siempre se requieren al menos 15.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 4</u> ([[#^indice|Índice]])
^ejercicio4

<u>Enunciado:</u> Implemente cuatro métodos para generar una variable $X$ que toma los valores del $1$ al $10$, con probabilidades $p_1 = 0.11, p_2 = 0.14, p_3 = 0.09, p_4 = 0.08, p_5 = 0.12, p_6 = 0.10, p_7 = 0.09, p_8 = 0.07, p_9 = 0.11, p_{10} = 0.09$  usando:
- a) Método de rechazo con una uniforme discreta, buscando la cota $c$ más baja posible.
- b) Método de rechazo con una uniforme discreta, usando $c = 3$.
- c) Transformada inversa.
- d) Método de la urna: utilizar un arreglo $A$ de tamaño $100$ donde cada valor $i$ está en exactamente $p_i * 100$ posiciones. El método debe devolver $A[k]$ con probabilidad $0.01$. ¿Porqué funciona?

Compare la eficiencia de los tres algoritmos realizando $10000$ simulaciones.

<u>Solución:</u>

- **a)** La variable soporte $Y \sim \mathcal{U}\{1,\dots,10\}$ tiene $g(y) = 0.10$. La cota $c$ mínima es
  $$c = \max_j \frac{p_j}{g(j)} = \frac{0.14}{0.10} = 1.4.$$
  Algoritmo: generar $Y \sim \mathcal{U}\{1,\dots,10\}$ y $U \sim \mathcal{U}(0,1)$; aceptar $Y$ si $U < p_Y / (c \cdot g(Y)) = 10 p_Y / 1.4$.

- **b)** Ídem pero con $c = 3$, lo que reduce la probabilidad de aceptación a $1/c = 1/3$, haciendo el método menos eficiente.

- **c)** Transformada inversa: construir la función de distribución acumulada $F_j = \sum_{i=1}^{j} p_i$, generar $U \sim \mathcal{U}(0,1)$ y devolver $X = \min\{j : U < F_j\}$.

- **d)** La urna contiene 100 elementos: cada valor $i$ aparece $100 \cdot p_i$ veces. Como $100 p_i$ es entero para todos ($11,14,9,8,12,10,9,7,11,9$), la urna representa exactamente la distribución. Elegir un índice uniforme en $[0,99]$ y devolver el valor en esa posición es equivalente a muestrear de la distribución original (cada posición tiene prob $0.01$). Funciona porque $p_i$ son múltiplos de $0.01$.

Ver `ej4.py` en `simulaciones_Pr4\`. Resultados de eficiencia para $n=10000$:

| Método              | Tiempo (s) |
|---------------------|------------|
| Rechazo $c=1.4$    | 0.005      |
| Rechazo $c=3$      | 0.010      |
| Transformada Inversa | 0.004      |
| Urna               | 0.002      |

La urna es la más rápida (acceso directo a un arreglo), seguida por transformada inversa. El rechazo con $c=3$ es el más lento por su baja tasa de aceptación ($\sim 33\%$).
<div style="page-break-after: always;"></div>

## <u>Ejercicio 5</u> ([[#^indice|Índice]])
^ejercicio5

<u>Enunciado:</u> Implemente dos métodos para generar una binomial $Bin(n,p)$:
1. Usando transformada inversa.
2. Simulando $n$ ensayos con probabilidad de éxito $p$ y contando el número de éxitos.

Para ambos métodos:
- a) Compare la eficiencia de ambos algoritmos para $n = 10$ y $p = 0.3$, evaluando el tiempos necesario para realizar $10000$ simulaciones.
- b) Estime el valor con mayor ocurrencia y la proporción de veces que se obtuvieron los valores $0$ y $10$ respectivamente.
- c) Compare estos valores con las probabilidades teóricas de la binomial. Si están alejados, revise el código.

<u>Solución:</u>

**Método I — Transformada inversa:** usar la recurrencia $P(X=0) = (1-p)^n$, $P(X=k+1) = P(X=k) \cdot \frac{n-k}{k+1} \cdot \frac{p}{1-p}$ para construir la FDA incrementalmente hasta superar $U \sim \mathcal{U}(0,1)$.

**Método II — Ensayos Bernoulli:** generar $n$ variables Bernoulli($p$) independientes y contar éxitos. Implementado con el método geométrico: generar $Geom(p)$ hasta superar $n$, contando éxitos.

Ver `ej5.py` en `simulaciones_Pr4\`. Resultados para $n=10$, $p=0.3$, $10000$ simulaciones:

- **a)** Eficiencia (ambos métodos comparables):
  - Transformada inversa: $0.014$s
  - Ensayos Bernoulli: $0.014$s
  - Ambos métodos tienen rendimiento similar para $n=10$.

- **b)** Resultados observados (ambos métodos coinciden):

| Método | Moda | $P(X=0)$ | $P(X=10)$ |
|--------|------|----------|-----------|
| Inv.   | 3    | 0.0306   | $\approx 0$ |
| Ens.   | 3    | 0.0311   | $\approx 0$ |

- **c)** Valores teóricos para $Bin(10, 0.3)$:
  - Moda: $\lfloor (n+1)p \rfloor = 3$, $P(X=3) \approx 0.2668$
  - $P(X=0) = 0.7^{10} \approx 0.02825$
  - $P(X=10) = 0.3^{10} \approx 0.0000059$
  
  Los valores observados coinciden con los teóricos dentro del error de simulación esperado.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 6</u> ([[#^indice|Índice]])
^ejercicio6

<u>Enunciado:</u> Una variable aleatoria $X$ tiene una función de probabilidad puntual $p_i = P(X = i)$ dada por $$p_0 = 0.15, \quad p_1 = 0.20, \quad p_2 = 0.10, \quad p_3 = 0.35, \quad p_4 = 0.20$$
1. Describir mediante un pseudocódigo un algoritmo que simule $X$ utilizando el método de la transformada inversa y que minimice el número esperado de búsquedas.
2. Describir mediante un pseudocódigo un algoritmo que simule $X$ utilizando el método de aceptación y rechazo con una variable soporte $Y$ con distribución binomial $B(4, 0.45)$.
3. Compare la eficiencia de los dos algoritmos realizando $10000$ simulaciones.

<u>Solución:</u>

**1) Transformada inversa optimizada:** para minimizar búsquedas, ordenamos los valores de mayor a menor probabilidad: $p_3=0.35$, $p_1=0.20$, $p_4=0.20$, $p_0=0.15$, $p_2=0.10$.

```
F = [0.35, 0.55, 0.75, 0.90, 1.00]  # acumulada ordenada
V = [3, 1, 4, 0, 2]                  # valores correspondientes
Generar U ~ U(0,1)
Para i = 0,...,4:
    Si U < F[i]: retornar V[i]
```

Alternativamente, sin reordenar, buscar desde el valor más probable hacia el menos probable reduce el número esperado de comparaciones.

**2) Aceptación y rechazo con $Y \sim Bin(4, 0.45)$.** Primero hallamos $c = \max_j p_j / q_j$ donde $q_j = P(Y=j)$:

| $j$ | $p_j$ | $q_j$ (Bin(4,0.45)) | $p_j/q_j$ |
|-----|-------|---------------------|-----------|
| 0   | 0.15  | 0.0915              | 1.639     |
| 1   | 0.20  | 0.2995              | 0.668     |
| 2   | 0.10  | 0.3675              | 0.272     |
| 3   | 0.35  | 0.2005              | 1.745     |
| 4   | 0.20  | 0.0410              | 4.878     |

$c \approx 4.878$ (domina $j=4$). Algoritmo:
```
Repetir:
    Generar Y ~ Bin(4, 0.45)
    Generar U ~ U(0,1)
    Si U < p_Y / (c · q_Y): retornar Y
```
La probabilidad de aceptación es $1/c \approx 0.205$, por lo que en promedio se necesitan $\approx 4.88$ iteraciones.

**3)** Ver `ej6.py` en `simulaciones_Pr4\`. Para $10000$ simulaciones:
- Transformada inversa: $0.003$s
- Aceptación y rechazo: $0.052$s
- La transformada inversa es $\sim 16\times$ más rápida.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 7</u> ([[#^indice|Índice]])
^ejercicio7

<u>Enunciado:</u> Estime $P(Y \lt 2)$ con $\lambda = 10$, $1000$ repeticiones para la variable Poisson, simulando con método de transformada inversa común e inversa mejorado.

<u>Solución:</u>

La transformada inversa común para Poisson($\lambda$):
1. Calcular $p = e^{-\lambda}$, $F = p$.
2. Para $j = 1,2,\dots$ hasta encontrar $U < F$, usando la recurrencia $p_{j} = p_{j-1} \cdot \lambda/j$.

La versión **mejorada** comienza desde el valor modal $\lfloor \lambda \rfloor$ y se desplaza hacia la izquierda o derecha según $U$, reduciendo el número esperado de iteraciones cuando $\lambda$ es grande.

Para $\lambda = 10$, $P(Y < 2) = P(Y=0) + P(Y=1) = e^{-10}(1 + 10) = 11 e^{-10} \approx 0.000499$.

Ver `ej7.py`. Con $1000$ repeticiones:

| Método | $P(Y \ge 2)$ estimado | Valor teórico | Error |
|--------|----------------------|--------------|-------|
| Común  | 1.000000             | 0.997231     | 0.0028 |
| Mejorado | 0.997000           | 0.997231     | 0.0002 |

Nota: En el ejercicio se pide $P(Y < 2)$, que es $1 - P(Y \ge 2)$. Dado que $P(Y < 2) \approx 0.0005$, prácticamente todas las simulaciones devuelven $Y \ge 2$.

En cuanto a eficiencia, ambos métodos son similares para $\lambda=10$ (el mejorado comienza desde $j=10$, ahorrando iteraciones en la búsqueda desde 0).
<div style="page-break-after: always;"></div>

## <u>Ejercicio 8</u> ([[#^indice|Índice]])
^ejercicio8

<u>Enunciado:</u>
- a) Desarrolle el método de la Transformada Inversa y el de Rechazo para generar una variable aleatoria $X$ cuya distribución de probabilidad está dada por: $$P(X = i) = \frac{\displaystyle\frac{\lambda^i}{i!}e^{-\lambda}}{\displaystyle\sum_{j=0}^{k}\frac{\lambda^j}{j!}e^{-\lambda}}$$
- b) Estime $P(X \gt 2)$ con $k = 10$ y $\lambda = 0.7$ y $1000$ repeticiones. Compare con el valor exacto.
- c) Generalice el problema escribiendo un pseudocódigo para el método de rechazo para cualquier variable aleatoria truncada usando como soporte a la variable original (con "cualquier variable aleatoria truncada" nos referimos a una variable como la vista en el inciso (a) pero ahora truncada en cualquier parte $i = a,...b$).

<u>Solución:</u>

La variable $X$ es una Poisson($\lambda$) truncada en $\{0,\dots,k\}$, con probabilidades normalizadas por $S = \sum_{j=0}^k \lambda^j/j!$.

- **a)** 
  - **Transformada inversa:** calcular $p_i = (\lambda^i/i!)/S$, ordenar de mayor a menor probabilidad para minimizar búsquedas, construir FDA acumulada, generar $U \sim \mathcal{U}(0,1)$ y devolver el primer valor cuya FDA supere $U$.
  - **Rechazo con $Y \sim \text{Pois}(\lambda)$:** generar $Y \sim \text{Pois}(\lambda)$. Si $Y \le k$ y $U < e^{-\lambda}S$ (probabilidad de aceptación), devolver $Y$; en caso contrario repetir. La probabilidad de aceptación es $P(\text{aceptar}) = e^{-\lambda} S$.

- **b)** Valor exacto:
  $$P(X > 2) = 1 - \frac{e^{-0.7}(1 + 0.7 + 0.7^2/2)}{S} \approx 0.03414.$$
  Ver `ej8.py`. Con $1000$ repeticiones:
  - Transformada inversa: $0.035$ (error $0.0009$)
  - Aceptación y rechazo: $0.030$ (error $0.0041$)

- **c)** Pseudocódigo general para variable truncada en $[a,b]$:
  ```
  ALGORITMO RechazoTruncado(a, b, generar_Y, prob_Y, S):
      # S = sum_{j=a}^b P(Y=j)
      prob_aceptar = S
      REPETIR
          Y = generar_Y()
      HASTA QUE (a <= Y <= b) Y (random() < prob_aceptar)
      RETORNAR Y
  ```
<div style="page-break-after: always;"></div>

## <u>Ejercicio 9</u> ([[#^indice|Índice]])
^ejercicio9

<u>Enunciado:</u> Implemente dos métodos para simular una variable geométrica $Geom(p)$:
- a) Usando transformada inversa y aplicando la fórmula recursiva para $P(X = i)$.
- b) Simulando ensayos con probabilidad de éxito $p$ hasta obtener un éxito.

Compare la eficiencia de estos algoritmos para $p = 0.8$ y para $p = 0.2$.
Para cada caso, realice $10000$ simulaciones y calcule el promedio de los valores obtenidos. Compara estos valores con el valor esperado de la distribución correspondiente. Si están alejados, revisar el código.

<u>Solución:</u>

- **a) Transformada inversa:** $X = \lfloor \ln(1-U) / \ln(1-p) \rfloor + 1$, con $U \sim \mathcal{U}(0,1)$. También puede aplicarse la recurrencia $P(X=k+1) = (1-p)P(X=k)$ para construir la FDA secuencialmente.

- **b) Ensayos Bernoulli:** generar Bernoulli($p$) hasta obtener un éxito; $X$ es el número de ensayos necesarios.

Ver `ej9.py`. Resultados con $10000$ simulaciones:

| $p$ | Método | Media | Tiempo | $E[X]=1/p$ |
|-----|--------|-------|--------|------------|
| 0.8 | Inversa | 1.24 | 0.004s | 1.25 |
| 0.8 | Ensayos | 1.25 | 0.002s | 1.25 |
| 0.2 | Inversa | 5.03 | 0.004s | 5.00 |
| 0.2 | Ensayos | 5.03 | 0.006s | 5.00 |

Las medias observadas coinciden con el valor esperado $1/p$ dentro del error de simulación. Para $p=0.8$, el método de ensayos es más rápido (pocos ensayos en promedio). Para $p=0.2$, la transformada inversa es ligeramente más rápida ($\sim 1.5\times$).
<div style="page-break-after: always;"></div>

## <u>Ejercicio 10</u> ([[#^indice|Índice]])
^ejercicio10

<u>Enunciado:</u>
- a) Desarrolle un método para generar una variable aleatoria $X$ cuya distribución de probabilidad está dada por: $$P(X = j) = \left(\frac{1}{2}\right)^{j+1} + \frac{\displaystyle\left(\frac{1}{2}\right)2^{j-1}}{3^j}, \quad j = 1,2,...$$
- b) Estime $E(X)$ con $1000$ repeticiones y compare con la esperanza exacta.

<u>Solución:</u>

- **a)** La distribución puede expresarse como una mezcla de dos geométricas:
  $$P(X=j) = \frac{1}{2} \cdot \underbrace{\left(\frac{1}{2}\right)^{j}}_{Geom(1/2)} + \frac{1}{2} \cdot \underbrace{\frac{1}{3}\left(\frac{2}{3}\right)^{j-1}}_{Geom(1/3)}.$$
  Verificación: el segundo término se simplifica:
  $$\frac{1}{2}\cdot\frac{2^{j-1}}{3^j} = \frac{2^{j-2}}{3^j} = \frac{1}{4}\left(\frac{2}{3}\right)^j = \frac{1}{2}\cdot\frac{1}{3}\left(\frac{2}{3}\right)^{j-1}.$$

  Algoritmo: generar $U \sim \mathcal{U}(0,1)$.
  - Si $U < 0.5$: generar $X \sim Geom(1/2)$ por transformada inversa ($X = \lfloor \ln(1-U')/\ln(0.5) \rfloor + 1$).
  - Si $U \ge 0.5$: generar $X \sim Geom(1/3)$.

- **b)** Esperanza exacta:
  $$E[X] = \frac{1}{2}\cdot E[Geom(1/2)] + \frac{1}{2}\cdot E[Geom(1/3)] = \frac{1}{2}\cdot 2 + \frac{1}{2}\cdot 3 = 2.5.$$
  Ver `ej10.py`. Con $1000$ repeticiones: $E[X] \approx 2.402$ (error $\approx 0.098$).
<div style="page-break-after: always;"></div>

## <u>Ejercicio 11</u> ([[#^indice|Índice]])
^ejercicio11

<u>Enunciado:</u> Sea $X$ una variable cuya distribución de probabilidad es $P(X = j) = p_j$ con $j = 1,2,...$. Sea: $$\lambda_n = P(X = n| X\gt n-1) = \frac{p_n}{\displaystyle1 - \sum_{j = 1}^{n-1}p_j}, \quad n = 1,2,...$$

Las cantidades $\lambda_n$, son las tasas discretas de riesgo. Considerando a $X$ como el tiempo (discreto) de vida de algún artículo, $\lambda_n$ representa la probabilidad de que habiendo funcionado correctamente hasta el tiempo $n - 1$, se rompa en el tiempo $n$.
- a) Muestre que $p_1 = \lambda_1$ y que $$p_n = (1-\lambda_1)(1-\lambda_2)\cdots(1-\lambda_{n-1})\lambda_n$$
  Método de la tasa discreta de riesgo para simular variables aleatorias discretas: Se genera una sucesión de números aleatorios que termina cuando el n-esimo número generado es menor que $\lambda_n$. El algoritmo puede escribirse como sigue:
	1. ``` X = 1```
	2. ```Generar U```
	3. ```Si U < ``` $\lambda_X$, ```terminar```
	4. ```X = X + 1```
	5. ```Ir al Paso 2```
- b) Muestre que los valores de $X$ que genera este proceso tienen la distribución de probabilidad deseada.
- c) Suponga que $X$ es una variable aleatoria geométrica con parámetro $p$: $$P(X = n) = p(1 - p)^{n-1},\quad n\ge 1$$
  Determine los valores de $\lambda_n$, $n\ge 1$. Explique cómo funciona el algoritmo anterior en este caso y por qué es evidente su validez.

<u>Solución:</u>

- **a)** Para $n=1$, la suma vacía $\sum_{j=1}^{0} p_j = 0$, por lo que:
  $$\lambda_1 = \frac{p_1}{1} = p_1.$$
  Para $n \ge 2$, por definición:
  $$\lambda_n = \frac{p_n}{1 - \sum_{j=1}^{n-1} p_j}.$$
  Notamos que $P(X > n-1) = 1 - \sum_{j=1}^{n-1} p_j = (1-\lambda_1)(1-\lambda_2)\cdots(1-\lambda_{n-1})$, pues la probabilidad de sobrevivir hasta $n-1$ es el producto de no fallar en cada paso anterior. Despejando:
  $$p_n = \lambda_n \cdot P(X > n-1) = (1-\lambda_1)(1-\lambda_2)\cdots(1-\lambda_{n-1})\,\lambda_n.$$

- **b)** El algoritmo genera $X$ como el primer índice $n$ donde $U_n < \lambda_n$. La probabilidad de que $X = n$ es:
  $$P(X=n) = P(U_1 \ge \lambda_1,\, U_2 \ge \lambda_2,\, \dots,\, U_{n-1} \ge \lambda_{n-1},\, U_n < \lambda_n).$$
  Como los $U_i$ son independientes $\mathcal{U}(0,1)$:
  $$P(X=n) = (1-\lambda_1)(1-\lambda_2)\cdots(1-\lambda_{n-1})\,\lambda_n = p_n,$$
  que es precisamente la distribución deseada.

- **c)** Para $X \sim Geom(p)$:
  $$P(X=n) = p(1-p)^{n-1}, \quad P(X>n-1) = (1-p)^{n-1}.$$
  Por lo tanto:
  $$\lambda_n = \frac{p(1-p)^{n-1}}{(1-p)^{n-1}} = p, \quad \forall n \ge 1.$$
  La tasa de riesgo es constante $p$ para todo $n$. El algoritmo se reduce a: generar $U \sim \mathcal{U}(0,1)$; si $U < p$, devolver $X$; si no, incrementar $X$ y repetir. Esto es exactamente simular ensayos Bernoulli hasta el primer éxito, que es la definición misma de la geométrica. Su validez es evidente: en cada paso se "lanza una moneda" con probabilidad $p$ de éxito.
<div style="page-break-after: always;"></div>

## <u>Ejercicio 12</u> ([[#^indice|Índice]])
^ejercicio12

<u>Enunciado:</u> ¿Qué distribución tiene la variable simulada por el siguiente algoritmo?
```python
def QueDevuelve(p1,p2):
	X = int(np.log(1-random())/np.log(1-p1))+1
	Y = int(np.log(1-random())/np.log(1-p2))+1
	return min(X,Y)
```
Escriba otro algoritmo que utilice un único número aleatorio (random()) y que simule una variable con la misma distribución que la simulada por QueDevuelve(0.05, 0.2).

<u>Solución:</u>

$X \sim Geom(p_1)$ e $Y \sim Geom(p_2)$ son independientes (se generan con dos uniformes independientes). Para el mínimo:
$$P(\min(X,Y) > n) = P(X > n)P(Y > n) = (1-p_1)^n (1-p_2)^n = [(1-p_1)(1-p_2)]^n.$$
Por lo tanto $\min(X,Y) \sim Geom(p)$ con $p = 1 - (1-p_1)(1-p_2) = p_1 + p_2 - p_1 p_2$.

Para $p_1=0.05$, $p_2=0.2$: $p = 0.05 + 0.2 - 0.01 = 0.24$.

Algoritmo con un único número aleatorio:
```python
def QueDevuelveUnSoloRandom():
    U = random()
    p = 0.24
    return int(math.log(1 - U) / math.log(1 - p)) + 1
```
Ver `ej12.py`.
<div style="page-break-after: always;"></div>