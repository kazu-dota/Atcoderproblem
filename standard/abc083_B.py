N, A, B = map(int, input().split())
result = 0
for n in range(N+1):
    total = 0
    for s in str(n):
        total += int(s)

    if total >= A and total <= B:
        result += n

print(result)
