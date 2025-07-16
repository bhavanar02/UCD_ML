from bisect import bisect_right, bisect_left
#import time

if __name__ == "__main__":

    #start_time = time.time()
    n, d = map(int, input().split())
    A = list(map(int, input().split()))

    results = [0] * (n + 1)
    left = 0
    max_coverage = 0

# First part: calculate coverage for each city based on its distance
    for i in range(n):
        end_right = A[i] + d
        end_left = A[i] - d
        right_split = bisect_right(A, end_right) - 1
        left_split = bisect_left(A, end_left)
        coverage = right_split-left_split + 1

        results[i] = coverage
        print(results[i])
        max_coverage = max(max_coverage, coverage)

# Second part: optimize the maximum cities covered for overlapping ranges
    for right in range(n):
        while (A[right] - A[left] > 2*d):
            left += 1
        center = right- left
        max_coverage = max(max_coverage, center + 1)
    print(max_coverage)

    #end_time = time.time()
    #print(f"Runtime: {end_time - start_time:.6f} seconds")