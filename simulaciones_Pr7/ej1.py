"""Ejercicio 1: Mendel genetics chi-squared test + simulation"""
import math
import random
from scipy.stats import chi2

obs = [141, 291, 132]
n = sum(obs)
p = [1/4, 1/2, 1/4]
k = len(obs)

chi2_obs = sum((o - n * pi) ** 2 / (n * pi) for o, pi in zip(obs, p))
p_chi2 = 1 - chi2.cdf(chi2_obs, k - 1)

B = 100000
count = 0
for _ in range(B):
    sim = [random.random() for _ in range(n)]
    freq = [0] * k
    for u in sim:
        if u < p[0]:
            freq[0] += 1
        elif u < p[0] + p[1]:
            freq[1] += 1
        else:
            freq[2] += 1
    chi2_sim = sum((f - n * pi) ** 2 / (n * pi) for f, pi in zip(freq, p))
    if chi2_sim >= chi2_obs:
        count += 1
p_sim = count / B

print(f"Ejercicio 1 - Mendel")
print(f"Chi2 observado: {chi2_obs:.4f}")
print(f"p-valor (chi2 teorico): {p_chi2:.4f}")
print(f"p-valor (simulacion): {p_sim:.4f}")
