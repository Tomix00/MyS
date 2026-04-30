"""

Sum_{K=1}^N exp(k/N) where N=10.000

a) Script
b) aproximate with 100 random numbers
c) calculate the sum with N=100, and
   compare the exact value with the
   two previous aproximations, and time
"""

from transf_inversa import discreteGenerators as dg
from math import exp
import time

def ejercicio2():
    start_time_exact = time.perf_counter()
    def exact_number():
        sum = 0
        N = 10000
        for k in range(1,N+1):
            sum += exp(k/N)
        return sum
    end_time_exact = time.perf_counter()

    start_time_aprox = time.perf_counter()
    def aproximate():
        sum = 0
        n = 10000
        Nsim = 100
        for k in range(1,Nsim):
            u = dg.udiscrete1n(10000)
            sum += exp(k+1/u)
        sum = sum / Nsim
        return sum
    end_time_aprox = time.perf_counter()

    a = exact_number()
    b = aproximate()
    comp = a-b if (a-b)>0 else b-a
    exact_time = end_time_exact - start_time_exact
    aprox_time = end_time_aprox - start_time_aprox
    print(f"a) exact value: {a:.6f}")
    print(f"b) aproximate with 100 random numbers: {b:.6f}")
    print(f"c) comparation: {comp:.6f}")
    print(f"c) times:\n\texact value -> {exact_time:.6f}\n\taprox value -> {aprox_time:.6f}")
    




if __name__ == "__main__":
    ejercicio2()

    