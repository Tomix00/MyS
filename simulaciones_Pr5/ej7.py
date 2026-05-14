from random import random
import math
import time

def generaX_inversa():
    U = random()
    return math.exp(U)

def generaX_rechazo():
    while True:
        Y = 1 + (math.e - 1) * random()
        U = random()
        if U < 1 / Y:
            return Y
        
def eficiencia():
    n = 10000

    start = time.time()
    suma_inv = 0
    for _ in range(n):
        suma_inv += generaX_inversa()
    timepo_inv = time.time() - start
    media_inv = suma_inv / n

    start = time.time()
    suma_rech = 0
    for _ in range(n):
        suma_rech += generaX_rechazo()
    tiempo_rech = time.time() - start
    media_rech = suma_rech / n

    print(f"Esperanza exacta: {math.e - 1:.6f}")
    print(f"Inversa: media = {media_inv:.6f}, tiempo = {timepo_inv:.4f} seg")
    print(f"Rechazo: media = {media_rech:.6f}, tiempo = {tiempo_rech:.4f} seg")

def ejercicio7c():
    def estimar_probabilidad(generador, n=10000):
        cuenta = 0
        for _ in range(n):
            if generador() <= 2:
                cuenta += 1
        return cuenta / n
    
    print(f"P(X<=2) exacta: {math.log(2):.6f}")
    print(f"Inversa: {estimar_probabilidad(generaX_inversa):.6f}")
    print(f"Rechazo: {estimar_probabilidad(generaX_rechazo):.6f}")


if __name__ == "__main__":
    ejercicio7c()

