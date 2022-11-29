N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

flag = True
M = 0

while flag:
    M += 1
    result = 0
    for n in range(1,N):
        if A[n+1] - A[n] > M:
            result += 1
            if result == K:
                break

    flag = False

print(M-1)