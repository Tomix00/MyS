# Práctica 3 — Generadores de números pseudoaleatorios

## Archivos de herramientas

- **`generators.py`** — Clase `generators` con 6 métodos estáticos para generar secuencias pseudoaleatorias:
  - `genMul`: generador congruencial lineal multiplicativo: `x_{n+1} = (a * x_n) % M`
  - `genMix`: generador congruencial lineal mixto: `x_{n+1} = (a * x_n + c) % M`
  - `genComb_sum`: combinación (suma) de los dos anteriores: `(genMul + genMix) % M`
  - `vonNeumann`: método de cuadrados medios: `(x_n² // 100) % 10000`
  - `randu`: generador RANDU: `(x_n * 65539) % 2³¹`
  - `randu2`: generador Park-Miller: `(x_n * 16807) % (2³¹ - 1)`
- **`graphics.py`** — Genera scatter-plot 3-panel de pares (x_i, x_i+1) para los 3 generadores congruenciales. Construye la secuencia con `build_sequence` y grafica con `matplotlib`. Uso: `python graphics.py <seed> <a> <c> <M> <iterations>`
- **`RP.py`** — Encuentra la raíz primitiva más grande de un número primo usando `sympy.ntheory.residue_ntheory.primitive_root(p, smallest=False)`. Uso: `python RP.py <prime>`

## Ejercicios

### ej1.py — Estimación del volumen de una esfera con RANDU y RANDU2

**`ejercicio1(seed, n_points, m=2³¹)` — usando RANDU:**
1. Se inicializa `x = seed`. Se define el centro de la esfera en `(M/2, M/2, M/2)` y el radio `M/10`.
2. Para cada uno de los `n_points` puntos:
   - Se generan 3 valores consecutivos con `Generators.randu(x)`, actualizando `x` cada vez. Estos son (u₁, u₂, u₃).
   - Se calcula la distancia euclídea al cuadrado desde el centro: `d² = (u₁ - M/2)² + (u₂ - M/2)² + (u₃ - M/2)²`.
   - Si `d² ≤ (M/10)²`, se incrementa el contador `inside`.
3. Se devuelve el porcentaje: `100 * inside / n_points`.

**`ejercicio2(seed, n_points, m=2³¹)` — usando RANDU2 (Park-Miller):**
- Idéntico algoritmo, pero usando `Generators.randu2(x)` en lugar de `randu`.
- El generador Park-Miller usa `a=16807`, `M=2³¹-1`, lo que produce una secuencia diferente.

**`main()`:** Lee `seed` y `n_points` de CLI, ejecuta ambos métodos e imprime resultados en español.

---

### ej2.py — Suma de uniformes con elección de cantidad

**`ejercicio2b(iterations)`:**
1. Para cada iteración:
   - Se genera `u = random()`. Si `u < 0.5`: se generan 2 uniformes y se suman.
   - Si `u ≥ 0.5`: se generan 3 uniformes y se suman.
   - Si la suma `≥ 1`, se incrementa `wins`.
2. Se imprime `wins / iterations` como estimación de P(sumar ≥ 1).

La probabilidad teórica se calcula por convolución de uniformes: P(U₁ + U₂ ≥ 1) = 1/2 para 2 uniformes; para 3 uniformes es 5/6. Con la mezcla 0.5-0.5, el valor esperado es `0.5 × 1/2 + 0.5 × 5/6 = 2/3`.

---

### ej3.py — Suma de uniformes con probabilidad variable

**`ejercicio3b(iterations)`:**
1. Para cada iteración:
   - Se genera `u = random()`.
   - Si `u < 1/3`: se suman 2 uniformes.
   - Si no: se suman 3 uniformes.
   - Si la suma `≤ 2`, se incrementa `hits`.
2. Se imprime `hits / iterations`.

---

### ej4.py — Tiempo de espera en supermercado

**`ejercicio4c(n)`:**
1. Para cada cliente:
   - Se genera `u = random()`. Se selecciona la caja por acumulación de probabilidades:
     - Caja 1 si `u < 0.4` (media = 3 min).
     - Caja 2 si `u < 0.75` (media = 4 min).
     - Caja 3 en otro caso (media = 5 min).
   - Se genera un tiempo de espera exponencial con `np.random.exponential(scale=media)`.
   - Si `tiempo < 4`: incrementa `menor4`.
   - Si no: incrementa `mayor4_por_caja[caja]`.
