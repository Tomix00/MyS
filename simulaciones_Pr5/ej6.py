from random import random
import time

def max_uniforme_rechazo(n):
    while True:
        Y = random()
        U = random()
        if U < Y ** (n-1):
            return Y

def max_uniforme_inv(n):
    U = random()
    return U ** (1 / n)

def max_uniforme_composicion(n):
    maximo = 0
    for _ in range(n):
        U = random()
        if U > maximo:
            maximo = U
    return maximo

def eficiencia():
    n = 10
    repeticiones = 10000

    start_inv = time.time()
    for _ in range(repeticiones):
        _ += max_uniforme_inv(n)
    end_inv = time.time()
    print(f"Inversa: {end_inv - start_inv:.4f} seg")

    start_comp = time.time()
    for _ in range(repeticiones):
        _ += max_uniforme_composicion(n)
    end_comp = time.time()
    print(f"Composicion: {end_comp - start_comp:.4f} seg")

    start_rech = time.time()
    for _ in range(repeticiones):
        _ += max_uniforme_rechazo(n)
    end_rech = time.time()
    print(f"Rechazo: {end_rech - start_rech:.4f} seg")

if __name__ == "__main__":
    eficiencia()