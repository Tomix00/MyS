import random
import math

def poisson_process(lam, T):
    tiempos = []
    t = 0
    while True:
        u = random.random()
        t += -math.log(u) / lam
        if t > T:
            break
        tiempos.append(t)
    return tiempos

def ejercicio12(lam=5.0, T=1.0):
    eventos = poisson_process(lam, T)
    n = len(eventos)
    print(f"Parametros: lambda={lam}, T={T}")
    print(f"Numero de eventos: {n}")
    print(f"Tiempos de arribo: {[round(t, 4) for t in eventos]}")

if __name__ == "__main__":
    ejercicio12()
