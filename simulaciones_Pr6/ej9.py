import random
import math

def lambda_t(t):
    return 7 - 1 / (t + 1)

LAMBDA_MAX = 7
MU1 = 3
MU2 = 4
N_CLIENTS = 1000

def simulate_once():
    t = 0.0
    q1, q2 = 0, 0
    busy1, busy2 = False, False
    end1, end2 = float('inf'), float('inf')
    next_arrival = -math.log(random.random()) / LAMBDA_MAX
    served1 = 0
    served_total = 0
    total_time = 0.0

    while served_total < N_CLIENTS:
        next_event = min(next_arrival, end1, end2)

        if next_event == next_arrival:
            t = next_arrival
            if q1 <= q2:
                q1 += 1
            else:
                q2 += 1
            next_arrival = t - math.log(random.random()) / LAMBDA_MAX
            if not busy1 and q1 > 0:
                end1 = t - math.log(random.random()) / MU1
                busy1 = True
                q1 -= 1
            if not busy2 and q2 > 0:
                end2 = t - math.log(random.random()) / MU2
                busy2 = True
                q2 -= 1

        elif next_event == end1:
            t = end1
            busy1 = False
            served1 += 1
            served_total += 1
            total_time += t
            if q1 > 0:
                end1 = t - math.log(random.random()) / MU1
                busy1 = True
                q1 -= 1
            else:
                end1 = float('inf')
            if served_total >= N_CLIENTS:
                break

        else:
            t = end2
            busy2 = False
            served_total += 1
            total_time += t
            if q2 > 0:
                end2 = t - math.log(random.random()) / MU2
                busy2 = True
                q2 -= 1
            else:
                end2 = float('inf')
            if served_total >= N_CLIENTS:
                break

    avg_time = total_time / N_CLIENTS
    prop1 = served1 / N_CLIENTS
    return avg_time, prop1

def ejercicio9():
    n = 0
    s_time = 0.0
    s2_time = 0.0
    s_prop = 0.0
    s2_prop = 0.0

    while True:
        n += 1
        avg_t, prop = simulate_once()
        s_time += avg_t
        s2_time += avg_t * avg_t
        s_prop += prop
        s2_prop += prop * prop
        if n >= 30:
            se_t = math.sqrt(max((s2_time / n - (s_time / n) ** 2) / n, 0))
            se_p = math.sqrt(max((s2_prop / n - (s_prop / n) ** 2) / n, 0))
            if se_t < 0.01 and se_p < 0.01:
                break

    mean_t = s_time / n
    mean_p = s_prop / n
    z = 1.96
    print(f"b) Tiempo promedio en sistema: {mean_t:.4f} IC95=[{mean_t-z*se_t:.4f},{mean_t+z*se_t:.4f}] (n={n})")
    print(f"c) Prop. servidor 1: {mean_p:.4f} IC95=[{mean_p-z*se_p:.4f},{mean_p+z*se_p:.4f}]")

if __name__ == "__main__":
    ejercicio9()
