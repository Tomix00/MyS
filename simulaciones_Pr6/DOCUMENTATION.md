# Práctica 6 — Estimación secuencial e integración Monte Carlo

## Ejercicios

### ej1.py — Estimación secuencial de media y varianza

**`ejercicio1()` — Algoritmo de actualización en línea:**
1. **Inicialización:** `d = 0.1` (error estándar máximo), `n = 1`, genera `x ~ N(0,1)`. Inicializa `mean = x`, `scuad = 0.0`.
2. **Bucle de muestreo:** mientras `n ≤ 100` (mínimo de muestras) o `√(scuad / n) ≥ d` (error estándar > tolerancia):
   - Incrementa `n`.
   - Genera `x ~ N(0,1)`.
   - Guarda `mean_ant = mean`.
   - **Actualización de media en línea:** `mean = mean_ant + (x - mean_ant) / n`.
   - **Actualización de suma de cuadrados en línea:** `scuad = scuad * (1 - 1/(n-1)) + n * (mean - mean_ant)²`.
3. **Criterio de paro:** se detiene cuando el error estándar estimado `√(scuad / n) < d` y se cumplieron al menos 100 muestras.
4. Retorna `n` (tamaño de muestra final), `mean` (media estimada) y `scuad` (suma de cuadrados para varianza).

**Fórmulas de actualización en línea:**
- Media: `x̄_n = x̄_{n-1} + (x_n - x̄_{n-1}) / n`
- Suma de cuadrados recursiva: `S_n = S_{n-1} * (1 - 1/(n-1)) + n * (x̄_n - x̄_{n-1})²`
- Varianza muestral: `s²_n = S_n / n`
- Error estándar de la media: `SE = s_n / √n`

---

### ej2.py — Integración Monte Carlo con criterio de paro

Ambos incisos usan el mismo esquema de estimación secuencial que ej1 pero aplicado a integrales.

**`ejercicio2_i()` — Integral `∫₀¹ e^x / √(2x) dx`:**
1. **Transformación:** la integral se escribe como `E[f(U)]` con `U ~ Uniforme(0,1)` donde `f(u) = e^u / √(2u)`.
   - Nota: la función tiene una singularidad en `x=0`, pero como `1/√(2x)` es integrable, la esperanza es finita.
2. **Estimación secuencial:** mismo algoritmo que ej1 pero aplicado a `f(u)` en lugar de `N(0,1)`.
   - `d = 0.01`, mínimo 100 muestras.
   - En cada paso genera `u ~ Uniforme(0,1)`, calcula `f = exp(u) / sqrt(2*u)`, actualiza media y suma de cuadrados en línea.
3. Retorna `n` (muestras), `estimación` (media de f), `error estándar`.

**`ejercicio2_ii()` — Integral `∫₋∞^∞ x² exp(-x²) dx`:**
1. **Transformación simétrica:** la integral de `-∞` a `∞` es el doble de la de `0` a `∞`.
2. **Cambio de variable:** para integral en `(0, ∞)` se usa `t = u / (1-u)` que mapea `(0,1) → (0, ∞)`.
   - `dt = du / (1-u)²`
   - El integrando transformado es: `f(u) = (u² / (1-u)⁴) * exp(-(u/(1-u))²)`
   - La integral total es `2 * E[f(U)]`.
3. **Estimación secuencial:** mismo esquema que el inciso i), con `d = 0.01`, mínimo 100 muestras.
   - En cada paso genera `u ~ Uniforme(0,1)`, calcula `f(u)`, actualiza en línea.
   - Al final multiplica la media por 2.
4. Retorna `n`, `estimación = 2 * mean`, `error estándar`.
