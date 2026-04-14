import sys
import numpy as np

def ejercicio5a(n: int):
    sum = 0
    for _ in range(n):
        u = np.random.uniform(0, 1)
        sum += (1-u**2)**(3/2) 
    rta = sum/n
    return rta

def ejercicio5b(n: int):
    sum = 0
    for _ in range(n):
        u = np.random.uniform(0, 1)
        sum += (u+2)/((u+3)*(u+1))
    rta = sum/n
    return rta

def ejercicio5c(n: int):
    sum = 0
    for _ in range(n):
        u = np.random.uniform(0, 1)
        sum += ((1-u)*u)/((2*(u**2)-2*u+1)**2)
    rta = sum/n
    return rta

def ejercicio5d(n: int):
    sum = 0
    for _ in range(n):
        u = np.random.uniform(0, 1)
        sum += np.exp(-(1-u)**2/(u**2)) * ((1)/(u**2))

    rta = 2*sum/n
    return rta

def ejercicio5e(n: int):
    sum = 0
    for _ in range(n):
        u1 = np.random.uniform(0, 1)
        u2 = np.random.uniform(0, 1)
        sum += np.exp((u1+u2)**2)

    rta = sum/n
    return rta

def ejercicio5f(n: int):
    sum = 0
    for _ in range(n):
        u1 = np.random.exponential(1)
        u2 = np.random.exponential(1)
        if (u1 < u2):
            sum += 1
        else:
            sum += 0

    rta = sum/n
    return rta


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ej5.py <n>")
        sys.exit(1)
    elif int(sys.argv[1]) < 0:
        print("n must be a non-negative integer")
        sys.exit(1)
    n = int(sys.argv[1])

    a = ejercicio5a(n)
    b = ejercicio5b(n)
    c = ejercicio5c(n)
    d = ejercicio5d(n)
    e = ejercicio5e(n)
    f = ejercicio5f(n)

    print(f"En {n} iteraciones:")
    print(f"Ejercicio 5a: {a:.4f}")
    print(f"Ejercicio 5b: {b:.4f}")
    print(f"Ejercicio 5c: {c:.4f}")
    print(f"Ejercicio 5d: {d:.4f}")
    print(f"Ejercicio 5e: {e:.4f}")
    print(f"Ejercicio 5f: {f:.4f}")
