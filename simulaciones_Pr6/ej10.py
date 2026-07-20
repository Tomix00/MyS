import random
import math
from statistics import NormalDist

z = NormalDist().inv_cdf(0.975)
N_WORKING = 6
N_SPARES = 4
LAMBDA_F = 2
MU_R = 3

def simulate_once():
    fail_times = sorted([-math.log(random.random()) / LAMBDA_F
                         for _ in range(N_WORKING)])
    spares = N_SPARES
    repair_end = float('inf')
    in_repair = 0
    t = 0.0

    while True:
        next_fail = fail_times[0] if fail_times else float('inf')
        if next_fail < repair_end:
            t = next_fail
            if spares > 0:
                spares -= 1
                in_repair += 1
                fail_times.pop(0)
                if repair_end == float('inf'):
                    repair_end = t + (-math.log(random.random()) / MU_R)
            else:
                return t
        else:
            t = repair_end
            spares += 1
            in_repair -= 1
            if in_repair > 0:
                repair_end = t + (-math.log(random.random()) / MU_R)
            else:
                repair_end = float('inf')
            fail_times.append(t + (-math.log(random.random()) / LAMBDA_F))
            fail_times.sort()

def sequential_est(sample_fn, target_se, min_n=30):
    n = 0
    s = 0.0
    s2 = 0.0
    while True:
        n += 1
        x = sample_fn()
        s += x
        s2 += x * x
        if n >= min_n:
            mean = s / n
            var = max((s2 / n - mean * mean) / n, 1e-10)
            se = math.sqrt(var)
            if se < target_se:
                break
    mean = s / n
    se = math.sqrt(max((s2 / n - mean * mean) / n, 1e-10))
    return mean, se, n

def ejercicio10():
    mean_ttf, se_ttf, n_ttf = sequential_est(simulate_once, 0.01)
    ci_ttf = (mean_ttf - z * se_ttf, mean_ttf + z * se_ttf)
    print(f"b) Tiempo medio hasta falla: {mean_ttf:.4f} IC95=[{ci_ttf[0]:.4f},{ci_ttf[1]:.4f}] (n={n_ttf})")

    def sample_early():
        return 1.0 if simulate_once() < 1.5 else 0.0

    mean_p, se_p, n_p = sequential_est(sample_early, 0.01)
    ci_p = (mean_p - z * se_p, mean_p + z * se_p)
    print(f"d) P(falla antes 90 min): {mean_p:.4f} IC95=[{ci_p[0]:.4f},{ci_p[1]:.4f}] (n={n_p})")

if __name__ == "__main__":
    ejercicio10()
