from random import random
import math

def udiscrete1n(n: int) -> int:
    u = random()
    return int(n * u) + 1

def varY():
    u = random()
    if u < 0.2:
        k = udiscrete1n(5)
        return 2*k-1
    else:
        k = udiscrete1n(5)
        return 2*k

def rechazoX():
    c = 16 * math.exp(-2)
    while True:
        u1 = random()
        W = -2 * math.log(1 - u1)
        
        u2 = random()
        if u2 < (W**2 *math.exp(-W/2)) / c:
            return W

def jugador(p, lam):
    N = 0
    T = 0.0
    while True:
        U = random()
        X = -math.log(1 - U) / lam
        T += X
        N += 1
        if random() < p:
            return N, T

def ej4b():
    p = 0.4
    lam = 0.5
    n_sim = 10000
    suma_T = 0.0
    for _ in range(n_sim):
        _, T = jugador(p, lam)
        suma_T += T
    media_T = suma_T / n_sim
    print(f"Tiempo promedio estimado: {media_T:.4f} minutos")

def ej4c():
    contador = 0
    p = 0.4
    lam = 0.5
    n_sim = 10000
    for _ in range(n_sim):
        N, _ = jugador(p, lam)
        if N >= 3:
            contador += 1
    prob_est = contador / n_sim
    print(f"Probabilidad estimada de N>=3: {prob_est:.4f}")

if __name__ == "__main__":
    ej4b()
    ej4c()