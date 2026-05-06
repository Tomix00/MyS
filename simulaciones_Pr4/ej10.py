from random import random
from transf_inversa import discreteGenerators as dg

def generar_X():
    u = random()
    if u < 0.5:
        return dg.geometric(0.5)   # Geom(1/2)
    else:
        return dg.geometric(1/3)   # Geom(1/3)

# Simulación
n = 1000
suma = 0
for _ in range(n):
    suma += generar_X()

media_estimada = suma / n
esperanza_exacta = 2.5

print(f"Esperanza exacta: {esperanza_exacta}")
print(f"Media estimada con {n} repeticiones: {media_estimada:.4f}")