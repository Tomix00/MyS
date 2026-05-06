import random
import time
import math
from transf_inversa import discreteGenerators

# Parámetros
lam = 10
n_simulaciones = 1000

# Método 1: Transformada inversa común (la que viene en la clase)
def poisson_comun():
    return discreteGenerators.poisson(lam)

# Método 2: Transformada inversa mejorado (buscando desde el valor más probable)
def poisson_mejorado(lam):
    """Versión mejorada que comienza desde el valor más probable [λ]"""
    p = math.exp(-lam)
    F = p
    
    # Calcular F acumulada hasta el valor más probable
    k_modal = int(lam)
    for j in range(1, k_modal + 1):
        p *= lam / j
        F += p
    
    u = random.random()
    
    if u >= F:
        # Buscar hacia la derecha
        j = k_modal + 1
        while u >= F:
            p *= lam / j
            F += p
            j += 1
        return j - 1
    else:
        # Buscar hacia la izquierda
        j = k_modal
        while u < F:
            F -= p
            p *= j / lam
            j -= 1
        return j + 1

# Simulación con método común
muestras_comun = []
inicio = time.time()
for _ in range(n_simulaciones):
    x = poisson_comun()
    muestras_comun.append(x)
tiempo_comun = time.time() - inicio

prob_comun = sum(1 for x in muestras_comun if x > 2) / n_simulaciones

# Simulación con método mejorado
muestras_mejorado = []
inicio = time.time()
for _ in range(n_simulaciones):
    x = poisson_mejorado(lam)
    muestras_mejorado.append(x)
tiempo_mejorado = time.time() - inicio

prob_mejorado = sum(1 for x in muestras_mejorado if x > 2) / n_simulaciones

# Resultados
print(f"\n{'='*50}")
print(f"Estimación de P(Y > 2) con λ = {lam}")
print(f"{'='*50}")
print(f"Método común:      {prob_comun:.6f}")
print(f"Método mejorado:   {prob_mejorado:.6f}")
print(f"\nTiempo común:      {tiempo_comun:.4f}s")
print(f"Tiempo mejorado:   {tiempo_mejorado:.4f}s")
print(f"Mejora:            {tiempo_comun/tiempo_mejorado:.2f}x más rápido")

# Valor teórico
from math import exp
p0 = exp(-lam)
p1 = lam * p0
p2 = (lam**2 / 2) * p0
p_teorico = 1 - (p0 + p1 + p2)
print(f"\nValor teórico:     {p_teorico:.6f}")
print(f"Error común:       {abs(prob_comun - p_teorico):.6f}")
print(f"Error mejorado:    {abs(prob_mejorado - p_teorico):.6f}")