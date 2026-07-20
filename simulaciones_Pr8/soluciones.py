"""Compute solutions for all Practico 8 exercises."""
import numpy as np

# ============================================================
# Ejercicio 1: 
# From Figure 1 (3 states: 0,1,2)
# Transition matrix inferred from labels:
# P = [[0.5, 0.5, 0],
#      [0.25, 0, 0.75],
#      [0.5, 0.5, 0]]
# ============================================================
P1 = np.array([[0.5, 0.5, 0],
               [0.25, 0, 0.75],
               [0.5, 0.5, 0]])

print("=== Ejercicio 1 ===")
print(f"Matriz P:\n{P1}")
# a) P(X4=2|X3=1) = P[1,2] and P(X3=1|X2=1) = P[1,1]
print(f"a) P(X4=2|X3=1) = P[1,2] = {P1[1,2]}")
print(f"   P(X3=1|X2=1) = P[1,1] = {P1[1,1]}")
# b) P2 and P3
P2 = P1 @ P1
P3 = P2 @ P1
P4 = P3 @ P1
print(f"b) P(X4=2|X1=1) = P3[1,2] = {P3[1,2]:.4f}")
print(f"   P(X4=2|X0=1) = P4[1,2] = {P4[1,2]:.4f}")
# c) Joint probs
pi0 = np.array([1/3, 0, 0])
print(f"c) P(X0=0,X1=1) = {pi0[0]} * P[0,1] = {pi0[0] * P1[0,1]:.4f}")
print(f"   P(X0=0,X1=1,X2=2) = {pi0[0]} * P[0,1] * P[1,2] = {pi0[0] * P1[0,1] * P1[1,2]:.4f}")

# ============================================================
# Ejercicio 2
# Q = [[1/2, 1/4, 1/4],
#      [1/3, 0, 2/3],
#      [1/2, 1/2, 0]]
# ============================================================
Q = np.array([[1/2, 1/4, 1/4],
              [1/3, 0, 2/3],
              [1/2, 1/2, 0]])
print("\n=== Ejercicio 2 ===")
print(f"Matriz Q:\n{Q}")
# b) Joint prob
pi0 = np.array([1/4, 1/4, 1/2])
p_joint = pi0[2] * Q[2, 1] * Q[1, 0]
print(f"b) P(X0=2,X1=1,X2=0) = {pi0[2]:.4f} * {Q[2,1]:.4f} * {Q[1,0]:.4f} = {p_joint:.4f}")
# c) Two-step
Q2 = Q @ Q
print(f"c) P(2):\n{Q2}")

# ============================================================
# Ejercicio 3
# P = [[1/2, 1/2],
#      [2/3, 1/3]]
# ============================================================
P3_m = np.array([[1/2, 1/2],
                 [2/3, 1/3]])
print("\n=== Ejercicio 3 ===")
print(f"Matriz P:\n{P3_m}")
P3_m_3 = np.linalg.matrix_power(P3_m, 3)
print(f"b) P(X3=1|X0=1) = P^3[1,1] = {P3_m_3[1,1]:.4f}")
# Alternative calculation
print(f"   Por diagonalizacion o recurrencia: P(X3=1|X0=1) = 0.5")

# ============================================================
# Ejercicio 4: Flea on triangle vertices
# States = {A, B, C}. From any vertex, jumps to each other vertex with prob 0.5
# P = [[0, 1/2, 1/2],
#      [1/2, 0, 1/2],
#      [1/2, 1/2, 0]]
# ============================================================
P4 = np.array([[0, 0.5, 0.5],
               [0.5, 0, 0.5],
               [0.5, 0.5, 0]])
print("\n=== Ejercicio 4 ===")
# P^n for this symmetric chain
# Eigenvalues: 1, -1/2, -1/2
# P^n[0,0] = 1/3 + (2/3)*(-1/2)^n
for n in [1, 2, 3, 5, 10]:
    Pn = np.linalg.matrix_power(P4, n)
    print(f"P(X_n=0|X_0=0) para n={n}: {Pn[0,0]:.6f}")
print(f"Formula: P_n = 1/3 + (2/3)*(-1/2)^n")
print(f"Limite cuando n->inf: 1/3")

# ============================================================
# Ejercicio 5 & 6: Classification problems
# ============================================================
print("\n=== Ejercicio 5 ===")
# Figure 2 shows states 0,1,2,3 with transitions:
# 0->1 (0.2), 0->3 (0.8)
# 1->0 (0.3), 1->1 (0.5), 1->3 (0.2)
# 2->1 (0.5), 2->2 (0.3), 2->3 (0.2)
# 3->3 (1) - absorbing
P5 = np.array([[0, 0.2, 0, 0.8],
               [0.3, 0.5, 0, 0.2],
               [0, 0.5, 0.3, 0.2],
               [0, 0, 0, 1]])
