import random,sys

def ejercicio2b(iterations: int):
    wins = 0
    for _ in range(iterations):
        u = random.random()
        if u < 0.5:
            w1 = random.random()
            w2 = random.random()
            s = w1 + w2
        else:
            w1 = random.random()
            w2 = random.random()
            w3 = random.random()
            s = w1 + w2 + w3
        if s >= 1:
            wins += 1
    print(f"Probability of winning: {wins / iterations:.4f}")


if __name__ == "__main__":
    n = int(sys.argv[1])
    if len(sys.argv) != 2:
        print("Usage: python script.py <iterations>")
        sys.exit(1)
    elif n <= 0:
        print("Iterations must be a positive integer.")
        sys.exit(1)
    ejercicio2b(n)