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
    if len(sys.argv) != 2:
        print("Usage: python script.py <iterations>")
        sys.exit(1)
    elif int(sys.argv[1]) <= 0:
        print("Iterations must be a positive integer.")
        sys.exit(1)
        
    n = int(sys.argv[1])
    ejercicio3b(n)

# Para n=100            obtuvimos 0.9400
# Para n=1.000          obtuvimos 0.8880
# Para n=10.000         obtuvimos 0.8901
# Para n=100.000        obtuvimos 0.8886
# Para n=1.000.000      obtuvimos 0.8890
