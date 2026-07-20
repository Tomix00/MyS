import random
import math

def thinning_poisson(lam_func, T, lam_max):
    """Adelgazamiento para Poisson no homogeneo con intensidad lam_func en [0,T]."""
    tiempos = []
    t = 0
    while True:
        u1 = random.random()
        t += -math.log(u1) / lam_max
        if t > T:
            break
        u2 = random.random()
        if u2 < lam_func(t) / lam_max:
            tiempos.append(t)
    return tiempos


def lam1(t):
    return 3 + 4 / (t + 1)


def lam2(t):
    return (t - 2) ** 2 - 5 * t + 17


def lam3(t):
    if 2 <= t <= 3:
        return t / 2 - 1
    elif 3 <= t <= 6:
        return 1 - t / 6
    else:
        return 0


def ejercicio14():
    casos = [
        ("lambda(t)=3+4/(t+1), T=3", lam1, 3, 7),
        ("lambda(t)=(t-2)^2-5t+17, T=5", lam2, 5, 17),
        ("lambda(t) por tramos, T=6", lam3, 6, 0.5),
    ]
    for nombre, func, T, lam_max in casos:
        tiempos = thinning_poisson(func, T, lam_max)
        print(f"{nombre}")
        print(f"  N eventos: {len(tiempos)}")
        if tiempos:
            print(f"  Tiempos: {[round(t, 3) for t in tiempos[:8]]}{'...' if len(tiempos) > 8 else ''}")
        print()

    print("--- Mejora: adelgazamiento por intervalos ---")
    print("Para lam1(t) en [0,3]: max en t=0 vale 7, decrece a 4 en t=3.")
    print("  Conviene dividir en subintervalos con cota mas ajustada.")
    print("Para lam2(t) en [0,5]: parabola con max = 17 en t=0.")
    print("  Dividir en [0,2] (decreciente: max 17) y [2,5] (creciente: max 14).")
    print("Para lam3(t) en [2,6]: max = 0.5 en t=3,")
    print("  valor por tramos ya acotado eficientemente.")

if __name__ == "__main__":
    ejercicio14()