2. Al final: `P(T < 4) = menor4 / n`.
3. Para las condicionales: `P(C_i | T > 4) = mayor4_por_caja[i] / total_mayor4`.

---

### ej5.py — Integrales Monte Carlo

Cada subejercicio transforma una integral definida en una esperanza y la estima por Monte Carlo.

**`ejercicio5a(n)`:**
- Integral: `∫₀¹ (1 - u²)^(3/2) du`
- Algoritmo: genera `u ~ Uniforme(0,1)`, evalúa `(1-u²)^(3/2)`, promedia.

**`ejercicio5b(n)`:**
- Integral: `∫₀¹ (u+2)/((u+3)(u+1)) du`
- Algoritmo: genera `u ~ Uniforme(0,1)`, evalúa el integrando, promedia.

**`ejercicio5c(n)`:**
- Integral: `∫₀¹ u(1-u) / (2u² - 2u + 1)² du`
- Algoritmo: genera `u ~ Uniforme(0,1)`, evalúa, promedia.

**`ejercicio5d(n)`:**
- Integral: `2 * ∫₀¹ exp(-(1-u)²/u²) * (1/u²) du`
- Algoritmo: genera `u ~ Uniforme(0,1)`, transforma, suma, multiplica por 2.

**`ejercicio5e(n)`:**
- Integral: `∫₀¹ ∫₀¹ exp((u₁+u₂)²) du₁ du₂`
- Algoritmo: genera dos uniformes independientes, evalúa, promedia.

**`ejercicio5f(n)`:**
- Probabilidad: `P(X < Y)` con `X, Y ~ Exp(1)`.
- Algoritmo: genera dos exponenciales, cuenta si `u₁ < u₂`, divide por n.
- Valor teórico: `P(X < Y) = λ_X / (λ_X + λ_Y) = 1/2`.

---

### ej6.py — Estimación de π

**`ejercicio6(n)` — Método de dardos:**
1. Para cada iteración: genera `u, v ~ Uniforme(-1, 1)` (transformando `2 * rand() - 1`).
2. Si `u² + v² ≤ 1`, está dentro del círculo unitario → `hit += 1`.
3. Retorna `4 * hit / n`, que converge a π.

---

### ej7.py — Valor esperado del número de uniformes para superar 1

**`simulate_trial()`:**
1. Inicializa `sum = 0`, `count = 0`.
2. Mientras `sum ≤ 1`: genera `u ~ Uniforme(0,1)`, suma a `sum`, incrementa `count`.
3. Retorna `count` (la cantidad de uniformes necesarios).

**`ejercicio7(n)`:**
1. Ejecuta `simulate_trial()` un total de `n` veces.
2. Retorna el promedio de los valores obtenidos (estimación de E[N]).
- Valor teórico: `E[N] = e ≈ 2.71828`.

---

### ej8.py — Máximo producto de uniformes antes de caer bajo e⁻³

**`simulate_trial()`:**
1. Inicializa `prod = 1.0`, `n = 0`.
2. Mientras `prod >= exp(-3)`: multiplica por `U ~ Uniforme(0,1)`, incrementa `n`.
3. Retorna `n - 1` (el máximo número de uniformes cuyo producto ≥ e⁻³).
- Relación con proceso de Poisson: tomando logaritmo, `-ln(producto) = ∑ -ln(Uᵢ)` es suma de Exp(1); el máximo n tal que la suma ≤ 3. Por lo tanto N ~ Poisson(3), con E[N] = 3.

**`ejercicio8a(n)`:**
- Ejecuta `simulate_trial()` n veces y retorna el promedio (estimación de E[N] = 3).

**`ejercicio8b(n)`:**
- Ejecuta `simulate_trial()` n veces, cuenta frecuencias para i=0..6, retorna proporciones (estima P(N=i) para Poisson(3)).

**Uso:** `python ej8.py <N> [opcion]` donde opcion=1 estima E[N], opcion=2 estima P(N=i).

---

### ej9.py — Juego de dados

**`ejercicio9b(n)`:**
1. Para cada juego:
   - Se lanza el primer dado: `d1 = randint(1, 6)`.
   - Si `d1` es 1 o 6: se lanza un segundo dado `d2` y los puntos son `2 * d2`.
   - Si `d1` no es 1 ni 6: se lanzan `d3` y `d4`, y los puntos son `d3 + d4`.
   - Si `puntos > 6`: se incrementa `win`.
2. Retorna `win / n` como estimación de P(ganar).
