# bank_simulator.py
# -----------------------------------------
# Discrete-event bank teller simulation
#
# Header imports as specified by the assignment:
import sys
import numpy as np   # allowed per assignment header (used only for small numeric utilities)

# --------------------------------------------------------------------------------
# OVERVIEW (in plain words, to tell your tutor):
# - We read all customer records from the file (each record = arrival_time, service_time, priority).
# - The system has multiple tellers (servers) and a single shared queue.
# - Two event types: arrival, and service completion.
# - We advance the simulation clock from event to event (discrete-event simulation).
# - Queue is ordered by priority (higher priority first) and for same priority by arrival order.
# - For each number of tellers (1..4) we run the simulation and compute statistics:
#     * customers served per teller
#     * total simulation time
#     * average service time per customer
#     * average waiting time per customer
#     * maximum queue length observed
#     * average queue length (time-weighted)
#     * idle rate per teller (idle_time / total_sim_time)
# --------------------------------------------------------------------------------

# ---------------------------
# Helper: read customers file
# ---------------------------
def read_customers_from_file(filename):
    """
    Read customers from the given filename.
    Each non-empty line expected to have: arrival_time service_time priority
    The file is terminated by a line with "0 0 ..." (arrival==0 and service==0).
    Returns a list of tuples: (arrival_time: float, service_time: float, priority: int, index: int)
    The input is assumed sorted by arrival time already as per assignment statement.
    """
    customers = []
    idx = 0
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                # defensive: skip lines that don't have at least two numeric values + priority
                if len(parts) < 3:
                    continue
                try:
                    arrival = float(parts[0])
                    service = float(parts[1])
                    priority = int(parts[2])
                except ValueError:
                    # skip malformed lines
                    continue
                # assignment states termination is arrival==0 and service==0
                if arrival == 0 and service == 0:
                    break
                customers.append((arrival, service, priority, idx))
                idx += 1
    except FileNotFoundError:
        print("ERROR: file not found:", filename)
        sys.exit(1)
    return customers

