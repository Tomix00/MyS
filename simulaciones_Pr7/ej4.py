"""Ejercicio 4: KS test for exponential(mean=50)"""
import math
from scipy.stats import kstest

data = [86.0, 133.0, 75.0, 22.0, 11.0, 144.0, 78.0, 122.0, 8.0, 146.0, 33.0, 41.0, 99.0]
lam = 1 / 50.0  # rate parameter

D, p = kstest(data, 'expon', args=(0, 50))
print(f"Ejercicio 4 - Test KS para Exponencial con media 50")
print(f"Datos: {data}")
print(f"Estadistico D = {D:.4f}")
print(f"p-valor = {p:.4f}")
