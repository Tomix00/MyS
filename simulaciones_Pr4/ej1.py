import sys
import random
from transf_inversa import discreteGenerators as dg


def simulate_trial(n=100):
    perm = list(range(1, n + 1))
    for i in range(n):
        j = random.randint(i, n - 1)
        perm[i], perm[j] = perm[j], perm[i]
    matches = sum(1 for i in range(n) if perm[i] == i + 1)
    first_r_matches = all(perm[i] == i + 1 for i in range(10))
    return matches, first_r_matches


def ejercicio1(n_iter):
    total_matches = []
    first_10_matches = 0
    for _ in range(n_iter):
        x, r10 = simulate_trial()
        total_matches.append(x)
        if r10:
            first_10_matches += 1
    mean = sum(total_matches) / n_iter
    var = sum((x - mean) ** 2 for x in total_matches) / n_iter
    p_first10 = first_10_matches / n_iter
    return mean, var, p_first10


if __name__ == "__main__":
    ns = [100, 1000, 10000, 100000]
    print(f"{'n':>8} | {'E[X]':>8} | {'Var[X]':>8} | {'P(primeras 10)':>15}")
    print("-" * 48)
    for n in ns:
        mean, var, p10 = ejercicio1(n)
        print(f"{n:8d} | {mean:8.4f} | {var:8.4f} | {p10:15.10f}")
    print("\nValores teóricos:")
    print(f"  E[X] = 1, Var[X] = 1")
    print(f"  P(primeras r coinciden) = 1 / P(100,10) = {1 / (100 * 99 * 98 * 97 * 96 * 95 * 94 * 93 * 92 * 91):.10f}")
