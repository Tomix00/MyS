# Práctica 4 — Transformada inversa para variables discretas

## Archivos de herramientas

- **`transf_inversa.py`** — Clase `discreteGenerators` con 7 métodos de generación por transformada inversa:
  - `udiscrete1n(n)`: uniforme discreta entre 1 y n. Genera `U ~ Uniforme(0,1)`, retorna `int(n * U) + 1`.
  - `udiscretemk(m, k)`: uniforme discreta entre m y k. Retorna `int(U * (k-m+1)) + m`.
  - `geometric(p)`: Geom(p). Retorna `int(log(1-U)/log(1-p)) + 1`.
  - `bernoulli(p)`: Bernoulli(p). Retorna `1` si `U < p`, `0` si no.
  - `Nbernoullis(n, p)`: genera n Bernoullis usando el método del salto geométrico (posiciones de éxitos).
  - `poisson(lam)`: Poisson(λ). Busca en la FDA desde el origen.
  - `binomial(n, p)`: Bin(n, p). Busca en la FDA con `math.comb`.
  
  Clase `permutation` con 3 variantes de Fisher-Yates: `permutation1`, `permutation2`, `subcRandom` (subconjunto aleatorio).

## Ejercicios

### ej2.py — Aproximación de suma exponencial

**`ejercicio2()`:**
1. **Valor exacto:** Suma `Σ_{k=1}^{10000} exp(k/10000)` mediante un bucle. Mide tiempo con `perf_counter`.
2. **Aproximación Monte Carlo:** Toma 100 muestras de `k` usando `udiscrete1n(10000)` y promedia `exp(k+1/u)` para cada una. Mide tiempo.
3. Imprime ambos valores, la diferencia absoluta y los tiempos de cómputo.

---

### ej3.py — Lanzamiento de dos dados hasta cubrir todas las sumas

**`roll_dice_sum()`:** Genera dos valores `UniformeDiscreta(1,6)` con `udiscrete1n(6)` y retorna su suma.

**`simulate_game()`:**
1. Inicializa un conjunto vacío `vistas` y contador `lanzamientos = 0`.
2. Mientras el conjunto tenga menos de 11 elementos (las sumas 2..12):
   - Genera una suma con `roll_dice_sum()`.
   - La agrega al conjunto.
   - Incrementa `lanzamientos`.
3. Retorna la cantidad de lanzamientos necesarios.

**`ejercicio3(repeticiones)`:**
1. Ejecuta `simulate_game()` `repeticiones` veces, recolectando los resultados.
2. Calcula: media, desviación estándar, proporción de `N ≥ 15` y `N ≤ 9`.
3. Repite para 100, 1000, 10000 y 100000 repeticiones.

---

### ej4.py — Generación de variable discreta arbitraria

Datos: valores 1..10 con probabilidades `[0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]`.

**`rejection_cmin()` — Aceptación y rechazo con c óptimo:**
1. `c = 1.4` (mínimo que satisface `c ≥ 10 * max(p_i) = 1.4`).
2. Genera `Y ~ UniformeDiscreta(1,10)` con `udiscrete1n(10)`.
3. Genera `U ~ Uniforme(0,1)` independiente.
4. Si `U < (10 * p[Y-1]) / c`, acepta y retorna Y. Si no, repite.

**`rejection_c3()` — Aceptación y rechazo con c = 3:**
- Mismo algoritmo, pero con `c = 3` (menos eficiente, menor probabilidad de aceptación).

**`inverse_transform()` — Transformada inversa:**
1. Precalcula FDA acumulada `F`.
2. Genera `U ~ Uniforme(0,1)`. Recorre `F` hasta encontrar `U < F[i]`, retorna `i+1`.

**`urn_method()` — Método de la urna:**
1. Preconstruye una urna con 100 elementos: cada valor `i` aparece `int(p_i * 100)` veces.
2. Genera índice `UniformeDiscreta(1, 100) - 1`, retorna el valor en esa posición de la urna.

**`ejercicio4(n=10000)`:** Ejecuta los 4 métodos, mide tiempo y error promedio respecto a las probabilidades teóricas.

---

### ej5.py — Distribución binomial: inversa vs ensayos Bernoulli

Parámetros: `n=10`, `p=0.3`.

**`binomial_inverse(n, p)`:** Delega en `discreteGenerators.binomial(n, p)` (transformada inversa sobre la FDA binomial).

**`binomial_trials(n, p)`:** Simula `n` ensayos Bernoulli con `bernoulli(p)` y cuenta los éxitos.

**`ejercicio5a(n_simulaciones=10000)`:**
1. Genera `n_simulaciones` valores con cada método, midiendo tiempo.
2. Imprime tabla comparativa de tiempos y eficiencia relativa.
3. Retorna las muestras para análisis posterior.

**`analyze_samples(muestras, metodo_nombre)`:** Calcula frecuencias, moda observada, proporciones de X=0 y X=10.

**`show_theoretical()`:** Calcula valores teóricos de Bin(10, 0.3): moda (valor `int((n+1)*p) = 3`), P(X=0) = 0.7¹⁰, P(X=10) = 0.3¹⁰.

**`compare_with_theoretical(muestras_inv, muestras_ens)`:** Calcula diferencias absolutas entre frecuencias observadas y teóricas.

---

