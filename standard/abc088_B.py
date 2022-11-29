N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
result = 0

for i in range(0, N-1, 2):
    result += A[i] - A[i+1]

if N % 2 == 1:
    result += A[-1]

print(result)
