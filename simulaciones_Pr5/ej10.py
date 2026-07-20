import random
import math
import time


def cauchy_razon():
    while True:
        u = random.random()
        v = 2 * random.random() - 1
        if u * u + v * v <= 1:
            return v / u


def cauchy_lambda(lam):
    return lam * cauchy_razon()


def ejercicio10():
    for lam in [1.0, 2.5, 0.3]:
        n = 10000
        muestras = [cauchy_lambda(lam) for _ in range(n)]
        dentro = sum(1 for x in muestras if -lam < x < lam)
        prob_obs = dentro / n
        prob_teo = 0.5  # P(-λ < X < λ) = 2 * arctan(1)/π = 2 * π/4 / π = 1/2
        print(f"lambda={lam:.1f} | P(-lambda<X<lambda) obs={prob_obs:.4f} teo={prob_teo:.4f}")

if __name__ == "__main__":
    ejercicio10()
