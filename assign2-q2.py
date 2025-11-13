
import time
import numpy as np
import matplotlib.pyplot as plt

def knapsack(values, weights, capacity):
    n = len(values)
    dp = np.zeros((n + 1, capacity + 1), dtype=int)

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][capacity]

def run_knapsack():
    print("\n--- Problem 2: 0/1 Knapsack (Dynamic Programming) ---")
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    start = time.time()
    result = knapsack(values, weights, capacity)
    end = time.time()

    print("Values:", values)
    print("Weights:", weights)
    print("Capacity:", capacity)
    print("Maximum Profit:", result)
    print("Execution Time:", round(end - start, 6), "sec")

    # Visualization (value vs weight scatter)
    plt.plot(weights, values, marker='o')
    plt.title("Knapsack: Weights vs Values")
    plt.xlabel("Weight")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_knapsack()
