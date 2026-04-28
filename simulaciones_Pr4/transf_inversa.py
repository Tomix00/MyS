from random import random

class generators:
    def udiscreta01(n: int) -> int:
        u = random()
        return int(n * u) + 1

    def udiscretamk(m: int, k: int) -> int:
        u = random()
        return int(u * (k - m + 1)) + m

class permutation:
    def permutacion1(a: list) -> list:
        N = len(a)
        for j in range(N-1):
            indice = int((N - j) * random()) + j
            a[j], a[indice] = a[indice], a[j]
        return a
    
    def permutacion2(a: list) -> list:
        N = len(a)
        for j in range(N-1, 0, -1):
            indice = int((j + 1) * random())
            a[j], a[indice] = a[indice], a[j]
        return a

    def subcAleatorio(r: int, a: list) -> list:
        n = len(a)
        for j in range(n - 1, n - 1 - r, -1):
            indice = int((j + 1) * random())
            a[j], a[indice] = a[indice], a[j]
        return a[n-r:]
