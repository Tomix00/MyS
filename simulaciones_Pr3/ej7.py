import sys
import numpy as np

def simular_N():
    sum = 0
    count = 0

    while sum <= 1:
        sum += np.random.uniform(0, 1)
        count += 1
    return count


def estimar(n: int):
    return np.mean([simular_N() for _ in range(n)])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python ej7.py <N>")
        sys.exit(1)
    elif int(sys.argv[1]) <= 0:
        print("N debe ser un entero positivo.")
        sys.exit(1)
    N = int(sys.argv[1])

    valor_estimado = estimar(N)

    print(f"En {N} iteraciones:")
    print(f"Valor estimado de E[N]: {valor_estimado}")