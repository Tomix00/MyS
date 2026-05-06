import random
import time
import math
from transf_inversa import discreteGenerators as gd

# Datos
valores = [0, 1, 2, 3, 4]
probs = [0.15, 0.20, 0.10, 0.35, 0.20]

# I) Transformada inversa optimizada (ordenar de mayor a menor)
pares = sorted(zip(probs, valores), reverse=True)
probs_ord = [p for p, _ in pares]
vals_ord = [v for _, v in pares]

F_acum = []
acum = 0
for p in probs_ord:
    acum += p
    F_acum.append(acum)

def transformada_inversa():
    U = random.random()
    for i, F in enumerate(F_acum):
        if U < F:
            return vals_ord[i]
    return vals_ord[-1]

# II) Aceptación y rechazo con Y ~ Bin(4, 0.45)
def prob_binomial(k, n=4, p=0.45):
    return math.comb(n, k) * (p**k) * ((1-p)**(n-k))

q_probs = [prob_binomial(k) for k in range(5)]
c = max(p / q for p, q in zip(probs, q_probs)) * 1.0001

def aceptacion_rechazo():
    while True:
        Y = gd.binomial(4, 0.45)
        U = random.random()
        if U < probs[Y] / (c * q_probs[Y]):
            return Y

# III) Comparación
def comparar(n=10000):
    # Transformada inversa
    inicio = time.time()
    muestras_inv = [transformada_inversa() for _ in range(n)]
    tiempo_inv = time.time() - inicio
    
    # Aceptación y rechazo
    inicio = time.time()
    muestras_rech = [aceptacion_rechazo() for _ in range(n)]
    tiempo_rech = time.time() - inicio
    
    print(f"Transformada inversa: {tiempo_inv:.4f}s")
    print(f"Aceptación y rechazo: {tiempo_rech:.4f}s")
    print(f"La transformada inversa es {tiempo_rech/tiempo_inv:.2f}x\
           más rápida")
    
    # Verificar distribuciones
    print("\nDistribución observada (Inv vs Rech vs Teórica):")
    print(f"{'Valor':>5} | {'Inversa':>8} | {'Rechazo':>8} | {'Teórica':>8}")
    print("-" * 38)
    for i in range(5):
        obs_inv = muestras_inv.count(i) / n
        obs_rech = muestras_rech.count(i) / n
        print(f"{i:5d} | {obs_inv:8.4f} | {obs_rech:8.4f} | {probs[i]:8.4f}")

if __name__ == "__main__":
    comparar(10000)