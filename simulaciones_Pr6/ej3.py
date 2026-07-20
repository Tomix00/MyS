import random
import math
from statistics import NormalDist

z = NormalDist().inv_cdf(0.975)

def sequential_mc(f_sample, target_se=0.001, min_n=1000):
    n = 0
    mean = 0.0
    M2 = 0.0
    while True:
        n += 1
        x = f_sample()
        delta = x - mean
        mean += delta / n
        M2 += delta * (x - mean)
        if n >= min_n:
            var = M2 / (n - 1)
            se = math.sqrt(var / n)
            if z * se < target_se:
                break
    ci = (mean - z * se, mean + z * se)
    return n, mean, se, ci

def mc_i():
    a, b = math.pi, 2 * math.pi
    x = random.uniform(a, b)
    return (b - a) * math.sin(x) / x

def mc_ii():
    u = random.random()
    x = u / (1 - u)
    f = 3 / (3 + x ** 4)
    return f / (1 - u) ** 2

def ejercicio3():
    for nombre, sample_fn in [("i) int sin(x)/x dx", mc_i),
                                ("ii) int 3/(3+x^4) dx", mc_ii)]:
        print(f"\n{nombre}")
        for n in [1000, 5000, 7000]:
            est = sum(sample_fn() for _ in range(n)) / n
            print(f"  n={n}: I={est:.4f}")
        n, mean, se, ci = sequential_mc(sample_fn)
        print(f"  N_S={n}: I={mean:.4f} IC=[{ci[0]:.4f},{ci[1]:.4f}]")

if __name__ == "__main__":
    ejercicio3()