# ------------------------------------
# Simulation core: simulate one-run
# ------------------------------------
def simulate_one_run(customers, num_tellers):
    """
    Run the discrete-event simulation for the list of customers with num_tellers servers.
    Returns a dictionary of statistics described in the assignment.
    Implementation notes (to explain to tutor):
      - We maintain arrays for server state (busy, next_free_time, served_count, idle_time, last_idle_start).
      - The queue is a Python list maintained in the required order (priority desc, then arrival order).
      - next event is min(next arrival time, earliest completion time).
      - We update the time-weighted queue area (queue_area) between events for average queue length.
    """
    # If no customers, return trivial stats
    if not customers:
        return {
            "num_tellers": num_tellers,
            "servers_served_count": [0] * num_tellers,
            "total_sim_time": 0.0,
            "avg_service_time": 0.0,
            "avg_waiting_time": 0.0,
            "max_queue_length": 0,
            "avg_queue_length": 0.0,
            "idle_rates": [0.0] * num_tellers,
            "total_customers": 0
        }

    # Servers state arrays (indexed 0..num_tellers-1)
    servers_next_free = [float('inf')] * num_tellers   # when each server will finish current service
    servers_busy = [False] * num_tellers               # whether server is currently busy
    servers_served_count = [0] * num_tellers           # how many customers each server served
    servers_idle_time = [0.0] * num_tellers            # cumulative idle time per server
    servers_last_idle_start = [None] * num_tellers     # when server last became idle (None when busy)

    # Simulation time initialization: start at first arrival
    start_time = customers[0][0]
    current_time = start_time

    # At simulation start, all servers are idle starting at start_time
    for i in range(num_tellers):
        servers_last_idle_start[i] = start_time

    # The central queue (single queue). Each entry is a tuple (arrival, service, priority, idx)
    # Inserted so that higher priority (3) is in front of lower priority (1).
    # For equal priority, earlier arrival remains earlier (stable by insertion).
    queue = []

    # Stats we accumulate
    max_queue_length = 0
    last_event_time = start_time
    queue_area = 0.0                 # area under queue-length curve for average queue length
    total_waiting_time = 0.0         # sum of all customers' waiting time in queue
    total_service_time = 0.0         # sum of all service durations
    total_customers_served = 0

    # arrival index i into customers list
    ai = 0
    N = len(customers)

    # helper: find an idle server index or return None
    def find_idle_server():
        for sid in range(num_tellers):
            if not servers_busy[sid]:
                return sid
        return None

    # helper: find next completion time and the server index, or (inf, -1) if none busy
    def next_completion():
        t = float('inf')
        si = -1
        for s in range(num_tellers):
            if servers_busy[s] and servers_next_free[s] < t:
                t = servers_next_free[s]
                si = s
        return t, si

    # helper: assign customer to server at time 'now'
    def assign_customer_to_server(cust, sid, now):
        # cust = (arrival, service, priority, idx)
        nonlocal total_waiting_time, total_service_time, total_customers_served
        arrival, service, priority, _ = cust
        # waiting time = when service begins (now) - arrival time
        wait = now - arrival
        total_waiting_time += wait
        total_service_time += service
        total_customers_served += 1
        # update server state
        servers_served_count[sid] += 1
        servers_busy[sid] = True
        servers_next_free[sid] = now + service
        # if the server was idle before (servers_last_idle_start set), add idle time
        if servers_last_idle_start[sid] is not None:
            idle_start = servers_last_idle_start[sid]
            if now > idle_start:
                servers_idle_time[sid] += (now - idle_start)
        # mark last_idle_start None because server now busy
        servers_last_idle_start[sid] = None

    # MAIN LOOP: process events until no arrivals left, no busy servers, and queue empty
    while True:
        # next arrival time (if any left), else +inf
        next_arrival_time = customers[ai][0] if ai < N else float('inf')
        # next service completion time and which server
        comp_time, comp_server = next_completion()

        # Decide which event happens next: arrival(s) or completion
        if next_arrival_time <= comp_time:
            # An arrival event occurs next (could be multiple arrivals at same time)
            # Update queue_area for time from last_event_time to this arrival
            dt = next_arrival_time - last_event_time
            if dt > 0:
                queue_area += dt * len(queue)
            current_time = next_arrival_time
            last_event_time = current_time

            # Process all arrivals that happen at exactly current_time
            while ai < N and abs(customers[ai][0] - current_time) < 1e-9:
                cust = customers[ai]
                # if any server is idle, assign immediately
                idle_sid = find_idle_server()
                if idle_sid is not None:
                    assign_customer_to_server(cust, idle_sid, current_time)
                else:
                    # all servers busy -> insert customer into queue respecting priority and arrival order
                    inserted = False
                    # We iterate over queue and insert before the first customer with lower priority
                    # This preserves arrival order among same priorities because we only insert before lower priority.
                    for pos in range(len(queue)):
                        if cust[2] > queue[pos][2]:  # compare priority values
                            queue.insert(pos, cust)
                            inserted = True
                            break
                    if not inserted:
                        # No lower-priority found => append to the end (same priority or lower)
                        queue.append(cust)
                    # track maximum length
                    if len(queue) > max_queue_length:
                        max_queue_length = len(queue)
                ai += 1
            # after processing arrivals, loop continues to next event
        else:
            # A completion event happens next
            dt = comp_time - last_event_time
            if dt > 0:
                queue_area += dt * len(queue)
            current_time = comp_time
            last_event_time = current_time

            # Completion: server comp_server finishes its service
            servers_busy[comp_server] = False
            servers_next_free[comp_server] = float('inf')
            # server becomes idle at current_time (until next assignment)
            servers_last_idle_start[comp_server] = current_time

            # If queue not empty, immediately assign first customer in queue to this server
            if queue:
                next_cust = queue.pop(0)
                # Immediately start service at current_time
                assign_customer_to_server(next_cust, comp_server, current_time)
                # after assign, server is busy again and servers_last_idle_start cleared in assign

        # Check termination condition:
        # - No more arrivals (ai >= N)
        # - No server busy (all False)
        # - Queue empty
        if ai >= N and all(not b for b in servers_busy) and not queue:
            break

    # After loop: compute final statistics
    end_time = current_time
    total_sim_time = end_time - start_time if end_time >= start_time else 0.0

    avg_service_time = (total_service_time / total_customers_served) if total_customers_served > 0 else 0.0
    avg_waiting_time = (total_waiting_time / total_customers_served) if total_customers_served > 0 else 0.0
    avg_queue_length = (queue_area / total_sim_time) if total_sim_time > 0 else 0.0

    # idle rate per server (idle_time / total_sim_time). Note: server that stayed idle from start to end counts that interval.
    idle_rates = []
    for s in range(num_tellers):
        # If server is currently idle and last_idle_start is set, add final idle interval up to end_time
        if servers_last_idle_start[s] is not None:
            # this covers the case server was never used or became idle and stayed idle to the end
            if end_time > servers_last_idle_start[s]:
                servers_idle_time[s] += (end_time - servers_last_idle_start[s])
            servers_last_idle_start[s] = None
        idle_rate = (servers_idle_time[s] / total_sim_time) if total_sim_time > 0 else 0.0
        idle_rates.append(idle_rate)

    # Pack results to return
    result = {
        "num_tellers": num_tellers,
        "servers_served_count": servers_served_count,
        "total_sim_time": total_sim_time,
        "avg_service_time": avg_service_time,
        "avg_waiting_time": avg_waiting_time,
        "max_queue_length": max_queue_length,
        "avg_queue_length": avg_queue_length,
        "idle_rates": idle_rates,
        "total_customers": total_customers_served,
        "total_service_time": total_service_time,
        "total_waiting_time": total_waiting_time
    }
    return result

