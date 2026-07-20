"""Ejercicio 2: fair die chi-squared test + simulation"""
import random
from scipy.stats import chi2

obs = [158, 172, 164, 181, 160, 165]
n = sum(obs)
k = 6
p = [1/6] * k

chi2_obs = sum((o - n / k) ** 2 / (n / k) for o in obs)
p_chi2 = 1 - chi2.cdf(chi2_obs, k - 1)

B = 100000
count = 0
for _ in range(B):
    sim = [random.randint(1, 6) for _ in range(n)]
    freq = [sim.count(i) for i in range(1, 7)]
    chi2_sim = sum((f - n / k) ** 2 / (n / k) for f in freq)
    if chi2_sim >= chi2_obs:
        count += 1
p_sim = count / B

print(f"Ejercicio 2 - Dado honesto")
print(f"Chi2 observado: {chi2_obs:.4f}")
print(f"p-valor (chi2 teorico): {p_chi2:.4f}")
print(f"p-valor (simulacion): {p_sim:.4f}")
