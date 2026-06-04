import random
import math

def ejercicio_2_i():
    d = 0.01
    n = 1
    x = random.uniform(0, 1)
    f = math.exp(x) / math.sqrt(2 * x)
    mean = f
    scuad = 0.0

    while n <= 100 or math.sqrt(scuad / n) >= d:
        n += 1
        x = random.uniform(0, 1)
        f = math.exp(x) / math.sqrt(2 * x)
        mean_ant = mean
        mean = mean_ant + (f - mean_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (mean - mean_ant) ** 2

    return n, mean, math.sqrt(scuad / n)

def ejercicio_2_ii():
    d = 0.01
    n = 1
    u = random.uniform(0, 1)
    t = u / (1 - u)
    f = (u ** 2 / (1 - u) ** 4) * math.exp(-(u / (1 - u)) ** 2)
    mean = f
    scuad = 0.0

    while n <= 100 or math.sqrt(scuad / n) >= d:
        n += 1
        u = random.uniform(0, 1)
        t = u / (1 - u)
        f = (u ** 2 / (1 - u) ** 4) * math.exp(-(u / (1 - u)) ** 2)
        mean_ant = mean
        mean = mean_ant + (f - mean_ant) / n
        scuad = scuad * (1 - 1 / (n - 1)) + n * (mean - mean_ant) ** 2

    return n, 2 * mean, math.sqrt(scuad / n)

if __name__ == "__main__":

    print("Ejercicio 2 i) ∫₀¹ e^x/√(2x) dx")
    n1, est1, err1 = ejercicio_2_i()
    print(f"n = {n1}")
    print(f"Estimación = {est1:.6f}")
    print(f"Desviación = {err1:.6f}\n")

    print("Ejercicio 2 ii) ∫₋∞^∞ x² exp(-x²) dx = 2∫₀^∞ x² exp(-x²) dx")
    n2, est2, err2 = ejercicio_2_ii()
    print(f"n = {n2}")
    print(f"Estimación = {est2:.6f}")
    print(f"Desviación = {err2:.6f}")