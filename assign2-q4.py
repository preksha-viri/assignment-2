
import time
import itertools
import matplotlib.pyplot as plt

def brute_force_crack(target, charset):
    attempts = 0
    for length in range(1, len(target) + 1):
        for combo in itertools.product(charset, repeat=length):
            attempts += 1
            if ''.join(combo) == target:
                return ''.join(combo), attempts
    return None, attempts

def run_bruteforce():
    print("\n--- Problem 4: Password Cracking (Brute Force) ---")
    target = "ab1"
    charset = "abc123"

    start = time.time()
    found, attempts = brute_force_crack(target, charset)
    end = time.time()

    print(f"Target: {target}, Found: {found}, Attempts: {attempts}")
    print("Execution Time:", round(end - start, 6), "sec")

    # Visualization (time vs password length)
    lengths = [1, 2, 3, 4]
    times = []
    for l in lengths:
        t0 = time.time()
        brute_force_crack("a" * l, charset)
        times.append(time.time() - t0)
    plt.plot(lengths, times, marker='o')
    plt.title("Password Length vs Time (Brute Force)")
    plt.xlabel("Password Length")
    plt.ylabel("Time (sec)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run_bruteforce()
