import random
import math

def lambda_t(t):
    """Periodic intensity: 10h cycle, 4→19→4"""
    t_mod = t % 10
    if t_mod <= 5:
        return 4 + (19 - 4) * t_mod / 5
    else:
        return 19 - (19 - 4) * (t_mod - 5) / 5

LAMBDA_MAX = 19
MU = 25
TOTAL_H = 100

def simulate_once():
    t = 0.0
    server_busy = False
    queue = 0
    n_completed = 0
    rest_time = 0.0

    next_arrival = -math.log(random.random()) / LAMBDA_MAX
    next_service_end = float('inf')
    next_rest_end = 0.0
    resting = False

    while t < TOTAL_H or queue > 0 or server_busy:
        # Thin arrival
        if next_arrival < next_service_end and next_arrival < (next_rest_end if resting else float('inf')):
            t = next_arrival
            # Accept/reject
            u = random.random()
            if u < lambda_t(t) / LAMBDA_MAX:
                queue += 1
            next_arrival = t - math.log(random.random()) / LAMBDA_MAX
            if not resting and not server_busy:
                next_service_end = t + (-math.log(random.random()) / MU)
                server_busy = True
                queue -= 1
        elif next_service_end < (next_rest_end if resting else float('inf')):
            t = next_service_end
            n_completed += 1
            server_busy = False
            if queue > 0:
                next_service_end = t + (-math.log(random.random()) / MU)
                server_busy = True
                queue -= 1
            else:
                rest_start = t
                rest_dur = random.uniform(0, 0.3)
                rest_time += rest_dur
                resting = True
                next_rest_end = t + rest_dur
        else:
            t = next_rest_end
            resting = False
            if queue > 0:
                next_service_end = t + (-math.log(random.random()) / MU)
                server_busy = True
                queue -= 1

    return rest_time, n_completed

def ejercicio7():
    for target_se, name in [(0.05, "rest_time"), (0.01, "n_completed")]:
        n = 0
        sum_x = 0.0
        sum_x2 = 0.0
        while True:
            n += 1
            rest, completed = simulate_once()
            x = rest if name == "rest_time" else completed
            sum_x += x
            sum_x2 += x * x
            if n >= 30:
                mean = sum_x / n
                var = (sum_x2 / n - mean * mean) / n
                se = math.sqrt(max(var, 0))
                if se < target_se:
                    break
        mean = sum_x / n
        print(f"Estimacion de {name}: {mean:.4f} (n={n}, SE={se:.4f})")

if __name__ == "__main__":
    ejercicio7()