### ej6.py — Variable discreta con inversa optimizada vs aceptación y rechazo

Datos: valores `[0,1,2,3,4]` con probabilidades `[0.15, 0.20, 0.10, 0.35, 0.20]`.

**`inverse_transform()` — Transformada inversa optimizada:**
1. Ordena los pares (probabilidad, valor) de mayor a menor probabilidad.
2. Precalcula FDA acumulada sobre los valores ordenados.
3. Genera `U` y recorre la FDA ordenada, retornando el primer valor cuya FDA supere a U.
- La optimización reduce iteraciones porque los valores más probables se evalúan primero.

**`acceptance_rejection()` — Aceptación y rechazo:**
1. Usa `Y ~ Bin(4, 0.45)` como distribución propuesta. Precalcula `q(k) = P(Y=k)`.
2. Calcula `c = max(p_k / q_k) * 1.0001` (constante de rechazo mínima).
3. Genera `Y` con `binomial(4, 0.45)` y `U ~ Uniforme(0,1)`.
4. Si `U < p_Y / (c * q_Y)`, acepta. Si no, repite.

**`ejercicio6(n=10000)`:** Compara tiempo de ambos métodos y verifica que las distribuciones observadas coincidan con las teóricas.

---

### ej7.py — Poisson: transformada inversa básica vs mejorada

Parámetro: `λ=10`, `n_simulaciones=1000`.

**`common_poisson()`:** Usa `discreteGenerators.poisson(10)` (búsqueda desde k=0).

**`improved_poisson(lam)`:**
1. Inicializa `p = exp(-λ)`, `F = p`. Calcula FDA hasta el valor modal `k_modal = int(λ)`.
2. Genera `U`.
3. Si `U ≥ F`: busca hacia la derecha desde `k_modal + 1`.
4. Si `U < F`: busca hacia la izquierda desde `k_modal`, aprovechando la relación de recurrencia `p_{k-1} = p_k * k / λ`.

**Ejecución principal:**
1. Genera 1000 muestras con cada método, midiendo tiempo.
2. Estima `P(Y > 2)` empíricamente para ambos.
3. Compara con valor teórico: `1 - (e^{-λ} + λe^{-λ} + λ²e^{-λ}/2)`.
- La versión mejorada suele ser más rápida porque comienza desde la zona de mayor probabilidad.

---

### ej8.py — Poisson truncada

Parámetros: `k=10`, `λ=0.7`, `n=1000`.

**`truncated_probs(lam, k)`:** Calcula `P(X=i | X ≤ k)` para `i=0..k` donde `X ~ Poisson(λ)`:
1. Calcula términos `λ^i / i!` para cada i.
2. Normaliza dividiendo por `S = Σ_{i=0}^{k} λ^i / i!`.

**`truncated_inverse()`:**
1. Precalcula FDA sobre los valores ordenados por probabilidad descendente.
2. Genera `U`, recorre hasta encontrar el valor.

**`truncated_rejection()`:**
1. Calcula `prob_aceptar = e^{-λ} * S` (probabilidad de que una Poisson(λ) caiga en [0,k]).
2. Genera `Y ~ Poisson(λ)` con `discreteGenerators.poisson(lam)`.
3. Si `Y ≤ k` y `U < prob_aceptar`, acepta Y. Si no, repite.
- Nota: este método de rechazo tiene una probabilidad de aceptación de `P(Y ≤ k) * prob_aceptar`, que disminuye si k es pequeño.

**`ejercicio8(metodo)`:** Ejecuta el método de generación n veces y estima `P(X > 2)` como proporción.

---

### ej9.py — Geométrica: inversa vs simulación de ensayos

**`inverse_geom(p)`:**
1. Genera `U ~ Uniforme(0,1)`.
2. Retorna `int(log(1-U) / log(1-p)) + 1`.

**`trial_geom(p)`:**
1. Inicializa `x = 1`.
2. Mientras `random() > p`: incrementa `x`.
3. Retorna `x` (simula ensayos Bernoulli hasta el primer éxito).

**`ejercicio9(p, n=10000)`:**
1. Ejecuta ambos métodos `n` veces, midiendo tiempo y calculando media muestral.
2. Compara con valor esperado teórico `E[X] = 1/p`.
3. Evalúa para `p=0.8` y `p=0.2`.

---

### ej10.py — Mezcla de dos geométricas

**`ejercicio10()`:**
1. Genera `u ~ Uniforme(0,1)`.
2. Si `u < 0.5`: retorna `Geometrica(0.5)` (esperanza = 2).
3. Si no: retorna `Geometrica(1/3)` (esperanza = 3).
4. En `main`: genera 1000 valores, promedia, compara con esperanza exacta `E[X] = 0.5 * 2 + 0.5 * 3 = 2.5`.

---

### ej12.py — Mínimo de dos geométricas

**`ejercicio12()`:**
- Genera directamente `M ~ Geom(0.24)`.
- Justificación teórica: `M = min(X, Y)` con `X ~ Geom(p₁)`, `Y ~ Geom(p₂)`.
- `P(M > n) = P(X > n) * P(Y > n) = (1-p₁)^n * (1-p₂)^n = (1-p)^n` donde `p = p₁ + p₂ - p₁*p₂`.
- Para `p₁=0.05`, `p₂=0.2`: `p = 0.05 + 0.2 - 0.01 = 0.24`.
