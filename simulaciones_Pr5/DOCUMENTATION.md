# Práctica 5 — Transformada inversa para variables continuas

## Archivos de herramientas

- **`transf_inversa.py`** — Contiene:
  - Clase `discreteGenerators` (ídem Práctica 4): `udiscrete1n`, `udiscretemk`, `geometric`, `bernoulli`, `Nbernoullis`, `poisson`, `binomial`.
  - Clase `continousGenerators`:
    - `exponential1()`: Exp(1) por transformada inversa: `X = -ln(1-U)`.
    - `exponentialL(lam)`: Exp(λ): `X = -ln(U)/λ`.
    - `poisson_with_exp(lam)`: genera Poisson(λ) usando el método de la exponencial (producto de uniformes hasta que el producto < e^{-λ}).
    - `gamma(n, lam)`: Gamma(n, λ) como suma de n exponenciales Exp(λ).
  - Clase `permutation` (ídem Práctica 4).

## Ejercicios

### ej1.py — Densidades personalizadas por transformada inversa

Cada función calcula F(x) analíticamente, invierte y aplica la transformada inversa.

**`ejercicio1a()` — Densidad a trozos en [2,6]:**
- FDA: `F(x) = (x-2)²/4` para `x∈[2,3]`, `F(x) = x - x²/12 - 2` para `x∈[3,6]`.
- Inversa:
  - Si `U < 1/4`: `X = 2 + 2√U`.
  - Si no: `X = 6 - 2√(3(1-U))`.

**`ejercicio1b()` — Densidad a trozos en [-3,2]:**
- FDA: `F(x) = (3x²+18x)/35` para `x∈[0,1]`, `F(x) = (2x³+19)/35` para `x∈[1,2]`, con probabilidad 3/5 de caer en el primer tramo.
- Inversa:
  - Si `U < 3/5`: `X = -3 + √(9 + 35U/3)`.
  - Si no: `X = ((35U - 19)/2)^(1/3)`.

**`ejercicio1c()` — Densidad con exponencial en (-∞,0] y uniforme en [0, 15/4]:**
- FDA: `F(x) = e^{4x}/16` para `x≤0`, `F(x) = 1/16 + x/4` para `x∈[0, 15/4]`.
- Inversa:
  - Si `U < 1/16`: `X = ln(16U)/4`.
  - Si no: `X = 4U - 1/4`.

---

### ej2.py — Distribuciones Pareto, Erlang y Weibull

**`pareto_sample(a)`:**
- FDA: `F(x) = 1 - x^{-a}`, con `x ≥ 1`, `a > 0`.
- Inversa: `X = U^{-1/a}` (usando `1-U` equivalente).

**`erlang_sample(k, mu)`:**
- Erlang(k, μ) es suma de k exponenciales independientes Exp(μ).
- Algoritmo: suma `k` variables generadas con `exponentialL(1/μ)`.

**`weibull_sample(lam, beta)`:**
- FDA: `F(x) = 1 - exp(-(x/λ)^β)`.
- Inversa: `X = λ * (-ln(U))^{1/β}`.

**`ejercicio2()`:** Genera 10000 muestras de cada distribución (con parámetros `a=2`, `k=2`, `μ=2`, `λ=1`, `β=2`), calcula medias muestrales y las imprime. Valores teóricos: Pareto E[X]=2, Erlang E[X]=4, Weibull E[X]=Γ(1.5) ≈ 0.8862.

---

### ej3.py — Mezcla de distribuciones

**`ejercicio3a(p_list, gen_list)`:**
1. Genera `U ~ Uniforme(0,1)`.
2. Acumula probabilidades hasta que `U < acum`, selecciona el índice `i`.
3. Ejecuta `gen_list[i]()` y retorna el resultado.

**`ejercicio3b()`:** Mezcla de 3 exponenciales:
- Exp(1/3) con prob 0.5 (media 3).
- Exp(1/5) con prob 0.3 (media 5).
- Exp(1/7) con prob 0.2 (media 7).
- Genera una variable de la mezcla usando el mismo esquema de `ejercicio3a`.

**`ejercicio3_runner()`:** Genera 10000 valores de la mezcla, estima la media y compara con el valor teórico `E[X] = 0.5*3 + 0.3*5 + 0.2*7 = 4.4`.

