#!/usr/bin/env python3
# bank_simulator_v2.py
# -----------------------------------------
import sys

EPS = 1e-12

def read_customers_from_file(filename):
    customers = []
    idx = 0
    with open(filename, 'r') as f:
        for raw in f:
            line = raw.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            try:
                a = float(parts[0])
                s = float(parts[1])
                p = int(parts[2]) if len(parts) >= 3 else 1
            except ValueError:
                continue
            if abs(a) < EPS and abs(s) < EPS:
                break
            customers.append((a, s, p, idx))
            idx += 1
    return customers

def simulate_one_run(customers, num_tellers):
    if not customers:
        return {
            "num_tellers": num_tellers,
            "servers_served_count": [0]*num_tellers,
            "total_sim_time": 0.0,
            "avg_service_time": 0.0,
            "avg_waiting_time": 0.0,
            "max_queue_length": 0,
            "avg_queue_length_est": 0.0,
            "avg_queue_length_time_weighted": 0.0,
            "idle_rates": [0.0]*num_tellers,
            "total_customers": 0
        }
    next_free = [float('inf')]*num_tellers
    busy = [False]*num_tellers
    served_count = [0]*num_tellers
    idle_time = [0.0]*num_tellers
    idle_since = [None]*num_tellers

    start_time = customers[0][0]
    current_time = start_time
    for i in range(num_tellers):
        idle_since[i] = start_time

    Q = []
    max_q = 0
    last_event_time = start_time
    queue_area = 0.0
    total_wait = 0.0
    total_service = 0.0
    total_served = 0

    ai = 0
    N = len(customers)

    def find_idle():
        for sid in range(num_tellers):
            if not busy[sid]:
                return sid
        return None

    def next_completion():
        t = float('inf'); si = -1
        for s in range(num_tellers):
            if busy[s] and next_free[s] < t:
                t = next_free[s]; si = s
        return t, si

    def queue_insert(cust):
        a, s, p, idx = cust
        pos = 0
        while pos < len(Q):
            a2, s2, p2, idx2 = Q[pos]
            if p > p2:
                break
            if p == p2 and a < a2 - EPS:
                break
            pos += 1
        Q.insert(pos, cust)

    def assign(cust, sid, now):
        nonlocal total_wait, total_service, total_served
        a, s, p, _ = cust
        wait = now - a
        if wait < 0:
            wait = 0.0
        total_wait += wait
        total_service += s
        total_served += 1
        served_count[sid] += 1
        busy[sid] = True
        next_free[sid] = now + s
        if idle_since[sid] is not None and now > idle_since[sid]:
            idle_time[sid] += (now - idle_since[sid])
        idle_since[sid] = None

    while True:
        next_arr = customers[ai][0] if ai < N else float('inf')
        comp_time, comp_sid = next_completion()

        if comp_time <= next_arr:
            dt = comp_time - last_event_time
            if dt > 0:
                queue_area += dt * len(Q)
            current_time = comp_time
            last_event_time = current_time

            busy[comp_sid] = False
            next_free[comp_sid] = float('inf')
            idle_since[comp_sid] = current_time

            if Q:
                cust = Q.pop(0)
                assign(cust, comp_sid, current_time)

        else:
            dt = next_arr - last_event_time
            if dt > 0:
                queue_area += dt * len(Q)
            current_time = next_arr
            last_event_time = current_time

            while ai < N and abs(customers[ai][0] - current_time) < EPS:
                cust = customers[ai]
                sid = find_idle()
                if sid is not None:
                    assign(cust, sid, current_time)
                else:
                    queue_insert(cust)
                    if len(Q) > max_q:
                        max_q = len(Q)
                ai += 1

        if ai >= N and all(not b for b in busy) and not Q:
            break

    end_time = current_time
    total_sim = max(0.0, end_time - start_time)

    rates = []
    for s in range(num_tellers):
        if idle_since[s] is not None and end_time > idle_since[s]:
            idle_time[s] += (end_time - idle_since[s])
        rates.append((idle_time[s] / total_sim) if total_sim > 0 else 0.0)

    avg_service = (total_service / total_served) if total_served > 0 else 0.0
    avg_wait = (total_wait / total_served) if total_served > 0 else 0.0
    avg_q_est = (total_wait / total_served) if total_served > 0 else 0.0
    avg_q_time = (queue_area / total_sim) if total_sim > 0 else 0.0

    return {
        "num_tellers": num_tellers,
        "servers_served_count": served_count,
        "total_sim_time": total_sim,
        "avg_service_time": avg_service,
        "avg_waiting_time": avg_wait,
        "max_queue_length": max_q,
        "avg_queue_length_est": avg_q_est,
        "avg_queue_length_time_weighted": avg_q_time,
        "idle_rates": rates,
        "total_customers": total_served
    }

def parse_inputs():
    tokens = sys.stdin.read().strip().split()
    if tokens:
        first = tokens[0]
        try:
            n = int(first)
            fname = tokens[1] if len(tokens) >= 2 else 'a1-sample.txt'
            return ('single', n, fname)
        except ValueError:
            return ('multi', None, first)
    argv = sys.argv
    if len(argv) >= 3:
        try:
            n = int(argv[1])
            return ('single', n, argv[2])
        except ValueError:
            pass
    if len(argv) >= 2:
        return ('multi', None, argv[1])
    return ('multi', None, 'a1-sample.txt')

def main():
    mode, num, fname = parse_inputs()
    try:
        customers = read_customers_from_file(fname)
    except FileNotFoundError:
        print(f"ERROR: file not found: {fname}")
        return
    if not customers:
        print("No valid customers found in file.")
        return

    if mode == 'single':
        res = simulate_one_run(customers, num)
        print(f"=== Simulation with {res['num_tellers']} teller(s) ===")
        print(f"Number of customers served by each teller: {res['servers_served_count']}")
        print(f"Total time of the simulation: {res['total_sim_time']:.6f}")
        print(f"Average service time per customer: {res['avg_service_time']:.6f}")
        print(f"Average waiting time per customer: {res['avg_waiting_time']:.6f}")
        print(f"Maximum length of the queue: {res['max_queue_length']}")
        print(f"Average length of the queue (est.): {res['avg_queue_length_est']:.6f}  # total_wait/N")
        print(f"Average length of the queue (time-weighted): {res['avg_queue_length_time_weighted']:.6f}  # area/time")
        print(f"Idle rate of each teller: {[round(x, 6) for x in res['idle_rates']]}")
    else:
        for k in [1, 2, 3, 4]:
            res = simulate_one_run(customers, k)
            print(f"=== Simulation with {res['num_tellers']} teller(s) ===")
            print(f"Number of customers served by each teller: {res['servers_served_count']}")
            print(f"Total time of the simulation: {res['total_sim_time']:.6f}")
            print(f"Average service time per customer: {res['avg_service_time']:.6f}")
            print(f"Average waiting time per customer: {res['avg_waiting_time']:.6f}")
            print(f"Maximum length of the queue: {res['max_queue_length']}")
            print(f"Average length of the queue (est.): {res['avg_queue_length_est']:.6f}  # total_wait/N")
            print(f"Average length of the queue (time-weighted): {res['avg_queue_length_time_weighted']:.6f}  # area/time")
            print(f"Idle rate of each teller: {[round(x, 6) for x in res['idle_rates']]}")
            print()

if __name__ == "__main__":
    main()
