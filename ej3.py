
#
# Sean las VAs U,W_1,W_2,W_3 \sim \mathcal{U}(0,1)
# Sea X = suma de los numeros aleatorios respectivamente
# 
# P(X\le 2) = P(U\lt 1/3)\cdot P(W_1+W_2\le 2) + P(U\ge 1/3)\cdot P(W_1+W_2+W_3\le 2)
# 
# tomando
#     P(W_1+W_2\le 2) como 1-P(W_1+W_2\gt 2)
#     P(W_1+W_2+W_3\le 2) como 1-P(W_1+W_2+W_3\gt 2)
# Se calcula de la misma manera que le ejer 2a
#

import random,sys

def ejercicio3b(iterations: int):
    hits = 0
    for _ in range(iterations):
        u = random.random()
        if u < (1/3):
            w1 = random.random()
            w2 = random.random()
            s = w1 + w2
        else:
            w1 = random.random()
            w2 = random.random()
            w3 = random.random()
            s = w1 + w2 + w3
        if s <=2:
            hits += 1
    print(f"Probability of winning: {hits / iterations:.4f}")


if __name__ == "__main__":
    n = int(sys.argv[1])
    if len(sys.argv) != 2:
        print("Usage: python script.py <iterations>")
        sys.exit(1)
    elif n <= 0:
        print("Iterations must be a positive integer.")
        sys.exit(1)
    ejercicio3b(n)

# Para n=100            obtuvimos 0.9400
# Para n=1.000          obtuvimos 0.8880
# Para n=10.000         obtuvimos 0.8901
# Para n=100.000        obtuvimos 0.8886
# Para n=1.000.000      obtuvimos 0.8890
