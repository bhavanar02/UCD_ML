import bisect

def can_cover_all_cities(Q, P, A, k):
    n = len(A)
    towers_used = 0
    i = 0
    intervals = [(A[j] - (Q * P[j]) // 100, A[j] + (Q * P[j]) // 100) for j in range(n)]
    intervals.sort()

    j = 0
    while i < n:
        candidate_found = False
        best_r = i - 1

        while j < n and intervals[j][0] <= A[i]:
            best_r = max(best_r, bisect.bisect_right(A, intervals[j][1]) - 1)
            candidate_found = True
            j += 1

        if not candidate_found:
            return False

        towers_used += 1
        if towers_used > k:
            return False

        i = best_r + 1

    return True

def compute_min_radius(P, A, k):
    n = len(P)
    if k >= n:
        return 0
    A = [a * 60 for a in A]
    low, high = 0, (A[-1] - A[0]) * 100 // min(P)

    while low < high:
        mid = (low + high) // 2
        if can_cover_all_cities(mid, P, A, k):
            high = mid
        else:
            low = mid + 1

    return low

tc = int(input())
results = []
for _ in range(tc):
    n, k = map(int, input().split())
    P = list(map(int, input().split()))
    A = list(map(int, input().split()))
    print(compute_min_radius(P, A, k))