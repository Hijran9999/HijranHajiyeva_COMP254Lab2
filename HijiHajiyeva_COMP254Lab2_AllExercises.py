import time
import random
import matplotlib.pyplot as plt
import math

############################################################
# EXERCISE 1 – Big-O Analysis (Documented in Comments)
############################################################

# example1 → O(n)
def example1(n):
    total = 0
    for i in range(n):
        total += 1
    return total
# Running time: O(n)
# Explanation: Single loop runs n times.


# example2 → O(n)
def example2(n):
    total = 0
    for i in range(n):
        total += 1
    for j in range(n):
        total += 1
    return total
# Running time: O(n)
# Explanation: Two separate loops of n → 2n → O(n).


# example3 → O(n^2)
def example3(n):
    total = 0
    for i in range(n):
        for j in range(n):
            total += 1
    return total
# Running time: O(n²)
# Explanation: Nested loops → n × n = n².


# example4 → O(n^2)
def example4(n):
    total = 0
    for i in range(n):
        for j in range(i + 1):
            total += 1
    return total
# Running time: O(n²)
# Explanation: 1 + 2 + ... + n = n(n+1)/2 → O(n²).


# example5 → O(log n)
def example5(n):
    total = 0
    i = 1
    while i < n:
        total += 1
        i *= 2
    return total
# Running time: O(log n)
# Explanation: i doubles each time → log₂(n) iterations.


############################################################
# EXERCISE 2 – prefixAverage Experimental Analysis
############################################################

# O(n^2)
def prefixAverage1(x):
    n = len(x)
    a = [0] * n
    for i in range(n):
        total = 0
        for j in range(i + 1):
            total += x[j]
        a[i] = total / (i + 1)
    return a


# O(n)
def prefixAverage2(x):
    n = len(x)
    a = [0] * n
    total = 0
    for i in range(n):
        total += x[i]
        a[i] = total / (i + 1)
    return a


def experimental_prefix():
    sizes = [1000, 2000, 4000, 8000, 16000]
    times1 = []
    times2 = []

    for n in sizes:
        data = [random.random() for _ in range(n)]

        start = time.time()
        prefixAverage1(data)
        end = time.time()
        times1.append(end - start)

        start = time.time()
        prefixAverage2(data)
        end = time.time()
        times2.append(end - start)

        print(f"n={n} | prefix1={times1[-1]:.4f}s | prefix2={times2[-1]:.4f}s")

    # Log-log plot
    plt.figure()
    plt.loglog(sizes, times1, marker='o')
    plt.loglog(sizes, times2, marker='o')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Running Time (seconds)")
    plt.title("prefixAverage1 vs prefixAverage2 (Log-Log)")
    plt.legend(["prefixAverage1 O(n^2)", "prefixAverage2 O(n)"])
    plt.show()


############################################################
# EXERCISE 3 – unique1 vs unique2
############################################################

# O(n^2)
def unique1(A):
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] == A[j]:
                return False
    return True


# O(n log n)
def unique2(A):
    B = sorted(A)
    for i in range(len(B) - 1):
        if B[i] == B[i + 1]:
            return False
    return True


def max_n_under_one_minute(func):
    low = 1
    high = 100000
    best = 0

    while low <= high:
        mid = (low + high) // 2
        data = list(range(mid))  # all unique elements

        start = time.time()
        func(data)
        end = time.time()

        elapsed = end - start

        if elapsed <= 60:
            best = mid
            low = mid + 1
        else:
            high = mid - 1

        print(f"Testing n={mid} | time={elapsed:.4f}s")

    return best


############################################################
# MAIN EXECUTION
############################################################

if __name__ == "__main__":

    print("\n===== EXERCISE 2 – Experimental Analysis =====")
    experimental_prefix()

    print("\n===== EXERCISE 3 – Finding Max n Under 1 Minute =====")

    print("\nTesting unique1 (O(n^2))...")
    max_unique1 = max_n_under_one_minute(unique1)
    print(f"Maximum n for unique1 under 60 seconds: {max_unique1}")

    print("\nTesting unique2 (O(n log n))...")
    max_unique2 = max_n_under_one_minute(unique2)
    print(f"Maximum n for unique2 under 60 seconds: {max_unique2}")