---

### ej4.py — Transformación de variables

**`ejercicio4()` — Método de composición:**
1. Genera `Y ~ Exp(1)` usando `exponential1()` (por transformada inversa).
2. Genera `U ~ Uniforme(0,1)` independiente.
3. Retorna `X = U^{1/Y}`.
- Justificación: la FDA condicional es `P(X ≤ x | Y = y) = x^y`, y marginalmente `Y ~ Exp(1)`. La FDA no condicional resulta ser `F(x) = ∫₀^∞ x^y e^{-y} dy`.

---

### ej5.py — Máximo y mínimo de exponenciales

**`generate_max()`:** Genera `X₁ ~ Exp(1)`, `X₂ ~ Exp(2)`, `X₃ ~ Exp(3)` con `exponentialL`. Retorna el máximo de los tres.

**`generate_min()`:** Igual pero retorna el mínimo.

**`ejercicio5()`:** Genera 10 valores de M (máximo) y 10 de m (mínimo) y los imprime.
- Justificación: `F_M(x) = ∏ F_i(x)` (producto de FDA), `F_m(x) = 1 - ∏ (1 - F_i(x))`.

---

### ej6.py — Distribución del máximo de n uniformes

**`max_uniform_inverse(n)`:**
- FDA: `F(x) = x^n`. Inversa: `X = U^{1/n}`.

**`max_uniform_composition(n)`:**
- Genera `n` uniformes y retorna el máximo. Equivalente por composición.

**`max_uniform_rejection(n)`:**
- Propuesta: `Y ~ Uniforme(0,1)`. Densidad objetivo: `f(x) = nx^{n-1}`.
- Cociente: `f(y)/g(y) = ny^{n-1} / 1`, máximo en y=1 → `c = n`.
- Criterio de aceptación: `U < Y^{n-1}`.

**`ejercicio6()`:** Ejecuta los 3 métodos con `n=10`, `10000` repeticiones cada uno, y compara tiempos.

---

### ej7.py — Generación de f(x) = 1/x para 1 ≤ x ≤ e

**`generate_X_inverse()`:**
- FDA: `F(x) = ln x`. Inversa: `X = e^U`.

**`generate_X_rejection()`:**
- Propuesta: `Y ~ Uniforme(1, e)` con `g(y) = 1/(e-1)`.
- Cociente: `f(y)/g(y) = (e-1)/y`, máximo en y=1 → `c = e-1`.
- Simplificación: `f(y) / (c·g(y)) = 1/y`.
- Acepta si `U < 1/Y`.

**`ejercicio7a()`:** Genera 10000 valores con cada método, mide tiempos, calcula medias y compara con `E[X] = e - 1 ≈ 1.71828`.

**`ejercicio7c()`:**
- Estima `P(X ≤ 2)` con ambos métodos y compara con valor teórico `ln(2) ≈ 0.6931`.
- Usa una función anidada `estimate_probability` que ejecuta el generador n veces y cuenta las veces que el resultado ≤ 2.

---

### ej8.py — Triangular(0,1,2)

**`triangular_sum()`:** Genera `X = U₁ + U₂` con `U₁, U₂ ~ Uniforme(0,1)` independientes. Por convolución, esto da una distribución triangular.

**`triangular_inverse()`:**
- FDA: `F(x) = x²/2` para `x∈[0,1]`, `F(x) = 2x - x²/2 - 1` para `x∈[1,2]`.
- Inversa:
  - Si `U < 0.5`: `X = √(2U)`.
  - Si no: `X = 2 - √(2(1-U))`.

**`triangular_rejection()`:**
- Propuesta: `Y ~ Uniforme(0,2)` con `g(y) = 1/2`.
- Cociente: `f(y)/g(y) = 2f(y)`, máximo de f es 1 → `c = 2`.
- Acepta si `U < f(Y)` (densidad triangular evaluada en Y).

**`ejercicio8a()`:** Ejecuta los 3 métodos con 10000 repeticiones, mide tiempos y medias (esperanza teórica E[X] = 1).

**`ejercicio8b()`:** Estima `P(X > 1.5)` con cada método y compara con valor teórico `0.125`.
