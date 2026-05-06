import random
import time
from transf_inversa import discreteGenerators as dg

valores = list(range(1, 11))
probs = [0.11, 0.14, 0.09, 0.08, 0.12, 0.10, 0.09, 0.07, 0.11, 0.09]

# Precalculo de F para transforada inversa
F = []
acum = 0
for p in probs:
    acum += p
    F.append(acum)

# Urna: cada valor i aparece int(p_1 * 100) veces
urna = []
for i, p in enumerate(probs, start=1):
    urna.extend([i] * int(p * 100))

def rechazo_cmin():
    # p_j / (1/10) <= c
    # para todo j, c >= 10 * max{p_j} = 10 * 0.14 = 1.4
    c = 1.4
    while True:
        Y = dg.udiscrete1n(10)
        U = random.random()
        if U < (10 * probs[Y-1]) / c :
            return Y
        
def rechazo_c3():
    c = 3
    while True:
        Y = dg.udiscrete1n(10)
        U = random.random()
        if U < (10 * probs[Y-1]) / c :
            return Y
        
def transformada_inversa():
    U = random.random()
    for i, f in enumerate(F):
        if U < f:
            return i + 1
    return 10

def metodo_urna():
    indice = dg.udiscrete1n(100) - 1
    return urna[indice]

def comparar(n=10000):
    metodos = [
        ("Rechazo c=1.4", rechazo_cmin),
        ("Rechazo c=3", rechazo_c3),
        ("Transformada Inversa", transformada_inversa),
        ("Metodo Urna", metodo_urna)
    ]

    print(f"Compararcion con {n} simulaciones:")
    for nombre, metodo in metodos:
        inicio = time.time()
        muestras = [metodo() for _ in range(n)]
        tiempo = time.time() - inicio
        
        # Frecuencias observadas
        freqs = [muestras.count(i) / n for i in range(1, 11)]
        error = sum(abs(freqs[i] - probs[i]) for i in range(10)) / 10
        
        print(f"{nombre:22} | Tiempo: {tiempo:.4f}s | Error: {error:.6f}")

if __name__ == "__main__":
    print("Generación de 5 valores con cada método:\n")
    for _ in range(5):
        print(f"c=1.4: {rechazo_cmin():2d}, c=3: {rechazo_c3():2d}, "
              f"inversa: {transformada_inversa():2d}, urna: {metodo_urna():2d}")
    
    comparar(10000)