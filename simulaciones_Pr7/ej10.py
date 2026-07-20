"""Ejercicio 10: Normal goodness of fit"""
import math
from scipy.stats import kstest, shapiro, norm

data = [91.9, 97.8, 111.4, 122.3, 105.4, 95.0, 103.8, 99.6, 96.6, 119.3, 104.8, 101.7]
mu = sum(data) / len(data)
var = sum((x - mu) ** 2 for x in data) / (len(data) - 1)
sigma = math.sqrt(var)

# KS test with estimated parameters
D_ks, p_ks = kstest(data, 'norm', args=(mu, sigma))

# Shapiro-Wilk test (more powerful for normality)
W, p_sw = shapiro(data)

print(f"Ejercicio 10 - Prueba de Normalidad")
print(f"Datos: {data}")
print(f"Media={mu:.2f}, Desvio={sigma:.2f}")
print(f"KS: D={D_ks:.4f}, p-valor={p_ks:.4f}")
print(f"Shapiro-Wilk: W={W:.4f}, p-valor={p_sw:.4f}")
