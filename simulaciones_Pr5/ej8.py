from random import random
import math
import time

def triangular_sum():
    return random() + random()

def triangular_inverse():
    U = random()
    if U < 0.5:
        return math.sqrt(2 * U)
    else:
        return 2 + math.sqrt(2 * (1-U))
    
def triangular_pdf(x):
    if 0 <= x < 1:
        return x
    elif 1 <= x < 2:
        return 2-x
    else:
        return 0

def triangular_rejection():
    while True:
        Y = 2 * random()
        U = random()
        if U < triangular_pdf(Y):
            return Y
        
def ejercicio8a():
    n = 10000
    suma_sum = 0
    suma_inv = 0
    suma_rech = 0

    start_sum = time.time()
    for _ in range(n):
        suma_sum += triangular_sum()
    end_sum = time.time()
    print(f"Suma: {end_sum - start_sum:.4f} seg, media: {suma_sum / n:.6f}")

    start_inv = time.time()
    for _ in range(n):
        suma_inv += triangular_inverse()
    end_inv = time.time()
    print(f"Inversa: {end_inv - start_inv:.4f} seg, media: {suma_inv / n:.6f}")

    start_rech = time.time()
    for _ in range(n):
        suma_rech += triangular_rejection()
    end_rech = time.time()
    print(f"Rechazo: {end_rech - start_rech:.4f} seg, media: {suma_rech / n:.6f}")

def ejercicio8b():
    x0 = 1.5
    p_teorica = 0.125
    n = 10000

    lista = [
        ("Suma", triangular_sum),
        ("Inversa", triangular_inverse),
        ("Rechazo", triangular_rejection)
        ]

    for nombre, func in lista:
        cuenta = 0
        for _ in range(n):
            if func() > x0:
                cuenta += 1
        prop = cuenta / n
        print(f"{nombre}: proporción = {prop:.4f} (teórica: {p_teorica:.3f})")

if __name__ == "__main__":
    ejercicio8b()
    