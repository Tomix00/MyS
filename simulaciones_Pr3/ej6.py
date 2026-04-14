import numpy as np
import sys


def valorpi(n: int):
    hit = 0
    for _ in range(n):
        u = 2 * np.random.rand() - 1
        v = 2 * np.random.rand() - 1
        if u**2 + v**2 <= 1:
            hit += 1
    return 4 * hit / n


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ej5.py <n>")
        sys.exit(1)
    elif int(sys.argv[1]) < 0:
        print("n must be a non-negative integer")
        sys.exit(1)
    n = int(sys.argv[1])

    pi_estimate = valorpi(n)
    print(f"En {n} iteraciones:")
    print(f"Valor estimado de pi: {pi_estimate}")
    print(f"Valor real de pi en numpy: {np.pi}")
    print(f"Error absoluto: {abs(pi_estimate - np.pi)}")
