"""Ejercicio 9: Exponential goodness of fit for vibration data"""
from scipy.stats import kstest

data = [1.6, 10.3, 3.5, 13.5, 18.4, 7.7, 24.3, 10.7, 8.4, 4.9, 7.9, 12, 16.2, 6.8, 14.7]
mean_est = sum(data) / len(data)

D, p = kstest(data, 'expon', args=(0, mean_est))
print(f"Ejercicio 9 - Vida util componentes (Exponencial)")
print(f"Datos: {data}")
print(f"Media estimada: {mean_est:.2f}")
print(f"Estadistico D = {D:.4f}")
print(f"p-valor = {p:.4f}")
