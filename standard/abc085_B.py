N = int(input())
D = []

for i in range(N):
    D.append(int(input()))

D = list(set(D))

print(len(D))