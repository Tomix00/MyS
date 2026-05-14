from random import random
from transf_inversa import continousGenerators as cg

def ejercicio3a(p_list, gen_list):
    """
    p_list: Lista de probabilidades
    gen_list: lista de funciones que
              generan una variable
              de la distribución F_i
    """
    U = random()
    acum = 0
    for i, p in enumerate(p_list):
        acum += p
        if U < acum:
            return gen_list[i]()
    return gen_list[-1]()

def ejercicio3b():
    p = [0.5, 0.3, 0.2]
    medias = [3, 5, 7]
    lambdas = [1/mu for mu in medias]

    U = random()
    acum = 0
    for i, prob in enumerate(p):
        acum += prob
        if U < acum:
            return cg.exponentialL(lambdas[i])

def simulate():
    n = 10000
    suma = 0
    for _ in range(n):
        suma += ejercicio3b()

    media_estimada = suma / n

    print(f"Esperanza exacta: 4.4")
    print(f"Media estiamda con {n} repeticiones: {media_estimada:.4f}")

if __name__ == "__main__":
    simulate()