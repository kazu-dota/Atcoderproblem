H, W = map(int,input().split())
C = [None for i in range(H)]
for i in range(H):
    C[i] = input()

ans = [0 for i in range(W)]

for w in range(W):
    for h in range(H):
        if C[h][w] == '#':
            ans[w] += 1

print(*ans)