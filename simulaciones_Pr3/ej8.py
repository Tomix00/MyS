import sys
import numpy as np

THRESHOLD = np.exp(-3)


def simulate_trial():
    prod = 1.0
    n = 0
    while prod >= THRESHOLD:
        prod *= np.random.uniform(0, 1)
        n += 1
    return n - 1


def ejercicio8a(n: int):
    return np.mean([simulate_trial() for _ in range(n)])


def ejercicio8b(n: int):
    counts = np.zeros(7, dtype=int)
    for _ in range(n):
        val = simulate_trial()
        if val <= 6:
            counts[val] += 1
    return counts / n


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("Uso: python ej8.py <N> [opcion]")
        print("  opcion 1 (default): estimar E[N]")
        print("  opcion 2: estimar P(N=i) para i=0..6")
        sys.exit(1)

    N = int(sys.argv[1])
    opcion = int(sys.argv[2]) if len(sys.argv) == 3 else 1

    if opcion == 1:
        valor = ejercicio8a(N)
        print(f"En {N} iteraciones:")
        print(f"E[N] estimado = {valor:.6f}")
    elif opcion == 2:
        probs = ejercicio8b(N)
        print(f"Estimacion de P(N=i) con {N} iteraciones:")
        for i, p in enumerate(probs):
            print(f"  P(N={i}) = {p:.6f}")
