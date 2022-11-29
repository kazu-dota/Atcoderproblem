N = int(input())
T, X, A = [None for i in range(N)],[None for i in range(N)],[None for i in range(N)]

for i in range(N):
    T[i], X[i], A[i] = map(int, input().split())

dp = [[0 for i in range(5)] for i in range(N)]
dp
for i in range(N):
    for t in range(5):
        if t != 0 and t != 4:
            dp[i][t] = max(dp[i-1][t-1], dp[i-1][t], dp[i-1][t+1])
        elif t == 0:
            dp[i][t] = max( dp[i-1][t], dp[i-1][t+1])
        elif t == 4:
            dp[i][t] = max(dp[i-1][t-1], dp[i-1][t])

        if i+1 in T and t == X[i]:
            dp[i][t] += A[i]

print(max(dp[-1]))