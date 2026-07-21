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

---

### ej3.py — Integración Monte Carlo con parada por IC95%

**`sequential_mc(f_sample, target_se=0.001, min_n=1000)`:**
- Algoritmo de estimación secuencial con parada cuando el semiancho del IC95% < `target_se`.
- Usa actualización en línea de media y varianza (Welford).

**`mc_i()`:** Muestra `x ~ Uniforme(π, 2π)`, retorna `(b-a) * sin(x)/x`.

**`mc_ii()`:** Muestra `u ~ Uniforme(0,1)`, transforma `x = u/(1-u)` para integral en $(0,\infty)$, retorna $f(x)/(1-u)^2$ con $f(x)=3/(3+x^4)$.

**`ejercicio3()`:** Estima ambas integrales para n=1000, 5000, 7000 y con el criterio de parada.

---

### ej4.py — Estimación de π con regla de parada

**`estimate_p(target_se=0.01, min_n=100)`:**
1. Muestra puntos $(x,y) \sim \mathcal{U}(-1,1)^2$.
2. Cuenta proporción dentro del círculo $x^2+y^2 \le 1$.
3. Detiene cuando SE de $\hat{p} < \text{target\_se}$.
4. Retorna $n$, $\hat{p}$, $\text{SE}(\hat{p})$.

**`ejercicio4()`:**
- **a)** Para $\text{SE}(\hat{p}) < 0.01$: estima $\pi = 4\hat{p}$.
- **b)** Busca n necesario para IC95% de $\pi$ con ancho $< 0.1$, $0.05$, $0.001$.

---

### ej5.py — Bootstrap para $P(-5 < \bar{X} - \mu < 5)$

Datos: $[56, 101, 78, 67, 93, 87, 64, 72, 80, 69]$, $\bar{X}=76.7$.

**`bootstrap_p(B=10000)`:**
1. Remuestrea con reemplazo $B$ veces la muestra original (tamaño 10).
2. Para cada remuestra, calcula $\bar{X}^* - \bar{X}$.
3. Retorna proporción de remuestras donde la diferencia cae en $(-5, 5)$.

---

### ej6.py — Bootstrap para $\text{Var}(S^2)$

**`var_muestral(xs)`:** Calcula varianza muestral $S^2 = \frac{1}{n-1}\sum (x_i - \bar{x})^2$.

**`bootstrap_var_s2(datos, B=10000)`:**
1. Remuestrea con reemplazo $B$ veces.
2. Para cada remuestra, calcula $S^{2*}$.
3. Retorna $S^2$ observado, $\mathbb{E}_{\text{boot}}[S^{2*}]$ y $\text{Var}_{\text{boot}}(S^{2*})$.

**`ejercicio6()`:**
- **a)** n=2, datos $[1,3]$: $S^2=2$, $\text{Var}_{\text{boot}}(S^2) \approx 1$.
- **b)** n=15: $S^2 \approx 34.31$, $\text{Var}_{\text{boot}}(S^2) \approx 59.58$.

---

### ej7.py — Cola M/G/1 con Poisson no homogéneo y descansos

Servidor único con:
- Arribos: Poisson no homogéneo periódico (ciclo 10h: $\lambda$ entre 4 y 19).
- Servicio: $\text{Exp}(25)$ por hora.
- Descanso: si no hay trabajo, toma pausa $\sim \mathcal{U}(0, 0.3)$ horas.

**`simulate_once()`:** Simula 100 horas de operación, retorna `(rest_time, n_completed)`.

**`ejercicio7()`:** Estima tiempo total de descanso (SE<0.05) y número de trabajos completados (SE<0.01).

---

### ej8.py — Centro de diagnóstico en serie (dos etapas)

Dos etapas: Admisión ($\sim\text{Exp}(15)$) → Diagnóstico ($\sim\text{Exp}(12)$).
- Arribos: Poisson no homogéneo (ciclo 8h: $\lambda$ entre 4 y 14). Jornada de 16h, luego no ingresan pacientes.
- Cola FIFO en cada etapa.

**`simulate_once()`:** Simula una jornada completa, retorna `(n_patients, total_time, remaining, finish_t)`.

**`ejercicio8()`:** Estima con SE<0.01: tiempo promedio en sistema, P(pacientes restantes tras cierre), tiempo extra necesario. Construye IC95%.

---

### ej9.py — Dos servidores en paralelo (cola más corta)

Servidores: S1 ($\sim\text{Exp}(3)$), S2 ($\sim\text{Exp}(4)$). Cliente se une a la cola más corta (empate → S1).
- Arribos: $\lambda(t) = 7 - 1/(t+1)$.

**`simulate_once()`:** Simula hasta atender 1000 clientes, retorna `(avg_time, prop1)`.

**`ejercicio9()`:** Estima con SE<0.01: tiempo promedio en sistema y proporción atendida por servidor 1. IC95%.

---

### ej10.py — Modelo de reparación (n máquinas + s repuestos)

- $n=6$ máquinas funcionando, $s=4$ repuestos.
- Tiempos de funcionamiento: $\text{Exp}(2)$. Reparación: $\text{Exp}(3)$, una reparación a la vez.
- Sistema falla cuando falla una máquina y no hay repuestos disponibles.

**`simulate_once()`:** Simula hasta la falla del sistema, retorna tiempo hasta falla.

**`ejercicio10()`:**
- **b)** Estima tiempo medio hasta falla (SE<0.01). IC95%.
- **d)** Estima $P(\text{falla antes de 90 min}=1.5\text{h})$ (SE<0.01). IC95%.