# ------------------------------------------------------------
# Main entry: read input filename from stdin and run 1..4
# ------------------------------------------------------------
def main():
    # Prompt the user for the filename (read from stdin)
    print("Enter the input filename (e.g. a1-sample.txt):", file=sys.stdout)
    filename = sys.stdin.readline().strip()
    if not filename:
        print("No filename provided. Exiting.")
        return

    # Read customers
    customers = read_customers_from_file(filename)
    if not customers:
        print("No customers found in file or file empty/invalid. Exiting.")
        return

    # The assignment asks to run 4 simulations for tellers = 1,2,3,4
    runs = [1, 2, 3, 4]
    for num in runs:
        res = simulate_one_run(customers, num)
        # Present results in a clear, tutor-friendly style
        print("\n" + "="*60)
        print(f"Simulation results with {res['num_tellers']} teller(s):")
        print("-" * 60)
        # customers served by each teller (list length equals number of tellers)
        print("Number of customers served by each teller: ", res["servers_served_count"])
        print("Total number of customers served:", res["total_customers"])
        # Simulation time
        print("Total time of the simulation (end - start): {:.6f}".format(res["total_sim_time"]))
        # Averages
        print("Average service time per customer: {:.6f}".format(res["avg_service_time"]))
        print("Average waiting time per customer: {:.6f}".format(res["avg_waiting_time"]))
        # Queue stats
        print("Maximum length of the queue observed:", res["max_queue_length"])
        print("Average length of the queue (time-weighted): {:.6f}".format(res["avg_queue_length"]))
        # Idle rates per teller
        idle_rates_str = [ "{:.6f}".format(r) for r in res["idle_rates"] ]
        print("Idle rate for each teller (idle_time / total_time):", idle_rates_str)
        print("="*60)

if __name__ == "__main__":
    main()
