"""Ejercicio 6: Wheel of fortune goodness of fit"""
import random
from scipy.stats import chi2

p = [0.31, 0.22, 0.12, 0.10, 0.08, 0.06, 0.04, 0.04, 0.02, 0.01]
obs = [188, 138, 87, 65, 48, 32, 30, 34, 13, 2]
n = sum(obs)
k = len(p)

chi2_obs = sum((o - n * pi) ** 2 / (n * pi) for o, pi in zip(obs, p))
p_chi2 = 1 - chi2.cdf(chi2_obs, k - 1)

B = 10000
count = 0
for _ in range(B):
    freq = [0] * k
    for _ in range(n):
        u = random.random()
        acc = 0
        for i, pi in enumerate(p):
            acc += pi
            if u < acc:
                freq[i] += 1
                break
    chi2_sim = sum((f - n * pi) ** 2 / (n * pi) for f, pi in zip(freq, p))
    if chi2_sim >= chi2_obs:
        count += 1
p_sim = count / B

print(f"Ejercicio 6 - Rueda de la fortuna")
print(f"Chi2 observado: {chi2_obs:.4f}")
print(f"p-valor (chi2 teorico): {p_chi2:.4f}")
print(f"p-valor (simulacion): {p_sim:.4f}")
