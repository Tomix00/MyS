import random
import math
import time


def cauchy_inversa(lam):
    u = random.random()
    return lam * math.tan(math.pi * (u - 0.5))


def ejercicio11():
    for lam in [1.0, 2.5, 0.3]:
        n = 10000
        muestras = [cauchy_inversa(lam) for _ in range(n)]
        dentro = sum(1 for x in muestras if -lam < x < lam)
        prob_obs = dentro / n
        prob_teo = 0.5
        print(f"lambda={lam:.1f} | P(-lambda<X<lambda) obs={prob_obs:.4f} teo={prob_teo:.4f}")

    # Comparacion eficiencia con metodo de razon (ej10)
    n = 100000
    inicio = time.time()
    for _ in range(n):
        cauchy_inversa(1.0)
    t_inv = time.time() - inicio

    def cauchy_razon():
        while True:
            u = random.random()
            v = 2 * random.random() - 1
            if u * u + v * v <= 1:
                return v / u
    inicio = time.time()
    for _ in range(n):
        cauchy_razon()
    t_raz = time.time() - inicio

    print(f"\nComparacion eficiencia ({n} generaciones):")
    print(f"Transformada inversa: {t_inv:.4f}s")
    print(f"Razon entre uniformes: {t_raz:.4f}s")
    print(f"Razon es {t_inv / t_raz:.2f}x mas rapida" if t_raz > 0 else "")

if __name__ == "__main__":
    ejercicio11()