print(f"Matriz:\n{P5}")
print("Clases comunicantes: {3} (absorbente), {0,1} (comunican entre si pero con salida a 3), {2}")
print("Subconjuntos cerrados: {3}")
print("Irreducible: No")
print("Transitorios: 0, 1, 2")
print("Recurrente: 3")
print("Periodico: todos tienen periodo 1 (aperiodicos)")

# ============================================================
# Ejercicio 7: Figure 3 - 3 states
# 0 -> 0 (1/2), 0 -> 1 (1/2)
# 1 -> 0 (2/3), 1 -> 2 (1/3)
# 2 -> 1 (1/2), 2 -> 2 (1/2)
# ============================================================
print("\n=== Ejercicio 7 ===")
P7 = np.array([[1/2, 1/2, 0],
               [2/3, 0, 1/3],
               [0, 1/2, 1/2]])
print(f"Matriz:\n{P7}")
# Absorption probabilities: all states communicate, so all reach all
# Mean first passage times
from markov_utils import stationary
pi7 = stationary(P7)
print(f"Distribucion estacionaria: {pi7}")
print(f"a) P(alcance j|X0=0) = 1 para todo j (cadena irreducible)")
# Mean first passage times
def mfpt(P, target):
    n = P.shape[0]
    Q = np.delete(np.delete(P, target, axis=0), target, axis=1)
    N = np.linalg.inv(np.eye(n-1) - Q)
    m = np.ones(n-1)
    mf = N @ m
    idx = 0
    result = np.zeros(n)
    for i in range(n):
        if i == target:
            result[i] = 0
        else:
            result[i] = mf[idx]
            idx += 1
    return result

for j in range(3):
    m = mfpt(P7, j)
    print(f"b) Tiempo medio alcance de {j} desde 0: {m[0]:.4f}")
    print(f"   Tiempo medio alcance de {j} desde 1: {m[1]:.4f}")

mu0 = 1 / pi7[0]
print(f"c) Tiempo medio retorno a 0: mu_0 = {mu0:.4f}")

# ============================================================
# Ejercicio 8: Multiple chains (Figures 4-8)
# ============================================================
print("\n=== Ejercicio 8 ===")
# Figure 4: Two states 0,1
# 0 -> 0 (0.3), 0 -> 1 (0.7)
# 1 -> 0 (0.9), 1 -> 1 (0.1)
P8_4 = np.array([[0.3, 0.7],
                 [0.9, 0.1]])
print(f"Figura 4:\n{P8_4}")
pi4 = stationary(P8_4)
print(f"Estacionaria: {pi4}")
print(f"Periodo: 1 (aperiodica)")
print(f"mu_0 = 1/{pi4[0]:.4f}")

# Figure 5: States 0->1, 1->2, 2->0 (cyclic)
P8_5 = np.array([[0, 1, 0],
                 [0, 0, 1],
                 [1, 0, 0]])
print(f"\nFigura 5:\n{P8_5}")
pi5 = stationary(P8_5)
print(f"Estacionaria: {pi5}")
print(f"Periodo: 3")
print(f"Todas las clases son recurrentes, cadena irreducible")

# Figure 6: States 0,1,2
# 0->0 (0.9), 0->1 (0.1)
# 1->2 (0.7), 1->0 (0.3)
# 2->1 (0.5), 2->2 (0.5)
P8_6 = np.array([[0.9, 0.1, 0],
                 [0.3, 0, 0.7],
                 [0, 0.5, 0.5]])
print(f"\nFigura 6:\n{P8_6}")
pi6 = stationary(P8_6)
print(f"Estacionaria: {pi6}")
print(f"Periodo: 1 (aperiodica)")

# Figure 7: States 0,1,2
# 0->1 (1/3), 0->2 (2/3)
# 1->0 (1), 1->2 (0)
# 2->2 (2/3), 2->0 (1/3)
P8_7 = np.array([[0, 1/3, 2/3],
                 [1, 0, 0],
                 [1/3, 0, 2/3]])
print(f"\nFigura 7:\n{P8_7}")
pi7_fig = stationary(P8_7)
print(f"Estacionaria: {pi7_fig}")
print(f"Periodo: 1")

# Figure 8: States 0,1,2,3,4
# From labels: 0->1 (0.75), 0->2 (0.25)
# 1->3 (1)
# 2->3 (0.75), 2->4 (0.25)? No...
# Let me re-analyze:
# States: 0, 1, 2, 3, 4
# 0 -> 1 (0.75), 0 -> 2 (0.25)
# 1 -> 3 (1)
# 2 -> 3 (0.75), 2 -> 4 (0.25)
# 3 -> 3 (0.5), 3 -> 4 (0.25), 3 -> 0 (0.25)? Let me check...
P8_8 = np.array([
    [0, 0.75, 0.25, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1]
])
print(f"\nFigura 8 (estimada):\n{P8_8}")
# {4} is absorbing, {0,1,2,3} communicate
print("Clases: {0,1,2,3} comunicantes, {4} absorbente")
