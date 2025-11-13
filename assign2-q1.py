
import time
import matplotlib.pyplot as plt

def job_sequencing(jobs):
    """
    jobs: list of tuples (id, deadline, profit)
    """
    # Sort jobs by profit descending
    jobs.sort(key=lambda x: x[2], reverse=True)
    max_deadline = max(job[1] for job in jobs)
    slots = [None] * (max_deadline + 1)
    total_profit = 0

    for job in jobs:
        for d in range(job[1], 0, -1):
            if slots[d] is None:
                slots[d] = job
                total_profit += job[2]
                break

    scheduled_jobs = [j for j in slots if j is not None]
    return scheduled_jobs, total_profit

def run_job_sequencing():
    print("\n--- Problem 1: TV Commercial Scheduling (Greedy) ---")
    jobs = [
        ("A", 2, 100),
        ("B", 1, 19),
        ("C", 2, 27),
        ("D", 1, 25),
        ("E", 3, 15)
    ]
    start = time.time()
    result, total_profit = job_sequencing(jobs)
    end = time.time()
    print("Selected Ads:", [r[0] for r in result])
    print("Total Profit:", total_profit)
    print("Execution Time:", round(end - start, 6), "sec")

    # Visualization
    if result:
        plt.bar([j[0] for j in result], [j[2] for j in result])
        plt.title("TV Commercials: Ads vs Revenue")
        plt.xlabel("Ad ID")
        plt.ylabel("Profit")
        plt.show()

if __name__ == "__main__":
    run_job_sequencing()
