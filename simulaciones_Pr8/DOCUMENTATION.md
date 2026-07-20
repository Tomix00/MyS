# Práctica 8 — Cadenas de Márkov

## Dependencias

Requiere `numpy` para operaciones con matrices.

```
pip install numpy
```

## Archivos

### markov_utils.py — Herramientas para cómputo de cadenas de Márkov

- `Pn(P, n)` — Matriz de transición en n pasos (Pⁿ).
- `stationary(P)` — Distribución estacionaria resolviendo π·P = π, Σπᵢ = 1.
- `absorption_prob(P, absorbing_states)` — Probabilidades de absorción para cada estado transitorio.
- `mean_first_passage(P, target)` — Tiempos medios de primer paso al estado `target`.
- `mean_return_time(pi, state)` — Tiempo medio de retorno = 1/πᵢ.

### soluciones.py — Cómputo de todos los ejercicios

Ejecutar para verificar numéricamente los resultados:

```
python soluciones.py
```

## Ejercicios

1. **Matriz de transición desde diagrama** — Probabilidades condicionales y conjuntas con P³ y P⁴.
2. **Cadena 3×3** — Cálculo de Q² y probabilidad conjunta.
3. **Cadena 2 estados** — P³₍₁,₁₎ por recurrencia.
4. **Pulga en triángulo** — Fórmula cerrada: Pₙ = 1/3 + (2/3)(-1/2)ⁿ.
5. **Clasificación de estados** — Clases comunicantes, recurrencia, periodicidad.
6. **Cadena 5×5 con período 2** — Identificación de clases y periodicidad.
7. **Tiempos de alcance y retorno** — μ₀₁, μ₀₂, μ₀ (tiempo medio de retorno).
8. **Cinco cadenas** (Figuras 4-8) — Clasificación, estacionaria, tiempos de retorno.
