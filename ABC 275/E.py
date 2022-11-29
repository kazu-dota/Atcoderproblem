N, M, K = map(int, input().split())

dp = [[0 for i in range(N+1)] for r in range(K)]

for m in range(1,M+1):
    dp[0][m] += 1

for k in range(K-1):
    for idx,d in enumerate(dp[k]):
        if idx == N:
            continue
        if d != 0:
            for m in range(1,M+1):
                if idx+m > N:
                    dp[k+1][N-(idx+m)-1] += d
                else:
                    dp[k+1][idx+m] += d
ald = dp[-1][-1]
sum = sum(dp[-1])
MOD = 998244353
print(pow(sum,-1, MOD)*(ald)%MOD)
