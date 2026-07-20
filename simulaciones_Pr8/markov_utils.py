"""Utility functions for Markov chain computations."""
import numpy as np

def Pn(P, n):
    """Compute P^n (n-step transition matrix)."""
    result = np.linalg.matrix_power(P, n)
    return result

def stationary(P):
    """Find stationary distribution by solving pi*P = pi, sum(pi) = 1."""
    n = P.shape[0]
    A = np.vstack([P.T - np.eye(n), np.ones(n)])
    b = np.zeros(n + 1)
    b[-1] = 1
    pi, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
    return pi

def absorption_prob(P, absorbing_states):
    """Compute absorption probabilities for each transient state."""
    n = P.shape[0]
    trans = [i for i in range(n) if i not in absorbing_states]
    abs_st = absorbing_states
    if not trans:
        return np.eye(n)
    Q = P[np.ix_(trans, trans)]
    R = P[np.ix_(trans, abs_st)]
    m = len(trans)
    N = np.linalg.inv(np.eye(m) - Q)
    B = N @ R
    return B

def mean_first_passage(P, target):
    """Compute mean first passage times to target state."""
    n = P.shape[0]
    Q = np.delete(np.delete(P, target, axis=0), target, axis=1)
    m = n - 1
    N = np.linalg.inv(np.eye(m) - Q)
    ones = np.ones(m)
    mfpt = N @ ones
    result = np.zeros(n)
    idx = 0
    for i in range(n):
        if i == target:
            result[i] = 0
        else:
            result[i] = mfpt[idx]
            idx += 1
    return result

def mean_return_time(pi, state):
    """Mean return time to a state given stationary distribution."""
    return 1.0 / pi[state]
