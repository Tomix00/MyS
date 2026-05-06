import random
import math
from transf_inversa import discreteGenerators

# Parámetros
k = 10
lam = 0.7
n = 1000

# Precalcular probabilidades de Poisson truncada
def probs_truncada(lam, k):
    terms = [lam**i / math.factorial(i) for i in range(k + 1)]
    S = sum(terms)
    return [t / S for t in terms]

probs = probs_truncada(lam, k)

# a) Transformada inversa
def inversa_truncada():
    # Ordenar de mayor a menor
    pares = sorted(zip(probs, range(k+1)), reverse=True)
    probs_ord = [p for p, _ in pares]
    vals_ord = [v for _, v in pares]
    
    F_acum = []
    acum = 0
    for p in probs_ord:
        acum += p
        F_acum.append(acum)
    
    U = random.random()
    for i, F in enumerate(F_acum):
        if U < F:
            return vals_ord[i]
    return vals_ord[-1]

# a) Aceptación y rechazo (Y ~ Poisson(λ))
def rechazo_truncada():
    S = sum(lam**i / math.factorial(i) for i in range(k + 1))
    prob_aceptar = math.exp(-lam) * S
    
    while True:
        Y = discreteGenerators.poisson(lam)
        if Y <= k and random.random() < prob_aceptar:
            return Y

# b) Estimar P(X > 2)
def estimar(metodo):
    return sum(1 for _ in range(n) if metodo() > 2) / n

p_exacta = sum(probs[i] for i in range(3, k + 1))

print(f"P(X > 2) exacta: {p_exacta:.6f}")
print(f"Estimación transformada inversa: {estimar(inversa_truncada):.6f}")
print(f"Estimación aceptación y rechazo: {estimar(rechazo_truncada):.6f}")

# c) Pseudocódigo para variable truncada en [a, b]
print("\n" + "="*50)
print("Pseudocódigo - Método de rechazo para variable truncada en [a, b]:")
print("""
ALGORITMO RechazoTruncado(a, b, generar_Y, prob_Y, S):
    # S = sum_{j=a}^b P(Y=j)
    prob_aceptar = S
    REPETIR
        Y = generar_Y()
    HASTA QUE (a <= Y <= b) Y (random() < prob_aceptar)
    RETORNAR Y
""")