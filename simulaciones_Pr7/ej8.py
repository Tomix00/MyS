"""Ejercicio 8: t-Student vs Normal KS test"""
import math
import random
from scipy.stats import kstest

def rt(df):
    x = random.gauss(0.0, 1.0)
    y = 2.0 * random.gammavariate(0.5 * df, 2.0)
    return x / math.sqrt(y / df)

def normal_cdf(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

print(f"Ejercicio 8 - t-Student vs N(0,1) via KS\n")
print(f"{'n':>6} | {'D':>8} | {'p-valor':>8}")
print("-" * 30)
for n in [10, 20, 100, 1000]:
    data = [rt(11) for _ in range(n)]
    D, p = kstest(data, 'norm', args=(0, 1))
    print(f"{n:6d} | {D:8.4f} | {p:8.4f}")
