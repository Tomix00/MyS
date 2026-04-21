import sys
import math
import random

def ejercicio1(Nsim: int):
    sum = 0
    for _ in range(n):
        u = random.random()
        sum += math.exp(-(-1+4*u)+math.exp(-(-1+4*u)))
    rta = (sum*4)/n
    return rta



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ej5.py <n>")
        sys.exit(1)
    elif int(sys.argv[1]) < 0:
        print("n must be a non-negative integer")
        sys.exit(1)
    n = int(sys.argv[1])


    sim = ejercicio1(n)

    print(f"Para {n} iteraciones:\n")
    print(f"Ejercicio 1: {sim:.6f}")


