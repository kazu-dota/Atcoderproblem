N = int(input())
A = list(map(int, input().split()))

am = {}

am[1] = 0
for idx,a in enumerate(A):
    am[2*(idx+1)] = am[a] + 1
    am[2*(idx+1)+1] = am[a] + 1

S = sorted(list(am.keys()))

for s in S:
    print(am[s])