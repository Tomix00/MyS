import random
import time
import math
from transf_inversa import discreteGenerators

# Método a) Transformada inversa con fórmula recursiva
def inverse_geom(p):
    """X ~ Geom(p) usando transformada inversa"""
    U = random.random()
    return int(math.log(1 - U) / math.log(1 - p)) + 1

# Método b) Simular ensayos hasta el primer éxito
def trial_geom(p):
    """X ~ Geom(p) simulando ensayos Bernoulli"""
    x = 1
    while random.random() > p:
        x += 1
    return x

# Comparación
def ejercicio9(p, n=10000):
    print(f"\n{'='*50}")
    print(f"p = {p}")
    print(f"{'='*50}")
    
    # Método a)
    inicio = time.time()
    muestras_a = [inverse_geom(p) for _ in range(n)]
    tiempo_a = time.time() - inicio
    media_a = sum(muestras_a) / n
    
    # Método b)
    inicio = time.time()
    muestras_b = [trial_geom(p) for _ in range(n)]
    tiempo_b = time.time() - inicio
    media_b = sum(muestras_b) / n
    
    # Valor esperado teórico
    esperado = 1 / p
    
    print(f"Método a) inversa:    media={media_a:.4f}, tiempo={tiempo_a:.4f}s")
    print(f"Método b) ensayos:    media={media_b:.4f}, tiempo={tiempo_b:.4f}s")
    print(f"Valor esperado:       {esperado:.4f}")
    print(f"Eficiencia: inversa es {tiempo_b/tiempo_a:.2f}x más rápida")

# Ejecutar
ejercicio9(0.8, 10000)
ejercicio9(0.2, 10000)