"""Ejercicio 3: randomness test (runs test)"""
import random
import math

data = [0.12, 0.18, 0.06, 0.33, 0.72, 0.83, 0.36, 0.27, 0.77, 0.74]
n = len(data)

# Runs test: count runs above/below median
med = sorted(data)[n // 2]
runs = 1
for i in range(1, n):
    if (data[i] >= med) != (data[i-1] >= med):
        runs += 1

n1 = sum(1 for x in data if x >= med)
n2 = n - n1

# Normal approximation for runs
mu = 2 * n1 * n2 / n + 1
sigma = math.sqrt((mu - 1) * (mu - 2) / (n - 1))
z = (runs - mu) / sigma
p_valor = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))

# Simulation
B = 100000
count = 0
for _ in range(B):
    sim = [random.random() for _ in range(n)]
    med_sim = sorted(sim)[n // 2]
    r = 1
    for i in range(1, n):
        if (sim[i] >= med_sim) != (sim[i-1] >= med_sim):
            r += 1
    if abs(r - mu) >= abs(runs - mu):
        count += 1
p_sim = count / B

print(f"Ejercicio 3 - Prueba de aleatoriedad")
print(f"Datos: {data}")
print(f"Numero de rachas observado: {runs}")
print(f"p-valor (aprox normal): {p_valor:.4f}")
print(f"p-valor (simulacion): {p_sim:.4f}")
