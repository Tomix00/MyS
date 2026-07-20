# Práctica 7 — Técnicas de Validación Estadística

## Dependencias

Requiere `scipy` para funciones de distribución (`chi2`, `kstest`, `shapiro`, etc.).

```
pip install scipy
```

## Ejercicios

### ej1.py — Test de bondad de ajuste χ² (Mendel)

- **Datos observados:** 141 blancas, 291 rosas, 132 rojas (n=564).
- **H₀:** Proporciones teóricas 1/4, 1/2, 1/4.
- Calcula el estadístico χ² y el p-valor mediante la aproximación χ² y por simulación (100k repeticiones).

### ej2.py — Test de bondad de ajuste χ² (dado)

- **Datos observados:** 158, 172, 164, 181, 160, 165 (n=1000).
- **H₀:** Dado equilibrado (pᵢ = 1/6).
- χ² observado + simulación.

### ej3.py — Test de rachas (aleatoriedad)

- **Datos:** 10 números en [0,1].
- Aplica el test de rachas (runs test) sobre/bajo la mediana.
- p-valor por aproximación normal y por simulación.

### ej4.py — Test KS para distribución exponencial

- **Datos:** 13 valores, H₀: Exp(media=50).
- Usa `scipy.stats.kstest` con `args=(0, 50)`.

### ej5.py — Bondad de ajuste binomial con p desconocido

- **Datos:** 18 valores, H₀: Bin(8, p) con p estimado de los datos.
- Agrupa categorías con frecuencia esperada < 1.
- χ² con df = k-2 (por estimar p).

### ej6.py — Test χ² para rueda de la fortuna

- **Datos:** 10 categorías con frecuencias observadas (n=637).
- **H₀:** Proporciones 31%, 22%, 12%, 10%, 8%, 6%, 4%, 4%, 2%, 1%.

### ej7.py — Test KS para exponencial simulada

- Genera 30 valores Exp(1) y aplica KS.
- Verifica que el p-valor típicamente no rechaza H₀.

### ej8.py — KS: t-Student vs Normal

- Genera muestras de t(11) para n = 10, 20, 100, 1000.
- Aplica KS contra N(0,1) y muestra cómo aumenta la potencia con n.

### ej9.py — Test KS para datos de vibraciones

- **Datos:** 15 tiempos de falla. H₀: Exp(media estimada).
- Usa `kstest` con `args=(0, mean_est)`.

### ej10.py — Test de normalidad

- **Datos:** 12 valores.
- Aplica KS (con media y desvío estimados) y Shapiro-Wilk.
- `scipy.stats.shapiro` para el test SW.
