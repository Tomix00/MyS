"""Ejercicio 7: KS test for simulated Exp(1) data"""
import math
import random
from scipy.stats import kstest

random.seed(12345)
data = [-math.log(random.random()) for _ in range(30)]

D, p = kstest(data, 'expon', args=(0, 1))
print(f"Ejercicio 7 - Test KS para 30 valores Exp(1) simulados")
print(f"Estadistico D = {D:.4f}")
print(f"p-valor = {p:.4f}")
