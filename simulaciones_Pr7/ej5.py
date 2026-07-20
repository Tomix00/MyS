"""Ejercicio 5: Binomial goodness of fit with unknown p"""
import math
import random
from scipy.stats import chi2

data = [6, 7, 3, 4, 7, 3, 7, 2, 6, 3, 7, 8, 2, 1, 3, 5, 8, 7]
n_trials = 8
n = len(data)
p_est = sum(data) / (n * n_trials)

# Build categories (group tails for expected >= 5)
cats = list(range(0, n_trials + 1))
obs_counts = [data.count(i) for i in cats]

# Expected under Bin(8, p_est)
def binom_pmf(k, n, p):
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

exp_counts = [n * binom_pmf(k, n_trials, p_est) for k in cats]

# Group categories with expected < 5
while min(exp_counts) < 1:
    idx = exp_counts.index(min(exp_counts))
    if idx == 0:
        exp_counts[1] += exp_counts[0]
        obs_counts[1] += obs_counts[0]
    elif idx == len(exp_counts) - 1:
        exp_counts[-2] += exp_counts[-1]
        obs_counts[-2] += obs_counts[-1]
    else:
        if exp_counts[idx - 1] <= exp_counts[idx + 1]:
            exp_counts[idx - 1] += exp_counts[idx]
            obs_counts[idx - 1] += obs_counts[idx]
        else:
            exp_counts[idx + 1] += exp_counts[idx]
            obs_counts[idx + 1] += obs_counts[idx]
    exp_counts.pop(idx)
    obs_counts.pop(idx)

k_groups = len(obs_counts)
chi2_obs = sum((o - e) ** 2 / e for o, e in zip(obs_counts, exp_counts))
df = k_groups - 1 - 1  # -1 for categories, -1 for estimated p
p_chi2 = 1 - chi2.cdf(chi2_obs, df)

# Simulation
B = 100000
count = 0
for _ in range(B):
    sim_data = [sum(1 for _ in range(n_trials) if random.random() < p_est) for _ in range(n)]
    sim_obs = [sim_data.count(i) for i in cats]
    sim_exp = [n * binom_pmf(k, n_trials, p_est) for k in cats]
    # Same grouping
    while min(sim_exp) < 1:
        idx = sim_exp.index(min(sim_exp))
        if idx == 0:
            sim_exp[1] += sim_exp[0]; sim_obs[1] += sim_obs[0]
        elif idx == len(sim_exp) - 1:
            sim_exp[-2] += sim_exp[-1]; sim_obs[-2] += sim_obs[-1]
        else:
            if sim_exp[idx - 1] <= sim_exp[idx + 1]:
                sim_exp[idx - 1] += sim_exp[idx]; sim_obs[idx - 1] += sim_obs[idx]
            else:
                sim_exp[idx + 1] += sim_exp[idx]; sim_obs[idx + 1] += sim_obs[idx]
        sim_exp.pop(idx); sim_obs.pop(idx)
    chi2_sim = sum((o - e) ** 2 / e for o, e in zip(sim_obs, sim_exp))
    if chi2_sim >= chi2_obs:
        count += 1
p_sim = count / B

print(f"Ejercicio 5 - Binomial(8, p) con p desconocido")
print(f"p estimado: {p_est:.4f}")
print(f"Chi2 observado: {chi2_obs:.4f} (df={df})")
print(f"p-valor (chi2 teorico): {p_chi2:.4f}")
print(f"p-valor (simulacion): {p_sim:.4f}")
