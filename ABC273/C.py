from collections import Counter
N = int(input())
A = list(map(int, input().split()))
count = Counter(A)

A = sorted(A,reverse=True)
set_A = set(A)

for a in set_A:
    print(count[a])

if len(A)-len(set_A) != 0:
    for i in range(len(A)-len(set_A)):
        print(0)