
def checkways(n, m, d, A, B):
    MOD = 10**9 + 7
    
    city_covered_by = [[] for _ in range(n)]
    for i in range(m):
        for j in range(n):
            if abs(B[i] - A[j]) <= d:
                city_covered_by[j].append(i)
    
    tower_covers = [[] for _ in range(m)]
    for j in range(n):
        for i in city_covered_by[j]:
            tower_covers[i].append(j)
    
    next_uncovered = [n] * m
    for i in range(m):
        for j in range(n):
            if A[j] > B[i] + d:
                next_uncovered[i] = j
                break
    
    check = [[0] * m for _ in range(m)]
    for i_prime in range(m):
        for i in range(i_prime + 1, m):
            covered_by_i_prime = set(tower_covers[i_prime])
            covered_by_i = set(tower_covers[i])
            if not covered_by_i_prime.intersection(covered_by_i):
                all_covered = True
                for city_idx in range(n):
                    if B[i_prime] + d < A[city_idx] < B[i] - d:
                        all_covered = False
                        break
                if all_covered:
                    check[i_prime][i] = 1
    
    dp = [[0] * (m + 1) for _ in range(m)]
    
    for i in range(m):
        all_covered = True
        for city_idx in range(n):
            if A[city_idx] <= B[i] and abs(B[i] - A[city_idx]) > d:
                all_covered = False
                break
        if all_covered:
            dp[i][1] = 1

    for i in range(m):
        for j in range(2, i + 2):
            for i_prime in range(i):
                if check[i_prime][i]:
                    dp[i][j] = (dp[i][j] + dp[i_prime][j-1]) % MOD
    
    result = [0] * m
    for k in range(1, m + 1):
        for i in range(m):
            if next_uncovered[i] == n:
                result[k-1] = (result[k-1] + dp[i][k]) % MOD
    
    return result

def main():
    C = int(input())
    for _ in range(C):
        n, m, d = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        
        result = checkways(n, m, d, A, B)
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()