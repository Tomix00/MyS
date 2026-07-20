from transf_inversa import continousGenerators as cg
from random import random
import math

# ----- Ejercicio 2-a -----
def pareto_sample(a):
    U = random()
    return U ** (-1/a)

def erlang_sample(k: int, mu: float):
    lam = 1 / mu
    suma = 0
    for _ in range(k):
        suma += cg.exponentialL(lam)
    return suma

def weibull_sample(lam, beta):
    U = random()
    return lam * (-math.log(U)) ** (1/beta)

# ----- Ejercicio 2-b -----
def ejercicio2():
    n = 10000

    sum_pareto = 0
    sum_erlang = 0
    sum_weibull = 0

    for _ in range(n):
        sum_pareto += pareto_sample(2)
        sum_erlang += erlang_sample(2, 2)
        sum_weibull += weibull_sample(1, 2)
    
    media_pareto = sum_pareto / n
    media_erlang = sum_erlang / n
    media_weibull = sum_weibull / n

    print(f"Pareto: {media_pareto:.4f}")
    print(f"Erlang: {media_erlang:.4f}")
    print(f"Weibull: {media_weibull:.4f}")

if __name__ == "__main__":
    ejercicio2()