import sys
import numpy as np

def ejercicio9b(n: int):
    win = 0

    for _ in range(n):
        d1 = np.random.randint(1, 7)
        if d1 in (1,6):
            d2 = np.random.randint(1, 7)
            points = 2*d2
        else:
            d3 = np.random.randint(1, 7)
            d4 = np.random.randint(1, 7)
            points = d3 + d4
        if points > 6:
            win+=1

    return win/n

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python ej9.py <N>")
        sys.exit(1)
    elif int(sys.argv[1]) <= 0:
        print("N debe ser un entero positivo.")
        sys.exit(1)
    N = int(sys.argv[1])

    estimate = ejercicio9b(N)
    print(f"En {N} iteraciones:")
    print(f"Probabilidad estimada de ganar: {estimate:.4f}")