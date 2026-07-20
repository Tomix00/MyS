from random import random
import math
import time

def generate_X_inverse():
    U = random()
    return math.exp(U)

def generate_X_rejection():
    while True:
        Y = 1 + (math.e - 1) * random()
        U = random()
        if U < 1 / Y:
            return Y
        
def ejercicio7a():
    n = 10000

    start = time.time()
    suma_inv = 0
    for _ in range(n):
        suma_inv += generate_X_inverse()
    timepo_inv = time.time() - start
    media_inv = suma_inv / n

    start = time.time()
    suma_rech = 0
    for _ in range(n):
        suma_rech += generate_X_rejection()
    tiempo_rech = time.time() - start
    media_rech = suma_rech / n

    print(f"Esperanza exacta: {math.e - 1:.6f}")
    print(f"Inversa: media = {media_inv:.6f}, tiempo = {timepo_inv:.4f} seg")
    print(f"Rechazo: media = {media_rech:.6f}, tiempo = {tiempo_rech:.4f} seg")

def ejercicio7c():
    def estimate_probability(generador, n=10000):
        cuenta = 0
        for _ in range(n):
            if generador() <= 2:
                cuenta += 1
        return cuenta / n
    
    print(f"P(X<=2) exacta: {math.log(2):.6f}")
    print(f"Inversa: {estimate_probability(generate_X_inverse):.6f}")
    print(f"Rechazo: {estimate_probability(generate_X_rejection):.6f}")


if __name__ == "__main__":
    ejercicio7c()

