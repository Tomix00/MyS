import random
import math

def simulate_fans(lam=5.0, T=1.0):
    """Simula llegada de aficionados en T=1 hora.
    Buses llegan segun Poisson(lam), cada bus tiene capacidad U{20,...,40}."""
    total = 0
    t = 0
    while True:
        u = random.random()
        t += -math.log(u) / lam
        if t > T:
            break
        capacidad = random.randint(20, 40)
        total += capacidad
    return total

def ejercicio13():
    n = 10000
    resultados = [simulate_fans() for _ in range(n)]
    media = sum(resultados) / n
    print(f"Simulacion de {n} horas:")
    print(f"Promedio de aficionados: {media:.2f}")
    print(f"Esperanza teorica: {5 * 30:.2f}  (5 buses/hora * capacidad media 30)")

if __name__ == "__main__":
    ejercicio13()
